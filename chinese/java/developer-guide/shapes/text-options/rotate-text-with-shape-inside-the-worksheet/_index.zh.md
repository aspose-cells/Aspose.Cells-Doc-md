---
title: 在工作表内旋转文本与形状
type: docs
weight: 110
url: /zh/java/rotate-text-with-shape-inside-the-worksheet/
---

## **可能的使用场景**

您可以使用Microsoft Excel在任何形状内添加文本。如果您使用非常老的Microsoft Excel 2003添加形状，则文本将不会随形状旋转。但如果您使用更新的版本的Microsoft Excel，例如2007、2010、2013或2016等添加形状，则文本将随形状旋转。您可以使用 [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape) 属性来控制文本是否应该随形状旋转。其默认值为 **true**，这意味着文本将随形状旋转，但如果您将其设置为 **false**，则文本将不会随形状旋转。

## **在工作表内旋转文本与形状**

以下示例代码加载了带有三角形形状且其文本随形状旋转的 [示例excel文件](64716919.xlsx)。如果您在Microsoft Excel中打开示例excel文件并旋转三角形形状，则文本也将随之旋转。然后，代码将将 [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape) 属性设置为 **false** 并保存为 [输出excel文件](64716917.xlsx)。如果您现在在Microsoft Excel中打开输出excel文件并旋转三角形形状，文本将不会随之旋转。请参考以下屏幕截图显示代码对示例excel文件的影响。

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-RotateTextWithShapeInsideWorksheet.java" >}}
