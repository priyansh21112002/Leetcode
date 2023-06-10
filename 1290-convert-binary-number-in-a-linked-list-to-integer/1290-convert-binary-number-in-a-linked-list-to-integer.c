/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 #include<math.h>
int getDecimalValue(struct ListNode* head){
int sum=0,count=0;
struct ListNode* temp=head;

while(temp->next!=NULL)
{
    temp=temp->next;
    count++;
}
temp=head;

while(temp!=NULL)
{
    sum+=(temp->val)*pow(2,count);
    count--;
    temp=temp->next;
}

return sum;
}