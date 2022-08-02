import unittest
from TestTasks import hash_string, HashType


def get_message(algorithm_name: str, website: str) -> str:
    return f"\nTo ensure that the algorithm {algorithm_name} is implemented correctly, " \
           f"you can use this website: \n{website}\n"


class Task1TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        website_sha1 = "https://emn178.github.io/online-tools/sha1.html"
        website_keccak = "https://emn178.github.io/online-tools/keccak_256.html"
        print(get_message("SHA1", website_sha1))
        print(get_message("Keccak", website_keccak))

    def test_default_execute(self):
        expected = "87230ee22218e7f2c203d9db81f6e404996128c9ab273f789047c11c3d499fd2"
        actual_hash = hash_string()
        self.assertEqual(actual_hash, expected)

    def test_diff_hash_functions(self):
        expected = "23b70fdd57680b3b83ab69467c219a6f1a8eed77"
        actual_hash = hash_string(HashType.SHA1)
        self.assertEqual(actual_hash, expected)

        expected = "87230ee22218e7f2c203d9db81f6e404996128c9ab273f789047c11c3d499fd2"
        actual_hash = hash_string(HashType.Keccak)
        self.assertEqual(actual_hash, expected)

    def test_diff_strings(self):
        expected = "f14c40085080e616b081e273527fb09c9fafb1e7"
        actual_hash = hash_string(HashType.SHA1, "New string")
        self.assertEqual(actual_hash, expected)

        expected = "a0682b40992d00d56c642f10b554520df23080b0640fad00712778fa722b2efb"
        actual_hash = hash_string(HashType.Keccak, "New string")
        self.assertEqual(actual_hash, expected)


if __name__ == '__main__':
    unittest.main()
