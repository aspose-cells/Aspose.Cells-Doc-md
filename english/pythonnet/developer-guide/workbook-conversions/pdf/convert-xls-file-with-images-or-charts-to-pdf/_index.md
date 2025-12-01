---
title: Convert XLS File with Images or Charts to PDF
type: docs
weight: 50
url: /python-net/convert-xls-file-with-images-or-charts-to-pdf/
description: Learn how to Convert XLS File with Images or Charts to PDF with Aspose.Cells for Python via .NET API.
keywords: Python Convert XLS File with Images or Charts to PDF, Convert xls to pdf using Python, Python XLS file with images to pdf, xls file with charts to pdf in python, python xls to pdf
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET supports converting XLS files that contain images and charts to PDF documents. Aspose.Cells for Python via .NET API can work independently to convert a spreadsheet to PDF: Aspose.PDF for .NET is not required for the conversion. The process can be done in memory as the process does not depend on temporary or intermediary XML files. This means that large Excel files, for example, ones containing images, charts, and other drawing objects, can be converted quickly and efficiently.

{{% /alert %}} 
## **Sample Code**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXLSFileToPDF-1.py" >}}

{{% alert color="primary" %}} 

If the spreadsheet contains formulas, it is best to call the [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) method just before rendering to PDF. Doing so ensures that formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
