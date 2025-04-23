---
title: 在工作表内设置评论或形状的边距
type: docs
weight: 1500
url: /zh/net/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **可能的使用场景**

Aspose.Cells允许您使用[**Shape.TextBody.TextAlignment**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/fontsettingcollection/properties/textalignment)属性设置任何形状或注释的边距。此属性返回[**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment)类的对象，其具有不同的属性，例如[**TopMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/topmarginpt)、[**LeftMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/leftmarginpt)、[**BottomMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/bottommarginpt)、[**RightMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rightmarginpt)等，可用于设置顶部、左侧、底部和右侧边距。

## **设置工作表内批注或形状的边距**

请参阅以下示例代码。它加载包含两个形状的[示例Excel文件](61767851.xlsx)。代码逐个访问形状，并设置它们的顶部、左侧、底部和右侧边距。请参阅由代码生成的[输出Excel文件](61767852.xlsx)以及显示代码对输出Excel文件的影响的屏幕截图。

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-SetMarginsOfCommentOrShapeInsideTheWorksheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
