import sys
sys.path.append("C:/Users/MLUSER/Documents/GitHub/Udacity/Reinforcement Learning/Part1")


from env import ArmEnv
from rl import DDPG



MAX_EPISODES = 500
MAX_EP_STEPS = 200

#set env
env = ArmEnv()
s_dim = env.state_dim
a_dim = env.action_dim
a_bound = env.action_bound

#set RL Method
rl = DDPG(a_dim,s_dim,a_bound)

#start training
for i in range(MAX_EPSIDODES):
    s = env.reset()
    for j in range(MAX_EP_STEPS):
        env.render()
        a = rl.choose_actions(s)
        s_,r,done = env.steps(a)
    rl.store_transition(s,a,r,s_)
    
    if rl.memory_full:
        rl.learn()