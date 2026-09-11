class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let strArr = [];
        for (let i = 0; i < strs.length; i++) {
            strArr.push(`${strs[i].length}:`)
            strArr.push(strs[i])
        }
        return strArr.join("")
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        const output = []
        for(let i = 0; i < str.length;) {
            const outputStr = [];
            let length = [];
            while(str[i] != ":") {
                length.push(str[i])
                i++;
            }
            length = parseInt(length.join(""))
            i++
            for (let j = 0; j < length; j++) {
                outputStr.push(str[i])
                i++
            }
            output.push(outputStr.join(""))
        }

        return output
    }
}
