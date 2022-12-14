---
title: 许可
type: docs
weight: 21
url: /zh/python-net/licensing/
---
{{% alert color="primary" %}}

您可以通过 .Net 从其网站轻松下载 Aspose.Cells Python 的评估版[下载页面](https://pypi.org/project/aspose-cells-python/)@Pypi 回购。评估版提供与许可版组件完全相同的功能。此外，当您购买许可证并添加几行代码来应用该许可证时，评估版就会成为许可证。

{{% /alert %}}

## **评估版限制**

评估版 Aspose.Cells Python 通过 .Net 产品（未指定许可证）提供完整的产品功能，但仅限于在一个程序中打开 100 个文件和一个带有评估水印的额外工作表。

限制如下所示：

- **打开的文件数** （Aspose.Cells Python 通过.Net）
运行程序时，您只能通过 .Net 库使用 Aspose.Cells Python 打开 100 个 Excel 文件。如果您的应用程序超过此数量，将抛出异常。


此外，带有评估水印的工作表将始终在使用 Aspose.Cells Python 通过库生成的 excel 文件中显示为活动工作表。只有在授权版本中，您可以将活动工作表设置为其他工作表。在 Aspose.Cells Python via 输出的 PDF 或图像文件中，评估水印将粘贴在文档/图像的顶部。

{{% alert color="primary" %}}

如果你想测试 Aspose.Cells Python via 没有评估版本限制，你也可以请求一个[30 天临时许可证](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

## **通过组件在 Aspose.Cells Python 申请许可证**

该许可证是一个纯文本 XML 文件，其中包含产品名称、获得许可的开发人员数量、订阅到期日期等详细信息。该文件经过数字签名，因此请勿修改该文件。即使无意中在文件中添加额外的换行符也会使其无效。如果您想避免其评估限制，则需要在使用 Aspose.Cells Python via 之前设置许可证。每个应用程序（或进程）只需要设置一次许可证。许可证可以从文件中加载。

Aspose.Cells Python via 尝试在显式路径位置中查找许可证。

从文件应用许可证有两种常用方法。

### **从磁盘应用许可证**

设置许可证最简单的方法是将许可证文件放在显式路径中。

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

license = License();
 //For Windows
license.set_license("D:\Aspose.Cells.lic");
 //For Linux or MacOS
license.set_license("/home/yourusername/Aspose.Cells.lic"); 
{{< /highlight >}}

{{% alert color="primary" %}}

当您呼叫话机时_license 方法，license 名称应与您的license 文件名相同。例如，您可以将许可证文件名更改为**Aspose.Cells.lic.xml**。然后在您的代码中，您应该使用修改后的许可证名称 (**Aspose.Cells.lic.xml**)_许可方式。

{{% /alert %}}


