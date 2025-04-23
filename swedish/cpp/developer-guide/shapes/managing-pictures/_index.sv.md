---
title: Hantera bilder med C++
linktitle: Hantera bilder
type: docs
weight: 10
url: /sv/cpp/managing-pictures/
description: Lägg till, placera och hantera bilder i kalkylblad med API Aspose.Cells for C++.
---

Aspose.Cells tillåter utvecklare att lägga till bilder i kalkylbladet under körtiden. Dessutom kan placeringen av dessa bilder styras under körtiden, vilket diskuteras mer utförligt i de kommande avsnitten.

Den här artikeln förklarar hur man lägger till bilder och hur man infogar en bild som visar innehållet i vissa celler.

## **Lägga till bilder**

Att lägga till bilder i ett kalkylblad är mycket enkelt. Det tar bara några rader kod:
Ring [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) metoden av [**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/) (innestad i [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) -objektet). [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) metoden tar följande parametrar:

- **Övre vänstra radindex**, indexet för den övre vänstra raden.
- **Övre vänstra kolumnindex**, indexet för den övre vänstra kolumnen.
- **Bildfilnamn**, namnet på bildfilen, komplett med sökväg.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Add worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add image to worksheet at F6 (row 5, column 5)
    U16String imagePath = srcDir + u"logo.jpg";
    worksheet.GetPictures().Add(5, 5, imagePath);

    // Save workbook
    U16String outputPath = outDir + u"output.xls";
    workbook.Save(outputPath);

    std::cout << "Worksheet with image created successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Placering av bilder**

Det finns två möjliga sätt att kontrollera placeringen av bilder med hjälp av Aspose.Cells:

- Proportionell placering: definiera ett läge proportionellt med radhöjden och kolumnbredden.
- Absolut positionering: definiera den exakta positionen på sidan där bilden kommer att infogas, till exempel 40 pixlar till vänster och 20 pixlar under cellens kant.

### **Proportionell placering**

Utvecklare kan placera bilder proportionellt efter radens höjd och kolumnens bredd med egenskaperna [**UpperDeltaX**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltax/) och [**UpperDeltaY**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltay/) av [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) -objektet. Ett [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) -objekt kan erhållas från [**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/) genom att ange dess bildindex. Detta exempel placerar en bild i cellen F6.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook workbook;

    // Add new worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add picture to worksheet at (5,5) position
    U16String imagePath = outDir + u"logo.jpg";
    int pictureIndex = worksheet.GetPictures().Add(5, 5, imagePath);

    // Access added picture and set positioning
    Drawing::Picture picture = worksheet.GetPictures().Get(pictureIndex);
    picture.SetUpperDeltaX(200);
    picture.SetUpperDeltaY(200);

    // Save modified workbook
    U16String outputPath = outDir + u"book1.out.xls";
    workbook.Save(outputPath);

    std::cout << "Picture added and positioned successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Absolut positionering**

Utvecklare kan också placera bilderna absolut genom att använda [**Left**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getleft/) och [**Top**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettop/) egenskaperna hos [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)-objektet. Detta exempel placerar en bild i cellen F6, 60 pixlar från vänster och 10 pixlar från toppen av cellen.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access worksheet collection and add new sheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    int sheetIndex = worksheets.Add();

    // Get reference to newly added worksheet
    Worksheet worksheet = worksheets.Get(sheetIndex);

    // Add picture to worksheet at row 5, column 5 (cell F6)
    PictureCollection pictures = worksheet.GetPictures();
    int pictureIndex = pictures.Add(5, 5, srcDir + u"logo.jpg");

    // Access added picture and set position
    Picture picture = pictures.Get(pictureIndex);
    picture.SetLeft(60);
    picture.SetTop(10);

    // Save modified workbook
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Workbook with inserted picture saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Infoga en bild baserad på cellreferens**

Aspose.Cells låter dig visa innehållet i en arbetsbladscell i en bildform. Du kan länka bilden till cellen som innehåller de data du vill visa. Eftersom cellen eller cellintervallet är länkat till den grafiska objektet, visas ändringar som du gör i data i den cellen eller cellintervallet automatiskt i den grafiska objektet.

Lägg till en bild i arbetsbladet genom att anropa [**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/) metoden av [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) (innestad i [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) -objektet). Specificera cellområdet med [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) attributet av [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) -objektet.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access first worksheet and cells collection
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    Cells cells = worksheet.GetCells();

    // Set cell values
    cells.Get(u"A1").PutValue(U16String(u"A1"));
    cells.Get(u"C10").PutValue(U16String(u"C10"));

    // Add picture to worksheet
    auto shapes = worksheet.GetShapes();
    Picture pic = shapes.AddPicture(0, 3, 10, 6, Vector<uint8_t>());

    // Set picture formula and update values
    pic.SetFormula(u"A1:C10");
    shapes.UpdateSelectedValue();

    // Save workbook
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Fortsatta ämnen**
- [Lägg till villkorliga ikoner inställda med celltexten](/cells/sv/cpp/add-conditional-icons-set-with-the-cell-text/)
- [Infoga en Länkbild från Webbadress](/cells/sv/cpp/insert-a-linked-picture-from-web-address/)
- [Infoga en Bild Baserat på Cellreferens](/cells/sv/cpp/insert-a-picture-based-on-cell-reference/)
- [Ladda en webbbild från en URL till ett Excel-arbetsblad](/cells/sv/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
