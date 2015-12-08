
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


db.review.store_id.on_delete = "SET NULL"



#-------------------------
# Testing messure tables
#-------------------------






db.define_table('Measure',
                Field('author'),
                Field('height', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('head', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('neck', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('chest', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('waist', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('shoulder', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('hip', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('wrist', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('biceps', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('forearm', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('arm_length', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('inseam', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('thigh', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('calf', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('ankle', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                )


db.define_table('Measure2',
                Field('author', db.auth_user, default=auth.user_id ),
                Field('height', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('head', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('neck', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('chest', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('waist', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('shoulder', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('hip', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('wrist', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('biceps', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('forearm', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('arm_length', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('inseam', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('thigh', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('calf', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                Field('ankle', requires=IS_IN_SET(['petite', 'regular', 'tall', '4', '5', '6', '7'])),
                )

