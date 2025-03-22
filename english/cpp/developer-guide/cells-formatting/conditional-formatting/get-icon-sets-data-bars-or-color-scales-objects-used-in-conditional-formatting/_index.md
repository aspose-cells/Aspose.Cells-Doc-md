---
title: Get Icon Sets, Data Bars or Color Scales Objects used in Conditional Formatting with C++
linktitle: Get Icon Sets, Data Bars or Color Scales Objects
description: Aspose.Cells for C++ is a library for working with spreadsheet files. It supports the use of icon sets, data bars, and color scale objects in conditional formatting to display data from spreadsheets. This article describes how to use the Aspose.Cells library to retrieve data for these objects.
keywords: Aspose.Cells, Conditional Formatting, Icon Set, Data Bar, Color Scale, Spreadsheet
type: docs
weight: 10
url: /cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/
---

{{% alert color="primary" %}} 

Sometimes, you need to retrieve icon sets that are used in the conditional formatting of a cell or a range of cells and you want to create an image file based on it. You might require to read the data bars or color scales used in the conditional formatting. Aspose.Cells for C++ supports this feature.

{{% /alert %}} 

The following code sample shows how to read icon sets that are used for conditional formatting. With Aspose.Cells' simple API, the icon set's image data is saved as an image.

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell cell = sheet.GetCells().Get(u"A1");

    // Get the conditional formatting result object
    ConditionalFormattingResult cfr = cell.GetConditionalFormattingResult();

    // Get the icon set
    ConditionalFormattingIcon icon = cfr.GetConditionalFormattingIcon();

    // Get the image data from the icon
    Vector<uint8_t> imageData = icon.GetImageData();

    // Create the image file based on the icon's image data
    ofstream outputFile((outDir + u"imgIcon.out.jpg").ToUtf8(), ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetCount());
    outputFile.close();

    std::cout << "Icon image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```