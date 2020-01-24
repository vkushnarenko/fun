import dataclasses
from dataclasses import dataclass

@dataclass
class Big:
    one: int = '1'
    two: int = '2'
    three: int =  '3'
    four: int =  '4'

@dataclass
class Small:
    one: int = None
    four: int = None

mega = Big()
mini = Small()


megadict=dataclasses.asdict(mega)
print(megadict)
small = dataclasses.asdict(mini)
print(small)

new_dict = dict(filter(lambda key: key[0] in small, megadict.items()))

print(new_dict)