---
title: 许可
type: docs
weight: 50
url: /zh/python-java/licensing/
---

{{% alert color="primary" %}} 

您可以通过`pip install aspose-cells`安装Python via Java的Aspose.Cells的评估版本。评估版本提供的功能与产品许可版本完全相同。此外，评估版本在购买许可并添加几行代码应用许可后，简单地变为许可版本。

一旦您满意使用 **Aspose.Cells** 的评估版本，您可以在 Aspose 网站上购买许可证。请熟悉所提供的不同订阅类型。如果有任何疑问，请随时联系 Aspose 销售团队。

每个Aspose许可证都享有一年的订阅权，可免费升级到此期间推出的任何新版本或修复版。技术支持是免费且无限的，向持有许可证的用户和评估用户提供支持。

{{% /alert %}} {{% alert color="primary" %}} 

如果您想测试 **Aspose.Cells** 而没有评估版的限制，请申请一个为期30天的临时许可证。有关更多信息，请参阅[如何获取临时许可证？](https://purchase.aspose.com/temporary-license)

{{% /alert %}}

## **评估版本限制**

 **Aspose.Cells** 产品的评估版本（未指定许可证）提供完整的产品功能，但仅限于在一个程序中打开100个文件和一个带有评估水印的额外工作表。

以下是限制内容:

### **第一个限制: 打开文件数**

运行程序时，您只能打开100个Excel文件。如果您的应用程序超过此数字，将抛出异常。

### **第二个限制: 带有评估水印的工作表**

![todo:image_alt_text](licensing_1.png)

此工作表将始终显示为活动工作表。仅在许可版本中，您可以将活动工作表设置为其他工作表。

## **设置许可证**

许可证是包含产品名称、许可给开发人员数量、订阅到期日期等详细信息的纯文本XML文件。该文件经过数字签名，因此请勿修改文件; 即使意外添加额外的换行符到文件中也会使其无效。

如果要避免其评估限制，则需要在使用Aspose.Cells之前设置许可证。每个应用程序或进程只需要设置许可证一次。

许可证可以从以下位置的文件中加载:

1. 明确的路径。
1. 工作文件夹。

使用 [License.setLicense](https://reference.aspose.com/cells/python-java/asposecells.api/License) 方法给组件授权。设置许可证的最简单方式通常是将许可证文件与 Aspose.Cells.jar 文件放在同一文件夹中，并仅指定文件名而不包括路径，如下例所示:

### **例子**

在此示例中，**Aspose.Cells** 将尝试在您的工作文件夹中找到许可证文件。

{{< highlight python >}}

from asposecells.api import License

lic = License()
lic.setLicense("Aspose.Cells.lic")

{{< /highlight >}}
