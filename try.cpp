#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <chrono>

using namespace std;
using namespace std::chrono;

const int MAX_N = 30;
const int INVALID_RESULT = -2147483;  // Named constant for invalid result

vector<int> large_input(MAX_N);
vector<int> Ring(MAX_N, 0);
vector<int> Ding(MAX_N, 0);

// Forward declarations
int ding(int k);
int ring(int k);
int bootforce(int k, int ringcounter, int dingcounter);

// Memoized recursive function to calculate the maximum sum (ding)
int ding(int k) {
    if (k < 0) {
        return 0;
    } else if (Ding[k] != 0) {
        return Ding[k];
    } else {
        if(k==5){
            cout<<"5";
        }
        int a1 = (k >= 0) ? large_input[k] : 0;
        int a2 = (k - 1 >= 0) ? large_input[k - 1] : 0;
        int a3 = (k - 2 >= 0) ? large_input[k - 2] : 0;
        int a4 = (k - 3 >= 0) ? large_input[k - 3] : 0;
        int a5 = (k - 4 >= 0) ? large_input[k - 4] : 0;

        int m = max({
            ding(k - 5) + a5 + a4 + a3 - a2 - a1,
            ding(k - 4) + a4 + a3 - a2 - a1,
            ding(k - 4) + a4 + a3 + a2 - a1,
            ding(k - 3) + a3 + a2 - a1,
            ding(k - 3) + a3 - a2 - a1,
            ring(k - 3) - a3 - a2 - a1,
            ring(k - 4) - a4 - a3 + a2 - a1,
            ring(k - 5) - a5 - a4 - a3 + a2 - a1,
            ring(k - 3) - a3 + a2 - a1
        });

        Ding[k] = m;
        return m;
    }
}

// Memoized recursive function to calculate the maximum sum (ring)
int ring(int k) {
    if (k < 0) {
        return 0;
    } else if (Ring[k] != 0) {
        return Ring[k];
    } else {
        int a1 = (k >= 0) ? large_input[k] : 0;
        int a2 = (k - 1 >= 0) ? large_input[k - 1] : 0;
        int a3 = (k - 2 >= 0) ? large_input[k - 2] : 0;
        int a4 = (k - 3 >= 0) ? large_input[k - 3] : 0;
        int a5 = (k - 4 >= 0) ? large_input[k - 4] : 0;

        int m = max({
            ring(k - 5) - a5 - a4 - a3 + a2 + a1,
            ring(k - 4) - a4 - a3 + a2 + a1,
            ring(k - 4) - a4 - a3 - a2 + a1,
            ring(k - 3) - a3 - a2 + a1,
            ring(k - 3) - a3 + a2 + a1,
            ding(k - 3) + a3 + a2 + a1,
            ding(k - 4) + a4 + a3 - a2 + a1,
            ding(k - 5) + a5 + a4 + a3 - a2 + a1,
            ding(k - 3) + a3 - a2 + a1
        });

        Ring[k] = m;
        return m;
    }
}

// Brute-force recursive function with counters
int bootforce(int k, int ringcounter, int dingcounter) {
    if (ringcounter >= 4 || dingcounter >= 4) {
        return INVALID_RESULT;
    }
    if (k < 0) {
        return 0;
    }

    return max(
        bootforce(k - 1, ringcounter + 1, 0) + large_input[k],
        bootforce(k - 1, 0, dingcounter + 1) - large_input[k]
    );
}

int main() {
    srand(time(0));


    // Dynamic programming solution
    auto start_time = high_resolution_clock::now();
    // Generate a list of 30 random integers between -100 and 100
    for (int i = 0; i < MAX_N; ++i) {
        large_input[i] = rand() % 201 - 100;
    }
    auto end_timee = high_resolution_clock::now();
    auto art = duration_cast<microseconds>(end_timee - start_time);
    cout << "Array Formed in: " << art.count() << " microseconds"<< endl;

    start_time = high_resolution_clock::now();
    vector<int> ring_list(MAX_N);
    for (int i = 0; i < MAX_N; ++i) {
        ring_list[i] = ring(i);
    }
    int dp_result = max(ring_list[MAX_N - 1], ding(MAX_N - 1));
    auto end_time = high_resolution_clock::now();
    auto dp_duration = duration_cast<microseconds>(end_time - start_time);

    cout << "Dynamic Programming Result: " << dp_result << endl;
    cout << "Dynamic Programming Time: " << dp_duration.count() << " microseconds" << endl;

    // Brute-force solution
    start_time = high_resolution_clock::now();
    int bf_result = bootforce(MAX_N - 1, 0, 0);
    end_time = high_resolution_clock::now();
    auto bf_duration = duration_cast<microseconds>(end_time - start_time);

    cout << "\nBrute-Force Result: " << bf_result << endl;
    cout << "Brute-Force Time: " << bf_duration.count() << " microseconds" << endl;

    return 0;
}
