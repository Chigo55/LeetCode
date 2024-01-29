class Solution:
    import re                                   # 정규 표현식 라이브러리

    def isPalindrome(self, s: str) -> bool:    # 실행 속도: 36ms
        s = s.lower()
        # 정규 표현식으로 불필요한문자 제거
        s = re.sub('[^a-z0-9]', '', s)          # 알파벳 소문자, 숫자를 제외한 다른 문자를 공백으로 대체(제거)
        return s == s[::-1]                     # while문이 끝날 경우 팰린드롬으로 판한 하여 True 반환