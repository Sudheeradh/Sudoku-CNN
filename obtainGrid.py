import cv2
import numpy as np

def obtain_grid(imgpath = 'sud.jpg', size = 900):
	#size = 900

	img = cv2.imread(imgpath)
	img = cv2.resize(img, (500, 500))
	original = img.copy()
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	greymain = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

	###### Adaptive Threshold ######
	th2 = cv2.adaptiveThreshold(greymain,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
	            cv2.THRESH_BINARY_INV,39,10)
	###### Adaptive Threshold ######


	'''cv2.imshow('window', th2)
	cv2.waitKey(0)'''

	#### Finding the biggest contour assuming it to be sudoku outline ####
	contours,heirarchy = cv2.findContours(th2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	maxarea = 0
	cnt = contours[0]
	for i in contours:
	    if cv2.contourArea(i)>maxarea:
	        cnt = i
	        maxarea = cv2.contourArea(i)

	#### Finding the biggest contour assuming it to be sudoku outline ####

	### Drawing the contour on blank image ###
	blank = np.zeros(img.shape, np.uint8)
	image = cv2.drawContours(blank, [cnt], -1, (255, 255, 255), 2)
	### Drawing the contour on blank image ###

	### Obtaining the contour as Lines ###
	edges = cv2.Canny(image,40,150,apertureSize = 3)
	lines = cv2.HoughLines(edges,1,np.pi/180,100)
	createhor = []
	createver = []
	created = []
	anglediff=10
	rhodiff=10
	flag=0
	count = 2
	### Obtaining the contour as Lines ###

	### Eliminating lines that are close to each other except one ###
	for line in lines:
	    for (rho,theta) in line:
	        flag=0
	        for (rho1,theta1) in created:
	            if abs(rho-rho1)<rhodiff and abs(theta-theta1)<anglediff:
	                flag=1
	                
	        if flag==0:
	            a = np.cos(theta)
	            b = np.sin(theta)
	            x0 = a*rho
	            y0 = b*rho
	            x1 = int(x0 + 1000*(-b))
	            y1 = int(y0 + 1000*(a))
	            x2 = int(x0 - 1000*(-b))
	            y2 = int(y0 - 1000*(a))
	            d = np.linalg.norm(np.array((x1,y1,0))-np.array((x2,y2,0)))
	            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
	            m=abs(1/np.tan(theta))
	            if m<1:
	                createhor.append((rho,theta))
	            else:
	                createver.append((rho,theta))
	            created.append((rho,theta))
	### Eliminating lines that are close to each other except one ###            

	### Obtaining the four corner points ###
	points=[]

	for (rho,theta) in createhor:
	        for (rho1,theta1) in createver:
	            if (rho,theta)!=(rho1,theta1):
	                a=[[np.cos(theta),np.sin(theta)],[np.cos(theta1),np.sin(theta1)]]
	                b=[rho,rho1]
	                cor=np.linalg.solve(a,b)
	                if list(cor) not in points:
	                    points.append(list(cor))
	### Obtaining the four corner points ###

	### Obtaining the sudoku in right perspective ###
	points.sort()

	## getting 4 outer points ##
	temp_pts = [points[0]]
	points.remove(points[0])
	dists = []

	for i in points:
	    dists.append(np.linalg.norm(np.array(temp_pts)-np.array(i)))
	#print(dists)
	temp_pts.append(points[np.argmax(np.array(dists))])
	dia_dist = max(dists)
	points.remove(points[np.argmax(np.array(dists))])

	for i in points:
	    if np.linalg.norm(np.array(temp_pts[0])-np.array(i)) > dia_dist / 3 and  np.linalg.norm(np.array(temp_pts[1])-np.array(i)) > dia_dist / 3:
	        third = i
	        break

	temp_pts.append(third)

	dists = []

	for i in points:
	    dists.append(np.linalg.norm(np.array(temp_pts[2])-np.array(i)))
	temp_pts.append(points[np.argmax(np.array(dists))])
	points = temp_pts
	## getting 4 outer points ##

	points.sort()
	points = [points[i] for i in range(0, len(points), len(points) // 4)]
	if (points[0][1]>points[1][1]):
	    points[0],points[1]=points[1],points[0]
	if (points[-1][1]<points[-2][1]):
	    points[-1],points[-2]=points[-2],points[-1]

	points[1],points[2]=points[2],points[1]
	for i in points:
	    images = cv2.circle(image,(int(i[0]),int(i[1])),4,(0,0,255),-1)
	pts1 = np.float32(points)
	pts2 = np.float32([[0,0],[size,0],[0,size],[size,size]])
	M = cv2.getPerspectiveTransform(pts1,pts2)

	warped2 = cv2.warpPerspective(blank,M,(size,size))
	img = cv2.warpPerspective(original,M,(size,size))
	### Obtaining the sudoku in right perspective ###

	return img






'''print(len(points))
for x in points:
    image = cv2.circle(original, tuple(x), radius=3, color=(0, 0, 255), thickness=-1)'''
#cv2.imshow('window', img)
#cv2.waitKey(0)