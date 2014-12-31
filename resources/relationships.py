

def update_relationship(self, whom, update):
	# whom = "thomas"
    pass
	# update = ("category":a_category, "change":int(a_change), "absolute":a_new_val)

class Character():
    def __init__(self,name):
        self.name = name
        self.character_index = False
        self.my_class = "human" # bathroom_troll, snake, 3_headed_dog
        self.outward_appearance = [self.my_class]
        self.rels = {}
        self.self_esteem = 0
        self.level = 1
        
    def update_relationship(self,other):
        '''
        Called whenever a Game Event happens such that a relationship needs to
        be updated. 
        Examples of such Game Events: 
        Caught Stealing, Initiate Combat, 
        Nonhealing Spells (spells have caveats), meeting a person for the
        first time, certain words depending on personality and context.
        '''
        
        if other.name not in [person_list["name"] for person_list in self.rels]:
            #print("My name is %s and Other's name is %s" %(self.name, other.name))
            self.build_rels(name=other.name)
        def new_acquaintence(other):
            pass #print("double test")
        new_acquaintence(other)

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