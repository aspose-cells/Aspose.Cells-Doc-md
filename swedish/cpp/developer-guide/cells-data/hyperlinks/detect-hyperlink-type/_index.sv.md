---
title: Upptäck hyperlänktstyp med C++
linktitle: Upptäck hyperlänktyp
type: docs
weight: 160
url: /sv/cpp/detect-hyperlink-type/
description: Lär dig hur du upptäcker hyperlänktstyp via API n Aspose.Cells for C++.
keywords: Upptäck hyperlänkstyp, Upptäck typen av hyperlänk, Få typen av hyperlänk
---

## **Identifiera hyperlänkstyp**

En Excel-fil kan ha olika typer av hyperlänkar som externa, cellreferens, filsökväg osv. Aspose.Cells stöder funktionen att upptäcka hyperlänkstypen. Hyperlänkstyperna representeras av [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/)-uppräkningen. [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/)-uppräkningen har följande medlemmar.

- Extern: Extern länk
- Filsökväg: Lokal och full sökväg till filer/mappar.
- E-post: E-post
- Cellreferens: Länk till cell eller namnområde.

För att kontrollera hyperlänkens typ, tillhandahåller [**Hyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/)-klassen en [**LinkType**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getlinktype/)-egenskap med en returtyp av [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/). Följande kodsnutt visar användningen av [**LinkType**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getlinktype/)-egenskapen med hjälp av denna [källa excel-fil](94896195.xlsx).

### Källkod

```c++
#include <iostream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook workbook(srcDir + u"LinkTypes.xlsx");

    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    if (!worksheet)
    {
        std::cerr << "Worksheet not found!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Range range = worksheet.GetCells().CreateRange(u"A1", u"A7");
    if (!range)
    {
        std::cerr << "Range creation failed!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();


    for (int i = 0; i < hyperlinks.GetLength(); ++i)
    {
        Hyperlink link = hyperlinks[i];
        if (link)
        {
            std::cout << link.GetTextToDisplay().ToUtf8() << ": "
                << static_cast<int>(link.GetLinkType()) << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Följande är utdatan som genereras av den tidigare givna kodsnutten.

### Konsolutfall
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
