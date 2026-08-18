def candidate_elimination(data):
    num_attributes = len(data[0]) - 1

    S = ['0'] * num_attributes
    G = [['?'] * num_attributes]

    for row in data:
        if row[-1] == 'Yes':
            S = row[:-1].copy()
            break

    for row in data:
        inputs, label = row[:-1], row[-1]

        if label == 'Yes':
            for i in range(num_attributes):
                if inputs[i] != S[i]:
                    S[i] = '?'

            G = [
                g for g in G
                if all(g[i] == '?' or g[i] == inputs[i]
                       for i in range(num_attributes))
            ]

        else:
            G_new = []

            for g in G:
                if not all(g[i] == '?' or g[i] == inputs[i]
                           for i in range(num_attributes)):
                    G_new.append(g)
                else:
                    for i in range(num_attributes):
                        if g[i] == '?' and inputs[i] != S[i]:
                            g_candidate = g.copy()
                            g_candidate[i] = S[i]

                            if g_candidate not in G_new:
                                G_new.append(g_candidate)

            G = G_new

    return S, G


if __name__ == "__main__":
    dataset = [
        ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
        ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
        ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
        ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
    ]

    s_boundary, g_boundary = candidate_elimination(dataset)

    print("Specific Boundary (S):", s_boundary)
    print("General Boundary (G):", g_boundary) 