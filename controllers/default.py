# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################



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

def add_store():
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
    list_button = A(' Back to Boards', _class='btn btn-info fa fa-reply',
                    _href=URL('default', 'show_store'))
    review = db(db.review.store_id == store.id).select()
    add_button = A(' Create New Post', _class='btn btn-success fa fa-plus',
                                             _href=URL('default', 'add_review', args=[store.id]))
    return dict(form=form, review=review, list_button=list_button, add_button=add_button, name=name)

def add_review():
    store = db.store(request.args(0))
    if store is None:
        session.flash = T("There is no such Store")
        redirct(URL('default', 'index'))

    form = SQLFORM(db.review)
    form.vars.store_id = store.id

    if form.process().accepted:
        form.vars.store_id = store.id
        session.flash = T("You review has been created!")
        redirect(URL('default', 'store_details', args=[store.id]))

    back_button = A(' Cancel', _class='btn btn-warning fa fa-times',
                    _href=URL('default', 'store_details', args=[store.id]))

    return dict(form=form, back_button=back_button)



#------------





def delete_post():
    db(db.post.id == request.args(0)).delete()
    board = db.board(request.args(1))
    session.flash = "Deleted"
    redirect(URL('default', 'board_details', args=[board.id]))

def delete_board():
    db(db.board.id == request.args(0)).delete()
    session.flash = "Board Deleted"
    redirect(URL('default', 'index'))
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


