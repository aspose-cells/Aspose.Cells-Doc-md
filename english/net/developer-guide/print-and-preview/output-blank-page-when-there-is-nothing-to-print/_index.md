---
title: Output Blank Page when there is Nothing to Print
type: docs
weight: 90
url: /net/output-blank-page-when-there-is-nothing-to-print/
---

## **Possible Usage Scenarios**

If the sheet is empty, then Aspose.Cells will not print anything when you export worksheet to image. You can change this behavior by using [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) property. When you will set it **true**, it will print the blank page.

## **Output Blank Page when there is Nothing to Print**

The following sample code creates the empty workbook which has an empty worksheet and renders the empty worksheet to an image after setting the [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) property as **true**. Consequently, it generates the blank page as there is nothing to print which you can see in the image below.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}