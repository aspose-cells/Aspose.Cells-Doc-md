---
title: Schriftarteinstellungen mit C++
linktitle: Schriftart Einstellungen
type: docs
weight: 30
url: /de/cpp/cells-font-settings/
description: Aspose.Cells ist eine C++ Bibliothek zum Arbeiten mit Tabellenkalkulationsdateien. Es unterstützt das Festlegen der Schriftarteinstellungen von Zellen, um den Schriftstil und die Eigenschaften der Zellen anzupassen. Dieser Artikel zeigt, wie man die Aspose.Cells Bibliothek zum Einstellen der Zellenschriftart verwendet.
keywords: Aspose.Cells, Zellen, Schriftarteinstellungen, Stile, Eigenschaften
---

{{% alert color="primary" %}}

Das Aussehen und Gefühl eines Textes kann durch Ändern der Schriftarteinstellungen gesteuert werden. Die Schriftarteinstellungen können Name, Stil, Größe, Farbe und andere Effekte der Schrift umfassen. Genau wie Microsoft Excel unterstützt Aspose.Cells auch die Konfiguration der Schriftarteinstellungen der Zellen.

{{% /alert %}}

## **Konfigurieren von Schriftarteinstellungen**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) enthält eine [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung, die den Zugriff auf jede Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse stellt eine [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-Sammlung bereit. Jedes Element in der [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-Sammlung repräsentiert ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells bietet die [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-Klasse' [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) und [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)-Methoden, die verwendet werden, um den Formatierungsstil einer Zelle abzurufen und festzulegen. Die Klasse [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) bietet Eigenschaften zur Konfiguration der Schriftarteinstellungen.

### **Schriftartname festlegen**

Entwickler können jede Schriftart auf den Text in einer Zelle anwenden, indem sie die [GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/) Eigenschaft des [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)-Objekts verwenden.

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

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font name to "Times New Roman"
    style.GetFont().SetName(u"Times New Roman");

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Schriftschnitt auf Fett setzen**

Entwickler können den Text fett machen, indem sie die Eigenschaft [**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/) des Objekts [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) auf **true** setzen.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font weight to bold
    style.GetFont().SetIsBold(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Schriftgröße festlegen**

Setzen Sie die Schriftgröße mit der [**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/)-Eigenschaft des Objekts [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font size to 14
    style.GetFont().SetSize(14);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Schriftfarbe festlegen**

Verwenden Sie die [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)-Objekt’s [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/)-Eigenschaft, um die Schriftfarbe festzulegen. Wählen Sie eine Farbe aus der Enum- (Farb-)Liste (Teil des C++-Frameworks) und weisen Sie sie der [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/)-Eigenschaft zu.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font color to blue
    style.GetFont().SetColor(Color::Blue());

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```

### **Schriftart-Unterstrich-Typ festlegen**

Verwenden Sie die Eigenschaft [**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/) des Objekts [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/), um Text zu unterstreichen. Aspose.Cells bietet verschiedene vordefinierte Schriftarten-Unterstreichungstypen in der [**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/) Enumeration.

|**Schriftart-Unterstreichungstypen**|**Beschreibung**|
| :- | :- |
|Accounting|Einzelne Buchhaltungsunterstreichung|
|Double|Doppelte Unterstreichung|
|DoubleAccounting|Doppelte Buchhaltungsunterstreichung|
|None|Keine Unterstreichung|
|Single|Einfache Unterstreichung|

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

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font to be underlined
    style.GetFont().SetUnderline(FontUnderlineType::Single);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Einstellung des Durchgestrichen-Effekts**

Wenden Sie den Durchgestrichen-Effekt an, indem Sie die Eigenschaft [**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/) des Objekts [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) auf **true** setzen.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Hello Aspose!");

    Style style = cell.GetStyle();
    style.GetFont().SetIsStrikeout(true);
    cell.SetStyle(style);

    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Einstellen des Tiefgestellt-Effekts**

Wenden Sie den Tiefgestellt-Effekt an, indem Sie die Eigenschaft [**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) des Objekts [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) auf **true** setzen.

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

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Obtain the style of the cell
    Style style = cell.GetStyle();

    // Set subscript effect
    style.GetFont().SetIsSubscript(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Einstellen des Hochgestellt-Effekts auf Schriftart**

Entwickler können den Hochgestellt-Effekt auf die Schriftart anwenden, indem sie die [**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/)-Eigenschaft des [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)-Objekts auf **true** setzen.

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

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Obtain the style of the cell
    Style style = cell.GetStyle();

    // Set superscript effect
    style.GetFont().SetIsSuperscript(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Erweiterte Themen**
- [Hoch- und Tiefgestellt-Effekte auf Schriftarten anwenden](/cells/de/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [Eine Liste der in einer Arbeitsmappe oder einem Arbeitsblatt verwendeten Schriftarten abrufen](/cells/de/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
