---
title: Füll Einstellungen mit C++
linktitle: Füllungseinstellungen
description: Aspose.Cells ist eine C++ Bibliothek zum Arbeiten mit Tabellenkalkulationsdateien. Es unterstützt das Festlegen der Fülloptionen von Zellen, sodass Benutzer den Hintergrund und den Stil der Zellen anpassen können. Dieser Artikel führt ein, wie man die Aspose.Cells Bibliothek zum Festlegen der Fülloptionen von Zellen benutzt.
keywords: Aspose.Cells, Zellen, Fülleinstellungen, Hintergrund, Stil
type: docs
weight: 50
url: /de/cpp/cells-fill-settings/
---

## **Farben und Hintergrundmuster**

Microsoft Excel kann die Vordergrund- (Rahmen) und Hintergrundfarben (Fülle) von Zellen sowie Hintergrundmuster festlegen.

Aspose.Cells unterstützt diese Funktionen ebenfalls in flexibler Weise. In diesem Thema lernen wir, diese Funktionen mit Aspose.Cells zu verwenden.

### **Einstellen von Farben und Hintergrundmustern**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) enthält eine [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung, die den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) bietet eine [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung repräsentiert ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Die Klasse [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) verfügt über die Methoden [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) und [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/), die zur Abfrage und Änderung der Formatierung einer Zelle verwendet werden. Die Klasse [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) stellt Eigenschaften zur Festlegung der Vordergrund- und Hintergrundfarben der Zellen bereit. Aspose.Cells bietet eine Enumeration [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/), die eine Reihe von vordefinierten Arten von Hintergrundmustern enthält, die unten aufgeführt sind.

|**Hintergrundmuster**|**Beschreibung**|
| :- | :- |
|DiagonalCrosshatch|: Stellt das diagonale Kreuzmuster dar
|DiagonalStripe|: Stellt das diagonale Streifenmuster dar
|Gray6|: Stellt das 6,25%-graue Muster dar
|Gray12|: Stellt das 12,5%-graue Muster dar
|Gray25|: Stellt das 25%-graue Muster dar
|Gray50|: Stellt das 50%-graue Muster dar
|Gray75|: Stellt das 75%-graue Muster dar
|HorizontalStripe|: Stellt das horizontale Streifenmuster dar
|None|: Stellt keinen Hintergrund dar
|ReverseDiagonalStripe|: Stellt das umgekehrte diagonale Streifenmuster dar
|Solid|: Stellt das einfarbige Muster dar
|ThickDiagonalCrosshatch|: Stellt das dicke diagonale Kreuzmuster dar
|ThinDiagonalCrosshatch|: Stellt das dünnere diagonale Kreuzmuster dar
|ThinDiagonalStripe|: Stellt das dünnere diagonale Streifenmuster dar
|ThinHorizontalCrosshatch|: Stellt das dünnere horizontale Kreuzmuster dar
|ThinHorizontalStripe|: Stellt das dünnere horizontale Streifenmuster dar
|ThinReverseDiagonalStripe|Stellt ein dünn umgekehrtes diagonales Streifenmuster dar|
|ThinVerticalStripe|Stellt ein dünn vertikales Streifenmuster dar|
|VerticalStripe|Stellt ein vertikales Streifenmuster dar|

Im folgenden Beispiel ist die Vordergrundfarbe der Zelle A1 festgelegt, aber A2 ist so konfiguriert, dass sowohl Vordergrund- als auch Hintergrundfarben mit einem vertikalen Streifenmuster hinterlegt sind.

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Define a Style and get the A1 cell style
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    // Setting the foreground color to yellow
    style.SetForegroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A1 cell
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    // Get the A2 cell style
    style = worksheet.GetCells().Get(u"A2").GetStyle();

    // Setting the foreground color to blue
    style.SetForegroundColor(Color::Blue());

    // Setting the background color to yellow
    style.SetBackgroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A2 cell
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Wichtig zu wissen**

{{% alert color="primary" %}}

