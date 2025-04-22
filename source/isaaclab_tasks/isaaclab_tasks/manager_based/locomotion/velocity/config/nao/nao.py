# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for the NAO robot."""

from __future__ import annotations

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets import ArticulationCfg
from isaaclab.utils.assets import ISAAC_NUCLEUS_DIR

##
# Configuration
##

NAO_MINIMAL_CFG = ArticulationCfg(
    prim_path="{ENV_REGEX_NS}/Robot",
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"C:/Users/reill/IsaacLab/nao/nao2/nao_nohands.usd",  # Path to NAO USD file
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            enable_gyroscopic_forces=True,
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=8,
            solver_velocity_iteration_count=1,  # Increased for better stability
            sleep_threshold=0.005,  # Lowered for more responsive behavior
            stabilization_threshold=0.001,
        ),
        copy_from_source=False,
        activate_contact_sensors=True,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.345),  # NAO is about 58cm tall, starting with feet on ground
        joint_pos={
            # Define specific initial poses for better stability if needed
            # Example: starting with slightly bent knees
            # ".*KneePitch": 0.1,
            "HeadYaw": 0.0,
            "HeadPitch": 0.0,
            
            # Arms
            "RShoulderPitch": 1.5,
            "LShoulderPitch": 1.5,
            "RShoulderRoll": -0.05,
            "LShoulderRoll": 0.05,
            ".*ElbowYaw": 0.0,
            ".*WristYaw": 0.0,
            # ".*Hand": 1.0,
            
            # Legs
            ".*HipYawPitch": 0.0,
            ".*HipRoll": 0.0,
            ".*HipPitch": 0.0,
            ".*KneePitch": 0.0,
            ".*AnklePitch": 0.0,
            ".*AnkleRoll": 0.0,
            "RElbowRoll": 0.05,
            "LElbowRoll": -0.05,
        },
    ),
    actuators={
       # Updated Actuator Configurations
        "Nao_arms": ImplicitActuatorCfg(
            joint_names_expr=[
                "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
                "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll"
            ],
            effort_limit=50.0,
            velocity_limit=1.5,
            stiffness=80.0,
            damping=4.0,
        ),
        "Nao_legs": ImplicitActuatorCfg(
            joint_names_expr=[
                "LHipYawPitch", "LHipRoll", "LHipPitch", "LKneePitch",
                "LAnklePitch", "LAnkleRoll", "RHipYawPitch", "RHipRoll",
                "RHipPitch", "RKneePitch", "RAnklePitch", "RAnkleRoll"
            ],
            effort_limit=100.0,
            velocity_limit=3,
            stiffness=120.0,
            damping=3.0,
        ),
        # "Nao_head": ImplicitActuatorCfg(
        #     joint_names_expr=["HeadYaw", "HeadPitch"],
        #     effort_limit=10.0,
        #     velocity_limit=1.0,
        #     stiffness=100.0,
        #     damping=5.0,
        # ),
        # "Nao_hands": ImplicitActuatorCfg(
        #     joint_names_expr=[
        #         "LHand", "RHand", "LFinger11", "RFinger11",
        #         "LFinger12", "RFinger12", "LFinger21", "RFinger21",
        #         "LFinger22", "RFinger22", "LThumb1", "RThumb1",
        #         "LThumb2", "RThumb2", "LFinger13", "LFinger23",
        #         "RFinger13", "RFinger23", "LWristYaw", "RWristYaw"
        #     ],
        #     effort_limit=5.0,
        #     velocity_limit=1.0,
        #     stiffness=50.0,
        #     damping=2.0,
        # ),
    },
)
"""Configuration for the NAO robot."""

# You can keep the HUMANOID_CFG if needed or comment it out
"""
HUMANOID_CFG = ArticulationCfg(
    # Original humanoid configuration...
)
"""