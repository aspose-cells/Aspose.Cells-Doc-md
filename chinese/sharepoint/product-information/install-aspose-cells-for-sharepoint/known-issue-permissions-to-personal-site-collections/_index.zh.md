---
title: 已知问题 - 对个人站点集的权限
type: docs
weight: 40
url: /zh/sharepoint/known-issue-permissions-to-personal-site-collections/
---

{{% alert color="primary" %}} 

SharePoint默认不会向门户管理员授予完整权限来管理个人站点。这就是为什么当由门户管理员执行个人站点集合的激活和停用时可能会失败。这包括在设置期间的激活和停用。

{{% /alert %}} 
### **授予个人站点权限**
如果在安装期间发生此问题，则会在SharePoint跟踪日志中记录Microsoft.SharePoint.SPFeature.Activate()中的UnauthorizedAccessException。当作为卸载的一部分停用失败时，将在停用失败的最后设置屏幕上显示UnauthorizedAccessException。

为避免此问题，授予门户管理员管理MySite Web应用程序的权限：

1. 转到 **SharePoint中央管理** 并选择 **应用程序管理** 选项卡。
1. 在 **应用程序安全性** 组下选择 **Web应用程序策略**。
1. 确保您在右侧的 **Web应用程序** 列表中选择正确的Web应用程序以供“我的网站”使用。
1. 在左上角选择 **添加用户**。
1. 在 **添加用户** 屏幕上默认选择 **所有区域** 并单击 **下一步**。
1. 添加适当的用户或希望控制您的“我的站点”Web应用程序的活动目录组。
1. 选择控制级别。 

   **添加用户和设置控制级别** 

![todo:image_alt_text](known-issue-permissions-to-personal-site-collections_1.png)




1. 单击 **完成**。
