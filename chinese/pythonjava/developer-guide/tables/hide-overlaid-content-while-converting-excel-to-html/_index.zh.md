---
title: 在将Excel转换为HTML时隐藏重叠内容
type: docs
weight: 40
url: /zh/python-java/hide-overlaid-content-while-converting-excel-to/
---

## **在将Excel转换为HTML时隐藏重叠内容**
将Excel文件保存为HTML时，您可以为单元格字符串指定不同的交叉类型。默认情况下，Aspose.Cells根据Microsoft Excel生成HTML，但当您将[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)设置为[CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)时，它将隐藏与单元格字符串重叠或覆盖的右侧所有字符串。

以下示例代码加载了[sample Excel文件](sampleHidingOverlaidContentWithCrossHideRight.xlsx)，在将[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)设置为[CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)之后，将其保存为[output HTML](HTML-outputHidingOverlaidContentWithCrossHideRight.zip)。截图说明了[CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)如何影响默认输出的HTML。

![todo:image_alt_text](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
