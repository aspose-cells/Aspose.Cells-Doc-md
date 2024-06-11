---
title: 已知问题 - 对个人站点集的权限
type: docs
weight: 40
url: /zh/sharepoint/known-issue-permissions-to-personal-site-collections/
---

{{% alert color="primary" %}} 

默认情况下，SharePoint 不会授予门户管理员管理个人站点的完全权限。这就是在由门户管理员执行个人站点集的激活和停用时可能会失败的原因。这包括在安装期间执行激活和停用。

{{% /alert %}} 
### **授予个人站点的权限**
当此问题在安装期间发生时，SharePoint 跟踪日志将记录到 Microsoft.SharePoint.SPFeature.Activate() 的未经授权的访问异常。当停用作为卸载的一部分失败时，未经授权的访问异常将显示在未能停用的最后设置屏幕上。

为了防止此问题，需要授予门户管理员管理 MySite Web 应用程序的权限：

1. 转到 SharePoint 中央管理，选择 应用程序管理 标签。
1. 在 应用程序安全 组下选择 Web 应用程序的 策略。
1. 确保在右侧的 Web 应用程序列表中选择“我的网站”对应的正确 Web 应用程序。
1. 在左上角选择 添加用户。
1. 在 添加用户 屏幕上，默认选择 所有区域，然后点击 下一步。
1. 添加适当的用户或活动目录组，以便他们管理您的“我的网站”Web 应用程序。
1. 选择控制级别。 

   添加用户并设置控制级别 

![todo:image_alt_text](known-issue-permissions-to-personal-site-collections_1.png)




1. 点击**完成**。
