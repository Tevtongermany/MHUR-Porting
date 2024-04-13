import bpy
from mathutils import Vector


class MHURRig:
    def __init__(self, rig:bpy.types.Armature):
        self.rig = rig.data
        self.rig_object = rig
        self.bones = self.rig.bones
        self.editBones = self.rig.edit_bones
        self.poseBones = self.rig_object.pose.bones

    def getBone(self, name:str) -> bpy.types.Bone:
        return self.bones.get(name)
    
    def getEditBone(self, name:str) -> bpy.types.EditBone:
        return self.editBones.get(name)
    
    def getPoseBone(self, name:str) -> bpy.types.PoseBone:
        return self.poseBones.get(name)
    
    def ApplyRig(self):
        print("Edit mode stuff")
        bpy.ops.object.mode_set(mode='EDIT')
        L_elbow_Edit = self.getEditBone("L_elbow")
        R_elbow_Edit = self.getEditBone("R_elbow")
        L_Hand_Edit = self.getEditBone("L_hand")
        R_Hand_Edit = self.getEditBone("R_hand")
        R_Knee_Edit = self.getEditBone("R_knee")
        L_Knee_Edit = self.getEditBone("L_knee")
        L_Ankle_Edit = self.getEditBone("L_ankle")
        R_Ankle_Edit = self.getEditBone("R_ankle")
        # Pose bones
        L_elbow_Pose = self.getPoseBone("L_elbow")
        R_elbow_Pose = self.getPoseBone("R_elbow")
        L_Hand_Pose = self.getPoseBone("L_hand")
        R_Hand_Pose = self.getPoseBone("R_hand")
        R_Knee_Pose = self.getPoseBone("R_knee")
        L_Knee_Pose = self.getPoseBone("L_knee")
        L_Ankle_Pose = self.getPoseBone("L_ankle")
        R_Ankle_Pose = self.getPoseBone("R_ankle")


        # Hand IK
        L_elbow_Edit.tail = L_Hand_Edit.head
        R_elbow_Edit.tail = R_Hand_Edit.head


        IK_Arm_R_Edit: bpy.types.EditBone = self.editBones.new("IK_Arm_R")
        IK_Arm_R_Edit.head = R_Hand_Edit.head
        IK_Arm_R_Edit.tail = R_Hand_Edit.tail
        IK_Arm_R_Edit.roll = 1.5707963705062866
        


        IK_Arm_L_Edit: bpy.types.EditBone = self.editBones.new("IK_Arm_L")
        IK_Arm_L_Edit.head = L_Hand_Edit.head
        IK_Arm_L_Edit.tail = L_Hand_Edit.tail
        IK_Arm_L_Edit.roll = 1.5707963705062866

        IK_ElbowPole_R_Edit: bpy.types.EditBone = self.editBones.new("IK_ElbowPole_R")
        IK_ElbowPole_R_Edit.head = R_elbow_Edit.head + Vector((0, 0.32, 0))
        IK_ElbowPole_R_Edit.tail = R_elbow_Edit.head + Vector((0, 0.36, 0))

        IK_ElbowPole_L_Edit: bpy.types.EditBone = self.editBones.new("IK_ElbowPole_L")
        IK_ElbowPole_L_Edit.head = L_elbow_Edit.head + Vector((0, 0.32, 0))
        IK_ElbowPole_L_Edit.tail = L_elbow_Edit.head + Vector((0, 0.36, 0))

        L_Knee_Edit.tail = L_Ankle_Edit.head
        R_Knee_Edit.tail = R_Ankle_Edit.head

        IK_Knee_R_Edit: bpy.types.EditBone = self.editBones.new("IK_Knee_R")
        IK_Knee_R_Edit.head = R_Ankle_Edit.head
        IK_Knee_R_Edit.tail = R_Ankle_Edit.tail
        IK_Knee_R_Edit.roll = -1.5707963705062866
        


        IK_Knee_L_Edit: bpy.types.EditBone = self.editBones.new("IK_Knee_L")
        IK_Knee_L_Edit.head = L_Ankle_Edit.head
        IK_Knee_L_Edit.tail = L_Ankle_Edit.tail
        IK_Knee_L_Edit.roll = -1.5707963705062866

        IK_Knee_Pole_R_Edit: bpy.types.EditBone = self.editBones.new("IK_Knee_Pole_R")
        IK_Knee_Pole_R_Edit.head = R_Knee_Edit.head + Vector((0, -0.4, 0))
        IK_Knee_Pole_R_Edit.tail = R_Knee_Edit.head + Vector((0, -0.43, 0))

        IK_Knee_Pole_L_Edit: bpy.types.EditBone = self.editBones.new("IK_Knee_Pole_L")
        IK_Knee_Pole_L_Edit.head = L_Knee_Edit.head + Vector((0, -0.4, 0))
        IK_Knee_Pole_L_Edit.tail = L_Knee_Edit.head + Vector((0, -0.43, 0))


        bpy.ops.object.mode_set(mode='POSE')

        IK_elbow_r_ik = R_elbow_Pose.constraints.new('IK')
        IK_elbow_r_ik.target = self.rig_object
        IK_elbow_r_ik.subtarget = 'IK_Arm_R'
        IK_elbow_r_ik.pole_target = self.rig_object
        IK_elbow_r_ik.pole_subtarget = 'IK_ElbowPole_R'
        IK_elbow_r_ik.chain_count = 2
        IK_elbow_r_ik.pole_angle = 1.5707963705062866
        IK_elbow_r_ik.iterations = 500

        IK_elbow_l_ik = L_elbow_Pose.constraints.new('IK')
        IK_elbow_l_ik.target = self.rig_object
        IK_elbow_l_ik.subtarget = 'IK_Arm_L'
        IK_elbow_l_ik.pole_target = self.rig_object
        IK_elbow_l_ik.pole_subtarget = 'IK_ElbowPole_L'
        IK_elbow_l_ik.chain_count = 2
        IK_elbow_l_ik.pole_angle = -1.5707963705062866
        IK_elbow_l_ik.iterations = 500

        copy_rotation_hand_R = R_Hand_Pose.constraints.new('COPY_ROTATION')
        copy_rotation_hand_R.target = self.rig_object
        copy_rotation_hand_R.subtarget = 'IK_Arm_R'

        copy_rotation_hand_L = L_Hand_Pose.constraints.new('COPY_ROTATION')
        copy_rotation_hand_L.target = self.rig_object
        copy_rotation_hand_L.subtarget = 'IK_Arm_L'

        copy_rotation_L_ankle = L_Ankle_Pose.constraints.new('COPY_ROTATION')
        copy_rotation_L_ankle.target = self.rig_object
        copy_rotation_L_ankle.subtarget = 'IK_Knee_L'

        copy_rotation_R_ankle = R_Ankle_Pose.constraints.new('COPY_ROTATION')
        copy_rotation_R_ankle.target = self.rig_object
        copy_rotation_R_ankle.subtarget = 'IK_Knee_R'

        IK_Knee_r_ik = R_Knee_Pose.constraints.new('IK')
        IK_Knee_r_ik.target = self.rig_object
        IK_Knee_r_ik.subtarget = 'IK_Knee_R'
        IK_Knee_r_ik.pole_target = self.rig_object
        IK_Knee_r_ik.pole_subtarget = 'IK_Knee_Pole_R'
        IK_Knee_r_ik.chain_count = 2
        IK_Knee_r_ik.pole_angle = 3.1415927410125732
        IK_Knee_r_ik.iterations = 500

        IK_Knee_l_ik = L_Knee_Pose.constraints.new('IK')
        IK_Knee_l_ik.target = self.rig_object
        IK_Knee_l_ik.subtarget = 'IK_Knee_L'
        IK_Knee_l_ik.pole_target = self.rig_object
        IK_Knee_l_ik.pole_subtarget = 'IK_Knee_Pole_L'
        IK_Knee_l_ik.chain_count = 2
        IK_Knee_l_ik.pole_angle = 3.1415927410125732
        IK_Knee_l_ik.iterations = 500

        # Leg IK






