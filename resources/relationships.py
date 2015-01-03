

def update_relationship(self, whom, update):
	# whom = "thomas"
    pass
	# update = ("category":a_category, "change":int(a_change), "absolute":a_new_val)

class Character():
    def __init__(self,name, already_existing=False):
        self.name = name
        self.character_index = False
        self.my_class = "human" # bathroom_troll, snake, 3_headed_dog
        self.outward_appearance = [self.my_class]
        self.rels = {}
        self.self_esteem = 0
        self.level = 1

        if not already_existing:
            f = open('names.txt', 'r+'):
            # filter (lambda ?) how do I get the max index??



    def assign_index():
        with open("names.txt", "r+") as f:
            f = f.read().split('\t')
        
    def update_relationship(self,other,change):
        '''
        type(self,other) = (object,object) 
        type(change) = dict
        Called whenever a Game Event happens such that a relationship needs to
        be updated. 
        Examples of such Game Events: 
        Caught Stealing, Initiate Combat, 
        Nonhealing Spells (spells have caveats), meeting a person for the
        first time, certain words depending on personality and context.

        For starters, everyone will assume the best in people, but later
        we may introduce misanthropy.
        '''

        change_to, change_from = [v for k,v in change.items()]
        

        

        

        

list1 = [1,2,3,4,5,6]
list1.delitem("1")

harry = Character(name="harry")
sam = Character(name="sam")
emma.update_relationship(sam)
sam.update_relationship(emma)
for relationship_list in emma.rels:
    for k,v in relationship_list.items():
        print("%s, %s" %(k,v))


def cast_shapeshift_spell(character_name,transforms_to):
    character_name.outward_appearance = transforms_to

cast_shapeshift_spell(snape,"snake")