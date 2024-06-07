---
title: 评估版本限制
type: docs
weight: 110
url: /zh/net/evaluation-version-limitations/
description: Aspose.Cells for .NET提供不同的购买计划或提供免费试用和提供30天临时许可证，以便在C#中使用许可证和订阅政策进行评估。
keywords: 评估版本限制，评估版本中打开的文件数量，评估版水印使用评估版本。
---

## **如何获取Aspose.Cells的评估版本**

您可以从[Maven存储库](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells)下载 **Aspose.Cells** for NET 的评估版本。评估版本提供的功能与产品的许可版本完全相同。此外，只需购买许可并添加几行代码即可将评估版本转为许可版本。

一旦您满意使用 **Aspose.Cells** 的评估版本，您可以在 Aspose 网站上购买许可证。请熟悉所提供的不同订阅类型。如果有任何疑问，请随时联系 Aspose 销售团队。

每个Aspose许可证都享有一年的订阅权，可免费升级到此期间推出的任何新版本或修复版。技术支持是免费且无限的，向持有许可证的用户和评估用户提供支持。

## **如何测试 Aspose.Cells 没有评估版本的限制**

如果您想测试 **Aspose.Cells** 而没有评估版的限制，请申请一个为期30天的临时许可证。有关更多信息，请参阅[如何获取临时许可证？](https://purchase.aspose.com/temporary-license)


## **评估版本限制**

 **Aspose.Cells** 产品的评估版本（未指定许可证）提供完整的产品功能，但仅限于在一个程序中打开100个文件和一个带有评估水印的额外工作表。

以下是限制内容:

### **第一个限制: 打开文件数**

运行程序时，您只能打开100个Excel文件。如果您的应用程序超过此数字，将抛出异常。

### **第二个限制: 带有评估水印的工作表**
此工作表将始终显示为活动工作表。仅在许可版本中，您可以将活动工作表设置为其他工作表。
<br>
<image src="1.png" width="70%" />
<br>

### **第三个限制: 带有评估信息的纯文本**
Aspose.Cells 导出的纯文本文件末尾会注入评估信息。
<br>
<image src="2.png" width="70%" />
<br>

### **第四个限制: PDF和带评估水印的图像**
Aspose.Cells 导出的PDF或图像文件顶部会添加评估水印。您无法隐藏GridWeb控件中的评估版警告（额外工作表），它将始终会被添加到控件中（在工作表选项卡的末尾）。您也无法通过在 web.config 文件中添加以下代码重新指定脚本路径。acw_client是一个包含文件的文件夹，Aspose.Cells.GridWeb使用此文件夹来管理其内部配置，其中包含脚本文件，图像文件和其他文件来指定GridWeb的行为和设置其他操作。配置文件用于防止控制使用内嵌的客户资源（图片，脚本等），这在某些情况/场景中非常有用。此外，在许可版本的控件中，web.config 文件中的这些配置设置才会生效。
<br>
<image src="3.png" width="70%" />
<br>

### **第5个限制：配置文件设置（Aspose.Cells.GridWeb）**
您不能通过向配置部分（例如在 web.config 文件中）添加以下代码行来重新指定脚本路径。 acw_client 是一个包含文件的文件夹，Aspose.Cells.GridWeb 使用此文件夹来管理其内部配置，其中包含脚本文件、图像文件和其他文件以指定 GridWeb 的行为和设置其他操作。配置文件用于防止控件使用嵌入式客户端资源（图像、脚本等），在某些情况/场景下很有用。此外，web.config 文件中的这些配置设置将仅对已许可版本的控件生效。

**XML**
{{< highlight csharp >}}
<appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

如果您在文件系统网站或 MS Ajax 扩展等情况下使用 Aspose.Cells.GridWeb 控件，则这些设置可能是必要的。

{{% /alert %}}
