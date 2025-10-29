---
title: 在工作表内设置评论或形状的边距
type: docs
weight: 1500
url: /zh/python-net/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **可能的使用场景**

Aspose.Cells for Python via .NET 允许您使用 [**Shape.text_body.text_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/fontsettingcollection/text_alignment) 属性设置任何形状或批注的边距。此属性返回 [**ShapeTextAlignment**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment) 类的对象，该对象具有不同的属性，例如 [**top_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/top_margin_pt)、[**left_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/left_margin_pt)、[**bottom_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/bottom_margin_pt)、[**right_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/right_margin_pt) 等，可用于设置上、左、下、右边距。

## **设置工作表内批注或形状的边距**

请参阅以下示例代码。它加载包含两个形状的[示例Excel文件](61767851.xlsx)。代码逐个访问形状，并设置它们的顶部、左侧、底部和右侧边距。请参阅由代码生成的[输出Excel文件](61767852.xlsx)以及显示代码对输出Excel文件的影响的屏幕截图。

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-SetMarginsOfCommentOrShapeInsideTheWorksheet.py" >}}
{{< app/cells/assistant language="python-net" >}}
