---
title: 在保存为 HTML 时使用 CrossHideRight 隐藏覆盖内容
type: docs
weight: 100
url: /zh/net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---
## **可能的使用场景**

当您将 Excel 文件保存为 HTML 时，您可以为单元格字符串指定不同的交叉类型。默认情况下，Aspose.Cells 按照 Microsoft Excel 生成 HTML，但是当您将交叉类型更改为[**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype), 然后它隐藏单元格右侧的所有字符串，这些字符串与单元格字符串重叠或重叠。

## **在保存为 Html 时使用 CrossHideRight 隐藏覆盖内容**

下面的示例代码加载[示例 Excel 文件](64716894.xlsx)并将其保存到[输出 HTML](64716893.zip)设置后[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/htmlcrossstringtype)作为[**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype).截图解释了如何[**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)影响默认输出的输出 HTML。

![待办事项：图像_替代_文本](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.cs" >}}
