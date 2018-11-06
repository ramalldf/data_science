import random

        
def calc_dist(val1, val2):
    my_dist= (val1-val2)**2
    
    return my_dist


def init_labeling(k, x):
    #Need to initialize position of the houses (cluster centers)
    #Centers be a random number between max and min values in x
    cluster0_pos= [random.uniform(min(x), max(x)) for i in range(k)]
    distances= []
    group_labels= []
    
    #For every point, calc. distance to cluster centers
    for m in range(len(x)):
        nearest_cluster= []
        
        for j in range(k):
            dist_to_cluster= calc_dist(x[m], cluster0_pos[j])
            nearest_cluster.append(dist_to_cluster)
            
        #From distances, find min distance of point to center to assign
        #it to that cluster
        group_labels.append(nearest_cluster.index(min(nearest_cluster)))    
        
    #Return intial positions and labels for all points
    return cluster0_pos, group_labels

def calc_group_dists(labels, orig_data, k_val):
    """Calculates the within cluster variation of each group."""
    group_data= []
    all_dists= []
    
    #Group data by label
    for n in range(k_val):
        group_vals= [orig_data[i] for i in range(len(labels)) if labels[i] == n]
        group_data.append(group_vals)
        
        #Find distance of all points to one another and take sum
        group_dist = [(group_vals[i]-group_vals[j])**2 for i in range(len(group_vals)) for j in range(len(group_vals)) if i != j]
        all_dists.append(sum(group_dist))
    
    #Return sum of all cluster sums divided by # of points
    #also return data in their groups
    return sum(all_dists)/len(labels), group_data

def recalc_center_pos(group_positions, orig_data):
    """Recalculates cluster centers by taking mean of points in that group."""
    new_mean_centers= [1.0*sum(x)/len(x) if len(x)!=0 else random.uniform(min(orig_data), max(orig_data)) for x in group_positions]
    
    
    return new_mean_centers
    
#=========================#
random.seed(a=42)
sample= [4,3,10,9,5,17,2,24,18,16,6,20,11]
k_val= 3

#Initialize centers and assign labels to data
center_positions_0, data_labels_0= init_labeling(3, sample)


#Calculate distance of points to centers and get 
#total cluster variation

cluster_var_0, cluster_data_0= calc_group_dists(data_labels_0, sample, 3)

#Now we'll enter loop to update the centers and variation every time
#Update the 
current_variation= cluster_var_0
current_mean_center= center_positions_0
cluster_data_iter= cluster_data_0

new_variation= current_variation+1

while new_variation != current_variation:
    #Assuming new variation score and current score aren't the same,
    #label current as new for new iteration
    current_variation= new_variation
    new_centers= recalc_center_pos(cluster_data_iter, sample)
    group_labels= []
    
    #For every point, calc. distance to cluster centers
    for m in range(len(sample)):
        nearest_cluster= []
        
        for j in range(k_val):
            dist_to_cluster= calc_dist(sample[m], new_centers[j])
            nearest_cluster.append(dist_to_cluster)
            
        #From distances, find min distance of point to center to assign
        #it to that cluster
        group_labels.append(nearest_cluster.index(min(nearest_cluster)))  
    

    #Update values for clustered_data and variation score    
    new_variation, cluster_data_new= calc_group_dists(group_labels, sample, 3)  
    cluster_data_iter= cluster_data_new
    
    print(group_labels, new_variation)
    


