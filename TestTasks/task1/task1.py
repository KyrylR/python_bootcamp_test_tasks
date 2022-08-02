from enum import Enum
from .hash import Hash


class HashType(Enum):
    Keccak = 1
    SHA1 = 2


def hash_string(hast_type: HashType = HashType.Keccak, string: str = 's = "Python Bootcamp"') -> str:
    """
    Hashes the given string.
    :param hast_type: specific hash function type (default: Keccak)
    :param string: plain text (default: s = "Python Bootcamp")
    :return: Hashed string.
    """
    if hast_type is HashType.Keccak:
        return Hash().to_keccak(string)

    if hast_type is HashType.SHA1:
        return Hash().to_sha1(string)