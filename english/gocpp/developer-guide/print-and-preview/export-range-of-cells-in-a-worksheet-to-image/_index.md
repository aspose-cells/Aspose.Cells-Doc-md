---
title: Export Range of Cells in a Worksheet to Image with Golang via C++
linktitle: Export Range of Cells to Image
type: docs
weight: 60
url: /go-cpp/export-range-of-cells-in-a-worksheet-to-image/
description: Learn how to export a specific range of cells in a worksheet to an image using Aspose.Cells with Golang via C++.
---

## **Possible Usage Scenarios**

You can make an image of a worksheet using Aspose.Cells. However, sometimes you need to export only a range of cells in a worksheet to an image. This article explains how to achieve this.

## **Export Range of Cells in a Worksheet to Image**

To take an image of a range, set the print area to the desired range and then set all margins to 0. Also set [**ImageOrPrintOptions.GetOnePagePerSheet()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getonepagepersheet/) to **true**. The following code takes an image of the range D8:G16. Below is a screenshot of the [sample Excel file](47153160.xlsx) used in the code. You can try the code with any Excel file.

## **Screenshot of Sample Excel File and its Exported Image**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Executing the code creates an image of the range D8:G16 only.

**![todo:image_alt_text](Output-Image.png)**

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportRangeOfCellsInAWorksheetToImage.go" >}}
{{< app/cells/assistant language="go" >}}
