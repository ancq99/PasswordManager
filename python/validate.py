import re


def validateOther(data: str):
    pattern = re.compile(r"""[\'\"!@#$%^&*()\-+=\[\]{}|<>?/]""")
    if re.fullmatch(pattern, data):
        return True

    return False


def validateEmail(data: str):
    pattern = re.compile(r"^[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$", re.I)
    if re.fullmatch(pattern, data):
        return True

    return False


def validateEmailList(data: str):
    pattern = re.compile(r"^$|^[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$", re.I | re.M)
    if re.match(pattern, data):
        return True

    return False


def validatePassword(data: str):
    pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{10,}")
    if re.fullmatch(pattern, data):
        return True

    return False
