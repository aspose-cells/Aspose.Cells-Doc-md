---
title: Benutzerdefinierte Dezimal und Gruppentrennzeichen für Arbeitsmappen mit C++ festlegen
linktitle: Benutzerdefinierte Dezimal und Gruppentrennzeichen spezifizieren
type: docs
weight: 110
url: /de/cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Ändern Sie Dezimal und Gruppentrennzeichen in MS Excel und mit C++ Code unter Verwendung der API Aspose.Cells for C++.
keywords: spezifiziere benutzerdefinierten Dezimaltrennzeichen in Excel, spezifiziere benutzerdefiniertes Dezimaltrennzeichen in Excel c++, spezifiere benutzerdefinierten Gruppentrennzeichen in Excel, spezifiere benutzerdefiniertes Gruppentrennzeichen in Excel c++, spezifiziere benutzerdefiniertes Dezimal und Gruppentrennzeichen in Excel, spezifiziere benutzerdefiniertes Dezimal und Gruppentrennzeichen in Excel c++, ändere Dezimal und Gruppentrennzeichen in Excel, ändere Dezimal und Gruppentrennzeichen in Excel, ändere Dezimaltrennzeichen in Excel, ändere Dezimaltrennzeichen in Excel c++, ändere Gruppentrennzeichen in Excel, ändere Gruppentrennzeichen in Excel c++
---

{{% alert color="primary" %}}

In Microsoft Excel können Sie die benutzerdefinierten Dezimal- und Tausendertrennzeichen festlegen, anstatt die Systemtrennzeichen aus den **Erweiterten Excel-Optionen** zu verwenden, wie im untenstehenden Screenshot gezeigt.

Aspose.Cells stellt die Eigenschaften [**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumberdecimalseparator/) und [**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/) zur Verfügung, um benutzerdefinierte Trennzeichen für die Formatierung/Analyse von Zahlen festzulegen.

{{% /alert %}}

## **Benutzerdefinierte Trennzeichen mit Microsoft Excel festlegen**

Der folgende Screenshot zeigt die **Erweiterten Excel-Optionen** und hebt den Abschnitt hervor, um die **Benutzerdefinierten Trennzeichen** festzulegen.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Benutzerdefinierte Trennzeichen mit Aspose.Cells festlegen**

Der folgende Beispielcode verdeutlicht, wie die benutzerdefinierten Trennzeichen mithilfe der Aspose.Cells-API festgelegt werden. Es legt die benutzerdefinierten Dezimal- und Gruppentrennzeichen als Punkt und Leerzeichen fest.

### C++ Code zur Spezifikation benutzerdefinierter Dezimal- und Gruppentrennzeichen

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

    // Specify custom separators
    workbook.GetSettings().SetNumberDecimalSeparator(u'.');
    workbook.GetSettings().SetNumberGroupSeparator(u' ');

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set cell value
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(123456.789);

    // Set custom cell style
    Style style = cell.GetStyle();
    style.SetCustom(u"#,##0.000;[Red]#,##0.000", true);
    cell.SetStyle(style);

    // Auto-fit columns
    worksheet.AutoFitColumns();

    // Save workbook as PDF
    workbook.Save(outDir + u"CustomSeparator_out.pdf");

    std::cout << "Workbook saved successfully with custom separators!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
