---
title: Render Unicode Supplementary characters in output PDF with Golang via C++ by Aspose.Cells
linktitle: Render Unicode Supplementary Characters
type: docs
weight: 350
url: /go-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Learn how to render Unicode Supplementary characters in output PDF using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Normal Unicode characters are 2-byte long, while Unicode Supplementary characters are 4-byte long. Aspose.Cells now supports rendering of these 4-byte Unicode characters.

In the Unicode Character Standard, Supplementary Characters are the characters assigned code points from U+10000 to U+10FFFF. In other words, these are the Unicode characters greater than U+FFFF.

- In UTF-8 these characters are each 4 bytes long.
- In UTF-16 these characters require 2 surrogates (16-bit units).

{{% /alert %}}

## Render Unicode Supplementary Characters in Output PDF by Aspose.Cells

The following screenshot shows how Aspose.Cells rendered the [source Excel file](5115563.xlsx) into the [output PDF](5115564.pdf). As you can see, all three Unicode Supplementary characters have been rendered exactly the same as in Microsoft Excel.

![todo:image_alt_text](output.png)

## Sample Code

You can use this sample code to convert the [source Excel file](5115563.xlsx) into the [output PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderUnicodeSupplementaryCharactersInOutputPdfByAsposeCells.go" >}}