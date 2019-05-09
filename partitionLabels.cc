#include <unordered_set>

class Solution {
public:
    int max(int a, int b) {
        if (a >= b) {
            return a;
        } else {
            return b;
        }
    }
    vector<int> partitionLabels(string s) {
        vector<int> result;
        if (s == "") {
            return result;
        }
        unordered_set<char> seen;
        seen.insert(s[0]);
        int right = s.find_last_of(s[0]);
        int i = 1;
        while (i < right) {
            if (seen.find(s[i]) != seen.end()) {
                i += 1;
                continue;
            }
            seen.insert(s[i]);
            right = max(right, s.find_last_of(s[i]));
            i += 1;
        }
        result.emplace_back(right + 1);
        vector<int> recursed_result = partitionLabels(s.substr(right + 1));
        result.insert(result.end(), recursed_result.begin(), recursed_result.end());
        return result;
    }
};
