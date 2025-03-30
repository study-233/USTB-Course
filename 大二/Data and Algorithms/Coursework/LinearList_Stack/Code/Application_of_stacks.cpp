/**
  * @author         : Andy Tao
  * @brief          : 栈的应用
  * @date           : 25-3-21 下午4:03
  */
#include <iostream>
#include <stack>
#include <vector>
#include <string>

using namespace std;

vector<string> all_sequences;
const vector<char> input = {'A', 'B', 'C', 'D'};

/**
 * @brief 回溯函数：递归生成所有可能的出栈序列
 * @param s 当前栈的内容（保存已入栈但未出栈的元素）
 * @param output 当前已生成的出栈序列
 * @param next_input 下一个待处理的输入元素索引（初始为0）
 */
void backtrack(stack<char> s, const string& output, int next_input) {
    // 终止条件：所有输入元素已处理完毕且栈为空时，保存当前出栈序列
    if (next_input == input.size() && s.empty()) {
        all_sequences.push_back(output);
        return;
    }

    // 入栈分支：将当前元素压入栈，并递归处理下一个输入元素
    if (next_input < input.size()) {
        s.push(input[next_input]);
        backtrack(s, output, next_input + 1);
        s.pop();  // 回溯：恢复栈状态
    }

    // 出栈分支：弹出栈顶元素并追加到出栈序列，递归处理后续操作
    if (!s.empty()) {
        char c = s.top();
        s.pop();
        backtrack(s, output + c, next_input);
        s.push(c);  // 回溯：恢复栈状态
    }
}

int main() {
    stack<char> s;  // 用于模拟入栈/出栈过程的辅助栈
    string output;
    backtrack(s, output, 0);  // 从第一个输入元素（索引0）开始回溯

    // 输出所有可能的出栈序列
    cout << "所有可能的出栈序列：" << endl;
    for (const auto& seq : all_sequences) {
        cout << seq << endl;
    }
    return 0;
}