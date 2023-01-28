struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* head = (struct ListNode*) malloc (sizeof(struct ListNode));
    bool flag = true;
    head->val = 0;
    head->next = NULL;
    struct ListNode* iter = head;
    int num1 = 0;
    int num2 = 0;
    int sum = 0;
    int carry = 0;
    while (l1 || l2 || carry) {
        if(l1) {
            num1 = l1->val;
            l1 = l1->next;
        }
        if (l2) {
            num2 = l2->val;
            l2 = l2->next;
        }
        sum = num1+num2 + carry;
        if (carry)
            carry = 0;
        if (sum > 9) {
            carry = 1;
            sum = sum%10;
        }
        if (flag) {
            flag = false;
            iter->val = sum;
        } else {
            struct ListNode* node = (struct ListNode*) malloc (sizeof(struct ListNode));
            node->next = NULL;
            iter->next = node;
            node->val = sum;
            iter = iter->next;
        }
        
        num1 = 0;
        num2 = 0;
    }
    
    return head;
}