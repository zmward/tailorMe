#########################################################################
## Define your tables below; for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

from datetime import datetime

# This is a table for all users.
db.define_table('people',
    Field('user_id', db.auth_user, default=auth.user_id),
    Field('name', required=True),
    Field('description', 'text'),
    )

db.people.id.readable = False
db.people.user_id.readable = False
db.people.description.represent = lambda v, r: DIV(v, _class="msg_content")


# Here is a table for messages.
db.define_table('messages',
    Field('user0', db.auth_user),
    Field('user1', db.auth_user),
    Field('sender',  db.auth_user, default=auth.user_id),
    Field('msg_time', 'datetime', default=datetime.utcnow()),
    Field('msg_id', 'text')) # Stored as a string

db.messages.user0.readable = db.messages.user0.writable = False
db.messages.user1.readable = db.messages.user1.writable = False
db.messages.msg_time.label = "Time"
db.messages.msg_id.label = "Message"
db.messages.msg_id.represent = lambda v, r: get_text(v)

def get_text(v):
    r = db2.textblob(v)
    return '' if r is None else r.mytext

# Table for big chunks of text.
db2.define_table('textblob',
    Field('mytext', 'text'),
    )



#-----------------------------


db.define_table('profile',
                Field('user_id', db.auth_user, default=auth.user_id),
                Field('User_name'),
                Field('First_name'),
                Field('Last_name'),
                Field('email'),
                Field('password'),
                )

db.profile.id.readable = False
db.profile.user_id.readable = db.profile.user_id.writable = False


#----------------
# All measurements in centimeters
#---------------

