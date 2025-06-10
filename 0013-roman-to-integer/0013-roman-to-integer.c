int getValue(char c);
int romanToInt(char* s);

int getValue(char c) {
    switch (c) {
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
        default: return -1;
    }
}

int romanToInt(char* s) {
    if (s == NULL || *s == '\0') 
        return -1;

    int res = 0;
    int len = strlen(s);

    for (int i = 0; i < len ; i++) {
        int currValue = getValue(s[i]);

        if (currValue == -1)
            return -1;

        if (i < len -1) {
            int nextValue = getValue(s[i + 1]);
            
            if (nextValue == -1)
                return -1;

            if (currValue < nextValue) {
                res -= currValue;
            } else {
                res += currValue;
            }
        }
        else {
            res += currValue;
        }
    }

    if (res < 1 || res > 3999)
        return -1;

    return res;
}