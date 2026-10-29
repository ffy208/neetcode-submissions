class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(word + "😭" for word in strs)

    def decode(self, s: str) -> List[str]:
        return s.split("😭")[:-1]
