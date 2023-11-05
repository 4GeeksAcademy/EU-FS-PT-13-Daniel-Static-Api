
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
import random

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []

    def _generateId(self):
        return random.randint(0, 99999999)

    def add_member(self, member):
        member_id = member.get("id", self._generateId())
        member["id"] = member_id
        self._members.append(member)
        return member_id

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
        return False

    def update_member(self, id, updated_member_info):
        for member in self._members:
            if member["id"] == id:
                member.update(updated_member_info)
                return True
        return False

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        return self._members
