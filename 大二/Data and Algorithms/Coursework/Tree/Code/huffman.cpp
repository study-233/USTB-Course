/**
  * @author         : Andy Tao
  * @brief          : huffman����
  * @date           : 25-3-27 ����8:21
  */
#include <iostream>
#include <map>
#include <queue>
#include <vector>
#include <climits>

using namespace std;

/**
 * ���������ڵ�ṹ��
 * �����ַ���Ƶ�ʡ���СASCIIֵ�������ӽڵ�ָ��
 */
struct HuffmanNode {
    char character;      // �洢�ַ�����Ҷ�ӽڵ���Ч��
    int frequency;       // �ڵ�Ȩ�أ��ַ�����Ƶ�ʣ�
    int min_ascii;       // ��ǰ��������С��ASCII��ֵ������Ƶ����ͬʱ������
    HuffmanNode* left;   // ���ӽڵ�ָ��
    HuffmanNode* right;  // ���ӽڵ�ָ��

    // ���캯������ʼ���ַ���Ƶ�ʺ���СASCIIֵ
    HuffmanNode(char c, int freq, int ascii)
        : character(c), frequency(freq), min_ascii(ascii), left(nullptr), right(nullptr) {}
};

/**
 * ���ȶ��бȽϽṹ��
 * ���ڹ�����������ʱ����С�ѱȽϹ���
 */
struct Compare {
    bool operator()(HuffmanNode* a, HuffmanNode* b) {
        // ���ȱȽ�Ƶ�ʣ�Ƶ��С������
        if (a->frequency != b->frequency)
            return a->frequency > b->frequency;
        // Ƶ����ͬ��Ƚ���СASCIIֵ��ASCIIֵС������
        return a->min_ascii > b->min_ascii;
    }
};

class HuffmanTree {
private:
    HuffmanNode* root;  // �����������ڵ�

    /**
     * �ݹ����ɻ����������
     * @param node ��ǰ�����Ľڵ�
     * @param code ��ǰ·���Ķ����Ʊ���
     * @param codeTable �洢�ַ�������ӳ���
     */
    void buildCodeTable(HuffmanNode* node, string code, map<char, string>& codeTable) {
        // ����Ҷ�ӽڵ�ʱ��¼���루���ڵ��������⴦��
        if (node->left == nullptr && node->right == nullptr) {
            codeTable[node->character] = code.empty() ? "0" : code;
            return;
        }
        // ������·�����'0'��������·�����'1'
        buildCodeTable(node->left, code + "0", codeTable);
        buildCodeTable(node->right, code + "1", codeTable);
    }

public:
    /**
     * ���캯��������Ƶ��ӳ�乹����������
     * @param freqMap �ַ�Ƶ��ӳ���
     */
    HuffmanTree(map<char, int>& freqMap) {
        // ʹ�����ȶ��У���С�ѣ��洢�ڵ�
        priority_queue<HuffmanNode*, vector<HuffmanNode*>, Compare> pq;

        // �������ַ���ΪҶ�ӽڵ�������ȶ���
        for (auto& pair : freqMap) {
            pq.push(new HuffmanNode(pair.first, pair.second, pair.first));
        }

        // �ϲ��ڵ�ֱ��ֻʣһ�����ڵ�
        while (pq.size() > 1) {
            HuffmanNode* left = pq.top(); pq.pop();
            HuffmanNode* right = pq.top(); pq.pop();

            // ȷ�����ӽڵ��min_ascii��С��Ƶ����ͬ����±���˳��
            if (left->min_ascii > right->min_ascii)
                swap(left, right);

            // �����ϲ�����½ڵ㣬Ƶ��Ϊ�ӽڵ�֮�ͣ�min_asciiȡ��Сֵ
            HuffmanNode* merged = new HuffmanNode('\0', left->frequency + right->frequency,
                                                 min(left->min_ascii, right->min_ascii));
            merged->left = left;
            merged->right = right;

            pq.push(merged);
        }

        root = pq.top();  // ���ø��ڵ�
    }

    /**
     * ��ȡ�����������
     * @return �ַ��������Ʊ����ӳ��
     */
    map<char, string> getCodeTable() {
        map<char, string> codeTable;
        if (root != nullptr) {
            buildCodeTable(root, "", codeTable);
        }
        return codeTable;
    }

    /**
     * ����������ַ���
     * @param encoded �����Ķ������ַ���
     * @return ������ԭʼ�ַ���
     */
    string decode(const string& encoded) {
        string result;
        HuffmanNode* current = root;

        // �����ڵ�������������������ַ���ͬ��
        if (root->left == nullptr && root->right == nullptr) {
            return string(encoded.size(), root->character);
        }

        // ���������ַ���������0/1�ƶ��ڵ�
        for (char bit : encoded) {
            current = (bit == '0') ? current->left : current->right;

            // ����Ҷ�ӽڵ�ʱ��¼�ַ������ñ������
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

    // ͳ���ַ�Ƶ��
    map<char, int> freqMap;
    for (char c : input) {
        freqMap[c]++;
    }

    // ���Ƶ��ͳ�Ʊ�
    cout << "�ַ�Ƶ��ͳ�Ʊ�" << endl;
    for (auto& pair : freqMap) {
        cout << pair.first << " " << pair.second << endl;
    }

    // �����������������ɱ����
    HuffmanTree tree(freqMap);
    map<char, string> codeTable = tree.getCodeTable();

    // ��������������
    cout << "\n�����������" << endl;
    for (auto& pair : codeTable) {
        cout << pair.first << " " << pair.second << endl;
    }

    // ���ɱ�����
    string encoded;
    for (char c : input) {
        encoded += codeTable[c];
    }
    cout << "\n��������" << endl << encoded << endl;

    // ��֤��������ԭ�ַ����Ƿ�һ��
    string decoded = tree.decode(encoded);
    cout << "\n������֤�����";
    cout << (decoded == input ? "һ��" : "��һ��") << endl;

    return 0;
}