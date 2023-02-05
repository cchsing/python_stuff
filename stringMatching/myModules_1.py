def naive_string_matcher(T, P):
    temp_T = str(T)
    temp_P = str(P)
    n = len(temp_T)
    m = len(temp_P)
    for i in range(0, n-m, 1):
        if temp_P[0:m] == temp_T[i:i+m]:
            print(f"Pattern occurs with shift {i}")
            return i
