---
title: Print and Preview Workbook with C++
linktitle: Print and Preview
type: docs
weight: 70
url: /cpp/workbook-and-worksheet-print-preview/
description: Aspose.Cells supports printing and previewing Excel files without Microsoft Excel installation using C++.
---

{{% alert color="primary" %}}

After creating a worksheet, you often want to print a hard copy of it. This article explains how to print spreadsheets with Aspose.Cells.

{{% /alert %}}

## **Print Introduction**

Microsoft Excel assumes that you want to print the entire worksheet area unless you specify a selection. To print using Aspose.Cells, first import the Aspose.Cells.Rendering namespace to the program. It has several useful classes, for example, [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) and [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/).


## **Print Preview**

There may be cases where Excel files with millions of pages need to be converted to PDF or images. Processing such files will consume a lot of time and resources. In such cases, the Workbook and Worksheet Print Preview feature might prove to be useful. Before converting such files, the user can check the total number of pages and then decide whether the file is to be converted or not. This article focuses on using the [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) and [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) classes to find out the total number of pages.

Aspose.Cells provides the print preview feature. For this, the API provides [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) and [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) classes. To create the print preview of the whole workbook, create an instance of the [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) class by passing [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) and [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) objects to the constructor. The [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) class provides an [**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/getevaluatedpagecount/) method which returns the number of pages in the generated preview. Similar to [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) class, the [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) class is used to generate a print preview for a specific worksheet. To create the print preview of a worksheet, create an instance of the [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) class by passing [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) and [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) objects to the constructor. The [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) class also provides an [**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/getevaluatedpagecount/) method which returns the number of pages in the generated preview.

The following code snippet demonstrates the use of both [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) and [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) classes by using the [sample excel file](94896177.xlsx).

### **Sample Code**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Create image or print options
    ImageOrPrintOptions imgOptions;

    // Create workbook printing preview
    WorkbookPrintingPreview preview(workbook, imgOptions);
    cout << "Workbook page count: " << preview.GetEvaluatedPageCount() << endl;

    // Create sheet printing preview
    SheetPrintingPreview preview2(workbook.GetWorksheets().Get(0), imgOptions);
    cout << "Worksheet page count: " << preview2.GetEvaluatedPageCount() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

The following is the output generated by executing the above code.

### **Console Output**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

## **Advance topics**
- [Configuring Fonts for Rendering Spreadsheets](/cells/cpp/configuring-fonts-for-rendering-spreadsheets/)
- [Convert Worksheet to Image - Remove whitespace around data](/cells/cpp/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Converting Worksheet to Image and Worksheet to Image by Page](/cells/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [Converting Worksheet to Image using ImageOrPrint Options](/cells/cpp/converting-worksheet-to-image-using-imageorprint-options/)
- [Export Range of Cells in a Worksheet to Image](/cells/cpp/export-range-of-cells-in-a-worksheet-to-image/)
- [Export Worksheet or Chart into Image with Desired Width and Height](/cells/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Extract Images from Worksheets using ImageOrPrintOptions](/cells/cpp/extract-images-from-worksheets-using-imageorprintoptions/)
- [Generate Thumbnail of the Worksheet](/cells/cpp/generate-thumbnail-of-the-worksheet/)
- [Output Blank Page when there is Nothing to Print](/cells/cpp/output-blank-page-when-there-is-nothing-to-print/)
- [Page Setup and Printing Options](/cells/cpp/page-setup-and-printing-options/)
- [Render Sequence of Pages using PageIndex and PageCount Properties of ImageOrPrintOptions](/cells/cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Render Worksheet to Graphic Context](/cells/cpp/render-worksheet-to-graphic-context/)
- [Specify Individual or Private Set of Fonts for Workbook Rendering](/cells/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)