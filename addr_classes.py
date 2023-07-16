from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone: Phone):
        if phone.value not in [p.value for p in self.phones]:
            self.phones.append(phone)
            return f"phone {phone} add to contact {self.name}"
        return f"{phone} present in phones of contact {self.name}"

    def change_phone(self, old_phone, new_phone):
        for idx, p in enumerate(self.phones):
            if old_phone.value == p.value:
                self.phones[idx] = new_phone
                return f"old phone {old_phone} change to {new_phone}"
        return f"{old_phone} not present in phones of contact {self.name}"

    def remove_phone(self, phone) -> None:
        idx = -1

        for i, p in enumerate(self.phones):
            if phone.value == p.value:
                idx = i
                break

        if idx == -1:
            return f"There are no {phone} for {self.name}"
        else:
            self.phones.pop(idx)
            return f"{phone} was deleted successfully"

    def __str__(self) -> str:
        return f"{self.name}: {', '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[str(record.name)] = record
        return f"Contact {record} add success"

    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())
