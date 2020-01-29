f = open("input6.txt", "r")
mapdata = f.read().split("\n")[:-1]
#mapdata = ["COM)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","E)J","J)K","K)L","K)YOU","I)SAN"]
    
def main():
    (children, parents) = generateAdjLists(mapdata)
    (total, depths) = assignWeights(children)
    print("Part 1: Total direct/indirect orbits =", total)
    lineageYOU = findLineage('YOU', parents)
    lineageSAN = findLineage('SAN', parents)
    commonAnc = findCommonAncestor(lineageYOU, lineageSAN)
    ans = minTransfersRequired('YOU', commonAnc, 'SAN', depths)
    print("Part 2: Minimum orbital transfers required =", ans)

# process textual mapdata into adjacency lists
# children[p] = list of planets which orbit p
# parents[p] = planet which p orbits
def generateAdjLists(mapdata):
    children = {}
    parents = {}
    for orbit in mapdata:
        parent = orbit.split(")")[0]
        child = orbit.split(")")[1]
        if (parent not in children):
            children[parent] = []
        children[parent].append(child)
        parents[child] = parent
    return (children, parents)

# runs a dfs, summing the planets weighted by their depth
# return the total, along with a dict of planet depths
def assignWeights(orbits):
    total = 0
    weights = {}
    process = [("COM", 0)]
    while (len(process) > 0):
        (inner, depth) = process.pop()
        weights[inner] = depth
        depth += 1
        if (inner not in orbits): continue
        total += depth * len(orbits[inner])
        for outer in orbits[inner]:
            process.append((outer, depth))
    return (total, weights)

# find a path from planet to root, given the parents adjlist dict
def findLineage(planet, parents):
    lineage = [planet]
    pos = planet
    while (pos != "COM"):
        pos = parents[pos]
        lineage.append(pos)
    return lineage

# find first element which appears in both lists
def findCommonAncestor(lineage1, lineage2):
    commonAnc = None
    for p in lineage1:
        if (p in lineage2):
            commonAnc = p
            break
    return commonAnc

# calculate minimum number of orbital transfers required
def minTransfersRequired(p, mid, q, depths):
    p2mid = depths[p] - depths[mid] - 1
    q2mid = depths[q] - depths[mid] - 1
    return p2mid + q2mid
    
main()
