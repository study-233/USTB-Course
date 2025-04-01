/**
  * @author         : Andy Tao
  * @brief          : huffman编码
  * @date           : 25-3-27 下午8:21
  */
#include <iostream>
#include <map>
#include <queue>
#include <vector>
#include <climits>

using namespace std;

/**
 * 霍夫曼树节点结构体
 * 包含字符、频率、最小ASCII值、左右子节点指针
 */
struct HuffmanNode {
    char character;      // 存储字符（仅叶子节点有效）
    int frequency;       // 节点权重（字符出现频率）
    int min_ascii;       // 当前子树中最小的ASCII码值（用于频率相同时的排序）
    HuffmanNode* left;   // 左子节点指针
    HuffmanNode* right;  // 右子节点指针

    // 构造函数：初始化字符、频率和最小ASCII值
    HuffmanNode(char c, int freq, int ascii)
        : character(c), frequency(freq), min_ascii(ascii), left(nullptr), right(nullptr) {}
};

/**
 * 优先队列比较结构体
 * 用于构建霍夫曼树时的最小堆比较规则
 */
struct Compare {
    bool operator()(HuffmanNode* a, HuffmanNode* b) {
        // 首先比较频率，频率小的优先
        if (a->frequency != b->frequency)
            return a->frequency > b->frequency;
        // 频率相同则比较最小ASCII值，ASCII值小的优先
        return a->min_ascii > b->min_ascii;
    }
};

class HuffmanTree {
private:
    HuffmanNode* root;  // 霍夫曼树根节点

    /**
     * 递归生成霍夫曼编码表
     * @param node 当前遍历的节点
     * @param code 当前路径的二进制编码
     * @param codeTable 存储字符与编码的映射表
     */
    void buildCodeTable(HuffmanNode* node, string code, map<char, string>& codeTable) {
        // 到达叶子节点时记录编码（单节点树需特殊处理）
        if (node->left == nullptr && node->right == nullptr) {
            codeTable[node->character] = code.empty() ? "0" : code;
            return;
        }
        // 左子树路径添加'0'，右子树路径添加'1'
        buildCodeTable(node->left, code + "0", codeTable);
        buildCodeTable(node->right, code + "1", codeTable);
    }

public:
    /**
     * 构造函数：根据频率映射构建霍夫曼树
     * @param freqMap 字符频率映射表
     */
    HuffmanTree(map<char, int>& freqMap) {
        // 使用优先队列（最小堆）存储节点
        priority_queue<HuffmanNode*, vector<HuffmanNode*>, Compare> pq;

        // 将所有字符作为叶子节点加入优先队列
        for (auto& pair : freqMap) {
            pq.push(new HuffmanNode(pair.first, pair.second, pair.first));
        }

        // 合并节点直到只剩一个根节点
        while (pq.size() > 1) {
            HuffmanNode* left = pq.top(); pq.pop();
            HuffmanNode* right = pq.top(); pq.pop();

            // 确保左子节点的min_ascii较小（频率相同情况下保持顺序）
            if (left->min_ascii > right->min_ascii)
                swap(left, right);

            // 创建合并后的新节点，频率为子节点之和，min_ascii取较小值
            HuffmanNode* merged = new HuffmanNode('\0', left->frequency + right->frequency,
                                                 min(left->min_ascii, right->min_ascii));
            merged->left = left;
            merged->right = right;

            pq.push(merged);
        }

        root = pq.top();  // 设置根节点
    }

    /**
     * 获取霍夫曼编码表
     * @return 字符到二进制编码的映射
     */
    map<char, string> getCodeTable() {
        map<char, string> codeTable;
        if (root != nullptr) {
            buildCodeTable(root, "", codeTable);
        }
        return codeTable;
    }

    /**
     * 解码二进制字符串
     * @param encoded 编码后的二进制字符串
     * @return 解码后的原始字符串
     */
    string decode(const string& encoded) {
        string result;
        HuffmanNode* current = root;

        // 处理单节点树的特殊情况（所有字符相同）
        if (root->left == nullptr && root->right == nullptr) {
            return string(encoded.size(), root->character);
        }

        // 遍历编码字符串，根据0/1移动节点
        for (char bit : encoded) {
            current = (bit == '0') ? current->left : current->right;

            // 到达叶子节点时记录字符并重置遍历起点
            if (current->left == nullptr && current->right == nullptr) {
                result += current->character;
                current = root;
            }
        }
        return result;
    }
};

int main() {
    string input;
    getline(cin, input);

    // 统计字符频率
    map<char, int> freqMap;
    for (char c : input) {
        freqMap[c]++;
    }

    // 输出频率统计表
    cout << "字符频率统计表：" << endl;
    for (auto& pair : freqMap) {
        cout << pair.first << " " << pair.second << endl;
    }

    // 构建霍夫曼树并生成编码表
    HuffmanTree tree(freqMap);
    map<char, string> codeTable = tree.getCodeTable();

    // 输出霍夫曼编码表
    cout << "\n霍夫曼编码表：" << endl;
    for (auto& pair : codeTable) {
        cout << pair.first << " " << pair.second << endl;
    }

    // 生成编码结果
    string encoded;
    for (char c : input) {
        encoded += codeTable[c];
    }
    cout << "\n编码结果：" << endl << encoded << endl;

    // 验证译码结果与原字符串是否一致
    string decoded = tree.decode(encoded);
    cout << "\n译码验证结果：";
    cout << (decoded == input ? "一致" : "不一致") << endl;

    return 0;
}