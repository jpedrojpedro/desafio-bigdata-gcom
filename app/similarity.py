def jaccard_distance(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return len(s1.intersection(s2)) / float(len(s1.union(s2)))


def cosine_similarity():
    raise NotImplementedError
