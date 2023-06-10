/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head){
    struct ListNode *temp=head;
    int i,count=0;

    if(head==NULL)
    return head;

    else{
    while(temp!=NULL)
    {
        temp=temp->next;
        count++;
    }
    temp=head;
    if(count%2==0)
    {
        for(i=0;i<count/2;i++)
        temp=temp->next;

        return temp;
    }

    else
    {
        for(i=0;i<count/2;i++)
        temp=temp->next;

        return temp;
    }
    }
}