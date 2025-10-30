---
title: Headers oder Footers mit C++ abrufen
linktitle: Header oder Footer erhalten
type: docs
weight: 30
url: /de/cpp/get-headers-or-footers/
description: Dieser Artikel erklärt, wie man programmatisch Header und Footer aus Excel oder OpenOffice Dateien mit der C++ API oder Library abruft.
---

{{% alert color="primary" %}}

Header und Fußzeilen werden nur in der Seitenlayoutansicht, der Druckvorschau und auf gedruckten Seiten angezeigt. 

Sie können auch das Dialogfeld Seitenlayout verwenden, wenn Sie Header oder Footer für mehr als ein Arbeitsblatt gleichzeitig anzeigen möchten. 

Für andere Blatttypen wie Diagrammblätter oder Diagramme können Header und Fußzeilen nur über das Dialogfeld Seitenlayout eingefügt werden.

{{% /alert %}}

## **Header und Fußzeilen in MS Excel erhalten**
1. Klicken Sie auf das Arbeitsblatt, auf dem Sie Header oder Footer anzeigen bzw. ändern möchten.
2. Klicken Sie auf der Ansicht-Registerkarte in der Gruppe Arbeitsblattansichten auf Seitenlayout.
  Excel zeigt das Arbeitsblatt in der Seitenlayoutansicht an.
3. Klicken Sie zum Anzeigen oder Bearbeiten eines Headers oder Footers auf die linke, mittlere oder rechte Kopf- oder Fußzeile am oberen oder unteren Rand der Arbeitsblattseite (unter Kopfzeile oder über Fußzeile).


## **Headers und Footers mit Aspose.Cells for C++ abrufen**
Mit den Methoden [**Worksheet.PageSetup.GetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheader/) und [**Worksheet.PageSetup.GetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfooter/) können C++-Entwickler Header oder Footer aus der Datei einfach abrufen.

1. Arbeitsmappe erstellen, um die Datei zu öffnen.
2. Holen Sie sich das Arbeitsblatt, von dem aus Sie Header oder Footer erhalten möchten.
3. Erhält Header oder Footer mit spezifischer Abschnitts-ID.

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
    Workbook workbook(srcDir + u"HeaderFooter.xlsx");
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    std::cout << sheet.GetPageSetup().GetHeader(0).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetHeader(1).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetHeader(2).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetFooter(1).ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Kopf- und Fußzeilen zu Befehlsliste parsen**
Der Header- oder Fußzeilentext kann spezielle Befehle enthalten, zum Beispiel einen Platzhalter für die Seitenzahl, das aktuelle Datum oder Textformatierungseigenschaften.

Spezialbefehle werden durch einen einzelnen Buchstaben mit einem vorangestellten Und-Zeichen ("&") dargestellt.

Die Header- und Footer-Strings werden unter Verwendung der ABNF-Grammatik aufgebaut. Ohne Viewer ist es schwer verständlich.

Aspose.Cells for C++ stellt die [**Worksheet.PageSetup.GetCommands**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcommands/) Methode zur Verfügung, um Header und Footer als Befehlsliste zu parsen.

Der folgende Code zeigt, wie Header oder Footer als Befehlsliste geparst und Befehle verarbeitet werden:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"HeaderFooter.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get left section of header
    U16String headerSection = sheet.GetPageSetup().GetHeader(0);

    // Get commands from the header section
    Vector<HeaderFooterCommand> commands = sheet.GetPageSetup().GetCommands(headerSection);

    // Iterate through each command
    for (int i = 0; i < commands.GetLength(); ++i)
    {
        HeaderFooterCommand c = commands[i];
        switch (c.GetType())
        {
            case HeaderFooterCommandType::SheetName:
                // Embedded the name of the sheet to header or footer
                break;
            default:
                break;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
