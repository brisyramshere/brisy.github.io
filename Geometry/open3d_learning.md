# open3d

## 点云配准

### global registration

全局配准方法可以依赖点云的初始摆位估计。

流程：
1. FPFH特征提取：o3d.pipelines.registration.compute_fpfh_feature()
2. 2.registration_ransac_based_on_feature_matching