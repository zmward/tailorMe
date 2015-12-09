# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations


@auth.requires_signature()
@auth.requires_login()
def profile():
    measure_form = SQLFORM(db.Measure2)
    if measure_form.vars.accepted:
        session.flash = "Thank you!"
        redirect(URL('default', index()))

    return dict(measure_form=measure_form)



def index():
    store_list = db(db.store).select()
    add_button = A(' Create New Store', _class='btn btn-success fa fa-plus',
                                             _href=URL('default', 'add_store'))
    fit_button =  A(' Create New Fit', _class='btn btn-info fa fa-plus',
                                             _href=URL('default', 'tailor_you'))
    return dict(store_list=store_list, fit_button=fit_button, add_button=add_button)


#--------------------------------------------
# Adding a measurement table to the Profile
#-------------------------------------------

def tailor_you():
    Measure_list = db(db.Measure2).select()
    add_button = A(' Fit Me!', _class='btn btn-success fa fa-plus', _href=URL('default', 'fit_me'))

    return dict(Measure_list=Measure_list, add_button=add_button)


def fit_me():
    form = SQLFORM(db.Measure2)
    if form.process().accepted:
        session.flash=T("Success!")
        redirect(URL('tailor_you'))

    back_button = A(' Back', _class='btn bth-info fa fa-reply', _href=URL('default', 'tailor_you'))

    return dict(form=form, back_button=back_button)

def check_complete(form):
    if form.vars.height == None:
        form.errors.height = T('Please Enter a Title for your Board')


#--------------------------------
# Creating a store and a review
#--------------------------------

def add_store(): #was add_store
    form = SQLFORM(db.store)
    if form.process(onvalidation=check_completea).accepted:
        session.flash=T("Success!")
        redirect(URL('show_store'))

    back_button = A(' Back', _class='btn bth-info fa fa-reply', _href=URL('default', 'show_store'))

    return dict(form=form, back_button=back_button)

def show_store():
    store_list = db(db.store).select()
    add_button = A(' Create New Store', _class='btn btn-success fa fa-plus',
                                             _href=URL('default', 'add_store'))
    fit_button =  A(' Create New Fit', _class='btn btn-info fa fa-plus',
                                             _href=URL('default', 'tailor_you'))
    return dict(store_list=store_list, fit_button=fit_button, add_button=add_button)


def check_completea(form):
    if form.vars.store_name == None:
        form.errors.store_name = T('Please Enter a Title for your Board')


def store_details():
    store = db.store(request.args(0))
    name = request.args(1)
    if store is None:
        session.flash = T('This Store does not Exist!')
        redirect(URL('default', 'show_boards'))
    form = SQLFORM(db.store, record=store, readonly=True)
    list_button = A(' Back to stores', _class='btn btn-primary btn-lg outline fa fa-reply',
                    _href=URL('default', 'show_store'))
    review = db(db.review.store_id == store.id).select()
    add_button = A(' Add a review', _class='btn btn-primary btn-lg outline fa fa-plus',
                                             _href=URL('default', 'add_review', args=[store.id]))
    return dict(form=form, review=review, list_button=list_button, add_button=add_button, name=name)

def add_review():
    store = db.store(request.args(0))
    if store is None:
        session.flash = T("There is no such Store")
        redirect(URL('default', 'index'))

    form = SQLFORM(db.review)
    form.vars.store_id = store.id

    if form.process().accepted:
        form.vars.store_id = store.id
        session.flash = T("You review has been created!")
        redirect(URL('default', 'store_details', args=[store.id]))

    back_button = A(' Cancel', _class='btn btn-primary btn-lg outline fa fa-times',
                    _href=URL('default', 'store_details', args=[store.id]))

    return dict(form=form, back_button=back_button)

def store_edit():
    store = db.store(request.args(0))
    if store is None:
        session.flash = T('No such Store')
        redirect(URL('default', 'show_store'))
    form = SQLFORM(db.store, record=store)
    if form.process(onvalidation=check_complete).accepted:
        session.flash = T('The data was edited')
        redirect(URL('default', 'store_details', args=[store.id]))
    edit_button = A(' View', _class='btn btn-warning',
                    _href=URL('default', 'store_details', args=[store.id]))
    return dict(form=form, edit_button=edit_button)

def review_edit():
    review = db.review(request.args(0))
    store = db.store(request.args(1))

    if review is None:
        session.flash = T('An error has Occurred')
        redirect(URL('default', 'show_stores'))
    form = SQLFORM(db.review, record=review)
    if form.process(onvalidation=check_complete_post).accepted:
        session.flash = T('The review was edited!')
        redirect(URL('default', 'store_details', args=[store.id]))
    back_button = A(' Back', _class='btn btn-warning fa fa-reply',
                    _href=URL('default', 'store_details', args=[store.id]))
    return dict(form=form, back_button=back_button)


def delete_review():
    db.review.id == request.args(0).delete()
    store = db.store(request.args(1))
    session.flash = "Deleted"
    redirect(URL('default', 'store_details', args=[store.id]))

def delete_store():
    db(db.store.id == request.args(0)).delete()
    session.flash = "Store Deleted"
    redirect(URL('default', 'show_store'))
#------------


#------------
# this is being usd to clear all tables then editing them
#------------
def reset():
    db(db.board.id > 0).delete()
    db(db.post.id > 0).delete()
    db(db.store.id > 0).delete()
    db(db.Measure.id > 0).delete()
    db(db.height_table.id > 0).delete()
    db(db.head_table.id > 0).delete()
    db(db.neck_table.id > 0).delete()
    db(db.chest_table.id > 0).delete()
    db(db.waist_table.id > 0).delete()
    db(db.sh_table.id > 0).delete()
    db(db.hip_table.id > 0).delete()
    db(db.wrist_table.id > 0).delete()
    db(db.biceps_table.id > 0).delete()
    db(db.forearm_table.id > 0).delete()
    db(db.arm_table.id > 0).delete()
    db(db.inseam_table.id > 0).delete()
    db(db.thigh_table.id > 0).delete()
    db(db.calf_table.id > 0).delete()
    db(db.ankle_table.id > 0).delete()
    db(db.review.id > 0).delete()

    redirect(URL('default', 'index'))


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


