
  #Assignment 1 , Submitted By Shoyab Shaikh and Tejaswini Ugale
  #Website Link  (JavaScript Implementation for BFS) - https://friendsbfs.000webhostapp.com


import queue  
  

class FriendsDriver:
    
     
    def __init__(self):
        self.user_name = { 0:'Shoaib',1:"Sarang",2:"Tanmay",3:"Shantanu",4:"Atharva",5:"Tejaswini",6:"Dhanesh",7:"Kedar" }
        self.users = len(self.user_name)
        self.user_id = [[] for i in range(20)]

        
          
        
            
             
        
        self.user_id[0].append(1)  
        self.user_id[0].append(2)  
        self.user_id[1].append(3)  
        self.user_id[1].append(4)  
        self.user_id[1].append(5)  
        self.user_id[2].append(5)  
        self.user_id[2].append(6)  
        self.user_id[6].append(7)


    def addAccount(self):
        name = input("Enter Your Name:")
        
        self.user_name[len(self.user_name)] = name
        
        print("ID   Name")
        for u_id, name in self.user_name.items():
        
            print(u_id,"   ",name)
    
    



    def printLevels(self,user_id, V, x): 
      
    
        level = [None] * V  
        marked = [False] * V  
        searched_id = x
     
        que = queue.Queue() 
  
    
        que.put(x)  
  
      
    
        level[x] = 0
  
   
        marked[x] = True
  
    
        while (not que.empty()): 
  
        
            x = que.get()  
  
            
            for i in range(len(user_id[x])): 
              
            
                b = user_id[x][i]  
  
            
                if (not marked[b]):  
  
                 
                    que.put(b)  
  
                
                    level[b] = level[x] + 1
  
                
                    marked[b] = True
  
     
        
        #counter for finding number of friends and mutual friends:
        count_friend = 0
        count_mutual = 0
        for i in range(V):
            # if level[i] < 3:
            
                if level[i] == 1:
                    print("---------------------------------------------------------------------------")

                    print(self.user_name[i],"is friend of",self.user_name[searched_id])
                    count_friend += 1
                elif level[i] == 2:
                    print("---------------------------------------------------------------------------")
                    print(self.user_name[i],"is Mutual friend of",self.user_name[searched_id])
                    count_mutual += 1
        
        if count_friend > 0:
            print("---------------------------------------------------------------------------")
            print(self.user_name[searched_id],"Have",count_friend,"friend(s)")
            if count_mutual > 0:
                print(self.user_name[searched_id],"Have",count_mutual,"Mutual friend(s)")
            else:
                print(self.user_name[searched_id],"Have No Mutual friend")
        else:
            print("\n",self.user_name[searched_id],"Have No friends")
    
    







    
    
                
         

# Main Method 


if __name__ == '__main__': 
    frnd = FriendsDriver()
    # creating adjacency user_id  
    ch = 1
    while ch == 1:
        
        print("\n==================================================================================================================")
        ch = int(input("1.Display All Users \n2.Add New User \n3.Find Friends and Mutual Friends \n4.Make New Friends \n"))
        if ch == 1:
            print("\nID   Name\n---------------------")
            for u_id, name in frnd.user_name.items():
                print(u_id,"   ",name)

        if ch == 2:
            frnd.addAccount()
            
            
            
            print("\nUser Added..!!")

        if ch == 3:
            flag = 0
            search_name = input("Enter Name:")
            for u_id, name in frnd.user_name.items():    
                if name == search_name:
                    search_id = u_id
                    frnd.printLevels(frnd.user_id, len(frnd.user_name), search_id)
        
        if ch == 4:
            rsender = input("Enter Your Name:")
            for u_id, name in frnd.user_name.items():    
                if name == rsender:
                    request_search_id = u_id

            reciever = input("Enter Name Of Person With Whome You Want To Be Friend:")
            for u_id, name in frnd.user_name.items():    
                if name == reciever:
                    reciever_search_id = u_id
            
            frnd.user_id[request_search_id].append(reciever_search_id)
            print("\nYou Are Now Friend OF",reciever,"..!!")
                    
        

        
        
        ch = int(input("Enter 1 to continue : "))
        

    
    
    
    
    
    
    
      

            
    
     
    
    
     
  





   
    
