---
title: Renderingsmönster för anpassad datumformat g och ge mm dd med C++
description: Aspose.Cells är ett C++ bibliotek för att arbeta med kalkylbladsfiler som stöder rendering av datum med hjälp av anpassade datumformatmönster g och ge . Den här artikeln beskriver hur man renderar anpassade datumformatmönster med hjälp av Aspose.Cells så att användare kan kontrollera hur datum visas om de vill.
keywords: Aspose.Cells, C++ bibliotek, elektroniskt kalkylblad, anpassat datumformat, rendering, mönster g , mönster ge , kontrollera visning
type: docs
weight: 160
url: /sv/cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/
---

{{% alert color="primary" %}}

Aspose.Cells kan nu rendera anpassade datumformatmallar som g, ge.mm.dd och liknande. Vänligen kontrollera den bifogade [källkalkylbladsfilen](5112361.xlsx) och den [konverterade PDF:en](5112360.pdf) av Aspose.Cells för din referens.

{{% /alert %}}

Följande exempelkod konverterar [källkalkylbladsfilen](5112361.xlsx) som innehåller datumvärden med anpassade formatmallar som g och ge.mm.dd till [utdata-PDF:en](5112360.pdf).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from an existing Excel file
    U16String inputFilePath = srcDir + u"SourceFile.xlsx";
    Workbook workbook(inputFilePath);

    // Save the Excel file as PDF
    workbook.Save(outDir + u"CustomDateFormat_out.pdf");

    std::cout << "File saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
