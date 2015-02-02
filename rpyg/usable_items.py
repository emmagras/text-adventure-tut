from items import Item

class UsableItem(Item):
    """The base class for all usable items"""
    def __init__(self,
                name,
                description,
                weight,
                actions=[],
                **kwargs):
        self.name = name
        self.description = description
        self.weight = weight

        if "contents" in kwargs.keys():
            self.contents = [c for c in kwargs["contents"]]

    def __str__(self):
        return "{}\n=====\n{}\n".\
            format(self.name, self.description)

    def do_action(self, *args, **kwargs):
        ''' This function will handle actions on items
            which have more than one way to be interacted with '''
        raise NotImplementedError()

class TreasureChest(UsableItem):
    '''
        A simple box containing an Item

        Implemented to replace the following code from LootRoom in tiles.py
    '''
    def __init__(self, 
                is_lockable="unlocked",
                is_openable="closed",
                weight=5,
                contents=[],
                actions=["open","close","lock","unlock"]):

        self.description = "A simple wooden box with a lid"
        self.is_lockable = "unlocked"
        self.is_openable = "closed"
        self.weight = weight
        self.contents = contents
        self.actions = self.available_actions()

        super().__init__(name="{} and {} Treasure Chest".\
                format(str(self.is_lockable).capitalize(),
                        str(self.is_openable)),
            description=self.description,
            is_lockable=self.is_lockable,
            is_openable=self.is_openable,
            weight=self.weight,
            contents=self.contents,
            actions=self.actions)

    def available_actions(self):
        '''
            Checks which actions are available for the item. Makes sure Closed
            doors cannot be Closed again.
        '''
        actions = []
        if self.is_lockable:
            if self.is_lockable == "unlocked":
                actions.append("unlock")
            else:
                actions.append("lock")
        if self.is_openable:
            if self.is_openable == "closed":
                actions.append("open")
            else:
                actions.append("close")
        return(actions)

    def do_action(self, *args, **kwargs):
        ''' This function will handle actions on items
            which have more than one way to be interacted with
        '''
        if "open" in args:
            self.open_up()
        if "close" in args:
            self.shut()
        if "lock" in args:
            self.lock()
        if "unlock" in args:
            self.unlock()


    def open_up(self):
        self.is_openable = "opened"
    def shut(self):
        self.is_openable = "closed"
    def lock(self):
        self.is_lockable = "locked"
    def unlock(self):
        self.is_openable = "unlocked"

    def give_content_item(self, item_name):
        content_index = [item.name for item in self.contents].index(item_name)
        the_character.inventory.append(contents.pop(content_index))

    def show_contents(self):
        return ["{}: {}\n=====\n".format\
            (str(item.name),str(item.description)) \
                for item in self.contents]

class Lock(UsableItem):
    '''
        Locks prevent items from doing their action.
    '''
    def __init__(self,
                is_lockable=False,
                weight=2.5,
                mechanical=True,
                key=False):
        self.is_lockable = is_lockable
        self.weight = weight

    def lock(self):
        
    def change_lock(self):
        if self.is_lockable:
            if self.is_lockable == "unlocked"
                self.is_lockable = "locked"
            else:
                self.is_lockable = "unlocked"
        else:
            self.lock_fail()

    
    def lock_fail(self):
        print("This door does not have a lock, and this message shouldnt"\
            +" ever be seen.")

class Door(UsableItem):
    def __init__(self,
                is_openable=False,
                is_lockable=False
                weight=35,
                base_hp=100):
        self.is_openable = is_openable
        self.weight = weight

        self.lock = Lock(is_lockable)

        super().__init__(name="Door",description="A heavy wooden door with\
            rusty hinges sits {} in front of you."\
                .format(str(self.is_lockable),str(self.is_openable)))

    def do_action(self, *args, **kwargs):
        ''' This function will handle actions on items
            which have more than one way to be interacted with
        '''
        if "open" in args:
            self.open_up()
        if "close" in args:
            self.shut()
        if "lock" in args:
            self.lock()
        if "unlock" in args:
            self.unlock()


    def open_up(self):
        self.is_openable = "opened"
    def shut(self):
        self.is_openable = "closed"