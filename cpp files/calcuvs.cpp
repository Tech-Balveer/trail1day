#include<iostream>
using namespace std;

int main()
{
	char operation;
	float num1,num2;
	cout<<"enter operator either +or-or*or/:";
	cin>>operation;
	cout<<"enter two operarands:";
	cin>>num1>>num2;
	switch(operation) {
		
		case'+':
			cout<<num1+num2;
			break;
		case'-':
			cout<<num1-num2;
				break;
		case'*':
			cout<<num1*num2;
				break;
		case'/':
			cout<<num1/num2;
			break;
			default:
				
			
		/*if operator is otherthan+,-,*,/,error message is shown*/
			cout<<"error! operator is not correct";
			break;
			
		
		}
	}
			
	
