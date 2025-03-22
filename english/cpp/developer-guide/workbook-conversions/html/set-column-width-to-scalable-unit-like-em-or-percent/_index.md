---
title: Set column width to scalable unit like em or percent with C++
linktitle: Set column width to scalable unit like em or percent
type: docs
weight: 130
url: /cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Learn how to set column width to scalable units like em or percent using Aspose.Cells for C++.
---

Generating an HTML file from a spreadsheet is very common. The size of the columns is defined in "pt" which works in many cases. However, there can be a case where this fixed size may not be required. For example, if a container panel width is 600px where this HTML page is being displayed. In this case, you may get a horizontal scrollbar if the generated table width is bigger. It was required that this fixed size shall be changed into a scalable unit like em or percent to get a better presentation. Following sample code can be used where [**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/widthscalable/) is set to **true** for creating scalable width.

Sample source file and output files can be downloaded from the following links:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample source file
    Workbook wb(srcDir + u"sampleForScalableColumns.xlsx");

    // Specify Html Save Options
    HtmlSaveOptions options;

    // Set the property for scalable width
    options.SetWidthScalable(true);

    // Specify image save format
    options.SetExportImagesAsBase64(true);

    // Save the workbook in Html format with specified Html Save Options
    wb.Save(outDir + u"outsampleForScalableColumns.html", options);

    std::cout << "Workbook saved successfully with scalable columns!" << std::endl;

    Aspose::Cells::Cleanup();
}
```