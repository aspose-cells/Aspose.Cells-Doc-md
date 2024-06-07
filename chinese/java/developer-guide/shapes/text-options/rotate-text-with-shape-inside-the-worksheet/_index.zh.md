---
title: 旋转工作表内形状中的文本
type: docs
weight: 110
url: /zh/java/rotate-text-with-shape-inside-the-worksheet/
---

## **可能的使用场景**

您可以使用 Microsoft Excel 在任何形状内添加文本。如果使用起初版本的 Microsoft Excel 2003 添加形状，则文本不会随形状旋转。但是，如果使用较新版本的 Microsoft Excel（如 2007、2010、2013 或 2016 等），则文本将随形状旋转。您可以使用 [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape) 属性来控制文本是否应随形状旋转。它的默认值为 **true**，表示文本将随形状旋转，但如果将其设置为 **false**，则文本将不会随形状旋转。

## **旋转工作表中形状中的文本**

以下示例代码加载了包含一个三角形形状，并且其文本随形状旋转的 [示例 Excel 文件](64716919.xlsx)。如果在 Microsoft Excel 中打开示例 Excel 文件并旋转三角形形状，文本将随之旋转。然后，代码将该 [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape) 属性设置为 **false**，并将其另存为 [输出 Excel 文件](64716917.xlsx)。如果现在在 Microsoft Excel 中打开输出 Excel 文件并旋转三角形形状，文本将不会随之旋转。请参阅以下屏幕截图，以了解代码对示例 Excel 文件的影响。

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-RotateTextWithShapeInsideWorksheet.java" >}}
