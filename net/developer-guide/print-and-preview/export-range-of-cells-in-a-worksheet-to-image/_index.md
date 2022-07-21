---
title: Export Range of Cells in a Worksheet to Image
type: docs
weight: 60
url: /net/export-range-of-cells-in-a-worksheet-to-image/
---

## **Possible Usage Scenarios**

You can make an image of a worksheet using Aspose.Cells. However, sometimes you need to export only a range of cells in a worksheet to an image. This article explains how to achieve this.

## **Export Range of Cells in a Worksheet to Image**

To take an image of a range, set the print area to the desired range and then set all margins to 0. Also set [**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet) to **true**. The following code takes an image of the range D8:G16. Below is a screenshot of the [sample Excel file](47153160.xlsx) used in the code. You can try the code with any Excel file.

## **Screenshot of Sample Excel File and its Exported Image**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Executing the code creates an image of the range D8:G16 only.

**![todo:image_alt_text](Output-Image.png)**

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
