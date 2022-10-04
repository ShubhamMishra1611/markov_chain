#Simulate a single layer markov chain

import numpy as np

class Markov_chain:

    def __init__(self,states:list,t_mat:list) -> None:
        '''
        The states takes name of states as list and convert them into the dictionary
        The t_mat represent the transition matrix .
        For verification with initialization of the class it shows how the transtion matrix
            like
        '''
        self.states={}
        self.t_mat=t_mat
        for i in range(len(states)):
            if not states[i] in self.states:
                self.states[i]=states[i]
        
        #write a code to explicitly show the transition matrix

        print("The given states are :",self.states)
        print("The transition matrix is :",t_mat)


    def calculating_stationary_states(self):
        #k=LA.eig()
        pass

    def simulation(self,initial_state=0,n_steps:int=10):
        for _ in range(n_steps):



        