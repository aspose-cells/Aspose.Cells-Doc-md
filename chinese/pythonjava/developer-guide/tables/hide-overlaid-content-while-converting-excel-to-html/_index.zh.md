---
title: 在将Excel转换为HTML时隐藏叠加内容
type: docs
weight: 40
url: /zh/python-java/hide-overlaid-content-while-converting-excel-to/
---

## **在将Excel转换为HTML时隐藏叠加内容**
当将Excel文件保存为HTML时，您可以为单元格字符串指定不同的交叉类型。默认情况下，Aspose.Cells根据Microsoft Excel生成HTML，但当您将 [HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) 设置为 [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) 时，它将隐藏所有与单元格字符串叠加或重叠的右侧字符串。

下面的示例代码加载了 [示例Excel文件](sampleHidingOverlaidContentWithCrossHideRight.xlsx)，并在将 [HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) 设置为 [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) 后将其保存为 [输出HTML](HTML-outputHidingOverlaidContentWithCrossHideRight.zip)。截图解释了 [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) 如何影响默认输出的HTML。

![todo:image_alt_text](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
