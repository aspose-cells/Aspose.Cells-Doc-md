---
title: 使用 CrossHideRight 在保存为 HTML 时隐藏重叠内容
type: docs
weight: 100
url: /zh/net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **可能的使用场景**

在保存Excel文件为HTML时，您可以为单元格字符串指定不同的交叉类型。 默认情况下，Aspose.Cells生成与Microsoft Excel相符的HTML，但当您将交叉类型更改为[**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)时，则隐藏单元格右侧的所有与单元格字符串叠加或重叠的字符串。

## **在保存为Html时使用CrossHideRight隐藏重叠内容**

以下示例代码加载了[sample Excel文件](64716894.xlsx)，并在设置[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/htmlcrossstringtype)为[**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)后将其另存为[output HTML](64716893.zip)。屏幕截图解释了[**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) 如何影响默认输出的HTML。

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.cs" >}}
