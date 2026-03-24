'''
import struct

def read_next_bytes(fid, num_bytes, format_char_sequence):
    data = fid.read(num_bytes)
    return struct.unpack(format_char_sequence, data)

def read_cameras_binary(path):
    cameras = {}
    with open(path, "rb") as fid:
        num_cameras = read_next_bytes(fid, 8, "Q")[0]
        for _ in range(num_cameras):
            cam_id, model_id, width, height = read_next_bytes(
                fid, 4 + 4 + 8 + 8, "iiQQ"
            )

            from collections import namedtuple
            CameraModel = namedtuple("CameraModel", ["model_name", "num_params"])
            CAMERA_MODEL_IDS = {
                0: CameraModel("SIMPLE_PINHOLE", 3),
                1: CameraModel("PINHOLE", 4),
                2: CameraModel("SIMPLE_RADIAL", 4),
                3: CameraModel("RADIAL", 5),
                4: CameraModel("OPENCV", 8),
            }

            model = CAMERA_MODEL_IDS[model_id]
            params = read_next_bytes(
                fid, 8 * model.num_params, "d" * model.num_params
            )

            cameras[cam_id] = {
                "model": model.model_name,
                "width": width,
                "height": height,
                "params": params
            }
    return cameras

cams = read_cameras_binary("cameras.bin")
for k, v in cams.items():
    print(k, v)
'''



import subprocess

result = subprocess.run(
    [r".\bin\MVS\DensifyPointCloud.exe",
            #"-w", r"result\dense",
            "-i", r"result\sparse\res.mvs",
            "-o", r"result\dense\dense_pointcloud"
     ],
    capture_output=True,
    text=True
)

print(result.stdout)