class NameTooShort(Exception):
    def __init__(self, message, *args):
        super().__init__(message, args)


class MustContainSymbol(Exception):
    def __init__(self, message, *args):
        super().__init__(message, args)


class InvalidDomainError(Exception):
    def __init__(self, message, *args):
        super().__init__(message, args)


command = input()

while command != "End":
    try:
        if "@" not in command:
            raise MustContainSymbol("The e-mail must contain a @")
        command = command.split("@")

        if len(command[0]) <= 4:
            raise NameTooShort("The e-mail name is too short")

        command = command[1].split(".")

        if command[1] != "com" and command[1] != "bg" and command[1] != "org" and command[1] != "net":
            raise InvalidDomainError("The e-mail domain is invalid")
    except NameTooShort as e:
        print(e)
    except InvalidDomainError as e:
        print(e)
    except MustContainSymbol as e:
        print(e)
    except IndexError as e:
        print(e)
    command = input()

