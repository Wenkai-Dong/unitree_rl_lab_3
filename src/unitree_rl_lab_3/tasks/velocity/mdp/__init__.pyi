# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

__all__ = [
    "UniformLevelVelocityCommandCfg",
    "lin_vel_cmd_levels",
    "ang_vel_cmd_levels",
    "newton_randomize_rigid_body_material",
    "gait_phase",
    "energy",
    "stand_still",
    "orientation_l2",
    "upward",
    "joint_position_penalty",
    "feet_stumble",
    "feet_height_body",
    "foot_clearance_reward",
    "feet_too_near",
    "feet_contact_without_cmd",
    "air_time_variance_penalty",
    "feet_gait",
    "joint_mirror",
]

# Forward stable MDP terms lazily, then override with environment-specific terms below.
from isaaclab.envs.mdp import *  # noqa: F401, F403
from isaaclab_tasks.core.velocity.mdp import *  # noqa: F401, F403


from .commands import UniformLevelVelocityCommandCfg
from .curriculums import lin_vel_cmd_levels, ang_vel_cmd_levels
from .events import newton_randomize_rigid_body_material
from .observations import gait_phase
from .rewards import (
    energy,
    stand_still,
    orientation_l2,
    upward,
    joint_position_penalty,
    feet_stumble,
    feet_height_body,
    foot_clearance_reward,
    feet_too_near,
    feet_contact_without_cmd,
    air_time_variance_penalty,
    feet_gait,
    joint_mirror,
)
