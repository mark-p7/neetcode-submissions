class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsets(nums) {
        const o = [[]];

        for (let i = 0; i < nums.length; i++) {
            let oLen = o.length;
            o.push([nums[i]]);
            for (let j = 1; j < oLen; j++) {
                o.push([...o[j], nums[i]]);
            }
        }

        return o;
    }
}
