---
title: 实现工作表的自定义纸张大小以进行渲染
type: docs
weight: 30
url: /zh/java/implement-custom-paper-size-of-worksheet-for-rendering/
---

## **可能的使用场景**

在MS Excel中，没有直接的选项来创建自定义纸张大小，但是在将Excel文件渲染为PDF文件格式时，您可以设置所需工作表的自定义纸张大小。本文解释了如何使用Aspose.Cells API来设置工作表的自定义纸张大小。

## **实现工作表的自定义纸张大小以进行渲染**

Aspose.Cells允许您使用[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)的[**customPaperSize**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#customPaperSize(double,%20double)）方法来实现所需的工作表纸张大小。以下示例代码说明了如何为工作簿中的第一个工作表指定自定义纸张大小。还请参见使用以下代码生成的[输出PDF](45056030.pdf)作为参考。

## **屏幕截图**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.java" >}}
