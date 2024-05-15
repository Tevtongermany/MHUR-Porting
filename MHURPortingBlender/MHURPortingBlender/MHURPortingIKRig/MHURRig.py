import bpy
from mathutils import Vector


class MHURRig:
    def __init__(self, rig:bpy.types.Armature):
        self.rig = rig.data
        self.rig_object = rig
        self.bones = self.rig.bones
        self.editBones: bpy.types.ArmatureEditBones = self.rig.edit_bones
        self.poseBones = self.rig_object.pose.bones

    def getBone(self, name:str) -> bpy.types.Bone:
        return self.bones.get(name)

    def getEditBone(self, name:str) -> bpy.types.EditBone:
        return self.editBones.get(name)

    def getPoseBone(self, name:str) -> bpy.types.PoseBone:
        return self.poseBones.get(name)

    def deleteEditBone(self, name:str):
        return self.editBones.remove(self.getEditBone(name))

    def addEditBone(self, name:str) -> bpy.types.EditBone:
        return self.editBones.new(name)

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
        L_Arm_Edit = self.getEditBone("L_arm")
        R_Arm_Edit = self.getEditBone("R_arm")
        Root = self.getEditBone("root")

        R_thumbfinger_C = self.getEditBone("R_thumbfinger_C")
        R_indexfinger_C = self.getEditBone("R_indexfinger_C")
        R_middlefinger_C = self.getEditBone("R_middlefinger_C")
        R_ringfinger_C = self.getEditBone("R_ringfinger_C")
        R_pinkyfinger_C = self.getEditBone("R_littlefinger_C")

        L_thumbfinger_C = self.getEditBone("L_thumbfinger_C")
        L_indexfinger_C = self.getEditBone("L_indexfinger_C")
        L_middlefinger_C = self.getEditBone("L_middlefinger_C")
        L_ringfinger_C = self.getEditBone("L_ringfinger_C")
        L_pinkyfinger_C = self.getEditBone("L_littlefinger_C")

        # Pose bones
        L_elbow_Pose = self.getPoseBone("L_elbow")
        R_elbow_Pose = self.getPoseBone("R_elbow")
        L_Hand_Pose = self.getPoseBone("L_hand")
        R_Hand_Pose = self.getPoseBone("R_hand")
        R_Knee_Pose = self.getPoseBone("R_knee")
        L_Knee_Pose = self.getPoseBone("L_knee")
        L_Ankle_Pose = self.getPoseBone("L_ankle")
        R_Ankle_Pose = self.getPoseBone("R_ankle")
        R_thumbfinger_C_Pose = self.getPoseBone("R_thumbfinger_C")
        R_indexfinger_C_Pose = self.getPoseBone("R_indexfinger_C")
        R_middlefinger_C_Pose = self.getPoseBone("R_middlefinger_C")
        R_ringfinger_C_Pose = self.getPoseBone("R_ringfinger_C")
        R_pinkyfinger_C_Pose = self.getPoseBone("R_littlefinger_C")

        L_thumbfinger_C_Pose = self.getPoseBone("L_thumbfinger_C")
        L_indexfinger_C_Pose = self.getPoseBone("L_indexfinger_C")
        L_middlefinger_C_Pose = self.getPoseBone("L_middlefinger_C")
        L_ringfinger_C_Pose = self.getPoseBone("L_ringfinger_C")
        L_pinkyfinger_C_Pose = self.getPoseBone("L_littlefinger_C")



    


        # connect the elbows to the hands
        # left arm


        L_Arm_Edit.tail = L_elbow_Edit.head
        L_elbow_Edit.use_connect = True
        L_Arm_Edit.tail = L_Arm_Edit.tail + Vector((0,0.003,0))

        # right arm
        R_Arm_Edit.tail = R_elbow_Edit.head
        L_elbow_Edit.use_connect = True
        R_Arm_Edit.tail = R_Arm_Edit.tail + Vector((0,0.003,0))



        # Hand IK Stuff
        L_elbow_Edit.tail = L_Hand_Edit.head
        R_elbow_Edit.tail = R_Hand_Edit.head

        # right IK Arm bones
        IK_Arm_R_Edit: bpy.types.EditBone = self.editBones.new("IK_Arm_R")
        IK_Arm_R_Edit.head = R_Hand_Edit.head
        IK_Arm_R_Edit.tail = R_Hand_Edit.tail
        IK_Arm_R_Edit.roll = 1.5707963705062866

        # Finger IK bones
        # Right Finger IK bones

        IK_Finger_R_Thumb_Edit: bpy.types.EditBone = self.editBones.new("IK_Finger_R_Thumb")
        IK_Finger_R_Thumb_Edit.head = R_thumbfinger_C.tail
        IK_Finger_R_Thumb_Edit.tail = R_thumbfinger_C.head -  Vector((0.018431,0.017664,0.00981))
        IK_Finger_R_Thumb_Edit.roll = 1.5707963705062866

        IK_Finger_R_Middle_Edit: bpy.types.EditBone = self.editBones.new("IK_Finger_R_Middle")
        IK_Finger_R_Middle_Edit.head = R_middlefinger_C.tail
        IK_Finger_R_Middle_Edit.tail = R_middlefinger_C.head + Vector((-0.1,0,0))
        IK_Finger_R_Middle_Edit.roll = 1.5707963705062866

        IK_Finger_R_Index_Edit: bpy.types.EditBone = self.editBones.new("IK_Finger_R_Index")
        IK_Finger_R_Index_Edit.head = R_indexfinger_C.tail
        IK_Finger_R_Index_Edit.tail = R_indexfinger_C.head + Vector((-0.1,0,0))
        IK_Finger_R_Index_Edit.roll = 1.5707963705062866


        IK_Finger_R_Ring_Edit: bpy.types.EditBone = self.editBones.new("IK_Finger_R_Ring")
        IK_Finger_R_Ring_Edit.head = R_ringfinger_C.tail
        IK_Finger_R_Ring_Edit.tail = R_ringfinger_C.head + Vector((-0.1,0,0))
        IK_Finger_R_Ring_Edit.roll = 1.5707963705062866

        IK_Finger_R_Pinky_Edit: bpy.types.EditBone = self.editBones.new("IK_Finger_R_Pinky")
        IK_Finger_R_Pinky_Edit.head = R_pinkyfinger_C.tail
        IK_Finger_R_Pinky_Edit.tail = R_pinkyfinger_C.head + Vector((-0.1,0,0))
        IK_Finger_R_Pinky_Edit.roll = 1.5707963705062866

        # parent fingers to hand
        IK_Finger_R_Thumb_Edit.parent = R_Hand_Edit
        IK_Finger_R_Index_Edit.parent = R_Hand_Edit
        IK_Finger_R_Middle_Edit.parent = R_Hand_Edit
        IK_Finger_R_Ring_Edit.parent = R_Hand_Edit
        IK_Finger_R_Pinky_Edit.parent = R_Hand_Edit

        

        # Left Finger IK bones
        IK_Finger_L_Thumb_Edit: bpy.types.EditBone = self.editBones.new("IK_Finger_L_Thumb")
        IK_Finger_L_Thumb_Edit.head = L_thumbfinger_C.tail
        IK_Finger_L_Thumb_Edit.tail = L_thumbfinger_C.head +  Vector((0.03743,-0.02453,-0.01969))
        IK_Finger_L_Thumb_Edit.roll = 1.5707963705062866

        IK_Finger_L_Index_Edit: bpy.types.EditBone = self.editBones.new("IK_Finger_L_Index")
        IK_Finger_L_Index_Edit.head = L_indexfinger_C.tail
        IK_Finger_L_Index_Edit.tail = L_indexfinger_C.head + Vector((0.1,0,0))
        IK_Finger_L_Index_Edit.roll = 1.5707963705062866

        IK_Finger_L_Middle_Edit: bpy.types.EditBone = self.editBones.new("IK_Finger_L_Middle")
        IK_Finger_L_Middle_Edit.head = L_middlefinger_C.tail
        IK_Finger_L_Middle_Edit.tail = L_middlefinger_C.head + Vector((0.1,0,0))
        IK_Finger_L_Middle_Edit.roll = 1.5707963705062866

        IK_Finger_L_Ring_Edit: bpy.types.EditBone = self.editBones.new("IK_Finger_L_Ring")
        IK_Finger_L_Ring_Edit.head = L_ringfinger_C.tail
        IK_Finger_L_Ring_Edit.tail = L_ringfinger_C.head + Vector((0.1,0,0))
        IK_Finger_L_Ring_Edit.roll = 1.5707963705062866

        IK_Finger_L_Pinky_Edit: bpy.types.EditBone = self.editBones.new("IK_Finger_L_Pinky")
        IK_Finger_L_Pinky_Edit.head = L_pinkyfinger_C.tail
        IK_Finger_L_Pinky_Edit.tail = L_pinkyfinger_C.head + Vector((0.1,0,0))
        IK_Finger_L_Pinky_Edit.roll = 1.5707963705062866

        # parent fingers to hand
        IK_Finger_L_Thumb_Edit.parent = L_Hand_Edit
        IK_Finger_L_Index_Edit.parent = L_Hand_Edit
        IK_Finger_L_Middle_Edit.parent = L_Hand_Edit
        IK_Finger_L_Ring_Edit.parent = L_Hand_Edit
        IK_Finger_L_Pinky_Edit.parent = L_Hand_Edit

                


        # Left IK Arm bones
        IK_Arm_L_Edit: bpy.types.EditBone = self.editBones.new("IK_Arm_L")
        IK_Arm_L_Edit.head = L_Hand_Edit.head
        IK_Arm_L_Edit.tail = L_Hand_Edit.tail
        IK_Arm_L_Edit.roll = 1.5707963705062866


        # Adding Pole Targets
        # Right Pole Target
        IK_ElbowPole_R_Edit: bpy.types.EditBone = self.editBones.new("IK_ElbowPole_R")
        IK_ElbowPole_R_Edit.head = R_elbow_Edit.head + Vector((0, 0.32, 0))
        IK_ElbowPole_R_Edit.tail = R_elbow_Edit.head + Vector((0, 0.36, 0))

        # Left Pole Target
        IK_ElbowPole_L_Edit: bpy.types.EditBone = self.editBones.new("IK_ElbowPole_L")
        IK_ElbowPole_L_Edit.head = L_elbow_Edit.head + Vector((0, 0.32, 0))
        IK_ElbowPole_L_Edit.tail = L_elbow_Edit.head + Vector((0, 0.36, 0))

        # Leg IK Stuff
        # Connect the knees to the ankles
        L_Knee_Edit.tail = L_Ankle_Edit.head
        R_Knee_Edit.tail = R_Ankle_Edit.head

        # Adding IK bones
        # Right IK Knee bones
        IK_Knee_R_Edit: bpy.types.EditBone = self.editBones.new("IK_Knee_R")
        IK_Knee_R_Edit.head = R_Ankle_Edit.head
        IK_Knee_R_Edit.tail = R_Ankle_Edit.tail
        IK_Knee_R_Edit.roll = -1.5707963705062866

        # Left IK Knee bones
        IK_Knee_L_Edit: bpy.types.EditBone = self.editBones.new("IK_Knee_L")
        IK_Knee_L_Edit.head = L_Ankle_Edit.head
        IK_Knee_L_Edit.tail = L_Ankle_Edit.tail
        IK_Knee_L_Edit.roll = -1.5707963705062866

        # Adding Pole Targets
        IK_Knee_Pole_R_Edit: bpy.types.EditBone = self.editBones.new("IK_Knee_Pole_R")
        IK_Knee_Pole_R_Edit.head = R_Knee_Edit.head + Vector((0, -0.4, 0))
        IK_Knee_Pole_R_Edit.tail = R_Knee_Edit.head + Vector((0, -0.43, 0))

        IK_Knee_Pole_L_Edit: bpy.types.EditBone = self.editBones.new("IK_Knee_Pole_L")
        IK_Knee_Pole_L_Edit.head = L_Knee_Edit.head + Vector((0, -0.4, 0))
        IK_Knee_Pole_L_Edit.tail = L_Knee_Edit.head + Vector((0, -0.43, 0))



        # connect all IK Bones to root
        IK_Arm_R_Edit.parent = Root
        IK_Arm_L_Edit.parent = Root
        IK_ElbowPole_R_Edit.parent = Root
        IK_ElbowPole_L_Edit.parent = Root
        IK_Knee_R_Edit.parent = Root
        IK_Knee_L_Edit.parent = Root
        IK_Knee_Pole_R_Edit.parent = Root
        IK_Knee_Pole_L_Edit.parent = Root



        bpy.ops.object.mode_set(mode='POSE')
        # Pose bones
        IK_Arm_R_Pose = self.getPoseBone("IK_Arm_R")
        IK_Arm_L_Pose = self.getPoseBone("IK_Arm_L")
        IK_ElbowPole_R_Pose = self.getPoseBone("IK_ElbowPole_R")
        IK_ElbowPole_L_Pose = self.getPoseBone("IK_ElbowPole_L")
        IK_Knee_R_Pose = self.getPoseBone("IK_Knee_R")
        IK_Knee_L_Pose = self.getPoseBone("IK_Knee_L")
        IK_Knee_Pole_R_Pose = self.getPoseBone("IK_Knee_Pole_R")
        IK_Knee_Pole_L_Pose = self.getPoseBone("IK_Knee_Pole_L")
        IK_Finger_R_Thumb_Pose = self.getPoseBone("IK_Finger_R_Thumb")
        IK_Finger_R_Index_Pose = self.getPoseBone("IK_Finger_R_Index")
        IK_Finger_R_Middle_Pose = self.getPoseBone("IK_Finger_R_Middle")
        IK_Finger_R_Ring_Pose = self.getPoseBone("IK_Finger_R_Ring")
        IK_Finger_R_Pinky_Pose = self.getPoseBone("IK_Finger_R_Pinky")
        IK_Finger_L_Thumb_Pose = self.getPoseBone("IK_Finger_L_Thumb")
        IK_Finger_L_Index_Pose = self.getPoseBone("IK_Finger_L_Index")
        IK_Finger_L_Middle_Pose = self.getPoseBone("IK_Finger_L_Middle")
        IK_Finger_L_Ring_Pose = self.getPoseBone("IK_Finger_L_Ring")
        IK_Finger_L_Pinky_Pose = self.getPoseBone("IK_Finger_L_Pinky")


        # Hand IK Stuff
        # Adding Ik constraints

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

        # Finger IK constraints
        # Right Finger IK constraints
        IK_Finger_R_Thumb_ik = R_thumbfinger_C_Pose.constraints.new('IK')
        IK_Finger_R_Thumb_ik.target = self.rig_object
        IK_Finger_R_Thumb_ik.subtarget = 'IK_Finger_R_Thumb'
        IK_Finger_R_Thumb_ik.chain_count = 3
        IK_Finger_R_Thumb_ik.iterations = 500
        IK_Finger_R_Thumb_ik.use_rotation = True

        IK_Finger_R_Index_ik = R_indexfinger_C_Pose.constraints.new('IK')
        IK_Finger_R_Index_ik.target = self.rig_object
        IK_Finger_R_Index_ik.subtarget = 'IK_Finger_R_Index'
        IK_Finger_R_Index_ik.chain_count = 3
        IK_Finger_R_Index_ik.iterations = 500
        IK_Finger_R_Index_ik.use_rotation = True
        
        IK_Finger_R_Middle_ik = R_middlefinger_C_Pose.constraints.new('IK')
        IK_Finger_R_Middle_ik.target = self.rig_object
        IK_Finger_R_Middle_ik.subtarget = 'IK_Finger_R_Middle'
        IK_Finger_R_Middle_ik.chain_count = 3
        IK_Finger_R_Middle_ik.iterations = 500
        IK_Finger_R_Middle_ik.use_rotation = True
        
        IK_Finger_R_Ring_ik = R_ringfinger_C_Pose.constraints.new('IK')
        IK_Finger_R_Ring_ik.target = self.rig_object
        IK_Finger_R_Ring_ik.subtarget = 'IK_Finger_R_Ring'
        IK_Finger_R_Ring_ik.chain_count = 3
        IK_Finger_R_Ring_ik.iterations = 500
        IK_Finger_R_Ring_ik.use_rotation = True

        IK_Finger_R_Pinky_ik = R_pinkyfinger_C_Pose.constraints.new('IK')
        IK_Finger_R_Pinky_ik.target = self.rig_object
        IK_Finger_R_Pinky_ik.subtarget = 'IK_Finger_R_Pinky'
        IK_Finger_R_Pinky_ik.chain_count = 3
        IK_Finger_R_Pinky_ik.iterations = 500
        IK_Finger_R_Pinky_ik.use_rotation = True
        
        # Left Finger IK constraints
        IK_Finger_L_Thumb_ik = L_thumbfinger_C_Pose.constraints.new('IK')
        IK_Finger_L_Thumb_ik.target = self.rig_object
        IK_Finger_L_Thumb_ik.subtarget = 'IK_Finger_L_Thumb'
        IK_Finger_L_Thumb_ik.chain_count = 3
        IK_Finger_L_Thumb_ik.iterations = 500
        IK_Finger_L_Thumb_ik.use_rotation = True

        IK_Finger_L_Index_ik = L_indexfinger_C_Pose.constraints.new('IK')
        IK_Finger_L_Index_ik.target = self.rig_object
        IK_Finger_L_Index_ik.subtarget = 'IK_Finger_L_Index'
        IK_Finger_L_Index_ik.chain_count = 3
        IK_Finger_L_Index_ik.iterations = 500
        IK_Finger_L_Index_ik.use_rotation = True
        
        IK_Finger_L_Middle_ik = L_middlefinger_C_Pose.constraints.new('IK')
        IK_Finger_L_Middle_ik.target = self.rig_object
        IK_Finger_L_Middle_ik.subtarget = 'IK_Finger_L_Middle'
        IK_Finger_L_Middle_ik.chain_count = 3
        IK_Finger_L_Middle_ik.iterations = 500
        IK_Finger_L_Middle_ik.use_rotation = True
        
        IK_Finger_L_Ring_ik = L_ringfinger_C_Pose.constraints.new('IK')
        IK_Finger_L_Ring_ik.target = self.rig_object
        IK_Finger_L_Ring_ik.subtarget = 'IK_Finger_L_Ring'
        IK_Finger_L_Ring_ik.chain_count = 3
        IK_Finger_L_Ring_ik.iterations = 500
        IK_Finger_L_Ring_ik.use_rotation = True

        IK_Finger_L_Pinky_ik = L_pinkyfinger_C_Pose.constraints.new('IK')
        IK_Finger_L_Pinky_ik.target = self.rig_object
        IK_Finger_L_Pinky_ik.subtarget = 'IK_Finger_L_Pinky'
        IK_Finger_L_Pinky_ik.chain_count = 3
        IK_Finger_L_Pinky_ik.iterations = 500
        IK_Finger_L_Pinky_ik.use_rotation = True

        






        # Copy rotation constraints

        copy_rotation_hand_R = R_Hand_Pose.constraints.new('COPY_ROTATION')
        copy_rotation_hand_R.target = self.rig_object
        copy_rotation_hand_R.subtarget = 'IK_Arm_R'

        copy_rotation_hand_L = L_Hand_Pose.constraints.new('COPY_ROTATION')
        copy_rotation_hand_L.target = self.rig_object
        copy_rotation_hand_L.subtarget = 'IK_Arm_L'

        # Leg IK Stuff
        # Adding IK constraints

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

        # Copy rotation constraints

        copy_rotation_L_ankle = L_Ankle_Pose.constraints.new('COPY_ROTATION')
        copy_rotation_L_ankle.target = self.rig_object
        copy_rotation_L_ankle.subtarget = 'IK_Knee_L'

        copy_rotation_R_ankle = R_Ankle_Pose.constraints.new('COPY_ROTATION')
        copy_rotation_R_ankle.target = self.rig_object
        copy_rotation_R_ankle.subtarget = 'IK_Knee_R'


        # Apply custom shapes to the IK bones
        # Hand IK Bones

        IK_Arm_R_Pose.custom_shape = bpy.data.objects.get('Hand_Controller')
        IK_Arm_R_Pose.custom_shape_scale_xyz = (0.5, 0.5, 0.5)
        IK_Arm_R_Pose.custom_shape_translation = (0, 0.12, 0)
        IK_Arm_R_Pose.custom_shape_rotation_euler = (0,1.5708,3.1416)

        IK_Arm_L_Pose.custom_shape = bpy.data.objects.get('Hand_Controller')
        IK_Arm_L_Pose.custom_shape_scale_xyz = (0.5, 0.5, 0.5)
        IK_Arm_L_Pose.custom_shape_translation = (0, 0.12, 0)
        IK_Arm_L_Pose.custom_shape_rotation_euler = (0,1.5708,3.1416)

        # Pole Targets
        IK_ElbowPole_R_Pose.custom_shape = bpy.data.objects.get('Pole')
        IK_ElbowPole_L_Pose.custom_shape = bpy.data.objects.get('Pole')
        IK_Knee_Pole_L_Pose.custom_shape = bpy.data.objects.get('Pole')
        IK_Knee_Pole_R_Pose.custom_shape = bpy.data.objects.get('Pole')

        # Leg IK Bones
        IK_Knee_R_Pose.custom_shape = bpy.data.objects.get('Spine')
        IK_Knee_R_Pose.custom_shape_scale_xyz = (0.3, 0.3, 0.3)
        IK_Knee_R_Pose.custom_shape_rotation_euler = (-0.5760,1.5708,0)

        # finger IK bones
        IK_Finger_R_Thumb_Pose.custom_shape = bpy.data.objects.get('Spine')
        IK_Finger_R_Thumb_Pose.custom_shape_scale_xyz = (0.3, 0.3, 0.3)
        IK_Finger_R_Thumb_Pose.custom_shape_rotation_euler = (-1.5708,0,0)

        IK_Finger_R_Index_Pose.custom_shape = bpy.data.objects.get('Spine')
        IK_Finger_R_Index_Pose.custom_shape_scale_xyz = (0.3, 0.3, 0.3)
        IK_Finger_R_Index_Pose.custom_shape_rotation_euler = (-1.5708,0,0)
        
        IK_Finger_R_Middle_Pose.custom_shape = bpy.data.objects.get('Spine')
        IK_Finger_R_Middle_Pose.custom_shape_scale_xyz = (0.3, 0.3, 0.3)
        IK_Finger_R_Middle_Pose.custom_shape_rotation_euler = (-1.5708,0,0)

        IK_Finger_R_Ring_Pose.custom_shape = bpy.data.objects.get('Spine')
        IK_Finger_R_Ring_Pose.custom_shape_scale_xyz = (0.3, 0.3, 0.3)
        IK_Finger_R_Ring_Pose.custom_shape_rotation_euler = (-1.5708,0,0)

        IK_Finger_R_Pinky_Pose.custom_shape = bpy.data.objects.get('Spine')
        IK_Finger_R_Pinky_Pose.custom_shape_scale_xyz = (0.3, 0.3, 0.3)
        IK_Finger_R_Pinky_Pose.custom_shape_rotation_euler = (-1.5708,0,0)

        IK_Finger_L_Thumb_Pose.custom_shape = bpy.data.objects.get('Spine')
        IK_Finger_L_Thumb_Pose.custom_shape_scale_xyz = (0.3, 0.3, 0.3)
        IK_Finger_L_Thumb_Pose.custom_shape_rotation_euler = (-1.5708,0,0)

        IK_Finger_L_Index_Pose.custom_shape = bpy.data.objects.get('Spine')
        IK_Finger_L_Index_Pose.custom_shape_scale_xyz = (0.3, 0.3, 0.3)
        IK_Finger_L_Index_Pose.custom_shape_rotation_euler = (-1.5708,0,0)

        IK_Finger_L_Middle_Pose.custom_shape = bpy.data.objects.get('Spine')
        IK_Finger_L_Middle_Pose.custom_shape_scale_xyz = (0.3, 0.3, 0.3)
        IK_Finger_L_Middle_Pose.custom_shape_rotation_euler = (-1.5708,0,0)

        IK_Finger_L_Ring_Pose.custom_shape = bpy.data.objects.get('Spine')
        IK_Finger_L_Ring_Pose.custom_shape_scale_xyz = (0.3, 0.3, 0.3)
        IK_Finger_L_Ring_Pose.custom_shape_rotation_euler = (-1.5708,0,0)

        IK_Finger_L_Pinky_Pose.custom_shape = bpy.data.objects.get('Spine')
        IK_Finger_L_Pinky_Pose.custom_shape_scale_xyz = (0.3, 0.3, 0.3)
        IK_Finger_L_Pinky_Pose.custom_shape_rotation_euler = (-1.5708,0,0)
        
        IK_Knee_L_Pose.custom_shape = bpy.data.objects.get('Spine')
        IK_Knee_L_Pose.custom_shape_scale_xyz = (0.3, 0.3, 0.3)
        IK_Knee_L_Pose.custom_shape_rotation_euler = (-0.5760,1.5708,0)



  






