---
title: Icons, Data Bars oder Color Scales in Bedingter Formatierung mit C++ abrufen
linktitle: Icon Sets, Datenbalken oder Farbskalen Objekte abrufen
description: Aspose.Cells for C++ ist eine Bibliothek zum Arbeiten mit Tabellenkalkulationsdateien. Sie unterstützt die Verwendung von Icon Sets, Datenbalken und Farbskalen Objekten in bedingter Formatierung zur Anzeige von Daten aus Tabellenkalkulationen. Dieser Artikel beschreibt, wie die Aspose.Cells Bibliothek verwendet wird, um Daten für diese Objekte abzurufen.
keywords: Aspose.Cells, Bedingte Formatierung, Icon Set, Data Bar, Farbskala, Tabellendokument
type: docs
weight: 10
url: /de/cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/
---

{{% alert color="primary" %}} 

Manchmal müssen Sie Icon-Sets abrufen, die in der bedingten Formatierung einer Zelle oder eines Zellbereichs verwendet werden, und ein Bild basierend darauf erstellen. Sie möchten möglicherweise die in der bedingten Formatierung verwendeten Datenbalken oder Farbskalen lesen. Aspose.Cells for C++ unterstützt diese Funktion.

{{% /alert %}} 

Das folgende Codebeispiel zeigt, wie man Icon-Sets liest, die für die bedingte Formatierung verwendet werden. Mit der einfachen API von Aspose.Cells wird die Bilddaten des Icon-Sets als Bild gespeichert.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell cell = sheet.GetCells().Get(u"A1");

    // Get the conditional formatting result object
    ConditionalFormattingResult cfr = cell.GetConditionalFormattingResult();

    // Get the icon set
    ConditionalFormattingIcon icon = cfr.GetConditionalFormattingIcon();

    // Get the image data from the icon
    Vector<uint8_t> imageData = icon.GetImageData();

    // Create the image file based on the icon's image data
    ofstream outputFile((outDir + u"imgIcon.out.jpg").ToUtf8(), ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Icon image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
