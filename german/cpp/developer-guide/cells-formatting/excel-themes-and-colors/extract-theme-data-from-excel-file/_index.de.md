---
title: Thema Daten aus Excel Datei mit C++ extrahieren
linktitle: Themendaten aus Excel Datei extrahieren
description: Aspose.Cells ist eine C++ Bibliothek zur Arbeit mit Tabellenkalkulationsdateien. Sie unterstützt das Extrahieren von Design Themen Daten aus Excel Dateien, sodass Benutzer die Stil und Formatierungsinformationen von Dokumenten erhalten können. Dieser Artikel stellt vor, wie man mit der Aspose.Cells Bibliothek Design Themen Daten aus Excel Dateien extrahiert.
keywords: Aspose.Cells, Excel Datei, Themen Daten, Stil, Format
type: docs
weight: 120
url: /de/cpp/extract-theme-data-from-excel-file/
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Benutzern, themenbezogene Daten aus einer Excel-Datei zu extrahieren. Zum Beispiel können Sie den angewendeten Design-Namen des Arbeitsbuchs und die Design-Farbe, die auf eine Zelle oder die Zellrahmen angewendet wird, extrahieren.

Sie können ein Design in Ihrem Arbeitsbuch mit Microsoft Excel über den Befehl Seitenlayout > Designs anwenden.

{{% /alert %}}

## C++-Code zum Extrahieren von Design-Daten aus Excel-Dateien

Das folgende Beispiel zeigt, wie man den angewendeten Design-Namen des Quell-Arbeitsbuchs extrahiert und dann die Design-Farbe, die auf die Zelle A1 angewendet ist, sowie die Design-Farbe für die untere Zelle erforderlich sind.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"source.xlsx");

    // Extract theme name applied to this workbook
    std::cout << "Theme: " << workbook.GetTheme().ToUtf8() << std::endl;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Get the style object
    Style style = cell.GetStyle();

    // Check if theme has foreground color defined
    if (style.GetForegroundThemeColor().IsNull())
    {
        std::cout << "Theme has not foreground color defined." << std::endl;
    }
    else
    {
        // Extract theme color applied to this cell
        std::cout << "Foreground Theme Color Type: " << static_cast<int>(style.GetForegroundThemeColor().GetColorType()) << std::endl;
    }

    // Extract theme color applied to the bottom border of the cell
    Border bot = style.GetBorders().Get(BorderType::BottomBorder);
    if (bot.GetThemeColor().IsNull())
    {
        std::cout << "Theme has not Border color defined." << std::endl;
    }
    else
    {
        std::cout << "Border Theme Color Type: " << static_cast<int>(bot.GetThemeColor().GetColorType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
