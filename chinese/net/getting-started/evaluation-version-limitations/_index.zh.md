---
title: 评估版限制
type: docs
weight: 110
url: /zh/net/evaluation-version-limitations/
description: Aspose.Cells for .NET 提供不同的购买计划，或使用 C# 中的许可和订阅政策提供免费试用和 30 天临时许可证进行评估。
keywords: Evaluation Version Limitations, Number of Opened Files in Evaluation Version, Evaluation Watermark using Evaluation Version.
---
##  **如何获取评估版 Aspose.Cells**

您可以下载评估版**Aspose.Cells** NET 来自[它的下载页面](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) Maven 仓库。评估版本提供与产品的许可版本完全相同的功能。此外，当您购买许可证并添加几行代码来应用许可证时，评估版就会获得许可。

一旦您对 *Aspose.Cells** 的评价感到满意，您可以[购买许可证](https://purchase.aspose.com)请访问 Aspose 网站。让自己熟悉所提供的不同订阅类型。如果您有任何疑问，请随时联系Aspose销售团队。

每个 Aspose 许可证都包含一年期订阅，可免费升级到在此期间发布的任何新版本或修复程序。技术支持是免费且不受限制的，并且向许可用户和评估用户提供。

##  **如何在没有评估版本限制的情况下测试 Aspose.Cells**

如果你想测试**Aspose.Cells**无评估版本限制，请求 30 天的临时许可证。请参阅[如何获得临时许可证？](https://purchase.aspose.com/temporary-license)了解更多信息。


##  **评估版限制**

评估版**Aspose.Cells**产品（未指定许可证）提供完整的产品功能，但仅限于在一个程序中打开 100 个文件以及带有评估水印的额外工作表。

限制如下所示：

###  **第一个限制：打开文件的数量**

运行程序时，您只能打开 100 个 Excel 文件。如果您的应用程序超过此数量，则会抛出异常。

###  **第二个限制：带有评估水印的工作表**
该工作表将始终显示为活动工作表。仅在许可版本中，您可以将活动工作表设置为其他工作表。
<br>
<image src="1.png" width="70%" />
<br>

###  **第三个限制：带有评估信息的纯文本**
在 Aspose.Cells 输出的纯文本文件中，将在文档末尾添加评估信息。
<br>
<image src="2.png" width="70%" />
<br>

###  **第四个限制：PDF和带有评估水印的图像**
在输出 PDF 或 Aspose.Cells 的图像文件中，评估水印将粘贴在文档/图像的顶部。您也无法在 GridWeb 控件中隐藏评估版权警告（额外的工作表），它始终会添加（在工作表选项卡的末尾）在控件中。
<br>
<image src="3.png" width="70%" />
<br>

###  **第 5 个限制：配置文件设置（Aspose.Cells.GridWeb）**
您无法通过将以下代码行添加到配置部分（例如在 web.config 文件中）来重新指定脚本路径。 acw_client是一个包含文件和Aspose.Cells的文件夹。GridWeb使用这个文件夹来管理其内部配置，它有脚本文件、图像文件和其他文件来指定GridWeb的行为并设置其他操作。配置文件用于防止控件使用嵌入式客户端资源（图像、脚本等），这在某些情况/场景中很有用。此外，web.config 文件中的此配置设置仅对控件的许可版本有效。

**XML**
{{< highlight "csharp" >}}
<appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

如果您在文件系统网站或 MS Ajax 扩展等中使用 Aspose.Cells.GridWeb 控件，这些设置在某些情况/场景下可能是强制性的。

{{% /alert %}}