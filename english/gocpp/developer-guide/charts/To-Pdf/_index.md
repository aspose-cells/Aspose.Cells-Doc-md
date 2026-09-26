---
title: Chart to PDF with Golang via C++
linktitle: Chart to PDF
description: Learn how to use Aspose.Cells for Go via C++ to convert a chart to a PDF document. Our guide will demonstrate how to export a chart from Microsoft Excel and save it as a PDF for further distribution and archiving.
keywords: Aspose.Cells for Go, Chart to PDF, Microsoft Excel, PDF Conversion, Export, Distribution, Archiving.
type: docs
weight: 47
url: /go-cpp/chart-to-pdf/
---

## **Rendering Chart to PDF**

In order to render the chart to PDF format, the Aspose.Cells APIs have exposed the [**Chart::ToPdf**](https://reference.aspose.com/cells/go-cpp/chart/topdf_string/) method with the ability to store the resultant PDF on a disk path or stream.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ToPdf.go" >}}

## **Create Chart PDF with Desired Page Size**

You can create a chart PDF with your desired page size using Aspose.Cells and specify how you want to align the chart inside the page—top, bottom, center, left, right, etc. Besides, the output chart can be created in a stream or on disk. Please see the following sample code that loads the [sample Excel file](64716906.xlsx), accesses the first chart inside the worksheet, and then converts it into [output PDF](64716907.pdf) with the desired page size. The following screenshot shows that the page size in the output PDF is 7 × 7 as specified in the code, and the chart is center‑aligned both horizontally and vertically.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)

## **Sample Code**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ToPdf-1.go" >}}
{{< app/cells/assistant language="go" >}}
