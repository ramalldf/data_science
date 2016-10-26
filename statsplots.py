def cdfPlot(numArray):
    '''Takes in an array and creates a cumulative 
    distribution function (CDF) plot.
    '''
    import matplotlib.pyplot as plt
    import numpy as np
    
    sortArray= sorted(numArray)
    step= 1.0/len(numArray)
    scaledArray= np.arange(0,1,step)
    
    
    fig, ax = plt.subplots(1,1, figsize=(5,5))
    plt.style.use('fivethirtyeight')

    plt.plot(scaledArray,sortArray)#, color= '#0099ff')   

        #Customize appearance of plot
    plt.title('Change Title', fontsize= 21, fontweight= 'bold')
    
    plt.xlabel('Your Label Here', fontsize=17,fontweight= 'bold')
    plt.ylabel('Your Label Here', fontsize=17, fontweight= 'bold')
    ax.tick_params(axis='both', which='major', labelsize=13, labelcolor= '#7c7e82')#Adjust size of x,y labels
    ax.tick_params(axis='both', which='major', labelsize=13)