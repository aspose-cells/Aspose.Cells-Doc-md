---
title: Convert XLS File with Images or Charts to PDF with Golang via C++
linktitle: Convert XLS File with Images or Charts to PDF
type: docs
weight: 50
url: /go-cpp/convert-xls-file-with-images-or-charts-to-pdf/
description: Convert XLS files containing images or charts to PDF documents using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}} 

Aspose.Cells supports converting XLS files that contain images and charts to PDF documents. Aspose.Cells for C++ can work independently to convert a spreadsheet to PDF: Aspose.PDF for C++ is not required for the conversion. The process can be done in memory as the process does not depend on temporary or intermediary XML files. This means that large Excel files, for example, ones containing images, charts, and other drawing objects, can be converted quickly and efficiently.

{{% /alert %}} 
## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertXlsFileWithImagesOrChartsToPdf.go" >}}
{{% alert color="primary" %}} 

If the spreadsheet contains formulas, it is best to call the [Calculate(CalculationData data)](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/calculate/) method just before rendering to PDF. Doing so ensures that formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}