---
title: Specify how to cross string in output PDF and image with Golang via C++
linktitle: Specify how to cross string in output PDF and image
type: docs
weight: 120
url: /go-cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Learn how to control text overflow in PDF and image outputs using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

When a cell contains text or string that is larger than the width of the cell, the string overflows if the next cell in the next column is null or empty. When you save your Excel file into PDF or Image, you can control this overflow by specifying the cross type using the [**TextCrossType**](https://reference.aspose.com/cells/go-cpp/textcrosstype/) enumeration. It has the following values:

- **TextCrossType.Default**: Display text like MS Excel, which depends on the next cell. If the next cell is null, the string will cross or it will be truncated.

- **TextCrossType.CrossKeep**: Display the string like MS Excel exporting PDF/Image.

- **TextCrossType.CrossOverride**: Display all the text by crossing other cells and override the text of crossed cells.

- **TextCrossType.StrictInCell**: Only display the string within the width of the cell.

## **Specify how to cross string in output PDF/Image using TextCrossType**

The following sample code loads the sample Excel file and saves it to PDF/Image format by specifying different [**TextCrossType**](https://reference.aspose.com/cells/go-cpp/textcrosstype/). The sample Excel file and output files can be downloaded from the following links:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Sample Code

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyHowToCrossStringInOutputPdfAndImage.go" >}}