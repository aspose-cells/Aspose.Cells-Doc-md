---
title: Specify how to cross strings in output PDF and image with Golang via C++
linktitle: Specify how to cross strings in output PDF and image
type: docs
weight: 120
url: /go-cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Learn how to control text overflow in PDF and image outputs using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

When a cell contains text that is larger than the width of the cell, the string overflows if the next cell in the next column is blank or empty. When you save your Excel file as PDF or Image, you can control this overflow by specifying the crossing type using the [**TextCrossType**](https://reference.aspose.com/cells/go-cpp/textcrosstype/) enumeration. It has the following values:

- **TextCrossType.Default**: Displays text like MS Excel, which depends on the next cell. If the next cell is blank, the string will cross, or it will be truncated.

- **TextCrossType.CrossKeep**: Displays the string as MS Excel does when exporting PDF/Image.

- **TextCrossType.CrossOverride**: Displays all the text by crossing other cells and overrides the text of the crossed cells.

- **TextCrossType.StrictInCell**: Only displays the string within the width of the cell.

## **Specify how to cross strings in output PDF/Image using TextCrossType**

The following sample code loads the sample Excel file and saves it to PDF/Image format by specifying different [**TextCrossType**](https://reference.aspose.com/cells/go-cpp/textcrosstype/). The sample Excel file and output files can be downloaded from the following links:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Sample Code

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyHowToCrossStringInOutputPdfAndImage.go" >}}