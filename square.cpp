#include <vector>

int square_sum(const std::vector<int>& numbers){
    int res = 0;
    for(int i = 0;i<numbers.size();i++){
        res += numbers[i]*numbers[i];
    }
    return res;
}
