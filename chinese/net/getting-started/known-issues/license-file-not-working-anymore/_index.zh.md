---
title: 许可文件不再起作用
type: docs
weight: 60
url: /zh/net/license-file-not-working-anymore/
---

## **症状**

有时，用户因为在将其Web项目发布到新服务器时，许可文件不再起作用而感到沮丧。他们因为他们的许可文件在以前（旧）服务器上正常工作，但是现在在新服务器上在生成报告时会出现额外的 **评估版版权警告** 水印工作表而感到沮丧。

### **场景**

"我们一直在我们的ASP.NET Web项目中使用Aspose.Cells来生成/操作Excel报告，我们得到了一个我们在使用的有效许可证。几天前，我们将网站迁移到新服务器；没有升级或任何改变，我们已经确保简单地将每个文件都移动到新服务器上，包括Aspose.Cells.dll和相关的.lic文件。现在，在新服务器环境中尝试生成Excel报告时，会在我们的报告上出现 **评估版版权警告** 水印工作表。我们尝试从网站的“我的订单”部分下载并安装新的许可证文件，但这完全没有解决问题。值得一提的是，我们通过将Aspose.Cells.lic文件放在站点的bin文件夹中与Aspose.Cells.dll组件文件一起来实施许可证，正如我已经提到的，在旧服务器上可以完全正常工作。"

### **解决方案**

Aspose拥有清洁可靠的许可机制。通常，问题应该与部署问题有关。如果一个许可文件在一个服务器上运行良好，它应该在其他服务器/环境中同样运行良好。通常用户在global.asax文件中利用Application_Start或Session_Start事件等。来放置许可证代码。因此，可能是Application_Start / Session_Start事件在新位置上不会触发以处理许可证代码。值得注意的是，如果组件在路径中找不到许可文件，Aspose.Cells将始终引发异常。用户应确保无论他们放置在哪里的许可证代码都应该被处理，并且应触发事件以在其中放置许可证代码。用户可以重新启动相关服务，即“World Wide Web Publishing”，并尝试跟踪在它们在新服务器环境中访问项目时是否触发Application_Start/Session_Start事件。

### **确认**

也请确保...

- 您在项目中使用有效的许可证文件。
- 您或其他人不应编辑/修改许可文件，否则许可文件将无法运行。
- 您应该了解您的许可订阅到期时间（您可以简单地在记事本中打开lic文件并检查到期日期）。
- 您不应使用许可订阅到期后发布的版本（Aspose.Cells.dll）。值得注意的是，许可文件永远不会过期，但如果您使用的组件版本是在您订阅到期后发布的，每当您创建excel文件时都会得到额外的 **评估版版权警告** 水印工作表。

### **参考资料**

<https://forum.aspose.com/t/license-file-not-working-on-new-server/83110>

<https://forum.aspose.com/t/license-not-being-detected/83516/4>
{{< app/cells/assistant language="csharp" >}}
