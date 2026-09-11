class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    findErrorNums(nums) {
        let set = new Set();
        let o = []
        for (let i = 0; i < nums.length; i++)
        {
            if (set.has(nums[i]))
            {
                o.push(nums[i])
            }
            set.add(nums[i]);
        }

        for (let i = 1; i < nums.length + 1; i++)
        {
            if (set.has(i) || o[0] == i)
            {
                continue;
            }
            o.push(i);
            return o;
        }
    }
}
