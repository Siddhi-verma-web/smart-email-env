from env import EmailEnv

env = EmailEnv()
obs = env.reset()

done = False

while not done:
    print("Email:", obs["email"])

    action = {"label": "spam"}

    obs, reward, done, _ = env.step(action)

    print("Reward:", reward)
    print("------")