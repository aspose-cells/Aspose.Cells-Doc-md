---
title: 许可
type: docs
weight: 50
url: /zh/python-java/licensing/
---
{{% alert color="primary" %}} 

您可以安装评估版**Aspose.Cells**for Python via Java 和 `pip install aspose-cells`。评估版提供与产品许可版完全相同的功能。此外，当您购买许可证并添加几行代码来应用该许可证时，评估版就会成为许可证。

一旦您对您的评价感到满意**Aspose.Cells**， 你可以[购买许可证](https://purchase.aspose.com)在 Aspose 网站上。让自己熟悉所提供的不同订阅类型。如有任何疑问，请随时联系 Aspose 销售团队。

每个 Aspose 许可证都包含一年订阅，可以免费升级到在此期间发布的任何新版本或修复程序。技术支持是免费和无限制的，同时提供给许可用户和评估用户。

{{% /alert %}} {{% alert color="primary" %}} 

如果你想测试**Aspose.Cells**没有评估版本限制，请求 30 天的临时许可证。请参阅[如何获得临时许可证？](https://purchase.aspose.com/temporary-license)了解更多信息。

{{% /alert %}}

## **评估版限制**

评估版**Aspose.Cells**产品（未指定许可证）提供完整的产品功能，但仅限于在一个程序中打开 100 个文件和一个带有评估水印的额外工作表。

限制如下所示：

### **第一个限制：打开文件的数量**

运行程序时，您只能打开 100 个 Excel 文件。如果您的应用程序超过此数量，将抛出异常。

### **第二个限制：带有评估水印的工作表**

![待办事项：图像_替代_文本](licensing_1.png)

此工作表将始终显示为活动工作表。只有在授权版本中，您可以将活动工作表设置为其他工作表。

## **设置许可证**

该许可证是一个纯文本 XML 文件，其中包含产品名称、获得许可的开发人员数量、订阅到期日期等详细信息。该文件经过数字签名，因此请勿修改该文件；即使无意中在文件中添加了额外的换行符也会使其无效。

如果您想避免其评估限制，则需要在使用 Aspose.Cells 之前设置许可证。您只需为每个应用程序或进程设置一次许可证。

可以从以下位置的文件加载许可证：

1. 显式路径。
1. 工作文件夹。

使用[许可证.setLicense](https://reference.aspose.com/cells/python-java/asposecells.api/License)许可组件的方法。设置许可证最简单的方法通常是将许可证文件放在与 Aspose.Cells.jar 相同的文件夹中，并仅指定不带路径的文件名，如下例所示：

### **例子**

在这个例子中**Aspose.Cells**将尝试在您的工作文件夹中查找许可证文件。

{{< highlight "python" >}}

from asposecells.api import License

lic = License()
lic.setLicense("Aspose.Cells.lic")

{{< /highlight >}}
