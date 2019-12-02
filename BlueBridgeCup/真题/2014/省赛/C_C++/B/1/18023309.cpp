/*
标题：啤酒和饮料

    啤酒每罐2.3元，饮料每罐1.9元。小明买了若干啤酒和饮料，一共花了82.3元。

    我们还知道他买的啤酒比饮料的数量少，请你计算他买了几罐啤酒。

    注意：答案是一个整数。请通过浏览器提交答案。

    不要书写任何多余的内容（例如：写了饮料的数量，添加说明文字等）。
*/
#include <iostream>

using namespace std;

int main(){
	for(int i = 0; i < 100; i++){
		for(int j = 0; j < 100; j++){
			if(2.3 * i + 1.9 * j == 82.3 && i < j){
				cout << "beer: " << i << " drink: " << j << endl;
			}
		}
	}
	return 0;
}
