---
title: Infoga Hyperlänkar i Excel eller OpenOffice med C++
linktitle: Hantera hyperlänkar
type: docs
weight: 45
url: /sv/cpp/insert-hyperlinks-to-excel/
description: Hur man infogar hyperlänkar i Excel fil med Aspose.Cells bibliotek utan MS Excel med C++.
keywords: Infoga hyperlänkar i Excel, Lägg till eller infoga hyperlänkar, Lägg till eller infoga länk till en URL, Lägg till eller infoga en länk till en cell, Lägg till en länk till en extern fil
---

{{% alert color="primary" %}} 

En hyperlänk används för att skapa en länk mellan två enheter. Alla är bekanta med användningen av hyperlänkar, särskilt på webbplatser.
Med Aspose.Cells kan utvecklare skapa olika typer av hyperlänkar i Microsoft Excel-filer. I det här ämnet diskuteras vilka typer av hyperlänkar som stöds av Aspose.Cells och hur de kan användas i våra Excel-filer.

{{% /alert %}} 

## **Lägga till hyperlänkar**
 Aspose.Cells tillåter utvecklare att lägga till hyperlänkar i Excel-filer antingen med API:et eller diagramblad (blad där hyperlänkar skapas manuellt och Aspose.Cells används för att importera dem till andra blad).

 Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) som ger tillgång till varje kalkylblad i filen. Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) erbjuder olika metoder för att lägga till olika hyperlänkar till Excel-filer.

## **Lägga till länk till en URL**
 Klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) innehåller en samling [GetHyperlinks()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/). Varje objekt i samlingen representerar en [Hyperlink](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/). Lägg till hyperlänkar till URL:er genom att anropa metoden [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) i samlingen [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). Metoden [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) tar följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i detta hyperrlänksområde.
- URL, URL-adressen.

```cpp
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

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a hyperlink to cell "A1"
    worksheet.GetHyperlinks().Add(u"A1", 1, 1, u"http://www.aspose.com");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

I det ovanstående exemplet läggs en hyperlänk till en URL i en tom cell, **A1**. I sådana fall, om en cell är tom, läggs URL-adressen också till den tomma cellen som dess värde. Om cellen inte är tom och en hyperlänk läggs till, ser cellens värde ut som vanlig text. För att få det att se ut som en hyperlänk, använd lämpliga formateringsinställningar på den cellen.

{{% /alert %}} 

## **Lägga till en länk till en cell i samma fil**
Det är möjligt att lägga till hyperlänkar i celler i samma Excel-fil genom att anropa metoden [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) i samlingen [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). Metoden [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) fungerar för både interna och externa hyperlänkar. En version av den överlagrade metoden tar följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i detta hyperrlänksområde.
- URL, adressen till målcellen.

```cpp
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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the first (default) worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in
    // The same Excel file
    worksheet.GetHyperlinks().Add(u"B3", 1, 1, u"Sheet2!B9");

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Lägga till en länk till en extern fil**
Det är möjligt att lägga till hyperlänkar till externa Excel-filer genom att anropa metoden [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) i samlingen [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/).

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i detta hyperrlänksområde.
- URL, adressen till målet, extern Excel-fil.

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Add an internal hyperlink to the "A5" cell of the other worksheet "Sheet2" in the same Excel file
    worksheet.GetHyperlinks().Add(U16String(u"A5"), 1, 1, srcDir + U16String(u"book1.xls"));

    // Save the Excel file
    workbook.Save(outDir + U16String(u"output.out.xls"));

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Fortsatta ämnen**
- [Lägg till bildhyperlänkar](/cells/sv/cpp/add-image-hyperlinks/)
- [Identifiera hyperlänkstyp](/cells/sv/cpp/detect-hyperlink-type/)
- [Redigera hyperlänkar på arbetsbladet](/cells/sv/cpp/editing-hyperlinks-of-worksheet/)
- [Hämta hyperlänkar i omfånget](/cells/sv/cpp/get-hyperlinks-in-range/)
