---
title: 在工作表内部发送形状到前面或后面
type: docs
weight: 3400
url: /zh/python-net/send-shape-front-or-back-inside-the-worksheet/
---

## **可能的使用场景**

当相同位置存在多个形状时，它们的可见性由它们的z顺序位置决定。Aspose.Cells for Python via .NET提供了[**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back)方法，用于更改形状的z顺序位置。如果想将形状置于背后，可以使用负数，如-1、-2、-3等；如果要将形状放到前面，可以使用正数，如1、2、3等。

## **在工作表内发送形状到最前或最后**

以下示例代码解释了 [**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back) 方法的使用。请查看代码中使用的[示例Excel文件](50528330.xlsx)，以及由此生成的[输出Excel文件](50528331.xlsx)。屏幕截图显示了代码对示例Excel文件的执行效果。

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-SendShapeFrontOrBackInWorksheet.py" >}}
{{< app/cells/assistant language="python-net" >}}
