import gym

def make(envname):
    print("🔥 🔥 🔥 Imporing Gym environment from Python:")
    en = str(envname, encoding='ascii')
    print("⏩ ⏩ ⏩ {0}".format(envname))
    print("🔥 🔥 🔥 😎")
    env = gym.make(en)
    env.reset()
    return env

def step(env, _step):
    observation = env.step(_step)
    return (env, observation)

def render(env):
    env.render()