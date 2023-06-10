/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteMiddle(struct ListNode* head){
    struct ListNode *temp1=head,*temp2=head,*t;
    
    if(head->next==NULL)
    {
        head=NULL;
        return head;
    }

    while(temp1!=NULL && temp1->next!=NULL)
    {
        t=temp2;
        temp1=temp1->next->next;
        temp2=temp2->next;
    }
    t->next=temp2->next;

    return head;
}