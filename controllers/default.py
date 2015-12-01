# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

def index():
    """
    Allows a person to register in the system, if they are not registered already.
    """
    # If the person is registered, we store the person id in session.person_id.
    db.people.name.label = "What's your name?"
    logger.info("Session: %r" % session)
    row = db(db.people.user_id == auth.user_id).select().first()
    db.people.user_id.readable = db.people.user_id.writable = False
    form = SQLFORM(db.people, record=row)
    if form.process().accepted:
        session.flash = "Welcome, %s!" % form.vars.name
        redirect(URL('default', 'people'))
    return dict(form=form)

@auth.requires_login()
def people():
    """
    Gives the person a table displaying all the people, to search.
    """
    db.people.name.label = "Name"
    # Creates a list of other people, other than myself.
    q = (db.people.id != auth.user_id)
    links = [dict(header='Click to chat',
                 body = lambda r: A(I(_class='fa fa-comments'), 'Chat', _class='btn btn-success',
                                    _href=URL('default', 'chat', args=[r.user_id])))]
    grid = SQLFORM.grid(q,
                        links=links,
                        editable=False,
                        details=False,
                        csv=False)
    return dict(grid=grid)


def store_message(form):
    form.vars.msg_id = str(db2.textblob.insert(mytext = form.vars.msg_id))


@auth.requires_login()
def chat():
    """This page enables you to chat with another person."""
    # Let us read the record telling us who is the other person.
    other = db(db.people.user_id == request.args(0)).select().first()
    logger.info("I am %r, chatting with %r" % (auth.user_id, other))
    if other is None:
        # Back to square 0.
        return redirect(URL('default', 'index'))
    # Pair of people involved.
    two_people = [auth.user_id, other.id]
    # We want them in order, so that all messages will be stored under the same pairs of ids.
    two_people.sort()
    # This query selects all messages between the two people.
    q = ((db.messages.user0 == two_people[0]) & (db.messages.user1 == two_people[1]))
    # This is the list of messages.
    db.messages.sender.represent = lambda v, r: 'You' if v == auth.user_id else other.name
    grid = SQLFORM.grid(q,
                        fields=[db.messages.msg_time, db.messages.sender, db.messages.msg_id],
                        details=False,
                        create=False,
                        orderby=~db.messages.msg_time,
                        csv=False,
                        sortable=False,
                        editable=False,
                        deletable=False,
                        searchable=False,
                        user_signature=False)

    # This is a form for adding one more message.

    db.messages.sender.readable = db.messages.sender.writable = False
    db.messages.msg_time.readable = db.messages.msg_time.writable = False
    form = SQLFORM(db.messages)
    form.vars.user0 = two_people[0]
    form.vars.user1 = two_people[1]
    if form.process(onvalidation=store_message).accepted:
        session.flash = "Message sent!"
        redirect(URL('default', 'chat', args=[other.user_id]))

    title = "Chat with %s" % other.name
    return dict(title=title, grid=grid, form=form)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


