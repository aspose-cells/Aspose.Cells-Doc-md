---
title: 在保存为HTML时使用CrossHideRight隐藏叠加内容
type: docs
weight: 100
url: /zh/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---

## **可能的使用场景**

当您将Excel文件保存为HTML时，可以为单元格字符串指定不同的交叉类型。默认情况下，Aspose.Cells生成与Microsoft Excel相符的HTML，但当您将[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)更改为[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)时，它将隐藏单元格右侧与单元格字符串重叠的所有字符串。

## **在保存为HTML时使用CrossHideRight隐藏叠加内容**

以下示例代码加载了包含外部资源的[sample Excel文件](64716916.xlsx)并在设置[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)为[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)后将其保存为[输出HTML](64716915.zip)。屏幕快照解释了[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)如何影响默认输出的HTML。

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
