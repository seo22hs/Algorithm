fr_info = {

    'Summer': ['John', 'Justin', 'Mike'],

    'John':   ['Summer', 'Justin'],

    'Justin': ['John', 'Summer', 'Mike', 'May'],

    'Mike':   ['Summer', 'Justin'],

    'May':    ['Justin', 'Kim'],

    'Kim':    ['May'],

    'Tom':    ['Jerry'],

    'Jerry':  ['Tom'],

}


def dfs_friends(g, start):

    done = set()      # 이미 방문한 사람 집합

    order = []        # 방문 순서 기록

    def _dfs(p):

        done.add(p)        # 방문 기록

        order.append(p)    # 순서 기록

        for x in g[p]:           # 이웃을 하나씩 확인

            if x not in done:    # 미방문이면

                _dfs(x)          # 재귀 호출

    _dfs(start)    # 시작 사람에서 탐색 시작

    return order


print("=== DFS: Summer의 모든 친구 ===")
result = dfs_friends(fr_info, 'Summer')
print(result)

print()

print("=== DFS: Jerry의 모든 친구 ===")
result = dfs_friends(fr_info, 'Jerry')
print(result)
