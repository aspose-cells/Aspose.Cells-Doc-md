---
title: 实现工作表的自定义纸张大小以进行渲染
type: docs
weight: 70
url: /zh/net/implement-custom-paper-size-of-worksheet-for-rendering/
description: 本文介绍在以编程方式将 Excel 文件呈现为 PDF 文件格式时，如何使用 C# API 或 .NET 库示例代码设置所需工作表的自定义纸张大小。
keywords: set custom paper size while rendering excel to pdf c#
---
##  **可能的使用场景**

在 MS Excel 中没有直接选项可用于创建自定义纸张尺寸，但是，您可以在将 Excel 文件呈现为 PDF 文件格式时设置所需工作表的自定义纸张尺寸。本文档说明如何使用 Aspose.Cells API 设置工作表的自定义纸张尺寸。

##  **实现工作表的自定义纸张大小以进行渲染**

 Aspose.Cells 允许您实现所需的工作表纸张大小。您可以使用[**自定义纸张大小**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/custompapersize)的方法[**页面设置**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)类来指定自定义页面大小。以下示例代码说明了如何为工作簿中的第一个工作表指定自定义纸张大小。另请参阅[输出 PDF](45056028.pdf)使用以下代码生成以供参考。

##  **截屏**

![待办事项：image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

##  **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.cs" >}}
