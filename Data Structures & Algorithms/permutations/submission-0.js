class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    permute(nums) {
        const output = []

        const dfs = (visited, currentPermutation) => {
            if (currentPermutation.length == nums.length) {
                output.push(currentPermutation);
                return;
            }

            for (let i = 0; i < nums.length; i++) {
                if (!visited[nums[i]]) {
                    dfs({ ...visited, [nums[i]]: true }, [...currentPermutation, nums[i]]);
                }
            }
            
        }

        dfs({}, []);

        return output;
    }
}
