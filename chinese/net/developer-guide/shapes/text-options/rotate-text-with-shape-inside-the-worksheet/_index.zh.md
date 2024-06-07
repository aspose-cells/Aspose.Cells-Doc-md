---
title: 旋转工作表内形状中的文本
type: docs
weight: 1300
url: /zh/net/rotate-text-with-shape-inside-the-worksheet/
---

## **可能的使用场景**

您可以使用Microsoft Excel在任何形状中添加文本。如果使用非常老的Microsoft Excel 2003添加形状，则文本不会随形状旋转。但是，如果使用更新版本的Microsoft Excel，如2007、2010、2013或2016等添加形状，则文本将随形状旋转。您可以使用[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape)属性控制文本是否应随形状旋转。它的默认值为true，这意味着文本将随形状旋转，但如果将其设置为false，则文本将不会随形状旋转。

## **旋转工作表中形状中的文本**

以下示例代码加载了一个包含三角形形状及其文本随形状旋转的[示例Excel文件](64716896.xlsx)。如果您在Microsoft Excel中打开示例Excel文件并旋转三角形形状，则文本也将随之旋转。然后，代码将[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape)属性设置为false，并保存为[输出Excel文件](64716897.xlsx)。如果您现在在Microsoft Excel中打开输出Excel文件并旋转三角形形状，则文本将不会随之旋转。请参考以下截图，显示了代码对示例Excel文件的影响。

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-RotateTextWithShapeInsideWorksheet.cs" >}}
