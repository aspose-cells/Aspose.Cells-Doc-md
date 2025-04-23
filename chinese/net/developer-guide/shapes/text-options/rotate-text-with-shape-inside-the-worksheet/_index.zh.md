---
title: 在工作表内旋转文本与形状
type: docs
weight: 1300
url: /zh/net/rotate-text-with-shape-inside-the-worksheet/
---

## **可能的使用场景**

您可以在Microsoft Excel中的任何形状中添加文本。如果您使用非常旧的Microsoft Excel 2003添加形状，则文本不会随形状旋转。但是，如果您使用较新的版本的Microsoft Excel，例如2007、2010、2013或2016等添加形状，则文本将随形状旋转。您可以使用[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape)属性控制文本是否应随形状旋转。其默认值为**true**，这意味着文本将随形状旋转，但如果将其设置为**false**，则文本将不会随形状旋转。

## **在工作表内旋转文本与形状**

以下示例代码加载包含三角形形状及其文本随形状旋转的示例Excel文件(64716896.xlsx)。如果在Microsoft Excel中打开示例Excel文件并旋转三角形形状，则文本也将随之旋转。然后将[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape)属性设置为**false**并保存为[输出Excel文件](64716897.xlsx)。现在，在Microsoft Excel中打开输出Excel文件并旋转三角形形状，文本将不会随之旋转。请参阅以下屏幕截图，以了解代码对示例Excel文件的影响。

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-RotateTextWithShapeInsideWorksheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
