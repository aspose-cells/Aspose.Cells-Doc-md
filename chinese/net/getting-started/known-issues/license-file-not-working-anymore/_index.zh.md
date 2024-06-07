---
title: 许可文件不再起作用
type: docs
weight: 60
url: /zh/net/license-file-not-working-anymore/
---

## **症状**

有时，用户因许可文件在将 Web 项目移动/发布到新服务器时不再起作用而感到沮丧。他们感到沮丧的原因是，他们的许可文件在之前（旧）服务器上正常工作，但现在在新服务器环境中生成报告时会在工作表上得到额外的 **Evaluation Copyright Warning** 水印。

### **一个场景**

"在我们的ASP.NET网站项目中，我们一直在使用Aspose.Cells生成/操作Excel报告，我们有一个有效的许可证在使用。几天前，我们将网站迁移到了新服务器；没有进行任何升级或更改，我们确保简单地将每个文件移动到了新服务器上，包括Aspose.Cells.dll和相关的lic文件。现在在新的服务器环境中尝试生成Excel报告时，我们在报告上看到一个**Evaluation Copyright Warning**水印工作表。我们尝试从网站的订单部分下载并安装一个新的许可证文件，但这并没有解决问题。值得一提的是，我们通过将Aspose.Cells.lic文件放在网站的bin文件夹中与Aspose.Cells.dll组件文件一起实施许可证，就像我提到的那样，在旧服务器上没有任何问题。"

### **解决方案**

Aspose具有清洁可靠的许可机制。一般情况下，问题应与部署问题有关。如果一个许可文件在一个服务器上正常工作，那么它也应该在其他服务器/环境上正常工作。通常用户在global.asax文件中利用Application_Start或Session_Start事件等来放置许可代码。因此，很可能应用程序启动/Session_Start事件并未触发处理位于新位置的许可代码。需要注意的是，如果组件无法在路径中找到许可文件，Aspose.Cells将始终引发异常。用户应确保无论他们将许可代码放在哪里，都应该处理许可代码，并且应该触发事件，在这些事件中放置了许可代码。用户可以重新启动相关服务，即“World Wide Web Publishing”，并尝试跟踪他们在新服务器环境中访问其项目时是否触发了Application_Start / Session_Start事件。

### **确认**

请确保...

- 您在项目中使用了有效的许可证文件。
- 您或其他人不应编辑/修改许可文件，否则许可文件将无效。
- 您应该注意您的许可订阅到期日期（您只需将lic文件打开到记事本中并检查到期日期即可）。
- 您不要使用许可订阅到期后发布的版本（Aspose.Cells.dll）。这里需要注意的是，许可文件永远不会过期，但如果您使用了许可订阅到期后发布的组件版本，每当创建Excel文件时，您都会获得额外的**Evaluation Copyright Warning**水印工作表。

### **参考**

<https://forum.aspose.com/t/license-file-not-working-on-new-server/83110>

<https://forum.aspose.com/t/license-not-being-detected/83516/4>
