'''
    The model.py module takes input from run.py to create
    a number of agents. The agents are set to interact with
    one another according to their characteristics (stats).
'''

import agents

def instantiate_agents(num_agents=1000,evenly_matched=True,**kwargs):
    '''
        Create a handful of agents, (1000, evenly matched by default)
        to pit against one another. For now, they attack as quickly as
        your RAM will allow, but later functionality will allow for turn based
        calculations.
    '''

    if evenly_matched:
        half_the_agents = int(round((num_agents/2)))
        
        red_team = []
        print("instantiating Red agents")
        for redTeamer in range(half_the_agents):
            red_team.append(agents.Agent())
        
        blue_team = []
        print("instantiating Blue agents")
        for redTeamer in range(half_the_agents):
            blue_team.append(agents.Agent())

        print("Red Team vs Blue Team, %s vs %s" % (len(red_team),
                                                    len(blue_team)))
        whole_lot = [red_team,blue_team]
        
        return(whole_lot)


def trivial_battle(teams):
    if teams!=[]:
        for redTeamer in teams[0]:
            redTeamer.attack(teams[1][0])
            teams[1][0].status_report()