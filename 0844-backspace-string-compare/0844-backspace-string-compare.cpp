class Solution {
public:
    bool backspaceCompare(string s, string t) {
        
        stack<int> st,sts;
        for(int i=0;i<s.length();i++){
            if(!st.empty() && s[i]=='#'){
                st.pop();   
            }
            else if(s[i]!='#') st.push(s[i]);
        }
        
        
        for(int i=0;i<t.length();i++){
            if(!sts.empty() && t[i]=='#' ){
                sts.pop();
            }
            else if(t[i]!='#') sts.push(t[i]);
        }
        
        if(sts==st) return true;
        return false;
    }
};