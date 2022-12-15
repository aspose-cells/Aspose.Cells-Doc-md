---
title: 已知问题 - 个人网站集的权限
type: docs
weight: 40
url: /zh/sharepoint/known-issue-permissions-to-personal-site-collections/
---
{{% alert color="primary" %}} 

默认情况下，SharePoint 不会向门户管理员授予管理个人网站的完全权限。这就是门户管理员执行个人网站集的激活和停用可能会失败的原因。这包括安装期间的激活和停用。

{{% /alert %}} 
### **授予对个人网站的许可**
安装期间出现此问题时，Microsoft.SharePoint.SPFeature.Activate() 处的 UnauthorizedAccessException 将记录到 SharePoint 跟踪日志中。当作为卸载的一部分停用失败时，UnauthorizedAccessException 将显示在上次设置屏幕上以显示停用失败。

为防止出现此问题，请授予门户管理员管理 MySite Web 应用程序的权限：

1. 去**SharePoint 中央管理**并选择**申请管理**标签。
1. 选择**网络应用政策**在下面**应用安全**团体。
1. 确保您在“我的网站”中选择了正确的 Web 应用程序**Web应用程序**列表在右边。
1. 选择**添加用户**在左上角。
1. 选择**所有区域**默认情况下**添加用户**屏幕并点击**下一个**.
1. 添加您希望控制“我的网站”Web 应用程序的适当用户或活动目录组。
1. 选择控制级别。

   **添加用户和设置控制级别** 

![待办事项：图像_替代_文本](known-issue-permissions-to-personal-site-collections_1.png)




1. 点击**结束**.
