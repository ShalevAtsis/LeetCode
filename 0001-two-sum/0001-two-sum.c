/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int i, j;
    int* resArr = (int*)malloc(2 * sizeof(int));

    if (!resArr)
    {
        printf("Memmory allocation error.\n");
        return 0;
    }

    for (i = 0; i < numsSize; i++) {
        for (j = i + 1; j < numsSize; j++) {
            if (target == nums[i] + nums[j]) {
                resArr[0] = i;
                resArr[1] = j;
                *returnSize = 2;
                return resArr;
            }
        }
    }

    *returnSize = 0;
    return NULL;
}