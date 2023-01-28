int search(int* nums, int numsSize, int target){
    int l = 0, r = numsSize - 1;
    
    while (l <= r) {
        int m = (l + r) >> 1;
        int left = nums[l];
        int right = nums[r];
        int middle = nums[m];
        
        if (middle == target)
            return m;
        
        if (middle >= left) {
            if (target < middle && target >= left)
                r = m - 1;
            else
                l = m + 1;
        } else {
            if (target > middle && target <= right)
                l = m + 1;
            else
                r = m - 1;
        }
    }
    return -1;
}