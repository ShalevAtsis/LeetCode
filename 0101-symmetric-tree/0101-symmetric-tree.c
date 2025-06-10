/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool isMirror(struct TreeNode* left, struct TreeNode* right) {
    // Both NULL: symmetric
    if (left == NULL && right == NULL) {
        return true;
    }

    // One NULL or different values: not symmetric
    if (left == NULL || right == NULL || left->val != right->val) {
        return false;
    }

    // Check mirror property: left's left vs. right's right, left's right vs. right's left
    return isMirror(left->left, right->right) && isMirror(left->right, right->left);
}

bool isSymmetric(struct TreeNode* root) {
    if (root == NULL) {
        return true; // Empty tree is symmetric
    }

    return isMirror(root->left, root->right);
}