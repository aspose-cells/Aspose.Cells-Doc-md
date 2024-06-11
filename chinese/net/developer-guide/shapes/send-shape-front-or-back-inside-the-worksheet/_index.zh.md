---
title: 在工作表内部发送形状到前面或后面
type: docs
weight: 3400
url: /zh/net/send-shape-front-or-back-inside-the-worksheet/
---

## **可能的使用场景**

当同一位置有多个形状时，它们的可见性由它们的z-order位置决定。 Aspose.Cells提供 [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/tofrontorback) 方法来更改形状的z-order位置。 如果你想把形状发送到后面，你将使用一个负数，如-1、-2、-3等，如果你想把形状发送到前面，你将使用一个正数，如1、2、3等。

## **在工作表内发送形状到最前或最后**

以下示例代码解释了 [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/tofrontorback) 方法的使用。请查看代码中使用的[示例Excel文件](50528330.xlsx)，以及由此生成的[输出Excel文件](50528331.xlsx)。屏幕截图显示了代码对示例Excel文件的执行效果。

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-SendShapeFrontOrBackInWorksheet.cs" >}}
