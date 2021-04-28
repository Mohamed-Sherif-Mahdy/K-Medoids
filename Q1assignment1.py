print("Alhamdulillah Done by Mohamed Sherif")
points=[(2,10),(2,5),(8,4),(5,8),(7,5),(6,4),(1,2),(4,9)]
allCostsWithMidoids=[]
allcosts=[]
cluster1=[]
cluster2=[]

def distancemedoid(m1,point):
    d1=abs(point[0]-m1[0])
    d2=abs(point[1]-m1[1])
    return d1+d2

def kmidoid(m1,m2):
    cost=0
    cluster1.clear()
    cluster2.clear()
    print("cost from first medoid , cost from second medoid , point")
    for point in points:
        distanceTuple=(distancemedoid(m1,point),distancemedoid(m2,point)) 
        if distancemedoid(m1,point)==min(distancemedoid(m1,point),distancemedoid(m2,point)):
            cluster1.append(point)
        else:
            cluster2.append(point)    
        print(distanceTuple[0],"    "*8,distanceTuple[1],"  "*6,point)
        cost+=min(distanceTuple)

    print()
    print("first cluster of data is",cluster1)
    print("second cluster of data is",cluster2)
    print('total cost',cost)
    print("-"*60)
    allCostsWithMidoids.append((m1,m2,cost))
    allcosts.append(cost)
    
#counter refers to the number of itterations used to cluster our data you can it by uncomment counter lines.
#counter=0 
for x in range(len(points)):
    for l in range(x+1,len(points)):
        #counter+=1
        print("when m1=",points[x],"and when m2=",points[l])
        kmidoid(points[x],points[l])
minmumCost=min(allcosts)
midoids=[[i,j,k] for i,j,k in allCostsWithMidoids if k == minmumCost]
kmidoid(midoids[0][0],midoids[0][1])
print("#"*70)
print("as we notice the best midoids for clustring our data are ",midoids[0][0],"and",midoids[0][1],"with cost",midoids[0][2])
print("#"*70)
print("-"*60)
#print("first group of data is",cluster1)
#print("second group of data is",cluster2)
#print(counter)