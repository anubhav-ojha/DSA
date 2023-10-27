/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let returnedArray = []
    n = arr.length ;
    for(let i=0; i<n; i++){
        returnedArray[i] = fn(arr[i], i);
    }
    
    return returnedArray;
};