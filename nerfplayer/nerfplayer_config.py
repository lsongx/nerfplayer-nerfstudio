"""
NeRFPlayer config.
"""


from nerfstudio.cameras.camera_optimizers import CameraOptimizerConfig
from nerfstudio.configs.base_config import ViewerConfig
from nerfstudio.data.datamanagers.base_datamanager import (
    VanillaDataManager,
    VanillaDataManagerConfig,
)
from nerfstudio.data.dataparsers.dycheck_dataparser import DycheckDataParserConfig
from nerfstudio.data.datasets.depth_dataset import DepthDataset
from nerfstudio.engine.optimizers import AdamOptimizerConfig
from nerfstudio.engine.trainer import TrainerConfig
from nerfstudio.engine.schedulers import ExponentialDecaySchedulerConfig
from nerfstudio.pipelines.base_pipeline import VanillaPipelineConfig
from nerfstudio.pipelines.dynamic_batch import DynamicBatchPipelineConfig
from nerfstudio.plugins.types import MethodSpecification

from nerfplayer.nerfplayer_nerfacto import NerfplayerNerfactoModelConfig
from nerfplayer.nerfplayer_ngp import NerfplayerNGPModelConfig


nerfplayer_nerfacto = MethodSpecification(
    config=TrainerConfig(
        method_name="nerfplayer-nerfacto",
        steps_per_eval_batch=500,
        steps_per_save=2000,
        max_num_iterations=30000,
        mixed_precision=True,
        pipeline=VanillaPipelineConfig(
            datamanager=VanillaDataManagerConfig(
                _target=VanillaDataManager[DepthDataset],
                dataparser=DycheckDataParserConfig(),
                train_num_rays_per_batch=4096,
                eval_num_rays_per_batch=4096,
            ),
            model=NerfplayerNerfactoModelConfig(
                eval_num_rays_per_chunk=1 << 15,
                camera_optimizer=CameraOptimizerConfig(mode="SO3xR3"),
            ),
        ),
        optimizers={
            "proposal_networks": {
                "optimizer": AdamOptimizerConfig(lr=1e-2, eps=1e-15),
                "scheduler": ExponentialDecaySchedulerConfig(lr_final=0.0001, max_steps=200000),
            },
            "fields": {
                "optimizer": AdamOptimizerConfig(lr=1e-2, eps=1e-15),
                "scheduler": ExponentialDecaySchedulerConfig(lr_final=0.0001, max_steps=200000),
            },
            "camera_opt": {
                "optimizer": AdamOptimizerConfig(lr=1e-3, eps=1e-15),
                "scheduler": ExponentialDecaySchedulerConfig(lr_final=1e-4, max_steps=5000),
            },
        },
        viewer=ViewerConfig(num_rays_per_chunk=1 << 15),
        vis="viewer",
    ),
    description="NeRFPlayer with nerfacto backbone.",
)

nerfplayer_ngp = MethodSpecification(
    config=TrainerConfig(
        method_name="nerfplayer-ngp",
        steps_per_eval_batch=500,
        steps_per_save=2000,
        max_num_iterations=30000,
        mixed_precision=True,
        pipeline=DynamicBatchPipelineConfig(
            datamanager=VanillaDataManagerConfig(
                _target=VanillaDataManager[DepthDataset],
                dataparser=DycheckDataParserConfig(),
                train_num_rays_per_batch=8192,
            ),
            model=NerfplayerNGPModelConfig(
                eval_num_rays_per_chunk=8192,
                grid_levels=1,
                alpha_thre=0.0,
                render_step_size=0.001,
                disable_scene_contraction=True,
                near_plane=0.01,
            ),
        ),
        optimizers={
            "fields": {
                "optimizer": AdamOptimizerConfig(lr=1e-2, eps=1e-15),
                "scheduler": ExponentialDecaySchedulerConfig(lr_final=0.0001, max_steps=200000),
            }
        },
        viewer=ViewerConfig(num_rays_per_chunk=64000),
        vis="viewer",
    ),
    description="NeRFPlayer with InstantNGP backbone.",
)
