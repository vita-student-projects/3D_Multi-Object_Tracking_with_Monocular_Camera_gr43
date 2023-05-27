# Chooose MOUNT_PATH to be the place where the repo folder is
# That folder should also have the dataset according to the path at line 10
MOUNT_PATH = "C:/Users/wilhe/Documents/DLAV"  # in case you are mounting data storage externally
SPLIT = 'mini_val'

KITTI_WORK_DIR = MOUNT_PATH + "/storage/slurm/kimal/eagermot_workspace/kitti"
KITTI_DATA_DIR = MOUNT_PATH + "/storage/slurm/osep/datasets/kitti"

NUSCENES_WORK_DIR = MOUNT_PATH + "/DLAV_GuillaumeMOT/Workspaces/NuScenes"
NUSCENES_DATA_DIR = MOUNT_PATH + "/Datasets/NuScenes/Mini"

# -------------- Altered code ----------------------------------------------------------------
VISUAL_SIM_NAME = "TorchReID"
# -------------- End altered code ------------------------------------------------------------
