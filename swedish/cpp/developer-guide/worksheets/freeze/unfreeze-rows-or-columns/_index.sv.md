---
title: Avfrosta rader eller kolumner i Excel ark med C++
linktitle: Avfrys fönster
type: docs
weight: 190
url: /sv/cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: I denna artikel lär du dig hur du avfrostar rader, kolumner eller paneler i Excel ark programmatiskt med Aspose.Cells for C++ API.
keywords: Avfrosta paneler, Avfrosta rader, Avfrosta kolumner, Avfrosta fönster.
---

## **Introduktion**

I denna artikel lär vi oss hur man avfrostar rader, kolumner och paneler i Excel-ark. Om arken i Excel-filer är frysta, vill man ibland avfostra arket eller justera frusna rader, kolumner eller paneler.

## **I Excel**

1. Klicka på **Visa** fliken > **Frys fönsterrutor** > **Koppla loss fönsterrutor**.

**![avfrysta fönster i Excel](Avfrys-Fönster.png)**

## **Avfrys rader, kolumner eller paneler med Aspose.Cells for C++**
Det är enkelt att avfrysa paneler med Aspose.Cells for C++. Använd [**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unfreezepanes/) metoden för att avfrysa paneler.

1. Bygg ett `Workbook` objekt för att öppna den frysta filen.
2. Avfrys paneler med `Worksheet.UnFreezePanes()` metoden.
3. Spara filen.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Frozen.xlsx");
    Workbook workbook(inputFilePath);

    // Unfreeze panes in the first worksheet
    workbook.GetWorksheets().Get(0).UnFreezePanes();

    // Save the modified workbook
    U16String outputFilePath(u"Unfrozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes unfrozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Bifogad [provkälla för Excel-filen](Fryst.xlsx).
