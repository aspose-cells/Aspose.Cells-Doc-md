---
title: Ta bort namngivna områden med C++
linktitle: Ta bort namngivna områden
type: docs
weight: 90
url: /sv/cpp/delete-named-ranges/
description: Lär dig hur man tar bort definierade namn eller namngivna områden från Excel eller OpenOffice filer med Aspose.Cells for C++.
---

## **Introduktion**
Om det finns för många definierade namn eller namngivna områden i Excel-filerna måste vi rensa några så att de inte längre refereras till.

## **Ta bort namngivet område i MS Excel**

För att ta bort ett namngivet område från Excel kan du följa dessa steg:
1. Öppna Microsoft Excel och öppna arbetsboken som innehåller det namngivna området.
2. Gå till fliken "Formler" i Excel-ribbonen.
3. Klicka på knappen "Namnhanterare" i gruppen "Definierade namn". Detta öppnar dialogrutan för Namnhanterare.
4. I dialogrutan för Namnhanterare väljer du det namngivna området du vill ta bort.
5. Klicka på knappen "Ta bort". Bekräfta borttagningen vid behov.
6. Klicka på knappen "Stäng" för att stänga dialogrutan för Namnhanterare.
7. Spara arbetsboken för att behålla ändringarna.

## **Tar bort Namngivet Område med Aspose.Cells for C++**
Med Aspose.Cells for C++ kan du ta bort namngivna områden eller definierade namn via [text](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/remove/)  eller [index](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/removeat/) i listan.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete a named range by text
    worksheets.GetNames().Remove(u"NamedRange");

    // Delete a defined name by index
    worksheets.GetNames().RemoveAt(0);

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Named ranges removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Obs: om det definierade namnet hänvisas av formler kan det inte tas bort. Vi kan endast ta bort formeln för det definierade namnet.

## **Tar bort vissa namngivna områden**
När vi tar bort ett definierat namn måste vi kontrollera om det används av alla formler i filen.
För att förbättra prestandan vid borttagning av namngivna områden kan vi ta bort några tillsammans.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete some defined names
    Vector<U16String> namesToRemove = { u"NamedRange1", u"NamedRange2" };
    worksheets.GetNames().Remove(namesToRemove);

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Named ranges removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Ta bort dubbla definierade namn**
Vissa Excel-filer blir korrupta eftersom några definierade namn är duplicerade. Därför kan vi ta bort dessa duplicerade namn för att reparera filen.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete some defined names
    worksheets.GetNames().RemoveDuplicateNames();

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully after removing duplicate names!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
