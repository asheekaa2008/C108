import random
#import plotly.express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
count=[]
diceResult=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceResult.append(dice1+dice2)
    count.append(i)
mean=sum(diceResult)/len(diceResult)
median=statistics.median(diceResult)
mode=statistics.mode(diceResult)
standardDeviation=statistics.stdev(diceResult)
#figure=px.bar(x=diceResult,y=count)
#figure=ff.create_distplot([diceResult],["result"],show_hist=False)
#figure.show()
#print(mean,median,mode)
#print(standardDeviation)
firstSDstart,firstSDend=mean-standardDeviation,mean+standardDeviation
secondSDstart,secondSDend=mean-(2*standardDeviation),mean+(2*standardDeviation)
thirdSDstart,thirdSDend=mean-(3*standardDeviation),mean+(3*standardDeviation)
figure=ff.create_distplot([diceResult],["result"],show_hist=False)
figure.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
figure.add_trace(go.Scatter(x=[firstSDstart,firstSDstart],y=[0,0.17],mode="lines",name="sd1"))
figure.add_trace(go.Scatter(x=[firstSDend,firstSDend],y=[0,0.17],mode="lines",name="sd1"))
figure.add_trace(go.Scatter(x=[secondSDstart,secondSDstart],y=[0,0.17],mode="lines",name="sd2"))
figure.add_trace(go.Scatter(x=[secondSDend,secondSDend],y=[0,0.17],mode="lines",name="sd12"))
figure.show()
listsd1=[result for result in diceResult if result>firstSDstart and result<firstSDend]
listsd2=[result for result in diceResult if result>secondSDstart and result<secondSDend]
listsd3=[result for result in diceResult if result>thirdSDstart and result<thirdSDend]
print("{}% of data lies between first standardDeviation ".format(len(listsd1)*100.0/len(diceResult)))
print("{}% of data lies between second standardDeviation ".format(len(listsd2)*100.0/len(diceResult)))
print("{}% of data lies between third standardDeviation ".format(len(listsd3)*100.0/len(diceResult)))































