#include <iostream>
#include <stack>
#include <vector>
#include <string>

using namespace std;

vector<string> all_sequences;
const vector<char> input = {'A', 'B', 'C', 'D'};

/**
 * @brief 递归回溯函数，生成所有可能的出栈序列
 * @param s 当前栈的状态
 * @param output 当前生成的出栈序列
 * @param next_input 下一个要进栈的元素的索引
 */
void backtrack(stack<char> s, string output, int next_input) {
    // 递归终止条件：所有元素已入栈且栈为空时，记录当前序列
    if (next_input == input.size() && s.empty()) {
        all_sequences.push_back(output);
        return;
    }

    // 尝试将下一个元素入栈
    if (next_input < input.size()) {
        stack<char> s_copy = s;  // 创建当前栈的拷贝
        s_copy.push(input[next_input]);  // 将下一个元素入栈
        backtrack(s_copy, output, next_input + 1);  // 递归处理下一个元素
    }

    // 尝试将栈顶元素出栈
    if (!s.empty()) {
        stack<char> s_copy = s;  // 创建当前栈的拷贝
        char c = s_copy.top();  // 获取栈顶元素
        s_copy.pop();  // 出栈
        backtrack(s_copy, output + c, next_input);  // 将出栈元素加入序列并递归
    }
}


int main() {
    stack<char> initial_stack;  // 初始栈为空
    string initial_output = "";  // 初始序列为空
    int start = 0;  // 从第一个元素开始

    // 开始递归生成所有序列
    backtrack(initial_stack, initial_output, start);

    // 输出所有可能的出栈序列
    cout << "所有可能的出栈序列：" << endl;
    for (const auto& seq : all_sequences) {
        cout << seq << endl;
    }

    return 0;
}