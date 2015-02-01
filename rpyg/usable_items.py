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
    def __init__(self, is_locked=False, chest_contents=None):
        self.is_lockable = "unlocked"
        self.is_openable = "closed"
        self.weight = 5
        self.contents = contents
        self.actions = ["open","close","lock","unlock"]

        super().__init__(name="{} and {} Treasure Chest".\
            format(str(self.is_lockable).capitalize(),str(self.is_openable)),
            description="A simple wooden box with a lid",
            weight=self.weight,
            contents=self.contents)

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



class Door(UsableItem):
    def __init__(self, is_locked):
        self.is_lockable = "unlocked"
        self.is_openable = "opened"
        self.weight = 35

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
    def lock(self):
        self.is_lockable = "locked"
    def unlock(self):
        self.is_openable = "unlocked"