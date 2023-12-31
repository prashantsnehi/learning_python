def get_event_date(event):
    return event.date


def current_user(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            # machines[event.machine] = set()
            machines[event.machine] = []
        if event.type == "login":
            # machines[event.machine].add(event.user)
            machines[event.machine].append(event.user)
        elif event.type == "logout" and event.user in machines[event.machine]:
            machines[event.machine].remove(event.user)
    return machines


def generate_report(machines):
    for machine_id, curr_user in machines.items():
        # print('user: ' + str(curr_user) + ' ' + str(len(curr_user)))
        if len(curr_user) > 0:
            print("{}: {}".format(machine_id, ", ".join(curr_user)))


class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:42', 'login', 'mailserver.local', 'chris'),
    Event('2020-01-23 11:24:42', 'login', 'mailserver.local', 'kuldeep'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'sushil'),
    Event('2020-01-21 08:20:01', 'logout', 'webserver.local', 'tusshar')
]

users = current_user(events)
print(users)

generate_report(users)
