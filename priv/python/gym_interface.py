import gym
from erlport.erlang import set_encoder, set_decoder


def make(envname):
    print("🔥 🔥 🔥 Imporing Gym environment from Python:")
    en = str(envname, encoding='ascii')
    print("⏩ ⏩ ⏩ {0}".format(envname))
    print("🔥 🔥 🔥 😎")
    env = gym.make(en)
    initial_state = env.reset()
    action_space = str(env.action_space).strip()
    return (env, initial_state, action_space)


def step(env, _step):
    observation = env.step(_step)
    return (env, observation)


def render(env):
    #    env.env.ale.saveScreenPNG(b'test_image.png')
    #res = env.render(mode='rgb_array')
    env.render()


def reset(env):
    initial_state = env.reset()
    return (env, initial_state, str(env.action_space).strip())


def action_space_sample(env):
    return env.action_space.sample()
