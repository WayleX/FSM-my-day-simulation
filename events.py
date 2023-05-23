class States:
    @staticmethod
    def eat_state(parameters):
        parameters[1] += 15
        parameters[2] += 3
        #state = 'eating'
        if 12 <= parameters[0] <= 16:
            new_state = 'enjoying beer'
        elif 8 <= parameters[0] < 12:
            new_state = 'commuting'
        else:
            new_state = 'working'
        return new_state
    @staticmethod
    def beer_state(parameters):
        parameters[2] += 11
        new_state = 'resting'
        #state = 'enjoying beer'
        return new_state
    @staticmethod
    def commute_state(parameters):
        parameters[1] -= 8
        parameters[2] -= 2
        #state = 'commuting'
        if parameters[0] > 18:
            new_state = 'eating'
        else:
            new_state = 'working'
        return new_state
    @staticmethod
    def work_state(parameters):
        parameters[1] -= 10
        parameters[2] -= 5
        if parameters[0] < 8:
            new_state = 'sleeping'
        elif 8 <= parameters[0] <= 13:
            new_state = 'working'
        elif 13 < parameters[0] <= 16:
            new_state = 'eating'
        elif 16 < parameters[0] <= 18:
            new_state = 'eating'
        elif 18 < parameters[0] <= 21:
            new_state = 'commuting'
        elif 21 < parameters[0] <= 22:
            new_state = 'working'
        else:
            new_state = 'sleeping'
        #state = 'working'
        return new_state
    @staticmethod
    def sleep_state(parameters):
        parameters[1] += 8
        parameters[2] += 2
        #state = 'sleeping'
        if parameters[0] < 8:
            return 'sleeping'
        else:
            return 'eating'
    @staticmethod
    def rest_state(parameters):
        parameters[1] += 5
        parameters[2] += 2
        if parameters[0] <= 9:
            return 'sleeping'
        return 'working'
class Random_Events:
    @staticmethod
    def kryven_dropped_lab(parameters):
        parameters[1] -= 12
        parameters[2] += 1
        print(f'Hour {parameters[0]}: New lab. Now I am doing DM lab')
    @staticmethod
    def cat_woke_up(parameters):
        parameters[1] -= 15
        print(f'Hour {parameters[0]}: Now I am feeding my cat')
    @staticmethod
    def forgot_deadline(parameters):
        parameters[1] -= 13
        parameters[2] -= 3
        print(f'Hour {parameters[0]}: I forgor. Now I will be catching deadline')
    @staticmethod
    def call_beer(parameters):
        parameters[1] -= 5
        parameters[2] += 3
        print(f'Hour {parameters[0]}: Nice call for beer')
