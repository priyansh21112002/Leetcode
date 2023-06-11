/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int llength(struct ListNode* head)
{
    struct ListNode *temp=head;
    int count=0;

    while(temp!=NULL)
    {
        count++;
        temp=temp->next;
    }
    return count;
}

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
  int lengthA=llength(headA), lengthB=llength(headB);
  struct ListNode *temp1=headA,*temp2=headB;

  if(lengthA<lengthB)
  {
      while(lengthA!=lengthB && temp2!=NULL)
      {
          temp2=temp2->next;
          lengthB--;
      }
  }
  else if(lengthA>lengthB)
  {
      while(lengthA!=lengthB && temp1!=NULL)
      {
          temp1=temp1->next;
          lengthA--;
      }
  }

  while(temp1!=temp2 && temp1!=NULL && temp2!=NULL)
      {
          temp1=temp1->next;
          temp2=temp2->next;
      }
  return temp1;
}