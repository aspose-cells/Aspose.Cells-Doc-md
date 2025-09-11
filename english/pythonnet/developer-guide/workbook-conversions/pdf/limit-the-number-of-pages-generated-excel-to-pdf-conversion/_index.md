---
title: Limit the Number of Pages Generated - Excel to PDF Conversion
type: docs
weight: 180
url: /python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Learn how to Limit the Number of Pages Generated while Rendering Excel to PDF with Aspose.Cells for Python via .NET API.
keywords: Python Limit the Number of Pages Generated while Rendering Excel to PDF, Limit the Number of Pages Generated while saving Excel to PDF using Python, Python Set the Number of Pages Generated while converting Excel to PDF, Control the Number of Pages Generated for Excel to PDF in python
---

{{% alert color="primary" %}}

Sometimes, you want to print a range of pages to an output PDF file. Aspose.Cells for Python via .NET has the ability to set a limit on how many pages are generated when converting an Excel spreadsheet to the PDF file format.

{{% /alert %}}

## **Limiting the Number of Pages Generated**

The following example shows how to render a range of pages (3 and 4) in a Microsoft Excel file to PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-LimitNumberOfPagesGenerated-1.py" >}}

{{% alert color="primary" %}}

If the spreadsheet contains formulas, it is best to call [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) method just before rendering it to PDF. Doing ensures that formula dependent values are recalculated, and the correct values are rendered in the output file.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}