---
title: 为呈现实现工作表的自定义纸张大小
type: docs
weight: 70
url: /zh/net/implement-custom-paper-size-of-worksheet-for-rendering/
description: 本文介绍如何使用C# API或.NET库示例代码，在以编程方式将Excel文件呈现为PDF文件格式时设置自定义纸张大小的工作表。
keywords: 在将Excel转换为PDF时设置自定义纸张大小C#
---

## **可能的使用场景**

MS Excel中没有直接的选项来创建自定义纸张大小，但是，您可以在将Excel文件呈现为PDF文件格式时设置自定义工作表的纸张大小。本文介绍如何使用Aspose.Cells APIs设置工作表的自定义纸张大小。

## **实现呈现的工作表的自定义纸张大小**

Aspose.Cells允许您实现所需的工作表纸张大小。您可以使用[**CustomPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/custompapersize)类的[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)方法指定自定义页面大小。以下示例代码说明如何为工作簿中的第一个工作表指定自定义纸张大小。请查看使用以下代码生成的[输出PDF](45056028.pdf)以供参考。

## **截图**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.cs" >}}
