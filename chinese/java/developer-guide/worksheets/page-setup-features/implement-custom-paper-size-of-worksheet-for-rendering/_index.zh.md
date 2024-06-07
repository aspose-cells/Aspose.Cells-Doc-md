---
title: 为呈现实现工作表的自定义纸张大小
type: docs
weight: 30
url: /zh/java/implement-custom-paper-size-of-worksheet-for-rendering/
---

## **可能的使用场景**

MS Excel中没有直接选项可用于创建自定义纸张大小，但是当将Excel文件渲染为PDF文件格式时，您可以使用Aspose.Cells API设置所需工作表的自定义纸张大小。本文档说明了如何使用Aspose.Cells API设置工作表的自定义纸张大小。

## **实现呈现的工作表的自定义纸张大小**

Aspose.Cells允许您通过使用[**customPaperSize**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#customPaperSize(double,%20double)）方法对工作表的页面设置实现所需的工作表自定义纸张大小。以下示例代码说明了如何为工作簿中的第一个工作表指定自定义纸张大小。另请参考使用以下代码生成的[output PDF](45056030.pdf)。

## **截图**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.java" >}}
