
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [ # lista
            { 
                "id": self._generateId(),
                "first_name": "Michael",
                "last_name": last_name,
                "age": 64,
                "lucky_numbers": [46, 14, 63]
            },
             {
                "id": self._generateId(),
                "first_name": "Latoya",
                "last_name": last_name,
                "age": 68,
                "lucky_numbers": [4, 11, 33]
            },
             {
                "id": self._generateId(),
                "first_name": "Janet",
                "last_name": last_name,
                "age": 58,
                "lucky_numbers": [6, 22, 7]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)
        # fill this method and update the return
        pass

    def delete_member(self, id):
        for index, member in enumerate(self._members):  
            if member["id"] == id:
                return self._members.pop(index) # retorna self members q incluye el done true 
            
        """ OTRA OPCION 
    def delete_member(self, id):
        for member in self._members:
            if member ["id"] == id:
                self._members.remove(member)
                return {"done":True}
        pass """

    def get_member(self, id):
        for member in self._members:
            if member ["id"] == id:
                return member
        # fill this method and update the return
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
