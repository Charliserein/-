# 虚拟数字人形象生成


我们使用了SMPLitex，这是一个3D人体外观的生成模型，可以从单个图像中估计3D人体纹理。SMPLitex利用最新的图像扩散融合模型进行2D图像合成，并使用像素到表面的对应估计来弥合2D图像和3D图像之间的差距。通过将扩散模型调整为单个视图中人类的可见像素，SMPLitex能够合成对象的完整纹理图。
 
![image](https://github.com/user-attachments/assets/3faf6087-9374-4a48-b765-71aa5fc750c9)

SMPLitex使用扩散模型作为生成主干。扩散模型是一种逐渐从图像中去除噪声来学习分布空间pθ的生成模型。在去噪过程的每一步中，扩散模型都会产生噪声εt，用于创建中间去噪图像xt。初始噪声xT对应于最终图像，而完全去噪的图像x0对应于起始图像。这种去噪过程通常建模为马尔可夫转移概率，如下所示


<p align="center">
  <img src="https://github.com/user-attachments/assets/5fda738a-0db5-4921-a07b-d1bb2b60c6bb" alt="image">
</p>

最后，我们使用Blender Python API 给模型贴上 UV 纹理贴图。

导入模块：import bpy 用于访问 Blender 的 API。

选择对象：通过 bpy.context.object 来获得当前选中的对象。

创建材质：bpy.data.materials.new(name="UV_Texture_Material") 来创建一个新材质。

使用节点系统：设置 material.use_nodes = True，然后通过节点系统添加 Diffuse BSDF 和 Image Texture 节点。

加载纹理图像：通过 bpy.data.images.load(image_path) 来加载 UV 纹理图片。将材质赋给对象：将材质赋予到当前对象上。


<p align="center">
  <img src="https://github.com/user-attachments/assets/80d7234e-36a7-4703-8e50-05c81b5ce711" alt="image">
</p>

视频演示

<video src="https://github.com/Charliserein/Virtual-3D-digital-human-image-generation/raw/main/媒体1.mp4" controls width="640" height="360">
  Your browser does not support the video tag.
</video>


