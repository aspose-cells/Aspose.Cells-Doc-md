---
title: 实现工作表的自定义纸张大小以进行渲染
type: docs
weight: 70
url: /zh/net/implement-custom-paper-size-of-worksheet-for-rendering/
description: 本文介绍了如何使用C# API或.NET库示例代码在以编程方式将Excel文件渲染为PDF文件格式时设置所需工作表的自定义纸张大小。
keywords: 在MS Excel中没有直接的选项可用来创建自定义纸张大小，但是您可以在以编程方式将Excel文件渲染为PDF文件格式时设置所需工作表的自定义纸张大小。本文介绍了如何使用Aspose.Cells API来设置工作表的自定义纸张大小。
---

## **可能的使用场景**

在MS Excel中没有直接选项可以创建自定义纸张尺寸，但是在将Excel文件渲染为PDF文件格式时，您可以设置工作表的所需自定义纸张大小。此文档解释了如何使用Aspose.Cells API设置工作表的自定义纸张大小。

## **实现工作表的自定义纸张大小以进行渲染**

Aspose.Cells允许您实现所需的工作表纸张大小。您可以使用[**CustomPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/custompapersize)类的[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)方法来指定自定义页面大小。以下示例代码说明了如何为工作簿中的第一个工作表指定自定义纸张大小。

## **屏幕截图**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.cs" >}}
{{< app/cells/assistant language="csharp" >}}
