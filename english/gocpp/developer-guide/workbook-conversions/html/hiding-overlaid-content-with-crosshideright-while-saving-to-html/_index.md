---
title: Hiding Overlaid Content with CrossHideRight while saving to HTML with Golang via C++
linktitle: Hiding Overlaid Content with CrossHideRight while saving to HTML
type: docs
weight: 100
url: /go-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: Use CrossHideRight with Aspose.Cells in C++ to hide overlaid content when saving to HTML.
---

## **Possible Usage Scenarios**

When you save your Excel file to HTML, you can specify different cross types for cell strings. By default, Aspose.Cells generates HTML as per Microsoft Excel, but when you change the cross type to [**CrossHideRight**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype), it hides all the strings on the right side of the cell that are overlaid or overlapping with the cell string.

## **Hiding Overlaid Content with CrossHideRight while saving to HTML**

The following sample code loads the [sample Excel file](64716894.xlsx) and saves it to [output HTML](64716893.zip) after setting the [**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/gethtmlcrossstringtype/) to [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype). The screenshot explains how [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) affects the output HTML compared with the default output.

![Hiding overlaid content with CrossHideRight while saving to HTML](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HidingOverlaidContentWithCrosshiderightWhileSavingToHtml.go" >}}