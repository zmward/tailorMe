__author__ = 'pmercado'



db.define_table('profile',
                Field('User_name'),
                Field('First_name'),
                Field('Last_name'),
                Field('email'),
                Field('password'),

                )

db.define_table('Measure',
                Field('user', 'reference profile'),
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

db.define_table('height_table',
                Feild('user', 'reference profile'),
                Feild('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('petite', 'boolean', default=False ),
                Field('regular', 'boolean', default=False),
                Field('tall', 'boolean', default=False),
                )


db.define_table('head_table',
                Feild('user', 'reference profile'),
                Feild('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('petite', 'boolean', default=False ),
                Field('regular', 'boolean', default=False),
                Field('tall', 'boolean', default=False),
                )


db.define_table('neck_table',
                Feild('user', 'reference profile'),
                Feild('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('petite', 'boolean', default=False ),
                Field('regular', 'boolean', default=False),
                Field('tall', 'boolean', default=False),
                )

db.define_table('chest_table',
                Feild('user', 'reference profile'),
                Feild('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('petite', 'boolean', default=False ),
                Field('regular', 'boolean', default=False),
                Field('tall', 'boolean', default=False),
                )

db.define_table('waist_table',
                Feild('user', 'reference profile'),
                Feild('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('petite', 'boolean', default=False ),
                Field('regular', 'boolean', default=False),
                Field('tall', 'boolean', default=False),
                )

db.define_table('sh_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),
                Field('B', 'boolean', default=False),
                Field('C', 'boolean', defalt=False),
                )

db.define_table('hip_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),
                Field('B', 'boolean', default=False),
                Field('C', 'boolean', defalt=False),
                )

db.define_table('wrist_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),
                Field('B', 'boolean', default=False),
                Field('C', 'boolean', defalt=False),
                )

db.define_table('biceps_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),
                Field('B', 'boolean', default=False),
                Field('C', 'boolean', defalt=False),
                )

db.define_table('forearm_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),
                Field('B', 'boolean', default=False),
                Field('C', 'boolean', defalt=False),
                )

db.define_table('arm_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),
                Field('B', 'boolean', default=False),
                Field('C', 'boolean', defalt=False),
                )

db.define_table('inseam_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),
                Field('B', 'boolean', default=False),
                Field('C', 'boolean', defalt=False),
                )

db.define_table('thigh_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),
                Field('B', 'boolean', default=False),
                Field('C', 'boolean', defalt=False),
                )

db.define_table('calf_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),
                Field('B', 'boolean', default=False),
                Field('C', 'boolean', defalt=False),
                )

db.define_table('ankle_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),
                Field('B', 'boolean', default=False),
                Field('C', 'boolean', defalt=False),
                )
