---
title: 将形状发送到工作表内的前后
type: docs
weight: 3400
url: /zh/net/send-shape-front-or-back-inside-the-worksheet/
---

## **可能的使用场景**

当同一位置存在多个形状时，它们的可见性由它们的Z顺序位置决定。Aspose.Cells提供[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/tofrontorback)方法，可以更改形状的Z顺序位置。如果要将形状发送到后面，您将使用类似-1、-2、-3等的负数，如果要将形状发送到前面，您将使用类似1、2、3等的正数。

## **将形状发送到工作表内的前面或后面**

以下示例代码解释了[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/tofrontorback)方法的用法。请查看代码中使用的 [示例Excel文件](50528330.xlsx) 和由其生成的 [输出Excel文件](50528331.xlsx)。屏幕截图显示了代码对示例Excel文件执行的影响。

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-SendShapeFrontOrBackInWorksheet.cs" >}}
