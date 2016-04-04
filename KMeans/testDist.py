import collections

map=collections.defaultdict(list)
for x in xrange(10):
	map[x].append([1,2,3])
print len(map)
for y in map[0]:
	print y