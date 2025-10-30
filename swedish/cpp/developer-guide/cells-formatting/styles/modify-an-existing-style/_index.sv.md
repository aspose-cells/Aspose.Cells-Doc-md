---
title: Modifiera en befintlig stil med C++
description: Aspose.Cells är ett C++ bibliotek för att arbeta med kalkylbladsfiler som tillåter användare att modifiera befintliga cellstilar. Denna artikel introducerar hur man ändrar en befintlig cellstil med Aspose.Cells biblioteket så att användare kan ändra utseendet på cellerna efter behov.
keywords: Modifiera befintliga stilar, anpassa utseendet på din applikation, guider, handledningar, hjälpdokumentation, utvecklingsdokumentation, API referenser, exempelkod, nedladdningar, support.
type: docs
weight: 90
url: /sv/cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

För att tillämpa samma formatering på celler, skapa ett ny formateringsstilobjekt. Ett formateringsstilobjekt är en kombination av formateringsegenskaper, såsom font, fontstorlek, indragning, nummer, kant, mönster etc., namngivet och lagrat som en uppsättning. När den appliceras tillämpas alla formatmallar i den stilen.

Du kan också använda en befintlig stil, spara den med arbetsboken och använda den för att formatera information med samma attribut.

När celler inte är explicit formaterade, tillämpas den **Normal** stilen (arbetsbokens standardstil). Microsoft Excel fördefinierar flera stilar förutom Normal-stilen, inklusive Komma, Valuta och Procent.

Aspose.Cells tillåter att modifiera någon av dessa stilar eller någon annan stil som du definierar med önskade attribut.

{{% /alert %}}

## **Använda Microsoft Excel**

För att uppdatera en stil i Microsoft Excel 97-2003:

1. På **Format**-menyn, klicka på **Stil**.
1. Välj den stil du vill modifiera från listan över **Stilnamn**.
1. Klicka på **Ändra**.
1. Välj de stilalternativ du vill använda med flikarna i dialogrutan Formatcells.
1. Klicka på **OK**.
1. Under **Stilen innehåller**, ange stilfunktionerna du vill använda.
1. Klicka på **OK** för att spara stilen och tillämpa den på det valda området.

## **Använda Aspose.Cells**

Följande exempel visar hur man använder [**Style.Update**](https://reference.aspose.com/cells/cpp/aspose.cells/style/update/)-metoden.

### **Skapa och modifiera en stil**

Detta exempel skapar ett [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)-objekt, tillämpar det på ett cellområde och modifierar [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)-objektet. Ändringarna tillämpas automatiskt på cellen och det område där stilen användes.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a workbook.
    Workbook workbook;

    // Create a new style object.
    Style style = workbook.CreateStyle();

    // Set the number format.
    style.SetNumber(14);

    // Set the font color to red color.
    style.GetFont().SetColor(Color::Red());

    // Name the style.
    style.SetName(u"Date1");

    // Get the first worksheet cells.
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Specify the style (described above) to A1 cell.
    cells.Get(u"A1").SetStyle(style);

    // Create a range (B1:D1).
    Range range = cells.CreateRange(u"B1", u"D1");

    // Initialize styleflag object.
    StyleFlag flag;

    // Set all formatting attributes on.
    flag.SetAll(true);

    // Apply the style (described above) to the range.
    range.ApplyStyle(style, flag);

    // Modify the style (described above) and change the font color from red to black.
    style.GetFont().SetColor(Color::Black());

    // Done! Since the named style (described above) has been set to a cell and range,
    // The change would be reflected (new modification is implemented) to cell (A1) and range (B1:D1).
    style.Update();

    // Save the excel file.
    U16String dataDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(dataDir + u"book_styles.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Modifiera en befintlig stil**

Detta exempel använder en enkel mall Excel-fil där en stil som heter Procent redan har tillämpats på en omfattning. Exemplet:

1. hämtar stilen,
1. skapar en stilobjekt och
1. modifierar stilformatering.

Modifieringarna tillämpas automatiskt på området där stilen applicerades.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputPath = srcDir + u"book1.xlsx";

    /*
     * Create a workbook.
     * Open a template file. 
     * In the book1.xlsx file, we have applied Ms Excel's 
     * Named style i.e., "Percent" to the range "A1:C8".
    */
    Workbook workbook(inputPath);

    // We get the Percent style and create a style object.
    Style style = workbook.GetNamedStyle(u"Percent");

    // Change the number format to "0.00%".
    style.SetNumber(11);

    // Set the font color.
    Color redColor = Color::Red();
    style.GetFont().SetColor(redColor);

    // Update the style. so, the style of range "A1:C8" will be changed too.
    style.Update();

    // Save the excel file.	
    U16String outputPath = srcDir + u"book2.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
