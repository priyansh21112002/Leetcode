class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = {}   # mapping from s → t
        t_s = {}   # mapping from t → s
        n = len(s)

        if len(s) != len(t):
            return False
        
        for i in range(n):
            sc, tc = s[i], t[i]

            # check s → t mapping
            if sc in s_t:
                if s_t[sc] != tc:   # mismatch in mapping
                    return False
            else:
                s_t[sc] = tc

            # check t → s mapping
            if tc in t_s:
                if t_s[tc] != sc:
                    return False
            else:
                t_s[tc] = sc

        return True