- Verwenden Sie zum Festlegen der Vordergrund- oder Hintergrundfarbe einer Zelle die Eigenschaften [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) oder [**GetBackgroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundcolor/) des Objekts [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Beide Eigenschaften werden nur wirksam, wenn die Eigenschaft [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) des Objekts [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) konfiguriert ist.
- Die Eigenschaft [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) legt die Schattierungsfarbe der Zelle fest.
  Die Eigenschaft [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) legt den Typ des Hintergrundmusters fest, das für die Vordergrund- oder Hintergrundfarbe verwendet wird. Aspose.Cells bietet eine Aufzählung, [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/), die eine Reihe von vordefinierten Arten von Hintergrundmustern enthält.
- Wenn Sie den Wert *BackgroundType.None* aus der Aufzählung [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/) auswählen, wird die Vordergrundfarbe nicht angewendet.
  - Ebenso wird die Hintergrundfarbe nicht angewendet, wenn Sie die Werte *BackgroundType.None* oder *BackgroundType.Solid* auswählen.
- Beim Abrufen der Schattierungs-/Füllfarbe der Zelle gibt [**Style.GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) *Color.Empty* zurück, wenn [**Style.GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) *BackgroundType.None* ist.

{{% /alert %}}

### **Anwendung von Verlaufsfülleffekten**

Verwenden Sie zum Anwenden Ihrer gewünschten Verlaufsfülleffekte auf die Zelle die Methode [**SetTwoColorGradient**](https://reference.aspose.com/cells/cpp/aspose.cells/style/settwocolorgradient/) des Objekts [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) entsprechend.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::System;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(2, 1).PutValue(u"test");

    Cell cell = worksheet.GetCells().Get(u"B3");
    Style style = cell.GetStyle();
    style.SetIsGradient(true);
    style.SetTwoColorGradient(
        Color{ 0xFF, 0xFF, 0xFF, 0xFF },
        Color{ 0xFF, 0x4F, 0x81, 0xBD },
        GradientStyleType::Horizontal,
        1
    );

    style.GetFont().SetColor(Color::Red());
    style.SetHorizontalAlignment(TextAlignmentType::Center);
    style.SetVerticalAlignment(TextAlignmentType::Center);

    cell.SetStyle(style);

    worksheet.GetCells().SetRowHeightPixel(2, 53);
    worksheet.GetCells().Merge(2, 1, 1, 2);

    workbook.Save(outDir + u"output.xlsx");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Farben und Palette**

Eine Palette ist die Anzahl der verfügbaren Farben zur Erstellung eines Bildes. Die Verwendung einer standardisierten Palette in einer Präsentation ermöglicht es dem Benutzer, ein konsistentes Erscheinungsbild zu erstellen. Jede Microsoft Excel (97-2003)-Datei hat eine Palette von 56 Farben, die auf Zellen, Schriften, Gitterlinien, grafische Objekte, Füllungen und Linien in einem Diagramm angewendet werden können.

Mit Aspose.Cells ist es möglich, nicht nur die vorhandenen Farben der Palette zu verwenden, sondern auch benutzerdefinierte Farben. Bevor Sie eine benutzerdefinierte Farbe verwenden, fügen Sie diese zunächst der Palette hinzu.

In diesem Thema wird erläutert, wie benutzerdefinierte Farben zur Palette hinzugefügt werden.

### **Hinzufügen von benutzerdefinierten Farben zur Palette**

Aspose.Cells unterstützt Microsoft Excels 56-Farben-Palette. Um eine benutzerdefinierte Farbe zu verwenden, die in der Palette nicht definiert ist, fügen Sie die Farbe der Palette hinzu.

Aspose.Cells stellt eine Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) bereit, die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) bietet eine Methode [**ChangePalette**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/changepalette/), die die folgenden Parameter verwendet, um eine benutzerdefinierte Farbe zur Modifizierung der Palette hinzuzufügen:

- Benutzerdefinierte Farbe, die benutzerdefinierte Farbe, die hinzugefügt werden soll.
- Index, der Index der Farbe in der Palette, die die benutzerdefinierte Farbe ersetzen wird. Sollte zwischen 0-55 liegen.

Das folgende Beispiel fügt eine benutzerdefinierte Farbe (Orchid) zur Palette hinzu, bevor sie auf eine Schriftart angewendet wird.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Check if Orchid color is in the palette
    std::cout << "Is Orchid in palette: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add Orchid color to the palette at index 55
    workbook.ChangePalette(Color::Orchid(), 55);

    // Verify if Orchid color is now in the palette
    std::cout << "Is Orchid in palette after change: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add a new worksheet
    int i = workbook.GetWorksheets().Add();

    // Get the reference to the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"Hello Aspose!");

    // Create a new style
    Style styleObject = workbook.CreateStyle();

    // Set the custom color (Orchid) to the font
    styleObject.GetFont().SetColor(workbook.GetColors()[55]);

    // Apply the style to the cell
    cell.SetStyle(styleObject);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Die Palette bietet Platz für nur 56 Farben. Wenn Sie eine benutzerdefinierte Farbe zur Palette hinzufügen, wird die Palette geändert und jedes Element in der Datei, das zuvor mit der Farbe formatiert wurde, wird geändert. Wenn Sie also die Palette ändern, seien Sie bitte sehr vorsichtig. Außerdem handelt es sich hierbei ausschließlich um eine Einschränkung im XLS (Excel 97 - 2003) Dateiformat, da es für XLSX oder andere fortgeschrittene MS Excel (2007/2010 oder 2013) Dateiformate keine solche Einschränkung gibt.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
