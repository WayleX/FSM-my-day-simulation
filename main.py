import random
from events import States, Random_Events

class StateQueue:
    def __init__(self):
        self.events = []
    def add_state(self, event):
        self.events.append(event)
    def get_state(self):
        return self.events.pop()
    def clear_state(self):
        self.events = []

class FSM_daily_routine:
    def __init__(self):
        self.hour = 24
        self.energy = 100
        self.happiness = 60
        self.state = 'sleeping'
        self.parameters = [self.hour,self.energy,self.happiness]
        self.queue = StateQueue()
        self.queue.add_state(States.sleep_state)
        self.state_dict = {'sleeping':States.sleep_state,
                            'eating':States.eat_state,
                            'enjoying beer':States.beer_state,
                            'commuting':States.commute_state,
                            'working':States.work_state,
                            'resting':States.rest_state}
    def run(self):
        i = 0
        while i < 240:
            if self.energy > 0 and self.happiness > 0:
                if self.hour == 24:
                    self.hour = 0
                    print(f'=== NEW DAY [DAY{i//24 + 1}] ===')
                self.parameters[0] = self.hour
                self.run_state()
                self.simulate_event()
                self.energy,self.happiness = self.parameters[1],self.parameters[2]
                self.print_current_state()
                self.hour += 1
            else:
                print("""
                _______  _______ _________ _______  ______  
        |\     /|(  ___  )(  ____ \\__   __/(  ____ \(  __  \ 
        | )   ( || (   ) || (    \/   ) (   | (    \/| (  \  )
        | | _ | || (___) || (_____    | |   | (__    | |   ) |
        | |( )| ||  ___  |(_____  )   | |   |  __)   | |   | |
        | || || || (   ) |      ) |   | |   | (      | |   ) |
        | () () || )   ( |/\____) |   | |   | (____/\| (__/  )
        (_______)|/     \|\_______)   )_(   (_______/(______/ 
                    """)
                break
            i += 1
    def simulate_event(self):
        chance = random.random()
        if chance <= 0.05:
            Random_Events.forgot_deadline(self.parameters)
            self.queue.clear_state()
            self.state = 'working'
            self.queue.add_state(self.state_dict['working'])
        if 0.05 < chance <= 0.1 and self.state == 'sleeping':
            Random_Events.cat_woke_up(self.parameters)
            self.queue.clear_state()
            self.state = 'resting'
            self.queue.add_state(self.state_dict['resting'])
        if 0.1 < chance <= 0.12 and self.state != 'sleeping':
            Random_Events.kryven_dropped_lab(self.parameters)
            self.queue.clear_state()
            self.state = 'working'
            self.queue.add_state(self.state_dict['working'])
        if 0.12 < chance <= 0.13 and self.state != 'sleeping':
            Random_Events.call_beer(self.parameters)
            self.queue.clear_state()
            self.state = 'enjoying beer'
            self.queue.add_state(self.state_dict['enjoying beer'])
    def run_state(self):
        current_state = self.queue.get_state()
        new_state = current_state(self.parameters)
        self.state = new_state
        self.queue.add_state(self.state_dict[new_state])
    def print_current_state(self):
        print(f'Hour {self.hour}: I am {self.state}, my energy: {self.energy},my hapiness:{self.happiness}')
if __name__ == '__main__':
    s = FSM_daily_routine()
    s.run()