import ray
from ray import tune

ray.init()
tune.run(
    "DQN",
    stop={"episode_reward_mean": 200},
    config={
        "env": "Breakout-v0",
        "num_gpus": 1,
        "num_workers": 1,
    },
)