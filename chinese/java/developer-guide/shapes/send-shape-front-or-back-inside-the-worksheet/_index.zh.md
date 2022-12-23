---
title: 在工作表内发送形状前面或后面
type: docs
weight: 600
url: /zh/java/send-shape-front-or-back-inside-the-worksheet/
---
## **可能的使用场景**

当同一位置存在多个形状时，它们的可见方式取决于它们的 z 顺序位置。 Aspose.Cells提供[**形状.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)) 方法改变形状的 z 顺序位置。如果你想将形状发送到后面，你将使用负数，如 -1、-2、-3 等，如果你想将形状发送到前面，你将使用正数，如 1、2、3，等等

## **在工作表内发送形状前面或后面**

下面的示例代码解释了[**形状.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)） 方法。请参阅[示例 Excel 文件](50528362.xlsx)在代码中使用[输出Excel文件](50528361.xlsx)由它产生。屏幕截图显示了代码对示例 Excel 文件的执行效果。

![待办事项：图片_替代_文本](send-shape-front-or-back-inside-the-worksheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-SendShapeFrontOrBackInWorksheet.java" >}}
