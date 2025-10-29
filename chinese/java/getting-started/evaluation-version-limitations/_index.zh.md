---
title: 评估版限制
type: docs
weight: 40
url: /zh/java/evaluation-version-limitations/
description: 本文可以帮助您了解如何获取评估版本及评估版本的限制。
keywords: 评估版限制，评估版中打开的文件数，使用评估版的评估水印。
---

## **如何获取Aspose.Cells的评估版**

您可以从[其下载页面](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells)的Maven存储库中下载**Aspose.Cells** for Java的评估版本。评估版本提供的功能与产品许可版本完全相同。此外，只需购买许可证并添加几行代码即可将评估版本变为已许可版本。

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
在Aspose.Cells生成的输出纯文本文件中，评估信息将被添加到文档末尾。当文件保存为纯文本（如CSV和TSV格式）时，只输出第一个工作表的内容。
<br>
<image src="2.png" width="70%" />
<br>

### **第四限制：带评估水印的 PDF 和图像**
在Aspose.Cells生成的输出PDF或图像文件中，将在文档/图像顶部粘贴评估水印。
<br>
<image src="3.png" width="70%" />
<br>
{{< app/cells/assistant language="java" >}}
