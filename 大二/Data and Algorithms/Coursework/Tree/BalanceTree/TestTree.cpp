// TestTree.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "AVLTree.h"
#include "RBTree.h"
#include <time.h>
#include <stdlib.h>
#include <windows.h>

#include <iostream>
#include <vector>
#include <random>
#include <algorithm>
using namespace std;

//std::vector<int> generateUniqueRandomNumbers(int start, int end, unsigned seed) {
//	std::vector<int> numbers;
//	// 填充指定范围内的所有数字
//	for (int i = start; i <= end; ++i) {
//		numbers.push_back(i);
//	}
//	// 使用随机数引擎进行随机洗牌
//	std::seed_seq seq{ seed };
//	std::mt19937 g(seq);
//	std::shuffle(numbers.begin(), numbers.end(), g);
//	return numbers;
//}

int getHeight(TreeNode* root)
{
	return -1;
}


int _tmain(int argc, _TCHAR* argv[])
{
	RBTree rbt;
	AVLTree avl;

	return 0;
}

