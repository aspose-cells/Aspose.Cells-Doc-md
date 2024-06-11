---
title: 许可证
type: docs
weight: 21
url: /zh/python-net/licensing/
---

{{% alert color="primary" %}}

您可以通过[下载页面](https://pypi.org/project/aspose-cells-python/) @ Pypi repos轻松获取Aspose.Cells Python的评估版本，该版本通过.Net。评估版提供与组件的授权版本完全相同的功能。此外，仅需购买许可证并添加几行代码即可将评估版本简单地变成许可版本。

{{% /alert %}}

## **评估版本限制**

Aspose.Cells Python via .Net产品的评估版本(未指定许可)提供完整的产品功能，但在一个程序中受制于只能打开100个文件以及额外工作表带有评估水印。

限制如下所示：

- **打开的文件数量** (Aspose.Cells Python via .Net)
  运行程序时，您只能使用Aspose.Cells Python via .Net库打开100个Excel文件。如果应用程序的文件数量超过这个限制，将会抛出异常。


此外，在使用Aspose.Cells Python via库生成的Excel文件中，始终会显示具有评估水印的工作表作为活动工作表。只有在授权版本中，才能将活动工作表设置为其他工作表。通过Aspose.Cells Python via生成的PDF或图像文件中，将在文档/图像顶部粘贴评估水印。

{{% alert color="primary" %}}

如果您想测试Aspose.Cells Python via而没有评估版限制，还可以申请[30天临时许可证](https://purchase.aspose.com/temporary-license)。

{{% /alert %}}

## **在Aspose.Cells Python via组件中应用许可证**

许可证是一个包含产品名称、许可的开发人员数量、订阅到期日期等详细信息的纯文本XML文件。该文件经过数字签名，不要修改该文件。即使是不经意地在文件中添加一个额外的换行符也会使其无效。如果要避免其评估限制，需要在使用Aspose.Cells Python via之前设置许可证。每个应用程序（或进程）只需设置一次许可证。许可证可以从文件加载。

Aspose.Cells Python via会尝试在显式路径位置中查找许可证。

有两种常见的方法可以从文件中应用许可证。

### **从磁盘中应用许可证**

设置许可证的最简单方法是将许可证文件放在显式路径中。

{{< highlight csharp >}}

# Instantiate an instance of license and set the license file through its path

license = License();
# For Windows
license.set_license("D:\Aspose.Cells.lic");
# For Linux or MacOS
license.set_license("/home/yourusername/Aspose.Cells.lic"); 
{{< /highlight >}}

{{% alert color="primary" %}}

当调用set_license方法时，许可证名称应与许可证文件名相同。例如，您可以将许可证文件名更改为**Aspose.Cells.lic.xml**。然后在您的代码中，应将修改后的许可证名称(**Aspose.Cells.lic.xml**)用于set_license方法。

{{% /alert %}}


