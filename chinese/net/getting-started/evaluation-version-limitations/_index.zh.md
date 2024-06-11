---
title: 评估版限制
type: docs
weight: 110
url: /zh/net/evaluation-version-limitations/
description: Aspose.Cells for .NET 提供不同的购买计划或提供免费试用和为评估使用 C# 中的许可和订阅政策提供 30 天临时许可。
keywords: 评估版限制，评估版中打开的文件数，使用评估版的评估水印。
---

## **如何获取Aspose.Cells的评估版**

您可以从[其下载页面](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) @ Maven repos下载Aspose.Cells for NET的评估版。评估版提供的功能与产品的许可版完全相同。此外，评估版在您购买许可并添加几行代码应用许可证后，就会简单地变为许可版。

一旦您满意**Aspose.Cells**的评估，您可以在Aspose网站上[购买许可证](https://purchase.aspose.com)。请熟悉提供的不同订阅类型。如果您有任何疑问，请随时联系Aspose销售团队。

每个Aspose许可证都包含一年的免费升级订阅，可以在此期间免费升级到任何新版本或修复版本。技术支持是免费且无限的，并提供给有许可证和评估用户。

## **如何在没有评估版限制的情况下测试Aspose.Cells**

如果您想在没有评估版本限制的情况下测试**Aspose.Cells**，请申请一个30天临时许可证。请参考[如何获取临时许可证？](https://purchase.aspose.com/temporary-license)获取更多信息。


## **评估版本限制**

**Aspose.Cells**产品的评估版本（未指定许可证）提供完整的产品功能，但在一个程序中限制了打开 100 个文件和带有评估水印的额外工作表。

限制如下所示：

### **第一限制: 打开文件数量**

运行程序时，您只能打开100个Excel文件。如果您的应用程序超过此数量，将会引发异常。

### **第二限制:评估水印工作表**
该工作表将始终显示为活动工作表。只有在授权版本中，您才能将活动工作表设置为其他工作表。
<br>
<image src="1.png" width="70%" />
<br>

### **第三限制：带评估信息的纯文本**
在 Aspose.Cells 生成的纯文本文件中，会在文档末尾添加一个评估信息。
<br>
<image src="2.png" width="70%" />
<br>

### **第四限制：带评估水印的 PDF 和图像**
在 Aspose.Cells 生成的 PDF 或图像文件中，会在文档/图像顶部添加一个评估水印。在 GridWeb 控件中，您也无法隐藏评估版权警告（额外工作表），它将始终被添加（在控件中的工作表选项卡末尾）。
<br>
<image src="3.png" width="70%" />
<br>

### **第五限制：配置文件设置（Aspose.Cells.GridWeb）**
您无法通过在配置部分（例如 web.config 文件中）添加以下代码行来重新指定脚本路径。acw_client 是一个包含文件的文件夹，Aspose.Cells.GridWeb 使用此文件夹来管理其内部配置，其中包含脚本文件、图像文件和其他文件以指定 GridWeb 的行为和设置其他操作。配置文件用于防止控件使用内嵌客户端资源（图像、脚本等），在某些情况/场景下很有用。此外，这些配置设置仅在控件的许可版本中生效。

XML
{{< highlight csharp >}}
<appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

在某些情况/场景下，如果您在文件系统网站或 MS Ajax 扩展等中使用 Aspose.Cells.GridWeb 控件，这些设置可能是强制性的。

{{% /alert %}}
