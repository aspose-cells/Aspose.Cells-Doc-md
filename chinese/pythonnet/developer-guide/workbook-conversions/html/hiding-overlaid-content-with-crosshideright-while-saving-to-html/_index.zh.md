---
title: 使用 CrossHideRight 在保存为 HTML 时隐藏重叠内容
type: docs
weight: 100
url: /zh/python-net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **可能的使用场景**

将Excel文件保存为HTML时，可以为单元格字符串指定不同的交叉类型。默认情况下，Aspose.Cells for Python via .NET 按照Microsoft Excel的方式生成HTML，但若将交叉类型更改为 [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/)，则会隐藏覆盖或重叠在单元格字符串右侧的所有字符串。

## **在保存为Html时使用CrossHideRight隐藏重叠内容**

以下示例代码加载了[sample Excel文件](64716894.xlsx)，并在设置[**HtmlSaveOptions.html_cross_string_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/html_cross_string_type)为[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/)后将其另存为[output HTML](64716893.zip)。屏幕截图解释了[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/) 如何影响默认输出的HTML。

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
{{< app/cells/assistant language="python-net" >}}
