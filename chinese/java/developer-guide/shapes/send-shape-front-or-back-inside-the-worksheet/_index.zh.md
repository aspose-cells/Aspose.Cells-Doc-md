---
title: 将形状发送到工作表内的前后
type: docs
weight: 600
url: /zh/java/send-shape-front-or-back-inside-the-worksheet/
---

## **可能的使用场景**

当同一位置存在多个形状时，它们的可见性由它们的z顺序位置决定。Aspose.Cells提供[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)）方法，更改形状的z顺序位置。如果要将形状发送到后面，则将使用-1、-2、-3等负数；如果要将形状发送到前面，则将使用1、2、3等正数。

## **将形状发送到工作表内的前面或后面**

以下示例代码说明了使用[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)）方法的用法。请查看代码中使用的[sample Excel file](50528362.xlsx)和执行后生成的[output Excel file](50528361.xlsx)的屏幕截图显示了代码对示例Excel文件的影响。

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-SendShapeFrontOrBackInWorksheet.java" >}}
