class Car(object):
    speed = 0
    vehicle_type = ''

    # class car constructor
    def __init__(self, name='General', model='GM', vehicle_type=None):
        # initialization of variables
        self.moving_speed = 0
        self.speed = 0
        self.name = name
        self.model = model
        self.vehicle_type = vehicle_type
        # setting number of wheels
        wheels = {'MAN': 8, 'Porshe': 4, 'Koenigsegg': 4}
        doors = {'Porshe': 2, 'Koenigsegg': 2, 'Opel': 4}
        self.num_of_wheels = wheels.get(self.name)
        self.num_of_doors = doors.get(self.name)

    # function for calculating speed
    def drive(self, moving_speed):
        if self.vehicle_type == 'trailer':
            self.speed = moving_speed * 11
        else:
            if moving_speed is not 0:
                self.speed = 10 ** moving_speed
        return self

    # function for setting type to saloon
    def is_saloon(self):
        if self.vehicle_type == 'trailer':
            return False
        else:
            self.vehicle_type == 'saloon'
            return True