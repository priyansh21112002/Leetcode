/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int count(struct ListNode* head)
{
    int c=0;
    while(head!=NULL)
    {
        head=head->next;
        c++;
    }
    return c;
} 
struct ListNode* oddEvenList(struct ListNode* head){
int c=count(head);
struct ListNode *temp,*temp1;
temp1=head;
for(int i=0;i<c-1;i++)
temp1=temp1->next;
temp=head;
for(int i=0;i<c/2;i++)
{
temp1->next=temp->next;
temp1=temp1->next;
temp->next=temp->next->next;
temp1->next=NULL;
temp=temp->next;
}
return head;
}