import gym
import gym_traffic
from gym.wrappers import Monitor
import gym
import time
from tqdm import tqdm
monitor = False 
fh = open("test.out","w")
#env = gym.make('Traffic-Simple-gui-v0')
env = gym.make('Traffic-Simple-cli-v0')
if monitor:
    env = Monitor(env, "output/traffic/simple/random", force=True)
for i_episode in tqdm(range(500)):
    observation = env.reset()
    for t in tqdm(range(1000)):
        #env.render()
        #print(observation)
        action = env.action_space.sample()[0][1]
        #time.sleep(1)
        observation, reward, done, info = env.step(action)
        fh.write(f"{action},{observation},{reward},{done},{info}\n")
        #print "Reward: {}".format(reward)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
