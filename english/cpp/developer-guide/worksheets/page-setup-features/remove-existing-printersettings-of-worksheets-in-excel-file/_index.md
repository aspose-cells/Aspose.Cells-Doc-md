---
title: Remove Existing PrinterSettings of Worksheets in Excel file with C++
linktitle: Remove Existing PrinterSettings of Worksheets
type: docs
weight: 60
url: /cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: Learn how to remove existing PrinterSettings of Worksheet inside the Excel file through Page Setup object programmatically using Aspose.Cells with C++.
keywords: remove printer settings of worksheet c++, remove printer settings of excel worksheet c++
---

## **Possible Usage Scenarios**
Sometimes developers want to prevent Excel from including *.bin* files of printer settings in the saved XLSX files. Printer settings files are located under *“[file "root"]\xl\printerSettings”.* This document explains how to remove existing printer settings using Aspose.Cells APIs.

## **Remove Existing PrinterSettings of Worksheets in Excel file**
Aspose.Cells allows you to remove existing printer settings specified for different sheets in the Excel file. The following sample code illustrates how to remove existing printer settings for all the worksheets in the workbook. Please see its [sample Excel file](45056020.xlsx), [output Excel file](45056021.xlsx), console output as well as the screenshot for a reference.

## **Screenshot**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Sample Code**
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source Excel file
    Workbook wb(srcDir + u"sampleRemoveExistingPrinterSettingsOfWorksheets.xlsx");

    // Get the sheet counts of the workbook
    int sheetCount = wb.GetWorksheets().GetCount();

    // Iterate all sheets
    for (int i = 0; i < sheetCount; i++)
    {
        // Access the i-th worksheet
        Worksheet ws = wb.GetWorksheets().Get(i);

        // Access worksheet page setup
        PageSetup ps = ws.GetPageSetup();

        // Check if printer settings for this worksheet exist
        if (ps.GetPrinterSettings().GetSize() != 0)
        {
            // Print the following message
            std::cout << "PrinterSettings of this worksheet exist." << std::endl;

            // Print sheet name and its paper size
            std::cout << "Sheet Name: " << ws.GetName().ToUtf8() << std::endl;
            std::cout << "Paper Size: " << static_cast<int>(ps.GetPaperSize()) << std::endl;

            // Remove the printer settings by setting them null
            ps.SetPrinterSettings(Vector<uint8_t>());
            std::cout << "Printer settings of this worksheet are now removed by setting it null." << std::endl;
            std::cout << std::endl;
        }
    }

    // Save the workbook
    wb.Save(outDir + u"outputRemoveExistingPrinterSettingsOfWorksheets.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Console Output**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}