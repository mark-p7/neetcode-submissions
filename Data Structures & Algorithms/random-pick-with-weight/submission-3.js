class Solution {
    /**
     * @param {number[]} w
     */
    constructor(w) {
        this.stack = []
        for (let i = 0; i < w.length; i++) {
            for (let j = 0; j < w[i]; j++) {
                this.stack.push(i);
            }
        }
    }

    /**
     * @return {number}
     */
    pickIndex() {
        return this.stack[Math.floor(Math.random() * this.stack.length - 1) + 1];
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(w)
 * var param_1 = obj.pickIndex()
 */
