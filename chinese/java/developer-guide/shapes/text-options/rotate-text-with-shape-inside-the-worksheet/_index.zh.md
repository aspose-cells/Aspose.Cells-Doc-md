---
title: 在工作表内旋转带有形状的文本
type: docs
weight: 110
url: /zh/java/rotate-text-with-shape-inside-the-worksheet/
---
## **可能的使用场景**

您可以使用 Microsoft Excel 在任何形状内添加文本。如果您使用非常旧的 Microsoft Excel 2003 添加形状，那么文本将不会随形状一起旋转。但是，如果您使用 Microsoft Excel 的较新版本（例如 2007、2010、2013 或 2016 等）添加形状，则文本将随形状一起旋转。您可以控制文本是否应随形状旋转或不使用[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape)财产。它的默认值为**真的**这意味着文本将随形状旋转，但如果您将其设置为**错误的**那么文字将不会随形状旋转。

## **在工作表内旋转带有形状的文本**

下面的示例代码加载[示例 Excel 文件](64716919.xlsx)具有三角形形状，其文本随形状旋转。如果您在 Microsoft Excel 中打开示例 Excel 文件并旋转三角形，文本也会随之旋转。然后代码设置[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape)财产作为**错误的**并将其另存为[输出Excel文件](64716917.xlsx).如果现在在 Microsoft Excel 中打开输出 Excel 文件并旋转三角形，文本将不会随之旋转。请参阅以下屏幕截图，显示代码对示例 Excel 文件的影响以供参考。

![待办事项：图片_替代_文本](rotate-text-with-shape-inside-the-worksheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-RotateTextWithShapeInsideWorksheet.java" >}}