db.define_table('height_table',
                Field('user_id', 'reference profile'),
                Field('mess', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('petite', 'boolean', default=False ), # <5'4'
                Field('regular', 'boolean', default=False), # 5'4-5'9"
                Field('tall', 'boolean', default=False),    # >5'9"
                )
db.height_table.user_id.on_delete = "SET NULL"

db.define_table('head_table',
                Field('user_id', 'reference profile'),
                Field('mess', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('flag1', 'boolean', default=False ), # <56cm
                Field('flag2', 'boolean', default=False),  # 56-57cm
                Field('flag3', 'boolean', default=False),  # > 57cm
                )
db.head_table.user_id.on_delete = "SET NULL"


db.define_table('neck_table',
                Field('user_id', 'reference profile'),
                Field('mess', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('flag1', 'boolean', default=False ),  # < 15 inches
                Field('flag2', 'boolean', default=False),  # 15-16 inches
                Field('flag3', 'boolean', default=False),     # > 16 inches
                )

db.neck_table.user_id.on_delete = "SET NULL"

db.define_table('chest_table',
                Field('user_id', 'reference profile'),
                Field('mess', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('flag1', 'boolean', default=False ), # < 16 inches
                Field('flag2', 'boolean', default=False),  # 16-18 inches
                Field('flag3', 'boolean', default=False),  # 19-21
                Field('flag4', 'boolean', default=False),  # 22-24
                Field('flag5', 'boolean', default=False),  # > 25
                )

db.chest_table.user_id.on_delete = "SET NULL"

db.define_table('waist_table',
                Field('user_id', 'reference profile'),
                Field('mess', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('flag1', 'boolean', default=False ), # < 25 inches
                Field('flag2', 'boolean', default=False),  # 25-26 inches
                Field('flag3', 'boolean', default=False),  # 27-29 inches
                Field('flag4', 'boolean', default=False),  # 30-32 inches
                Field('flag5', 'boolean', default=False),  # 33-35 inches
                Field('flag6', 'boolean', default=False),  # > 36 inches
                )

db.waist_table.user_id.on_delete = "SET NULL"

db.define_table('sh_table',
                Field('user_id', 'reference profile'),
                Field('mess', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('flag1', 'boolean', default=False),  # < 18 inches
                Field('flag2', 'boolean', default=False),  # 18-20 1/8 inches
                Field('flag3', 'boolean', default=False),   # > 20 1/8 inches
                )

db.sh_table.user_id.on_delete = "SET NULL"

db.define_table('hip_table',
                Field('user_id', 'reference profile'),
                Field('mess', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('flag1', 'boolean', default=False),  # < 38 5/8 inches
                Field('flag2', 'boolean', default=False),  # 38 5/8 - 41 inches
                Field('flag3', 'boolean', default=False),  # 42-45 inches
                Field('flag4', 'boolean', default=False),  # > 45 inches
                )

db.hip_table.user_id.on_delete = "SET NULL"

db.define_table('wrist_table',
                Field('user_id', 'reference profile'),
                Field('mess', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('flag1', 'boolean', default=False),  # < 5 1/2 inches
                Field('flag2', 'boolean', default=False),  # 5 1/2 - 6 1/2 inches
                Field('flag3', 'boolean', default=False),  # 6 1/2 - 7 1/2 inches
                Field('flag4', 'boolean', default=False),  # > 7 1/2 inches
                )

db.wrist_table.user_id.on_delete = "SET NULL"

db.define_table('biceps_table',
                Field('user_id', 'reference profile'),
                Field('mess', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('flag1', 'boolean', default=False),  # < 11 3/4 inches
                Field('flag2', 'boolean', default=False),  # 11 3/4 - 14 inches
                Field('flag3', 'boolean', default=False),  # 14 - 16 1/4 inches
                Field('flag4', 'boolean', default=False),  # > 16 1/4 inches
                )

db.biceps_table.user_id.on_delete = "SET NULL"

db.define_table('forearm_table',
                Field('user_id', 'reference profile'),
                Field('mess', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('flag1', 'boolean', default=False),  # < 9 1/4 inches
                Field('flag2', 'boolean', default=False),  # 9 1/4 - 11 inches
                Field('flag3', 'boolean', default=False),  # 11-12 1/2 inches
                Field('flag4', 'boolean', default=False),  # > 12 1/2 inches
                )

db.forearm_table.user_id.on_delete = "SET NULL"

db.define_table('arm_table',
                Field('user_id', 'reference profile'),
                Field('mess', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('flag1', 'boolean', default=False),  # < 43cm
                Field('flag2', 'boolean', default=False),  # 43-46cm
                Field('flag3', 'boolean', default=False),  # 46-49.5cm
                Field('flag4', 'boolean', default=False),  # > 49.5cm
                )

db.arm_table.user_id.on_delete = "SET NULL"

db.define_table('inseam_table',
                Field('user_id', 'reference profile'),
                Field('mess', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('flag1', 'boolean', default=False),  # < 26.5 inches
                Field('flag2', 'boolean', default=False),  # 26.5 - 28 inches
                Field('flag3', 'boolean', default=False),  # 28 - 29 inches
                Field('flag4', 'boolean', default=False),  # 29 - 30 inches
                Field('flag5', 'boolean', default=False),  # 30 - 31 inches
                Field('flag6', 'boolean', default=False),  # 31 - 32 inches
                Field('flag7', 'boolean', default=False),  # > 32 inches
                )

db.inseam_table.user_id.on_delete = "SET NULL"

db.define_table('thigh_table',
                Field('user_id', 'reference profile'),
                Field('mess', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('flag1', 'boolean', default=False),  # 18 inches
                Field('flag2', 'boolean', default=False),  # 18-24 inches
                Field('flag3', 'boolean', default=False),  # 24-27 inches
                Field('flag4', 'boolean', default=False),  # 27-30 inches
                Field('flag5', 'boolean', default=False),  # > 30 inches
                )

db.thigh_table.user_id.on_delete = "SET NULL"

db.define_table('calf_table',
                Field('user_id', 'reference profile'),
                Field('mess', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('flag1', 'boolean', default=False),  # < 11 inches
                Field('flag2', 'boolean', default=False),  # 11-13 inches
                Field('flag3', 'boolean', default=False),  # 13-16 inches
                Field('flag4', 'boolean', default=False),  # 16-19 inches
                Field('flag5', 'boolean', default=False),  # > 19 inches
                )

db.calf_table.user_id.on_delete = "SET NULL"

db.define_table('ankle_table',
                Field('user_id', 'reference profile'),
                Field('mess', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('flag1', 'boolean', default=False),  # < 7 inches
                Field('flag2', 'boolean', default=False),  # 7- 8 1/4 inches
                Field('flag3', 'boolean', default=False),  # 8 3/8 - 9 7/8 inches
                Field('flag4', 'boolean', default=False),  # 10 - 11 3/8 inches
                Field('flag5', 'boolean', default=False),  # > 11 1/2 inches
                )

db.ankle_table.user_id.on_delete = "SET NULL"



db.define_table('Measure',
                Field('user_id', 'reference profile'),
                Field('height', 'reference height_table'),
                Field('head', 'reference neck_table'),
                Field('neck', 'reference chest_table'),
                Field('chest', 'reference waist_table'),
                Field('waist', 'reference height_table'),
                Field('shoulder','reference sh_table'),
                Field('hip', 'reference hip_table'),
                Field('wrist', 'reference wrist_table'),
                Field('biceps', 'reference biceps_table'),
                Field('forearm', 'reference forearm_table'),
                Field('arm_length', 'reference arm_table'),
                Field('inseam', 'reference inseam_table'),
                Field('thigh', 'reference thigh_table'),
                Field('calf', 'reference calf_table'),
                Field('ankle', 'reference ankle_table'),
                )

db.Measure.user_id.on_delete = "SET NULL"
db.Measure.height.on_delete = "SET NULL"
db.Measure.head.on_delete = "SET NULL"
db.Measure.neck.on_delete = "SET NULL"
db.Measure.chest.on_delete = "SET NULL"
db.Measure.waist.on_delete = "SET NULL"
db.Measure.shoulder.on_delete = "SET NULL"
db.Measure.hip.on_delete = "SET NULL"
db.Measure.waist.on_delete = "SET NULL"
db.Measure.biceps.on_delete = "SET NULL"
db.Measure.forearm.on_delete = "SET NULL"
db.Measure.arm_length.on_delete = "SET NULL"
db.Measure.inseam.on_delete = "SET NULL"
db.Measure.thigh.on_delete = "SET NULL"
db.Measure.calf.on_delete = "SET NULL"
db.Measure.ankle.on_delete = "SET NULL"


db.define_table('Store',
                Field('Store_Name'),
                Field('Street'),
                Field('City'),
                Field('St'),
                )


db.define_table('User_review',
                Field('author', db.auth_user, default=auth.user_id ),
                Field('Store', 'reference Store'),
                Field('Tops', 'boolean', default=False),
                Field('FT', label='Fit', requires=IS_IN_SET(['1', '2', '3', '4', '5']), default=3),
                Field('CT', label='Cut', requires=IS_IN_SET(['1', '2', '3', '4', '5']), default=3),
                Field('QT', label='Quality', requires=IS_IN_SET(['1', '2', '3', '4', '5']), default=3),
                Field('Bottoms', 'boolean', default=False),
                Field('FB', label='Fit', requires=IS_IN_SET(['1', '2', '3', '4', '5']), default=3),
                Field('CB', label='Cut', requires=IS_IN_SET(['1', '2', '3', '4', '5']), default=3),
                Field('QB', label='Quality', requires=IS_IN_SET(['1', '2', '3', '4', '5']), default=3),
                Field('Dress', 'boolean', default=False),
                Field('FD', label='Fit', requires=IS_IN_SET(['1', '2', '3', '4', '5']), default=3),
                Field('CD', label='Cut', requires=IS_IN_SET(['1', '2', '3', '4', '5']), default=3),
                Field('QD', label='Quality', requires=IS_IN_SET(['1', '2', '3', '4', '5']), default=3),
                Field('Shoes', 'boolean', default=False),
                Field('Outerwear', 'boolean', default=False),
                Field('Intimates', 'boolean', default=False),

                Field('Fit', requires=IS_IN_SET(['1', '2', '3', '4', '5']), default=3),
                Field('Cut', requires=IS_IN_SET(['1', '2', '3', '4', '5']), default=3),
                Field('Quality', requires=IS_IN_SET(['1', '2', '3', '4', '5']), default=3),
                Field('review', 'text'),
                Field('This_is_image', 'boolean', default=False),
                )



db.User_review.author.readable = db.User_review.author.writable= False
