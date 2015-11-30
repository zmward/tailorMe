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

#----------------
# All measurements in centimeters
#---------------

db.define_table('height_table',
                Feild('user', 'reference profile'),
                Feild('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('petite', 'boolean', default=False ), # <5'4'
                Field('regular', 'boolean', default=False), # 5'4-5'9"
                Field('tall', 'boolean', default=False),    # >5'9"
                )


db.define_table('head_table',
                Feild('user', 'reference profile'),
                Feild('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False ), # <56cm
                Field('B', 'boolean', default=False),  # 56-57cm
                Field('C', 'boolean', default=False),  # > 57cm
                )


db.define_table('neck_table',
                Feild('user', 'reference profile'),
                Feild('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False ),  # < 15 inches
                Field('B', 'boolean', default=False),  # 15-16 inches
                Field('B', 'boolean', default=False),     # > 16 inches
                )

db.define_table('chest_table',
                Feild('user', 'reference profile'),
                Feild('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False ), # < 16 inches
                Field('B', 'boolean', default=False),  # 16-18 inches
                Field('C', 'boolean', default=False),  # 19-21
                Field('D', 'boolean', default=False),  # 22-24
                Field('E', 'boolean', default=False),  # > 25
                )

db.define_table('waist_table',
                Feild('user', 'reference profile'),
                Feild('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False ), # < 25 inches
                Field('B', 'boolean', default=False),  # 25-26 inches
                Field('C', 'boolean', default=False),  # 27-29 inches
                Field('D', 'boolean', default=False),  # 30-32 inches
                Field('E', 'boolean', default=False),  # 33-35 inches
                Field('F', 'boolean', default=False),  # > 36 inches
                )

db.define_table('sh_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),  # < 18 inches
                Field('B', 'boolean', default=False),  # 18-20 1/8 inches
                Field('C', 'boolean', default=False),   # > 20 1/8 inches
                )

db.define_table('hip_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),  # < 38 5/8 inches
                Field('B', 'boolean', default=False),  # 38 5/8 - 41 inches
                Field('C', 'boolean', default=False),  # 42-45 inches
                Field('D', 'boolean', default=False),  # > 45 inches
                )

db.define_table('wrist_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),  # < 5 1/2 inches
                Field('B', 'boolean', default=False),  # 5 1/2 - 6 1/2 inches
                Field('C', 'boolean', default=False),  # 6 1/2 - 7 1/2 inches
                Field('D', 'boolean', default=False),  # > 7 1/2 inches
                )

db.define_table('biceps_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),  # < 11 3/4 inches
                Field('B', 'boolean', default=False),  # 11 3/4 - 14 inches
                Field('C', 'boolean', default=False),  # 14 - 16 1/4 inches
                Field('D', 'boolean', default=False),  # > 16 1/4 inches
                )

db.define_table('forearm_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),  # < 9 1/4 inches
                Field('B', 'boolean', default=False),  # 9 1/4 - 11 inches
                Field('C', 'boolean', default=False),  # 11-12 1/2 inches
                Field('D', 'boolean', default=False),  # > 12 1/2 inches
                )

db.define_table('arm_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),  # < 43cm
                Field('B', 'boolean', default=False),  # 43-46cm
                Field('C', 'boolean', default=False),  # 46-49.5cm
                Field('D', 'boolean', default=False),  # > 49.5cm
                )

db.define_table('inseam_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),  # < 26.5 inches
                Field('B', 'boolean', default=False),  # 26.5 - 28 inches
                Field('C', 'boolean', default=False),  # 28 - 29 inches
                Field('D', 'boolean', default=False),  # 29 - 30 inches
                Field('E', 'boolean', default=False),  # 30 - 31 inches
                Field('F', 'boolean', default=False),  # 31 - 32 inches
                Field('G', 'boolean', default=False),  # > 32 inches
                )

db.define_table('thigh_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),  # 18 inches
                Field('B', 'boolean', default=False),  # 18-24 inches
                Field('C', 'boolean', default=False),  # 24-27 inches
                Field('D', 'boolean', default=False),  # 27-30 inches
                Field('E', 'boolean', default=False),  # > 30 inches
                )

db.define_table('calf_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),  # < 11 inches
                Field('B', 'boolean', default=False),  # 11-13 inches
                Field('C', 'boolean', default=False),  # 13-16 inches
                Field('D', 'boolean', default=False),  # 16-19 inches
                Field('E', 'boolean', default=False),  # > 19 inches
                )

db.define_table('ankle_table',
                Field('user', 'reference profile'),
                Field('value', 'float', requires=IS_FLOAT_IN_RANGE(0, 500)),
                Field('A', 'boolean', default=False),  # < 7 inches
                Field('B', 'boolean', default=False),  # 7- 8 1/4 inches
                Field('C', 'boolean', default=False),  # 8 3/8 - 9 7/8 inches
                Field('D', 'boolean', default=False),  # 10 - 11 3/8 inches
                Field('E', 'boolean', default=False),  # > 11 1/2 inches
                )
