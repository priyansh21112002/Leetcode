/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode *temp=head,*t=head;

    if(head==NULL)
        return false;

    while(temp!=NULL && temp->next!=NULL)
    {
        temp=temp->next->next;
        t=t->next;

        if(temp==t)
        return true;
    }
return false;
 
}