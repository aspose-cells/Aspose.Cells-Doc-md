---
title: 使用 CrossHideRight 在保存为 HTML 时隐藏重叠内容
type: docs
weight: 100
url: /zh/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---

## **可能的使用场景**

将 Excel 文件保存为 HTML 时，您可以为单元格字符串指定不同的交叉类型。Aspose.Cells 默认按照 Microsoft Excel 生成 HTML，但当将[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)更改为[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)时，它会隐藏与单元格字符串重叠或重叠的右侧的所有字符串。

## **在保存为 HTML 时隐藏重叠的内容与 CrossHideRight**

以下示例代码加载[sample Excel file](64716916.xlsx)并在将[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)设置为[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)后将其保存为[output HTML](64716915.zip)。屏幕截图说明了[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)如何影响默认输出的输出 HTML。

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
