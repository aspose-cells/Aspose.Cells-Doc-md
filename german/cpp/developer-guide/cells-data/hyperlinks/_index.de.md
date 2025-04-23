---
title: Hyperlinks in Excel oder OpenOffice mit C++ einfügen
linktitle: Hyperlinks verwalten
type: docs
weight: 45
url: /de/cpp/insert-hyperlinks-to-excel/
description: So fügen Sie Hyperlinks in eine Excel Datei mit Aspose.Cells Bibliothek ohne MS Excel mit C++ ein.
keywords: Hyperlinks in Excel einfügen, Hyperlinks hinzufügen oder einfügen, Link zu einer URL hinzufügen oder einfügen, Link zu einer Zelle hinzufügen oder einfügen, Link zu einer externen Datei hinzufügen
---

{{% alert color="primary" %}} 

Ein Hyperlink wird verwendet, um eine Verknüpfung zwischen zwei Entitäten herzustellen. Jeder kennt die Verwendung von Hyperlinks, insbesondere auf Websites.
Mithilfe von Aspose.Cells können Entwickler verschiedene Arten von Hyperlinks in Microsoft Excel-Dateien erstellen. Dieses Thema erläutert, welche Arten von Hyperlinks von Aspose.Cells unterstützt werden und wie sie in unseren Excel-Dateien verwendet werden können.

{{% /alert %}} 

## **Hinzufügen von Hyperlinks**
Aspose.Cells ermöglicht es Entwicklern, Hyperlinks entweder über die API oder Designer-Tabellen (Tabellen, in denen Hyperlinks manuell erstellt und mit Aspose.Cells in andere Tabellen importiert werden) hinzuzufügen.

Aspose.Cells stellt eine Klasse, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), bereit, die eine Microsoft Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse enthält eine [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse dargestellt. Die [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse bietet verschiedene Methoden zum Hinzufügen unterschiedlicher Hyperlinks zu Excel-Dateien.

## **Hinzufügen eines Links zu einer URL**
Die [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse enthält eine [GetHyperlinks()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/) Sammlung. Jedes Element in der [GetHyperlinks()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/) Sammlung stellt einen [Hyperlink](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/) dar. Fügen Sie Hyperlinks zu URLs hinzu, indem Sie die [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/) Sammlung mit ihrer [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) Methode aufrufen. Die [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) Methode benötigt die folgenden Parameter:

- Zellname, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen im Hyperlink-Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Hyperlink-Bereich.
- URL, die URL-Adresse.

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

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a hyperlink to cell "A1"
    worksheet.GetHyperlinks().Add(u"A1", 1, 1, u"http://www.aspose.com");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

Im obigen Beispiel wird einem leeren Zellfeld **A1** ein Hyperlink zu einer URL hinzugefügt. In solchen Fällen, wenn eine Zelle leer ist, wird auch die URL-Adresse zu dieser leeren Zelle als ihr Wert hinzugefügt. Wenn die Zelle nicht leer ist und ein Hyperlink hinzugefügt wird, sieht der Wert der Zelle wie normaler Text aus. Um ihn wie einen Hyperlink aussehen zu lassen, wenden Sie die entsprechenden Formatierungseinstellungen auf diese Zelle an.

{{% /alert %}} 

## **Hinzufügen eines Links zu einer Zelle in derselben Datei**
Es ist möglich, Hyperlinks zu Zellen in derselben Excel-Datei hinzuzufügen, indem die [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/) Sammlung mit ihrer [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) Methode aufgerufen wird. Die [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) Methode funktioniert sowohl für interne als auch für externe Hyperlinks. Eine Version der überladenen Methode nimmt die folgenden Parameter:

- Zellname, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen im Hyperlink-Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Hyperlink-Bereich.
- URL, die Adresse der Zielzelle.

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the first (default) worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in
    // The same Excel file
    worksheet.GetHyperlinks().Add(u"B3", 1, 1, u"Sheet2!B9");

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Hinzufügen eines Links zu einer externen Datei**
Es ist möglich, Hyperlinks zu externen Excel-Dateien hinzuzufügen, indem die [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/) Sammlung mit ihrer [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) Methode aufgerufen wird. Die [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) Methode benötigt die folgenden Parameter:

- Zellname, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen im Hyperlink-Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Hyperlink-Bereich.
- URL, die Adresse des Ziels, externen Excel-Datei.

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

    // Add an internal hyperlink to the "A5" cell of the other worksheet "Sheet2" in the same Excel file
    worksheet.GetHyperlinks().Add(U16String(u"A5"), 1, 1, srcDir + U16String(u"book1.xls"));

    // Save the Excel file
    workbook.Save(outDir + U16String(u"output.out.xls"));

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Erweiterte Themen**
- [Bild-Hyperlinks hinzufügen](/cells/de/cpp/add-image-hyperlinks/)
- [Hyperlink-Typ erkennen](/cells/de/cpp/detect-hyperlink-type/)
- [Hyperlinks im Arbeitsblatt bearbeiten](/cells/de/cpp/editing-hyperlinks-of-worksheet/)
- [Hyperlinks im Bereich abrufen](/cells/de/cpp/get-hyperlinks-in-range/)
