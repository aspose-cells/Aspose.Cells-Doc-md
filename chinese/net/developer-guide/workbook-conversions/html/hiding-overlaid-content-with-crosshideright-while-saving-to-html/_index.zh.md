---
title: 在保存为HTML时使用CrossHideRight隐藏叠加内容
type: docs
weight: 100
url: /zh/net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **可能的使用场景**

将Excel文件保存为HTML时，您可以指定单元格字符串的不同交叉类型。默认情况下，Aspose.Cells根据Microsoft Excel生成HTML，但当您将交叉类型更改为 [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)时，它会将单元格右侧与单元格字符串叠加或重叠的所有字符串隐藏起来。

## **在保存为HTML时使用CrossHideRight隐藏叠加内容**

以下示例代码加载 [示例Excel文件](64716894.xlsx)，在将 [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/htmlcrossstringtype)设置为 [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)后将其保存为 [输出HTML](64716893.zip)。屏幕截图解释了 [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) 如何影响默认输出的HTML。

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.cs" >}}
