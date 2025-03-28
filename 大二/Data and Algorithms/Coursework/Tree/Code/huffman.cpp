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

struct HuffmanNode {
    char character;
    int frequency;
    int min_ascii;
    HuffmanNode* left;
    HuffmanNode* right;

    HuffmanNode(char c, int freq, int ascii)
        : character(c), frequency(freq), min_ascii(ascii), left(nullptr), right(nullptr) {}
};

struct Compare {
    bool operator()(HuffmanNode* a, HuffmanNode* b) {
        if (a->frequency != b->frequency)
            return a->frequency > b->frequency;
        return a->min_ascii > b->min_ascii;
    }
};

class HuffmanTree {
private:
    HuffmanNode* root;

    void buildCodeTable(HuffmanNode* node, string code, map<char, string>& codeTable) {
        if (node->left == nullptr && node->right == nullptr) {
            codeTable[node->character] = code.empty() ? "0" : code;
            return;
        }
        buildCodeTable(node->left, code + "0", codeTable);
        buildCodeTable(node->right, code + "1", codeTable);
    }

public:
    HuffmanTree(map<char, int>& freqMap) {
        priority_queue<HuffmanNode*, vector<HuffmanNode*>, Compare> pq;

        for (auto& pair : freqMap) {
            pq.push(new HuffmanNode(pair.first, pair.second, pair.first));
        }

        while (pq.size() > 1) {
            HuffmanNode* left = pq.top(); pq.pop();
            HuffmanNode* right = pq.top(); pq.pop();

            if (left->min_ascii > right->min_ascii)
                swap(left, right);

            HuffmanNode* merged = new HuffmanNode('\0', left->frequency + right->frequency,
                                                 min(left->min_ascii, right->min_ascii));
            merged->left = left;
            merged->right = right;

            pq.push(merged);
        }

        root = pq.top();
    }

    map<char, string> getCodeTable() {
        map<char, string> codeTable;
        if (root != nullptr) {
            buildCodeTable(root, "", codeTable);
        }
        return codeTable;
    }

    string decode(const string& encoded) {
        string result;
        HuffmanNode* current = root;

        if (root->left == nullptr && root->right == nullptr) {
            return string(encoded.size(), root->character);
        }

        for (char bit : encoded) {
            if (bit == '0') current = current->left;
            else current = current->right;

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

    // 统计频率
    map<char, int> freqMap;
    for (char c : input) {
        freqMap[c]++;
    }

    // 输出频率统计表
    cout << "字符频率统计表：" << endl;
    for (auto& pair : freqMap) {
        cout << pair.first << " " << pair.second << endl;
    }

    // 构建霍夫曼树
    HuffmanTree tree(freqMap);
    map<char, string> codeTable = tree.getCodeTable();

    // 输出编码表
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

    // 验证译码
    string decoded = tree.decode(encoded);
    cout << "\n译码验证结果：";
    cout << (decoded == input ? "一致" : "不一致") << endl;

    return 0;
}