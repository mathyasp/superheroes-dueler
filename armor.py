import random

class Armor:
  def __init__(self, name, max_block):
    '''Instantiate instance properties.
        name: String
        max_block: Integer
    '''
    # TODO: Create instance variables for the values passed in.
    self.name = name
    self.max_block = max_block

  def block(self):
    ''' Return a value between 0 and the value set by self.max_block.'''

    # Pick a random value between 0 and self.max_block
    random_value = random.randint(0, self.max_block)
    return random_value


if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  armor = Armor("Debugging Shield", 10)
  print(armor.name)
  print(armor.block())
  