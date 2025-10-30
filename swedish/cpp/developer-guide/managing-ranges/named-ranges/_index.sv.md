---
title: Skapa arbetsbok och kalkylblad som scope för namngivna områden med C++
linktitle: Namngivet intervall
type: docs
weight: 40
url: /sv/cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Lär dig att skapa arbetsbok och kalkylbladsscope för namngivna områden med C++ med Aspose.Cells.
---

{{% alert color="primary" %}} 

Microsoft Excel tillåter användare att definiera namngivna områden med två olika omfång: arbetsbok (också känt som globalt omfång) och arbetsblad.

- Namngivna områden med ett arbetsboksomfång kan kommas åt från vilket arbetsblad som helst inom den arbetsboken genom att helt enkelt använda dess namn.
- Arbetsbladscoped namngivna områden kommas åt med referensen till det specifika arbetsbladet där det skapades.

Aspose.Cells tillhandahåller samma funktionalitet som Microsoft Excel för att lägga till arbetsbok och arbetsbladscoped namngivna områden. Vid skapande av ett arbetsbladscoped namngivet område bör arbetsbladsreferensen användas i det namngivna området för att specificera det som ett arbetsbladscoped namngivet område.

{{% /alert %}} 

## **Lägga till ett namngivet intervall med arbetsboksuppsikt**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells from Cell A1 to C10
    Range workbookScope = cells.CreateRange(u"A1", u"C10");

    // Assign the name to workbook scope named range
    workbookScope.SetName(u"workbookScope");

    // Save the workbook
    workbook.Save(srcDir + u"WorkbookScope.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Lägg till ett namngivet område med arbetsbladomfång**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells
    Range localRange = cells.CreateRange(u"A1", u"C10");

    // Assign name to range with sheet reference
    localRange.SetName(u"Sheet1!local");

    // Save the workbook
    U16String outputFilePath = u"..\\Data\\02_OutputDirectory\\output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Fortsatta ämnen**
- [Skapa åtkomst och kopiera namngivna områden](/cells/sv/cpp/create-access-and-copy-named-ranges/)
- [Formatera och modifiera namngivna områden](/cells/sv/cpp/format-and-modify-named-ranges/)
- [Hämta intervall med externa länkar](/cells/sv/cpp/get-range-with-external-links/)
- [Implementera icke-sekventiella områden](/cells/sv/cpp/implementing-non-sequential-ranges/)

{{< app/cells/assistant language="cpp" >}}
