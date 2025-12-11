---
title: Ignore Errors while Rendering Excel to PDF
type: docs
weight: 80
url: /python-net/ignore-errors-while-rendering-excel-to-pdf/
description: Learn how to Ignore Errors while Rendering Excel to PDF with Aspose.Cells for Python via .NET API.
keywords: Python Ignore Errors while Rendering Excel to PDF, Ignore Errors while saving Excel to PDF using Python, Python Ignore Errors while converting Excel to PDF, Ignore Errors for Excel to PDF in python
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Sometimes when you convert your Excel file to PDF, errors or exceptions occur and the conversion process terminates. You can ignore all such errors during the conversion process by using the [**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/) property. This way, the conversion process will complete smoothly without throwing any error or exception, but data loss may occur. Therefore, please use this property only if the loss of data is not critical for you.

## **Ignore Errors while Rendering Excel to PDF**

The following code loads the [sample Excel file](55541778.xlsx), but the sample Excel file is erroneous and throws an error during [conversion to PDF](55541779.pdf) in 17.11. Since we are using the [**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/) property, it does not throw an error. However, one *rounded red arrow‑like shape*, as shown in this screenshot, is lost.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-IgnoreErrorsWhileRenderingExcelToPdf.py" >}}
{{< app/cells/assistant language="python-net" >}}
