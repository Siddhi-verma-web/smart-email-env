from models import Observation, Action, Reward

class EmailEnv:

    def __init__(self):
        self.data = [
            ("Win a free iPhone now!!!", "spam"),
            ("Meeting at 5 PM", "important"),
            ("Huge discount offer", "spam"),
            ("Project submission tomorrow", "important")
        ]
        self.index = 0

    def reset(self):
        self.index = 0
        return {"email": self.data[self.index][0]}

    def step(self, action):
        correct = self.data[self.index][1]

        if action["label"] == correct:
            reward = 1
        else:
            reward = -1

        self.index += 1
        done = self.index >= len(self.data)

        next_obs = None if done else {"email": self.data[self.index][0]}

        return next_obs, reward, done, {}