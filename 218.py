class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        if len(buildings) == 1:
            l, r, h = buildings[0]
            return [[l, h], [r, 0]]
        
        mid = len(buildings) // 2
        leftSkyline = self.getSkyline(buildings[:mid])
        rightSkyline = self.getSkyline(buildings[mid:])
        
        return self.mergeSkylines(leftSkyline, rightSkyline)
    
    def mergeSkylines(self, left, right):
        hL = hR = 0
        i = j = 0
        output = []
        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                x, hL = left[i]
                i += 1
            elif left[i][0] > right[j][0]:
                x, hR = right[j]
                j += 1
            else:
                x = left[i][0]
                hL = left[i][1]
                hR = right[j][1]
                i += 1
                j += 1
            maxH = max(hL, hR)
            if not output or output[-1][1] != maxH:
                output.append([x, maxH])
        
        # Adiciona o que sobrou
        output.extend(left[i:])
        output.extend(right[j:])
        
        return output