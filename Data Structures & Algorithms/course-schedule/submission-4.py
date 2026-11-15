class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # hashmap of {class: [prereqs]}
        prereqs = {}
        for i,j in prerequisites:
            if i in prereqs:
                prereqs[i].append(j)
            else:
                prereqs[i] = [j]
            if j not in prereqs:
                prereqs[j] = []
        print(prereqs)
        q = deque()
        for clas in prereqs:
            counter = 0
            q.append(clas)
            while q:
                if counter > 2*numCourses:
                    return False
                for z in range(len(q)):
                    cur_class = q.popleft()
                    counter += 1
                    if prereqs[cur_class] == []:
                        continue
                    for pre in prereqs[cur_class]:
                        # print(pre,cur_class)
                        if pre == clas:
                            return False
                        q.append(pre)
        return True
