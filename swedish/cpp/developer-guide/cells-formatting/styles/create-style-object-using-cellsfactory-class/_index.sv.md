---  
title: Skapa Style objekt med CellsFactory klass i C++  
description: Aspose.Cells är ett C++ bibliotek för att arbeta med kalkylbladsfiler som tillhandahåller ett stilobjekt för att formatera celler. Den här artikeln introducerar hur man skapar ett cellstil objekt med hjälp av CellsFactory klassen i Aspose.Cells biblioteket så att användare kan anpassa cellernas utseende efter behov.  
keywords: Aspose.Cells, C++ bibliotek, elektroniskt kalkylblad, stilobjekt, cellstil, anpassning  
type: docs  
weight: 70  
url: /sv/cpp/create-style-object-using-cellsfactory-class/  
---  

## **Skapa Style-objekt med hjälp av CellsFactory-klassen**  
Följande exempel skapa ett [Style](https://reference.aspose.com/cells/cpp/aspose.cells/style) objekt med hjälp av [CellsFactory](https://reference.aspose.com/cells/cpp/aspose.cells/cellsfactory)-klass och ställer in standardstilen för arbetsboken. Vänligen ladda ner den [utdata Excel-filen](5115153.xlsx) för att se resultaten av denna kod som referens.  

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

    // Create a Style object using CellsFactory class
    CellsFactory cf;
    Style st = cf.CreateStyle();

    // Set the Style fill color to Yellow
    st.SetPattern(BackgroundType::Solid);
    st.SetForegroundColor(Color::Yellow());

    // Create a workbook and set its default style using the created Style object
    Workbook wb;
    wb.SetDefaultStyle(st);

    // Save the workbook
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
