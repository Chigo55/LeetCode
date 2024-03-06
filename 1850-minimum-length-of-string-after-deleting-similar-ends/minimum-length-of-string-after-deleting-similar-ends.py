class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        count = 0

        while left < right and s[left] == s[right]:
            # 왼쪽에서 동일한 문자 찾기
            while left <= right:
                if s[left] == s[left + 1]:
                    count += 1
                    left += 1
                    if left == len(s) -1:
                        count += 1
                        break
                else:
                    count += 1
                    break
            print(left, count)
            # 오른쪽에서 동일한 문자 찾기
            while left < right:
                if s[right] == s[right - 1]:
                    count += 1
                    right -= 1
                    if right == 0:
                        break
                else:
                    count += 1
                    break
            print(right, count)
            # 동일한 문자를 찾았으면 두 포인터를 다음 위치로 이동
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                break

        return len(s) - count
        