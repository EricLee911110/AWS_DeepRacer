# AWS_DeepRacer
Testing out the reward function, also work as a journal about how I reach the top 50s in the AWS Student League :D

![image](https://user-images.githubusercontent.com/79837982/167280862-d196ec67-24ad-4748-a4f5-e24c137c98bc.png)


## First Attempt
First try on a 10 minutes training.

![image](https://user-images.githubusercontent.com/79837982/167244407-58c81392-a65a-4487-98ce-f0e8dba398f1.png)

## Second Attempt
Try 60 minutes of training on the new method(Point to the tangent of the two closest waypoints). The distances between two waypoints are too far that's why it failed. A great lesson to learn is when you test out a new reward function. You should do an MVP and check out the result. Instead of waiting for it for 60 minutes, 20 minutes will be enough to see how the new method approach. 

![image](https://user-images.githubusercontent.com/79837982/167281225-ed8a397f-5e7e-4f0d-ae7f-bed086c0d660.png)
![image](https://user-images.githubusercontent.com/79837982/167281226-63c78f66-8680-4cc2-9a43-dffed8975973.png)
![image](https://user-images.githubusercontent.com/79837982/167280587-2f2a2cd4-7b36-461a-beb9-964120f38f6e.png)

For video ([link](https://user-images.githubusercontent.com/79837982/167280804-9c4370b3-420f-4a1d-a341-4913959fc3e2.mp4))

## Third Attempt
20 minutes of training focusing on the difference between heading and car_next_waypoint_degree. The system will get a heavy penalty(reward *= 0.1) if the difference this larger than the threshold(40 degrees). It turns out that when occurring corners, they think the previous behavior is completely wrong. So the system tends to have a hard right turn even if they should keep turning left.

![image](https://user-images.githubusercontent.com/79837982/167281387-a804d326-acdf-4625-ab49-8c3287ad889b.png)
![image](https://user-images.githubusercontent.com/79837982/167282891-428099a3-0a9d-48a0-940a-d90a5953aabc.png)


## Fourth Attempt
Same as Attempt_3 but less penalty which turns out the system behaves less sharp turns than the previous model. The system becomes numb to penalties and requires more time to train. Still, this idea won't work.

![image](https://user-images.githubusercontent.com/79837982/167284966-3f5ab1bc-8254-478f-b676-a4c6e311ba33.png)
Video ([link](https://user-images.githubusercontent.com/79837982/167285248-a2fb9a3d-c0d1-4aa0-81a8-0648deb88bb4.mp4))

## Fifth Attempt
The problem with all the attempts I have is that the system won't know what to do if it is approaching the corner. So, I decided to give a penalty if the car stays on the right side of the track in front of a left-turning corner and the same conversely. Another feature is to compare progress-difference between now and 30 seconds before. The system will get more reward if it progressed more than before.

![image](https://user-images.githubusercontent.com/79837982/167288731-4e677e18-1e22-4243-b57a-0d44a17c44c0.png)
Video([Link](https://user-images.githubusercontent.com/79837982/167288974-064254d3-fa50-469e-a3e4-925c1dc11e0e.mp4))

YESSS!! It only went off-track for 4 times and I got a really good score of 3:17. It is close to the Udacity nanodegree requirement. Let's keep the good pace going. :) 

## Fifth_two Attempt
There is three ways can fix the problem of running off-track. First, more reward is the car is cloeser to the center line. Second, more reward staying in either the right side or the left side. Third, more training time.

![image](https://user-images.githubusercontent.com/79837982/167291299-e8320507-385d-474c-816c-aa869351f5bf.png)

Simply add 10 minutes does help the model to perform better.

## Sixth Attempt
Less penalty if the car is on the other side-wanted. 0.7 -> 0.8
Try to be more at the center. Shrink marker_2 0.3 -> 0.25

![image](https://user-images.githubusercontent.com/79837982/167293705-0de689cc-7cff-412d-80af-221f74b72aba.png)
Video([link](Uploading output3.mp4…))

After the testing. I really think vague commands really need more time training.

## Seventh Attempt
Origin penalty if the car is on the other side-wanted 0.8 -> 0.7
Less reward on marker_2 0.9 -> 0.8

![image](https://user-images.githubusercontent.com/79837982/167296888-24799996-2783-4929-83a8-ceccd6c037db.png)
Video([Link](https://user-images.githubusercontent.com/79837982/167297034-d126a914-0674-4e70-8f66-f4617d777632.mp4))

I don't know what I did wrong.....

## Eighth Attempt
GAS GAS GAS! I'm gonna step on the gas.
Clone of Fifth Attempt. Add up the speed detection function.

![image](https://user-images.githubusercontent.com/79837982/167299534-5fb82dde-32dd-4a78-91d6-06b5be7db418.png)
Video([link](https://user-images.githubusercontent.com/79837982/167299550-1f6bbf15-8297-4bdf-b633-1faf0990eec7.mp4))

Maybe have to train it from the beginning to speed it up

## Ninth Attempt
Speed up with progress and avg_speed.

![image](https://user-images.githubusercontent.com/79837982/167302519-5eb0ea01-a449-421c-b522-c86fadaaf8e6.png)
Video([link](https://user-images.githubusercontent.com/79837982/167302538-14aa8f10-566c-4982-b7b1-6c096a2a196b.mp4))

The run is almost good as Fifth Attempt, but the speed didn't inprove significantly.

## Tenth Attempt
Canceled

## Eleventh Attempt

Check speed every 3 second and made the reward *1.32. Progress_diff turn up to *1.2
30 mins of training. No penalty while making a right turn.

![image](https://user-images.githubusercontent.com/79837982/167306147-2054fbd6-2019-4873-a178-51f26411c560.png)
Video([link](https://user-images.githubusercontent.com/79837982/167306211-a940ed0d-3fcb-44c3-a4eb-c225ad249816.mp4))

## Twelfth Attempt
Speed every 2 seconds *1.22 Progress_diff *1.1 More reward sticking toward boarder while turing *1.15. 
20 mins training

![image](https://user-images.githubusercontent.com/79837982/167309944-0c99762f-b45d-4a04-9f4e-51b583f3702c.png)
Video([link](https://user-images.githubusercontent.com/79837982/167312554-c9c7159b-a3b4-4a20-9b62-2a3f46c2059e.mp4))

## Thirteenth Attempt
20 more training with clone of 12th.

![image](https://user-images.githubusercontent.com/79837982/167312568-2f85edaf-7dc8-46ff-ba9c-5b80f2a3d24c.png)

Video([link](https://user-images.githubusercontent.com/79837982/167312527-4ed6cb48-b09d-41df-b6d0-cf285092c510.mp4))

## Fourteenth Attempt
20 mins. Speed every 1 second. Turn left penalty 0.7 -> 0.6. Remove speed up by progress.

![image](https://user-images.githubusercontent.com/79837982/167315428-abcbb412-06a0-4249-918a-05c6a3af3009.png)


## Fifteenth Attempt
20 more mins training clone of 14th.

![image](https://user-images.githubusercontent.com/79837982/167317983-989c678d-c0cc-4291-92c4-f2db93829fe6.png)


## Sixteenth Attempt
20 more mins training clone 14th.

## Seventeenth Attempt
20 more mins training clone 14th. But track_angle 10 -> 5

## Eighteenth Attempt
Less reward for being on the right side of the track 1.1 -> 1.05 Init waypoint set to 0 instead of 1. Marker_2 *0.8

## Nineteenth Attempt
20 more mins training clone 18th.

![image](https://user-images.githubusercontent.com/79837982/167358957-49510f05-1124-41d2-a066-7af62a6bb37c.png)
Video([link](https://user-images.githubusercontent.com/79837982/167359013-f0c3099b-af3c-4faa-8a98-1ff15f326446.mp4))

Still have the problem that will keep running off track on the same spot.

## Twentieth Attempt
15 mins. Right side rewar 1.05 -> 1.03 Turn left angle 5 -> 18

![image](https://user-images.githubusercontent.com/79837982/167367330-e2b4a714-16da-49b8-b848-c17062d22709.png)


## 21th Attempt

10 mins Turn left angle 18 -> 0


## 22th Attempt

Clone of 15th attempt. Right side bonus only on straight line or turning right. 

![image](https://user-images.githubusercontent.com/79837982/167399885-d4ca4acf-afa0-4f81-91c3-3a4ce69dba7f.png)



## 23th Attempt
Clone of 22th attempt. Straight line marker_2 0.75 -> 0.72. Left turn distance from center 1.15 -> 1.18

![image](https://user-images.githubusercontent.com/79837982/167426958-0415ad8c-58c6-46fe-8569-4d79e06ac820.png)


## 24th Attempt
Clone of 23 attempt. Right side rewar 1.03 -> 1.01 Left turn distance from cetner 1.18 -> 1.2

![image](https://user-images.githubusercontent.com/79837982/167445380-15fbfb3c-b93e-4914-a7ff-ab30eb327757.png)


## 25th Attempt
20 mins. marker_1*1.22 marker_2 * 1.2  

![image](https://user-images.githubusercontent.com/79837982/167518162-37c671c9-52f9-4eac-980b-f5c19e1a43fc.png)
Video([link](https://user-images.githubusercontent.com/79837982/167518392-05c32359-319f-4920-9296-2d4224ab9500.mp4))

Personal Best :D

## 26th Attempt

20 mins. clone of 25th attempt. Right side reward 1.02. marker2 when turning left 1.21. 

![image](https://user-images.githubusercontent.com/79837982/167525749-2b3bac37-b74f-4588-bc8f-7f97c17c8cee.png)
Video([link](https://user-images.githubusercontent.com/79837982/167525856-319d37bb-cca2-4b87-8dda-e6fdbf97c688.mp4))

Break personal best again!

## 27th Attempt

20 mins. Clone of 26th attempt. Right side reward 1.02 -> 1.01. Left side reward turning left 1.0 -> 1.02

![image](https://user-images.githubusercontent.com/79837982/167562773-3990ed64-d70f-4578-b583-ce878afa7db3.png)


## 28th Attempt

20 mins. Clone of 26th attempt. Track_4 *0.6 Track_3 0.1 -> 0.8 marker_1 1.22 -> 1.25

![image](https://user-images.githubusercontent.com/79837982/167575614-23919cf4-eff7-4670-897f-9129893c894b.png)


## 29th Attempt

55 mins. Same as 28th, but I think the problem with 28th attempt is that it keeps the memory from the pass. That's why it keeps failing. Last try of this month.

![image](https://user-images.githubusercontent.com/79837982/167607421-71f6d1ce-c606-4bac-9aef-332a494c4887.png)

Didn't go off track. That is the most happiest thing ever :D
Unfortunately, the speed isn't fast enough. The record final record is 03:10.126
Let's just put this aside and join again next month, you will see me come back June, 2022. Stay tuned. :)

