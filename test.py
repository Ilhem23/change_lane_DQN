import gym
import gym_sumo
from dqn import DQNAgent


env = gym.make('gym_sumo-v0')
agent = DQNAgent()
agent.train(env)






