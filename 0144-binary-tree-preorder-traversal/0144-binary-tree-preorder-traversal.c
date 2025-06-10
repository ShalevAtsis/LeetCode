/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

void preorderRecursive(struct TreeNode* root, int* result, int* index) {
    if (root == NULL) {
        return;
    }
    result[(*index)++] = root->val;
    preorderRecursive(root->left, result, index);
    preorderRecursive(root->right, result, index);
}


int* preorderTraversal(struct TreeNode* root, int* returnSize) {
    *returnSize = 0;

    if (root == NULL) {
        return NULL;
    }
    
    int* preorder = (int*)malloc(100 * sizeof(int));
    if (!preorder) {
        printf("Memory allocation failed.\n");
        return NULL;
    }
    
    preorderRecursive(root, preorder, returnSize);

    return preorder;
}