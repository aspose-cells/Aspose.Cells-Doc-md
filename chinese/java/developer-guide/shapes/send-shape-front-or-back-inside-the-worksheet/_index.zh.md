---
title: 在工作表内部发送形状到前面或后面
type: docs
weight: 600
url: /zh/java/send-shape-front-or-back-inside-the-worksheet/
---

## **可能的使用场景**

当同一位置有多个形状时，它们的可见性由它们的z-顺序位置决定。Aspose.Cells提供 [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int) 方法可以改变形状的z-顺序位置。如果要发送形状到后面，您将使用像 -1、-2、-3 等的负数；如果要发送形状到前面，您将使用像 1、2、3 等的正数。

## **在工作表内发送形状到最前或最后**

以下示例代码解释了[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int))方法的使用。请查看代码中使用的[sample Excel file](50528362.xlsx)以及它生成的[output Excel file](50528361.xlsx)。截图显示了代码在执行后对示例Excel文件的影响。

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-SendShapeFrontOrBackInWorksheet.java" >}}
