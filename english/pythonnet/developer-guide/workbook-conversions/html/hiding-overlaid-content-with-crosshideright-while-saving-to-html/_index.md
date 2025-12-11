---
title: Hiding Overlaid Content with CrossHideRight while saving to HTML
type: docs
weight: 100
url: /python-net/hiding-overlaid-content-with-crosshideright-while-saving-to/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When you save your Excel file to HTML, you can specify different cross types for cell strings. By default, Aspose.Cells for Python via .NET generates HTML as Microsoft Excel does, but when you change the cross type to [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/), it hides all the strings on the right side of the cell that are overlaid or overlapping with the cell string.

## **Hiding Overlaid Content with CrossHideRight while saving to HTML**

The following sample code loads the [sample Excel file](64716894.xlsx) and saves it to [output HTML](64716893.zip) after setting the [**HtmlSaveOptions.html_cross_string_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/html_cross_string_type) to [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/). The screenshot explains how [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/) affects the output HTML compared to the default output.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
{{< app/cells/assistant language="python-net" >}}
