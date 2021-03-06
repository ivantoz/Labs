class bcolors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def degrees_to_direction(angle):
    if 348.75 > angle <= 11.25:
        return 'North'
    elif angle <= 33.75:
        return 'North North East'
    elif angle <= 56.25:
        return 'North East'
    elif angle <= 78.75:
        return 'East North East'
    elif angle <= 101.25:
        return 'East'
    elif angle <= 123.75:
        return 'East South East'
    elif angle <= 146.25:
        return 'South East'
    elif angle <= 168.75:
        return 'South South East'
    elif angle <= 191.25:
        return 'South'
    elif angle <= 213.75:
        return 'South South West'
    elif angle <= 236.25:
        return 'South West'
    elif angle <= 258.75:
        return 'West South West'
    elif angle <= 281.25:
        return 'West'
    elif angle <= 303.75:
        return 'West North West'
    elif angle <= 326.25:
        return 'North West'
    elif angle <= 348.75:
        return 'North North West'
