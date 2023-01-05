---
title: 在保存到 HTML 时使用 CrossHideRight 隐藏覆盖内容
type: docs
weight: 100
url: /zh/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---
## **可能的使用场景**

当您将 Excel 文件保存为 HTML 时，您可以为单元格字符串指定不同的交叉类型。默认情况下，Aspose.Cells 根据 Microsoft Excel 生成 HTML，但是当您更改[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)到[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)然后它隐藏单元格右侧的所有字符串，这些字符串与单元格字符串重叠或重叠。

## **在保存到 HTML 时使用 CrossHideRight 隐藏覆盖内容**

下面的示例代码加载[示例 Excel 文件](64716916.xlsx)并将其保存到[输出 HTML](64716915.zip)设置后[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)作为[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT).截图解释了如何[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)影响默认输出的输出 HTML。

![待办事项：图片_替代_文本](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
