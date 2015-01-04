'''
    Call run.py to execute Agent Based Model code to test 
    character stats
'''
import agents, model

if __name__ == "__main__":
    teams = model.instantiate_agents()
    model.trivial_battle(teams)