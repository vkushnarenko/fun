from mashumaro import DataClassJSONMixin
from dacite import from_dict
import dataclasses
from datetime import datetime
from dataclasses_json import dataclass_json
from dataclasses import dataclass, field
from typing import Optional, List
import json



@dataclass
class simpleMazafaka(DataClassJSONMixin):
    name: str
    # date: datetime
    nick: str
    cash: Optional[int]


@dataclass
class ComplexMazafaka(DataClassJSONMixin):
    simple: simpleMazafaka
    some: int
    date: int
    another: str
    collect: List[simpleMazafaka]
    supa_simple: simpleMazafaka = field(default=None)

@dataclass_json
@dataclass
class simpleMazafakaA():
    name: str
    date: datetime
    nick: str
    cash: Optional[int]

@dataclass_json
@dataclass
class ComplexMazafakaA():
    simple: simpleMazafakaA
    some: int
    date: int
    another: str
    collect: List[simpleMazafakaA]
    supa_simple: simpleMazafakaA = field(default=None)



json_to_convert = {
    "simple": {"name": "hello999",
               "date": "2020-01-31 14:33:11.971262",
               "nick": "world999",
               "cash": 33},
    "some": 55,
    "another": "kk",
    "date": 243423423423,
    "collect": [{"name": "hello1",
                 "date": "2020-01-31 14:33:11.971262",
                 "nick": "world1",
                 "cash": 11},
                {"name": "hello2",
                 "date": "2020-01-31 14:33:11.971262",
                 "nick": "world2",
                 "cash": 22},
                {"name": "hello",
                 "date": "2020-01-31 14:33:11.971262",
                 "nick": "world3",
                 "cash": 33}]
}


john = ComplexMazafaka.from_dict(json_to_convert)


print(john)
print(john.simple.name)
print(john.supa_simple)
print(john.collect[2].cash)
#
ken_json = json.dumps(json_to_convert)

ken = ComplexMazafaka.from_json(ken_json)

print(ken)
print(ken.simple.name)
print(ken.supa_simple)
print(ken.collect[2].cash)


dacite_ben = from_dict(data_class=ComplexMazafaka, data=json_to_convert)
print(dacite_ben)
print(dacite_ben.simple.name)
print(dacite_ben.supa_simple)
print(dacite_ben.collect[2].cash)


data_json = ComplexMazafakaA.from_dict(json_to_convert)
print(data_json)
print(data_json.simple.name)
print(data_json.supa_simple)
print(data_json.collect[2].cash)



# mashumaro:
#
# Works with datetime and parse it nice
# works bad with str, cause parse there any shit, without type checking


#
#dacite can't recognize date time


# data-class json gives runtime warning for PEP optional and default none
# can work with date time automatically pushes them to from int via timestamp

