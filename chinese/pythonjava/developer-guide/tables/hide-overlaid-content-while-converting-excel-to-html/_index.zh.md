---
title: 将 Excel 转换为 HTML 时隐藏覆盖内容
type: docs
weight: 40
url: /zh/python-java/hide-overlaid-content-while-converting-excel-to/
---
## **将 Excel 转换为 HTML 时隐藏覆盖内容**
当您将 Excel 文件保存为 HTML 时，您可以为单元格字符串指定不同的交叉类型。默认情况下，Aspose.Cells 根据 Microsoft Excel 生成 HTML，但是当您更改[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)到[叉_隐藏_正确的](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)然后它隐藏单元格右侧的所有字符串，这些字符串与单元格字符串重叠或重叠。

下面的示例代码加载[示例 Excel 文件](sampleHidingOverlaidContentWithCrossHideRight.xlsx)并将其保存到[输出 HTML](HTML-outputHidingOverlaidContentWithCrossHideRight.zip)设置后[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)作为[叉_隐藏_正确的](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT).截图解释了如何[叉_隐藏_正确的](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)影响默认输出的输出 HTML。

![待办事项：图片_替代_文本](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
