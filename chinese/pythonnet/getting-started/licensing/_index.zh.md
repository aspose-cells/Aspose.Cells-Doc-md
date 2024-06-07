---
title: 许可
type: docs
weight: 21
url: /zh/python-net/licensing/
---

{{% alert color="primary" %}}

您可以从[下载页面](https://pypi.org/project/aspose-cells-python/)@ Pypi repos轻松下载Aspose.Cells Python通过.Net的评估版本。评估版本提供的功能与组件的许可版本绝对相同。此外，评估版本在购买许可证并添加几行代码以应用许可证后就会变成许可版本。

{{% /alert %}}

## **评估版本限制**

Aspose.Cells Python通过.Net产品的评估版本（未指定许可证）提供完整的产品功能，但在一个程序中限制为打开100个文件，额外的工作表带有评估水印。

以下是限制内容:

- **打开文件数量**（Aspose.Cells Python通过.Net）
  在运行程序时，您只能使用Aspose.Cells Python通过.Net库打开100个Excel文件。如果您的应用程序超过此数量，就会抛出异常。


此外，在使用Aspose.Cells Python通过库生成的Excel文件中，始终会显示带有评估水印的工作表作为活动工作表。只有在许可版本中，您才能将活动工作表设置为其他工作表。在Aspose.Cells Python通过输出的PDF或图像文件中，评估水印会粘贴在文件/图片顶部。

{{% alert color="primary" %}}

如果您想要测试Aspose.Cells Python通过的无评估版本限制，您也可以请求[30天临时许可证](https://purchase.aspose.com/temporary-license)。

{{% /alert %}}

## **在Aspose.Cells Python组件中应用许可证**

许可证是一个包含产品名称、被许可人数、订阅到期日期等详细信息的纯文本XML文件。该文件是数字签名的，所以不要修改该文件。即使无意中在文件中添加额外的换行符也会使其失效。如果您希望避免其评估限制，您需要在使用Aspose.Cells Python之前设置许可证。每个应用程序（或进程）只需设置一次许可证。许可证可从文件加载。

Aspose.Cells Python通过尝试在显式路径位置找到许可证。

从文件应用许可证的两种常见方法

### **从磁盘应用许可证**

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

当调用set_license方法时，许可证名称应与许可证文件名相同。例如，您可以将许可证文件名更改为**Aspose.Cells.lic.xml**。然后在您的代码中，您应该将修改后的许可证名称（**Aspose.Cells.lic.xml**）用于set_license方法。

{{% /alert %}}


