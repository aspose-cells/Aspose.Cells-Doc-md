---
title: Add WordArt Watermark to Worksheet with C++
linktitle: Managing WordArt
type: docs
weight: 180
url: /cpp/add-wordart-watermark-to-worksheet/
description: Learn how to add WordArt watermarks to Excel worksheets using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Use WordArt to add special text effects to spreadsheets. For example, stretch a title across the top of the file, decorate text, and make text fit a preset shape, or apply text to an Excel sheet as a background watermark. The WordArt becomes an object that you can move or position in spreadsheets to add decoration.

{{% /alert %}} 

The following example shows how to add a WordArt shape to set a background watermark for a worksheet.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first default sheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add Watermark
    Shape wordart = sheet.GetShapes().AddTextEffect(MsoPresetTextEffect::TextEffect1,
        u"CONFIDENTIAL", u"Arial Black", 50, false, true,
        18, 8, 1, 1, 130, 800);

    // Get the fill format of the word art
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the transparency
    wordArtFormat.SetTransparency(0.9);

    // Make the line invisible
    LineFormat lineFormat = wordart.GetLine();

    // Save the file
    U16String outputPath = outDir + u"Watermark_Test.out.xls";
    workbook.Save(outputPath);

    std::cout << "Watermark added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Advance topics**
- [Add Word Art Text with Built-in Styles](/cells/cpp/add-word-art-text-with-built-in-styles/)
- [Locking WordArt Watermark](/cells/cpp/locking-wordart-watermark/)
- [Set preset WordArt style to the text of the shape](/cells/cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
{{< app/cells/assistant language="cpp" >}}
