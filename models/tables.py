
#------------------------------
# Homework 3 stuff
#------------------------------

db.define_table( 'person',
                 Field('user_id', db.auth_user),
                 Field( 'name', required=True),
                 )

db.define_table('board',
                 Field( 'board_author', db.auth_user, default=auth.user_id),
                 Field('board_name', required=True),
)
db.board.id.readable = db.board.id.writable = False
db.board.board_author.readable = db.board.board_author.writable=False


db.define_table( 'post',
                 Field('post_author', db.auth_user, default=auth.user_id),
                 Field('board_id', 'reference board'),
                 Field('title' ),
                 Field('description', 'text'),
)
db.post.id.readable = db.post.id.writable = False
db.post.post_author.readable = db.post.post_author.writable=False
db.post.board_id.readable = db.post.board_id.writable=False

db.post.board_id.on_delete = "SET NULL"


#----------------------------------
# Tailor me stuff

db.define_table('store',
                Field('store_author', db.auth_user, default=auth.user_id),
                Field('store_name', required=True),
)

db.store.id.readable = db.store.id.writable = False
db.store.store_author.readable = db.store.store_author.writeable = False

db.define_table('review',
                Field('author', db.auth_user, default=auth.user_id ),
                Field('store_id', 'reference store'),
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

db.review.id.readable = db.review.id.writable = False
db.review.author.readable = db.review.author.writeable = False
db.review.store_id.on_delete = "SET NULL"



#-------------------------
# Testing messure tables
#-------------------------








db.define_table('Measure2',
                Field('author', db.auth_user, default=auth.user_id ),
                Field('height', requires=IS_IN_SET(['less than 5 foot 4 inches', '5 foot 4 inches -> 5 foot 9 inches', 'taller than 5 food 9 inches'])),
                Field('head', requires=IS_IN_SET(['< 56cm', '56 - 57cm', '> 57cm'])),
                Field('neck', requires=IS_IN_SET(['< 15 inches', '15 - 16 inches', '> 16 inches'])),
                Field('chest', requires=IS_IN_SET(['< 16 inches', '16 - 18 inches', '19 - 21 inches', '22 - 24 inches', '> 24 inches'])),
                Field('waist', requires=IS_IN_SET(['< 24 inches', '24 - 26 inches', '27 - 29 inches', '30 - 32 inches', '33 - 35 inches', '> 35 inches'])),
                Field('shoulder', requires=IS_IN_SET(['< 18 inches', '18 - 20.125 inches', '> 20.125 inches'])),
                Field('hip', requires=IS_IN_SET(['< 38.625 inches', '38.625 - 41 inches ', '41 - 45 inches', '> 45 inches'])),
                Field('wrist', requires=IS_IN_SET(['< 5.5 inches', '5.5 - 6.5 inches', '6.5 - 7.5 inches', '> 7.5 inches'])),
                Field('biceps', requires=IS_IN_SET(['< 11.75 inches', '11.75 - 14 inches', '14 - 16.25 inches', '> 16.25 inches'])),
                Field('forearm', requires=IS_IN_SET(['< 9.25 inches', '9.25 - 11 inches', '11 - 12.5 inches', '> 12.5'])),
                Field('arm_length', requires=IS_IN_SET(['< 43cm', '43 - 46cm', '47 - 49.5cm', '> 49.5cm'])),
                Field('inseam', requires=IS_IN_SET(['< 26.5 inches', '26.5 - 28 inches', '29 - 30 inches', '31 - 32 inches', '> 32 inches'])),
                Field('thigh', requires=IS_IN_SET(['< 18 inches', '18 - 24 inches', '25 - 27 inches', '28 - 30 inches', '> 30 inches'])),
                Field('calf', requires=IS_IN_SET(['< 11 inches', '11 - 13 inches', '14 - 16 inches', '17 - 19 inches', '> 19 inches'])),
                Field('ankle', requires=IS_IN_SET(['< 7 inches', '7 - 8.25 inches', '8.5 - 9.75 inches', '10 - 11.5 inches', '> 11.5 inches', '6', '7'])),
                )

db.Measure2.id.readable = db.Measure2.id.writable = False
db.Measure2.author.readable = db.Measure2.author.writable = False
