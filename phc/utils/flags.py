__all__ = ['flags', 'summation']

class Flags(object):
    def __init__(self, items):
        for key, val in items.items():
            setattr(self,key,val)

flags = Flags({
    'test': False, 
    'debug': False,
    "real_traj": False,
    "im_eval": False,
    "noise_sigma": 0.0,
    "noise_theta": 0.0,
    "joint_id_noise": 7,
    "motion_id": -1,
    })
