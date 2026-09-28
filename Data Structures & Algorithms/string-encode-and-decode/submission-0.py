import json

class Solution:
    def encode(self, strs: List[str]) -> str:
        str = json.dumps(strs)
        return str

    def decode(self, s: str) -> List[str]:
        strs = json.loads(s)
        return strs