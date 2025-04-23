---
title: 在工作表内设置评论或形状的边距
type: docs
weight: 90
url: /zh/java/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **可能的使用场景**

Aspose.Cells允许您使用 [**Shape.TextBody.TextAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/fontsettingcollection#TextAlignment) 属性设置任何形状或评论的边距。该属性返回 [**ShapeTextAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeTextAlignment) 类的对象，该对象具有不同的属性，例如 [**TopMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#TopMarginPt)、[**LeftMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#LeftMarginPt)、[**BottomMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#BottomMarginPt)、[**RightMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RightMarginPt) 等，可以用来设置顶部、左侧、底部和右侧边距。

## **设置工作表内批注或形状的边距**

请参阅以下示例代码。它加载了包含两个形状的 [示例excel文件](61767867.xlsx)。代码逐一访问形状并设置其顶部、左侧、底部和右侧边距。请查看代码生成的 [输出excel文件](61767866.xlsx) 和屏幕截图显示代码对输出excel文件的影响。

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-SetMarginsOfCommentOrShapeInsideTheWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
