---
title: Zeilen, Spalten und Bildlaufleisten mit C++ anzeigen und ausblenden
linktitle: Zeilen, Spalten und Bildlaufleisten anzeigen und ausblenden
type: docs
weight: 20
url: /de/cpp/show-and-hide-rows-columns-and-scroll-bars/
description: Dieser Artikel demonstriert, wie man Zeilen und Spalten eines Excel Arbeitsblatts mithilfe der C++ Sprache und der Aspose.Cells API programmatisch ein und ausblendet. Die Sichtbarkeit der Bildlaufleisten kann angepasst werden, und mehrere Zeilen und Spalten können versteckt werden.
---

{{% alert color="primary" %}}

Aspose.Cells bietet Möglichkeiten, die Sichtbarkeit von Zeilen, Spalten und Bildlaufleisten eines Arbeitsblatts zu steuern.

{{% /alert %}}

## **Zeilen und Spalten anzeigen und ausblenden**

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), bereit, die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) Sammlung, die Entwicklern ermöglicht, auf jedes Arbeitsblatt in der Excel-Datei zuzugreifen. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse bietet eine [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung, die alle Zellen im Arbeitsblatt darstellt. Die [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung bietet mehrere Methoden zur Verwaltung von Zeilen oder Spalten in einem Arbeitsblatt. Einige dieser Methoden werden nachstehend erläutert.

### **Zeilen und Spalten anzeigen**

Entwickler können jede ausgeblendete Zeile oder Spalte anzeigen, indem sie die Methoden [**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/) und [**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/) der [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung jeweils aufrufen. Beide Methoden nehmen zwei Parameter:

- **Zeilen- oder Spaltenindex** - der Index einer Zeile oder Spalte, der verwendet wird, um die spezifische Zeile oder Spalte anzuzeigen.
- **Zeilenhöhe oder Spaltenbreite** - die Zeilenhöhe oder Spaltenbreite, die der Zeile oder Spalte nach dem Ausblenden zugewiesen wird.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unhiding the 3rd row and setting its height to 13.5
    worksheet.GetCells().UnhideRow(2, 13.5);

    // Unhiding the 2nd column and setting its width to 8.5
    worksheet.GetCells().UnhideColumn(1, 8.5);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Beim Anzeigen einer ausgeblendeten Spalte, wenn die zuvor zugewiesene Breite wiederhergestellt oder auf die ursprüngliche Breite gesetzt werden soll, heben Sie die Spalte mit einer negativen Breite auf. Zum Beispiel: `worksheet->GetCells()->UnhideColumn(5, -1)`.

{{% /alert %}}

### **Zeilen und Spalten ausblenden**

Entwickler können eine Zeile oder Spalte ausblenden, indem sie die Methoden [**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/) und [**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/) der [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung aufrufen. Beide Methoden nehmen den Zeilen- und Spaltenindex als Parameter, um die spezifische Zeile oder Spalte auszublenden.

```cpp
#include <iostream>
#include <memory>
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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the 3rd row of the worksheet
    worksheet.GetCells().HideRow(2);

    // Hide the 2nd column of the worksheet
    worksheet.GetCells().HideColumn(1);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Es ist auch möglich, eine Zeile oder Spalte auszublenden, indem die Zeilenhöhe oder Spaltenbreite auf 0 gesetzt wird.

{{% /alert %}}

### **Mehrere Zeilen und Spalten ausblenden**

Entwickler können mehrere Zeilen oder Spalten gleichzeitig ausblenden, indem sie die Methoden [**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/) und [**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/) der [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung aufrufen. Beide Methoden nehmen den Startindex der Zeile oder Spalte und die Anzahl der Zeilen oder Spalten, die ausgeblendet werden sollen, als Parameter.

```c++
#include <iostream>
#include <memory>
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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide 3, 4, and 5 rows in the worksheet
    worksheet.GetCells().HideRows(2, 3);

    // Hide 2 and 3 columns in the worksheet
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"outputxls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Bildlaufleisten einblenden und ausblenden**

Bildlaufleisten werden verwendet, um den Inhalt einer Datei zu durchsuchen. Normalerweise gibt es zwei Arten von Bildlaufleisten:

- Vertikale Scrollleisten
- Horizontale Scrollleisten

Microsoft Excel bietet auch horizontale und vertikale Scrollleisten an, damit Benutzer durch die Inhalte des Arbeitsblatts scrollen können. Mit Aspose.Cells können Entwickler die Sichtbarkeit beider Arten von Scrollleisten in Excel-Dateien steuern.

### **Steuerung der Sichtbarkeit von Bildlaufleisten**

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), bereit, die eine Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung einer Excel-Datei. Um die Sichtbarkeit der Bildlaufleisten zu steuern, verwenden Sie die Eigenschaften [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse, [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) und [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/). [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) und [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) sind boolesche Eigenschaften, was bedeutet, dass diese Eigenschaften nur **true** oder **false** Werte speichern können.

#### **Sichtbarkeit von Bildlaufleisten herstellen**

Setzen Sie die [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse, [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) oder [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) Eigenschaft auf **true**, um die Bildlaufleisten sichtbar zu machen.

#### **Verbergen von Bildlaufleisten**

Setzen Sie die [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse, [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) oder [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) Eigenschaft auf **false**, um die Bildlaufleisten auszublenden.

**Beispielcode**

Unten ist ein vollständiger Code, der eine Excel-Datei öffnet, `book1.xls`, beide Bildlaufleisten ausblendet und die geänderte Datei als `output.xls` speichert.

```c++
#include <iostream>
#include <fstream>
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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Hide the vertical scroll bar of the Excel file
    workbook.GetSettings().SetIsVScrollBarVisible(false);

    // Hide the horizontal scroll bar of the Excel file
    workbook.GetSettings().SetIsHScrollBarVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Scroll bars hidden successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
