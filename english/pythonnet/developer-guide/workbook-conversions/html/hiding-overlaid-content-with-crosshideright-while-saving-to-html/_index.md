---
title: Hiding Overlaid Content with CrossHideRight while saving to HTML
type: docs
weight: 100
url: /python-net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Possible Usage Scenarios**

When you save your Excel file to HTML, you can specify different cross types for cell strings. By default, Aspose.Cells for Python via .NET generates HTML as per Microsoft Excel but when you change the cross type to [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/), then it hides all the strings at the right side of the cell which are overlaid or overlapping with cell string.

## **Hiding Overlaid Content with CrossHideRight while saving to Html**

The following sample code loads the [sample Excel file](64716894.xlsx) and saves it to [output HTML](64716893.zip) after setting the [**HtmlSaveOptions.html_cross_string_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/html_cross_string_type) as [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/). The screenshot explains how [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/) affects the output HTML from default output.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
