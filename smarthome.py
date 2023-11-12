import subprocess
import re

class Lamp:
    def __init__(self, ip, token):
        self.__ip = ip
        self.__token = token
        self.__generic_command = ["miiocli", "genericmiot", "--ip", self.__ip, "--token", self.__token]
        self.ambient = Ambient(self)
        self.light = Light(self)

    def get_property_value(self, property_name, print_text):
        command = self.__generic_command + ["status"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        response = stdout.decode('utf-8')

        pattern = r".+\(" + property_name + ", access: .+\): (\d+|True|False)"
        match = re.search(pattern, response)
        information = match.group(1)
        print(f"[GET] {print_text}: ", end="")
        return information

    def set_property_value(self, property_name, print_text, value):
        command = self.__generic_command + ["set", property_name, str(value)]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate()
        print(f"[SET] {print_text}: {value}")

    @property
    def status(self):
        command = self.__generic_command + ["status"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8')

    @status.setter
    def status(self, value):
        if (isinstance(value, bool)
                or isinstance(value, int) and value in [0, 1]
                or isinstance(value, str) and value in ["0", "1"]):
            self.set_property_value("light:on", "Light status", bool(int(value)))
            self.set_property_value("ambient-light:on", "Ambient-light status", bool(int(value)))


class Ambient:
    def __init__(self, main):
        self.__main = main
    @property
    def status(self):
        return self.__main.get_property_value("ambient-light:on", "Ambient-light status")

    @status.setter
    def status(self, value):
        if (isinstance(value, bool)
                or isinstance(value, int) and value in [0, 1]
                or isinstance(value, str) and value in ["0", "1"]):
            self.__main.set_property_value("ambient-light:on", "Ambient-light status", bool(int(value)))

    @property
    def color(self):
        return self.__main.get_property_value("ambient-light:color", "Ambient-light color")

    @color.setter
    def color(self, value):
        min_value = 1
        max_value = 16777215
        if (isinstance(value, int)
                or isinstance(value, str) and value.isdigit()):
            if min_value <= int(value) <= max_value:
                self.__main.set_property_value("ambient-light:color", "Ambient-light color", int(value))
            else:
                print(f"Value should be between {min_value} and {max_value}!")
        elif isinstance(value, str) and bool(re.match(r'^[0-9a-fA-F]+$', value.replace("#", ""))):
            self.__main.set_property_value("ambient-light:color", "Ambient-light color", int(value.replace("#", ""), 16))
        else:
            print("Value can be integer or hex!")

    @property
    def brightness(self):
        return self.__main.get_property_value("ambient-light:brightness", "Ambient-light brightness")

    @brightness.setter
    def brightness(self, value):
        min_value = 1
        max_value = 100
        if (isinstance(value, int)
                or isinstance(value, str) and value.isdigit()):
            if min_value <= int(value) <= max_value:
                self.__main.set_property_value("ambient-light:brightness", "Ambient-light brightness", int(value))
            else:
                print(f"Value should be between {min_value} and {max_value}!")

    @property
    def saturability(self):
        return self.__main.get_property_value("ambient-light:saturability", "Ambient-light saturability")

    @saturability.setter
    def saturability(self, value):
        min_value = 1
        max_value = 100
        if (isinstance(value, int)
                or isinstance(value, str) and value.isdigit()):
            if min_value <= int(value) <= max_value:
                self.__main.set_property_value("ambient-light:saturability", "Ambient-light saturability", int(value))
            else:
                print(f"Value should be between {min_value} and {max_value}!")


class Light:
    def __init__(self, main):
        self.__main = main
    @property
    def status(self):
        return self.__main.get_property_value("light:on", "Light status")

    @status.setter
    def status(self, value):
        if (isinstance(value, bool)
                or isinstance(value, int) and value in [0, 1]
                or isinstance(value, str) and value in ["0", "1"]):
            self.__main.set_property_value("light:on", "Light status", bool(int(value)))

    @property
    def color(self):
        return self.__main.get_property_value("light:color-temperature", "Light color temperature")

    @color.setter
    def color(self, value):
        min_value = 2700
        max_value = 6500
        if (isinstance(value, int)
                or isinstance(value, str) and value.isdigit()):
            if min_value <= int(value) <= max_value:
                self.__main.set_property_value("light:color-temperature", "Light color temperature", int(value))
            else:
                print(f"Value should be between {min_value} and {max_value}!")
        else:
            print("Value can be integer!")

    @property
    def brightness(self):
        return self.__main.get_property_value("light:brightness", "Light brightness")

    @brightness.setter
    def brightness(self, value):
        min_value = 1
        max_value = 100
        if (isinstance(value, int)
                or isinstance(value, str) and value.isdigit()):
            if min_value <= int(value) <= max_value:
                self.__main.set_property_value("light:brightness", "Light brightness", int(value))
            else:
                print(f"Value should be between {min_value} and {max_value}!")
