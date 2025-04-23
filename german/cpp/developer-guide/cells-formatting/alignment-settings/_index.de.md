---
title: Ausrichtungseinstellungen mit C++
linktitle: Ausrichtungseinstellungen
description: In der Aspose.Cells Bibliothek können Sie Zellenausrichtungseinstellungen verwenden, um das Layout und die Anzeige von Text anzupassen. Durch die Anpassung von Einstellungen wie horizontale Ausrichtung, vertikale Ausrichtung und Textumbruch haben Sie mehr Kontrolle darüber, wie der Text in den Zellen fließt. Dieses Dokument bietet Ihnen detaillierte Schritte und Beispielcode, um schnell zu erfassen, wie Sie Aspose.Cells für Zellenausrichtungseinstellungen verwenden.
keywords: Aspose.Cells, Zellenausrichtung, horizontale Ausrichtung, vertikale Ausrichtung, Textumbruch
type: docs
weight: 20
url: /de/cpp/cells-alignment-settings/
---

## **Konfigurieren von Ausrichtungseinstellungen**

### **Ausrichtungseinstellungen in Microsoft Excel**

Jeder, der Microsoft Excel verwendet hat, um Zellen zu formatieren, wird mit den Ausrichtungseinstellungen in Microsoft Excel vertraut sein.

Wie Sie aus der obigen Abbildung sehen können, gibt es verschiedene Arten von Ausrichtungsoptionen:

- Textausrichtung (horizontal & vertikal)
- Einrückung
- Orientierung
- Textkontrolle
- Textrichtung

Alle diese Ausrichtungseinstellungen werden vollständig von Aspose.Cells unterstützt und werden im Folgenden näher erläutert.

### **Ausrichtungseinstellungen in Aspose.Cells**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) enthält eine [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) bietet eine [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-Sammlung. Jedes Element in der [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-Sammlung stellt ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) dar.

Aspose.Cells bietet Methoden zum [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) und [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/), um die Formatierung einer Zelle abzurufen und festzulegen. Die Klasse [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) stellt nützliche Eigenschaften zur Konfiguration von Ausrichtungseinstellungen bereit.

Wählen Sie einen beliebigen Textausrichtungstyp mithilfe der Aufzählung [**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/) aus. Die vordefinierten Textausrichtungstypen in der Aufzählung [**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/) lauten:

|**Textausrichtungstypen**|**Beschreibung**|
| :- | :- |
|Bottom|Stellt die untere Textausrichtung dar
|Center|Stellt die zentrale Textausrichtung dar
|CenterAcross|Stellt die zentrale überkreuzte Textausrichtung dar
|Distributed|Stellt die verteilte Textausrichtung dar
|Fill|Stellt die Fülltextausrichtung dar
|General|Stellt die allgemeine Textausrichtung dar
|Justify|Stellt die Textausrichtung als blocksatz dar
|Left|Stellt die linksbündige Textausrichtung dar
|Right|Stellt die rechtsbündige Textausrichtung dar
|Top|Stellt die obere Textausrichtung dar
|JustifiedLow|Richtet den Text mit einer angepassten Kachidalänge für arabischen Text aus.
|ThaiDistributed|Verteilt insbesondere thailändischen Text, da jeder Buchstabe als Wort behandelt wird.

{{% alert color="primary" %}}

Sie können auch die Blocksatzverteilung mit der Eigenschaft [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/cpp/aspose.cells/style/isjustifydistributed/) anwenden.

{{% /alert %}}

#### **Horizontale Ausrichtung**

Verwenden Sie die Eigenschaft [**GetHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gethorizontalalignment/) des Objekts [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/), um den Text horizontal auszurichten.

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

    // Create workbook
    Workbook workbook;

    // Obtain the reference of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Visit Aspose!");

    // Set the horizontal alignment of the text in the "A1" cell
    Style style = cell.GetStyle();
    style.SetHorizontalAlignment(TextAlignmentType::Center);
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Vertikale Ausrichtung**

Ähnlich wie bei der horizontalen Ausrichtung verwenden Sie die Eigenschaft [**GetVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getverticalalignment/) des Objekts [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/), um den Text vertikal auszurichten.

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

    // Create workbook
    Workbook workbook;

    // Clearing all the worksheets
    workbook.GetWorksheets().Clear();

    // Adding a new worksheet to the Excel object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Visit Aspose!");

    // Setting the horizontal alignment of the text in the "A1" cell
    Style style = cell.GetStyle();

    // Setting the vertical alignment of the text in a cell
    style.SetVerticalAlignment(TextAlignmentType::Center);

    cell.SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Einrückung**

Es ist möglich, den Einrückungsgrad des Textes in einer Zelle mit der [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) -Objekteigenschaft [**GetIndentLevel()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getindentlevel/) festzulegen.

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set the indentation level
    style.SetIndentLevel(2);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Ausrichtung**

Legen Sie die Ausrichtung (Rotation) des Textes in einer Zelle mit der [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) -Objekteigenschaft [**GetRotationAngle()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getrotationangle/) fest.

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add value to the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set the rotation angle of the text to 25 degrees
    style.SetRotationAngle(25);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook in Excel 97-2003 format
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Textsteuerung**

