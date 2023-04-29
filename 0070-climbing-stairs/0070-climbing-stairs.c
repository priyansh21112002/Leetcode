int cache[100];

int climbStairs(int n) {
    if (n == 1 || n == 2) {
        return n;
    }
    else { 
        if (cache[n] == NULL) { 
        cache[n] = climbStairs(n-1) + climbStairs(n-2);
        }     
        return cache[n];
    }
}