---
title: Hyperlink Typ mit C++ erkennen
linktitle: Hyperlink Typ erkennen
type: docs
weight: 160
url: /de/cpp/detect-hyperlink-type/
description: Lernen Sie, wie man den Hyperlink Typ durch die API Aspose.Cells for C++ erkennt.
keywords: Hyperlink Typ erkennen, Den Typ des Hyperlinks erkennen, Den Typ des Hyperlinks erhalten
---

## **Hyperlink-Typ erkennen**

Eine Excel-Datei kann verschiedene Arten von Hyperlinks wie externe Links, Zellverweise, Dateipfade usw. enthalten. Aspose.Cells unterstützt die Funktion, den Typ des Hyperlinks zu erkennen. Die Arten von Hyperlinks werden durch die [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/)-Aufzählung repräsentiert. Die [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/)-Aufzählung enthält die folgenden Elemente.

- Extern: Externer Link
- Dateipfad: Lokaler und vollständiger Pfad zu Dateien/Ordnern.
- E-Mail: E-Mail
- Zellverweis: Verknüpfung zu Zelle oder benanntem Bereich.

Um den Hyperlink-Typ zu überprüfen, enthält die {0}-Klasse eine Eigenschaft {1} mit einem Rückgabetyp von {2}. Der folgende Codeausschnitt veranschaulicht die Verwendung der Eigenschaft {3} anhand dieser {source excel file} (94896195.xlsx).

### Quellcode

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

Das folgende ist die Ausgabe, die durch den obigen Codeausschnitt generiert wird.

### Konsolenausgabe
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