Im Folgenden wird erläutert, wie Sie Text steuern können, indem Sie Textrahmen, Anpassung an die Größe und andere Formatierungsoptionen festlegen.

##### **Textumschlag**

Das Umwickeln von Text in einer Zelle erleichtert das Lesen: Die Höhe der Zelle passt sich an, um den gesamten Text aufzunehmen, anstatt ihn abzuschneiden oder über benachbarte Zellen überlaufen zu lassen. Legen Sie das Textumwickeln mit der [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)-Objekteigenschaft [**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) ein oder aus.

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

    // Create Workbook Object
    Workbook wb;

    // Open first Worksheet in the workbook
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Get Worksheet Cells Collection
    Cells cell = ws.GetCells();

    // Increase the width of First Column Width
    cell.SetColumnWidth(0, 35);

    // Increase the height of first row
    cell.SetRowHeight(0, 36);

    // Add Text to the First Cell
    cell.Get(0, 0).PutValue(u"I am using the latest version of Aspose.Cells to test this functionality");

    // Make Cell's Text wrap
    Style style = cell.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cell.Get(0, 0).SetStyle(style);

    // Save Excel File
    wb.Save(outDir + u"WrappingText_out.xlsx");

    std::cout << "Text wrapping applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Anpassen an Größe**

Eine Option zum Umwickeln von Text in einem Feld ist das Verkleinern der Textgröße, um sich an die Abmessungen einer Zelle anzupassen. Dies erfolgt durch Festlegen der [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)-Objekteigenschaft [**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) auf **true**.

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add value to the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set shrink to fit
    style.SetShrinkToFit(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Zellen zusammenführen**

Wie Microsoft Excel unterstützt Aspose.Cells das Zusammenführen mehrerer Zellen. Aspose.Cells bietet zwei Ansätze für diese Aufgabe. Ein Weg besteht darin, die [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-Sammlungsmethode [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) aufzurufen. Die [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/)-Methode akzeptiert die folgenden Parameter zum Zusammenführen der Zellen:

- Erste Zeile: Die erste Zeile, ab der das Zusammenführen beginnt.
- Erste Spalte: Die erste Spalte, ab der das Zusammenführen beginnt.
- Anzahl der Zeilen: Die Anzahl der zu zusammenführenden Zeilen.
- Anzahl der Spalten: Die Anzahl der zu zusammenführenden Spalten.

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

    // Create a Workbook
    Workbook wbk;

    // Create a Worksheet and get the first sheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Create a Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Merge some Cells (C6:E7) into a single C6 Cell
    cells.Merge(5, 2, 2, 3);

    // Input data into C6 Cell
    worksheet.GetCells().Get(5, 2).PutValue(u"This is my value");

    // Create a Style object to fetch the Style of C6 Cell
    Style style = worksheet.GetCells().Get(5, 2).GetStyle();

    // Create a Font object
    Font font = style.GetFont();

    // Set the name
    font.SetName(u"Times New Roman");

    // Set the font size
    font.SetSize(18);

    // Set the font color
    font.SetColor(Color::Blue());

    // Bold the text
    font.SetIsBold(true);

    // Make it italic
    font.SetIsItalic(true);

    // Set the background color of C6 Cell to Red
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);

    // Apply the Style to C6 Cell
    worksheet.GetCells().Get(5, 2).SetStyle(style);

    // Save the Workbook
    wbk.Save(outDir + u"mergingcells.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Der andere Weg besteht darin, zuerst die [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-Sammlungsmethode [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) aufzurufen, um einen Bereich der zu zusammenführenden Zellen zu erstellen. Die [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/)-Methode akzeptiert denselben Satz von Parametern wie die zuvor diskutierte [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/)-Methode und gibt ein [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)-Objekt zurück. Das [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)-Objekt bietet auch eine [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/)-Methode, die den im [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)-Objekt angegebenen Bereich zusammenführt.

##### **Textausrichtung**

Es ist möglich, die Lesereihenfolge von Text in Zellen festzulegen. Die Lesereihenfolge gibt die visuelle Reihenfolge an, in der Zeichen, Wörter usw. angezeigt werden. Zum Beispiel ist Englisch eine von links nach rechts lesbare Sprache, während Arabisch eine von rechts nach links lesbare Sprache ist.

Die Lesereihenfolge wird mit der [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)-Objekteigenschaft [**GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gettextdirection/) festgelegt. Aspose.Cells bietet vordefinierte Textausrichtungstypen in der [**TextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/textdirectiontype/)-Enumeration.

|**Text Direction Types**|**Beschreibung**|
| :- | :- |
|Context|Die Lese-Reihenfolge, die mit der Sprache des ersten eingegebenen Zeichens übereinstimmt|
|LeftToRight|Lesereihenfolge von links nach rechts|
|RightToLeft|Lesereihenfolge von rechts nach links|

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"I am using the latest version of Aspose.Cells to test this functionality.");

    // Get the style of cell A1
    Style style = cell.GetStyle();

    // Set text direction to left-to-right
    style.SetTextDirection(TextDirectionType::LeftToRight);

    // Apply the modified style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(u"book1.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Erweiterte Themen**
- [Zellenausrichtung ändern und vorhandenes Format beibehalten](/cells/de/cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Zeilenumbrüche und Textumbrüche](/cells/de/cpp/line-breaks-and-text-wrapping/)
