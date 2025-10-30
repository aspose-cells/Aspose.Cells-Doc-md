---
title: Arbete med bakgrund i ODS filer med C++
linktitle: Arbeta med bakgrund i ODS filer
type: docs
weight: 150
url: /sv/cpp/working-with-background-in-ods-files/
description: Lär dig hantera färgade och grafiska bakgrunder i ODS filer med Aspose.Cells och C++.
---

## **Bakgrund i ODS-filer**

Bakgrund kan läggas till i kalkylblad i ODS-filer. Bakgrunden kan antingen vara en färgad bakgrund eller en grafisk bakgrund. Bakgrunden är inte synlig när filen är öppen, men om filen skrivs ut som PDF är bakgrunden synlig i den genererade PDF:en. Bakgrunden är också synlig i utskriftsvisningen.

Aspose.Cells ger möjlighet att läsa bakgrundsinformation och lägga till bakgrunden i ODS-filer.

## **Läs bakgrundsinformation från ODS-fil**

Aspose.Cells tillhandahåller klassen [**OdsPageBackground**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/) för att hantera bakgrund i ODS-filer. Följande kodexempel visar användningen av [**OdsPageBackground**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/) klassen genom att ladda [käll-ODS](90112030.ods) filen och läsa bakgrundsinformationen. Se den genererade Konsolutdata för referens.

### **Exempelkod**

```c++
#include <iostream>
#include <fstream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook workbook(srcDir + u"GraphicBackground.ods");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    OdsPageBackground background = worksheet.GetPageSetup().GetODSPageBackground();

    std::cout << "Background Type: " << static_cast<int>(background.GetType()) << std::endl;
    std::cout << "Background Position: " << static_cast<int>(background.GetGraphicPositionType()) << std::endl;

    Vector<uint8_t> graphicData = background.GetGraphicData();
    std::string filePath = (outDir + u"background.jpg").ToUtf8();
    std::ofstream fout(filePath, std::ios::binary);
    fout.write(reinterpret_cast<const char*>(graphicData.GetData()), graphicData.GetLength());
    fout.close();

    std::cout << "Background image saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Konsoloutput**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Lägg till färgad bakgrund i ODS-fil**

Aspose.Cells tillhandahåller klassen [**OdsPageBackground**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/) för att hantera bakgrund i ODS-filer. Följande kodexempel visar användningen av [**OdsPageBackground.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/) egenskapen för att lägga till en färgbakgrund till ODS-filen. Se den genererade [output ODS](90112031.ods) filen för referens.

### **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set cell values
    worksheet.GetCells().Get(0, 0).SetValue(1);
    worksheet.GetCells().Get(1, 0).SetValue(2);
    worksheet.GetCells().Get(2, 0).SetValue(3);
    worksheet.GetCells().Get(3, 0).SetValue(4);
    worksheet.GetCells().Get(4, 0).SetValue(5);
    worksheet.GetCells().Get(5, 0).SetValue(6);
    worksheet.GetCells().Get(0, 1).SetValue(7);
    worksheet.GetCells().Get(1, 1).SetValue(8);
    worksheet.GetCells().Get(2, 1).SetValue(9);
    worksheet.GetCells().Get(3, 1).SetValue(10);
    worksheet.GetCells().Get(4, 1).SetValue(11);
    worksheet.GetCells().Get(5, 1).SetValue(12);

    // Access the ODS page background
    OdsPageBackground background = worksheet.GetPageSetup().GetODSPageBackground();

    // Set background color and type
    background.SetColor(Color::Azure());
    background.SetType(OdsPageBackgroundType::Color);

    // Save the workbook
    workbook.Save(outDir + u"ColoredBackground.ods", SaveFormat::Ods);

    std::cout << "Workbook saved successfully with colored background!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Lägg till grafisk bakgrund i ODS-fil**

Aspose.Cells tillhandahåller klassen [**OdsPageBackground**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/) för att hantera bakgrund i ODS-filer. Följande kodexempel visar användningen av [**OdsPageBackground.GetGraphicData()**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/odspagebackground/getgraphicdata/) egenskapen för att lägga till grafisk bakgrund till ODS-filen. Se den genererade [output ODS](90112030.ods) filen för referens.

### **Exempelkod**

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

Vector<uint8_t> GetDataFromFile(const U16String& file)
{
    std::string f = file.ToUtf8();
    // open a file 
    std::ifstream fileStream(f, std::ios::binary);

    if (!fileStream.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;
    }

    // Get file size
    fileStream.seekg(0, std::ios::end);
    std::streampos fileSize = fileStream.tellg();
    fileStream.seekg(0, std::ios::beg);

    // Read file contents into uint8_t array
    uint8_t* buffer = new uint8_t[fileSize];
    fileStream.read(reinterpret_cast<char*>(buffer), fileSize);
    fileStream.close();

    Vector<uint8_t>data(buffer, fileSize);
    delete[] buffer;

    return data;
}


int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set values in cells
    worksheet.GetCells().Get(0, 0).SetValue(1);
    worksheet.GetCells().Get(1, 0).SetValue(2);
    worksheet.GetCells().Get(2, 0).SetValue(3);
    worksheet.GetCells().Get(3, 0).SetValue(4);
    worksheet.GetCells().Get(4, 0).SetValue(5);
    worksheet.GetCells().Get(5, 0).SetValue(6);
    worksheet.GetCells().Get(0, 1).SetValue(7);
    worksheet.GetCells().Get(1, 1).SetValue(8);
    worksheet.GetCells().Get(2, 1).SetValue(9);
    worksheet.GetCells().Get(3, 1).SetValue(10);
    worksheet.GetCells().Get(4, 1).SetValue(11);
    worksheet.GetCells().Get(5, 1).SetValue(12);

    // Get the ODS page background
    OdsPageBackground background = worksheet.GetPageSetup().GetODSPageBackground();

    // Set background type to graphic
    background.SetType(OdsPageBackgroundType::Graphic);

    // Read the background image file
    Vector<uint8_t> graphicData = GetDataFromFile(U16String(srcDir + u"background.jpg"));

    // Set graphic data and type
    background.SetGraphicData(graphicData);
    background.SetGraphicType(OdsPageBackgroundGraphicType::Area);

    // Save the workbook
    workbook.Save(outDir + u"GraphicBackground.ods", SaveFormat::Ods);

    std::cout << "Graphic background applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
