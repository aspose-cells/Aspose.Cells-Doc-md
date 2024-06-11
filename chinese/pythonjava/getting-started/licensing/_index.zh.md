---
title: 许可证
type: docs
weight: 50
url: /zh/python-java/licensing/
---

{{% alert color="primary" %}} 

您可以使用`pip install aspose-cells`安装Python via Java的**Aspose.Cells**的评估版本。评估版本提供的功能与产品许可版本完全一致。此外，评估版本在购买许可证并添加几行代码以应用许可证后，会变为许可版本。

一旦您满意**Aspose.Cells**的评估，您可以在Aspose网站上[购买许可证](https://purchase.aspose.com)。请熟悉提供的不同订阅类型。如果您有任何疑问，请随时联系Aspose销售团队。

每个Aspose许可证都包含一年的免费升级订阅，可以在此期间免费升级到任何新版本或修复版本。技术支持是免费且无限的，并提供给有许可证和评估用户。

{{% /alert %}} {{% alert color="primary" %}} 

如果您想在没有评估版本限制的情况下测试**Aspose.Cells**，请申请一个30天临时许可证。请参考[如何获取临时许可证？](https://purchase.aspose.com/temporary-license)获取更多信息。

{{% /alert %}}

## **评估版本限制**

**Aspose.Cells**产品的评估版本（未指定许可证）提供完整的产品功能，但在一个程序中限制了打开 100 个文件和带有评估水印的额外工作表。

限制如下所示：

### **第一限制: 打开文件数量**

运行程序时，您只能打开100个Excel文件。如果您的应用程序超过此数量，将会引发异常。

### **第二限制:评估水印工作表**

![todo:image_alt_text](licensing_1.png)

该工作表将始终显示为活动工作表。只有在授权版本中，您才能将活动工作表设置为其他工作表。

## **设置许可证**

许可证是一个包含产品名称、许可给多少开发人员、订阅到期日期等详细信息的纯文本XML文件。该文件经过数字签名，因此不要修改文件; 即使在文件中无意添加额外的换行符也会使其失效。

如果要避免其评估限制，您需要在使用 Aspose.Cells 之前设置许可证。每个应用程序或进程只需要设置一次许可证。

许可证可以从以下位置加载:

1. 明确的路径。
1. 工作文件夹。

使用[License.setLicense](https://reference.aspose.com/cells/python-java/asposecells.api/License)方法许可组件。设置许可证的最简单方法通常是将许可证文件放在与 Aspose.Cells.jar 相同的文件夹中，并只指定文件名而不包括路径，如下例所示:

### **示例**

在此示例中，**Aspose.Cells** 将尝试在您的工作文件夹中找到许可证文件。

{{< highlight python >}}

from asposecells.api import License

lic = License()
lic.setLicense("Aspose.Cells.lic")

{{< /highlight >}}
