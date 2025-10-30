---
title: Entferne führende leere Zeilen und Spalten beim Exportieren von Tabellenkalkulationen im CSV Format mit C++
linktitle: Entferne führende leere Zeilen und Spalten
type: docs
weight: 100
url: /de/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Lerne, wie du führende leere Zeilen und Spalten beim Exportieren von Tabellenkalkulationen im CSV Format mit Aspose.Cells for C++ trimmen kannst.
---

## **Mögliche Verwendungsszenarien**

Manchmal enthält deine Excel- oder CSV-Datei führende leere Spalten oder Zeilen. Zum Beispiel, diese Zeile:

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Hier sind die ersten drei Zellen oder Spalten leer. Wenn Sie eine solche CSV-Datei in Microsoft Excel öffnen, verwirft Microsoft Excel diese führenden leeren Zeilen und Spalten.

Standardmäßig verwirft Aspose.Cells keine führenden leeren Spalten und Zeilen beim Speichern, aber wenn Sie sie entfernen möchten, wie es Microsoft Excel tut, bietet Aspose.Cells die [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/)-Eigenschaft. Bitte setzen Sie sie auf **true**, dann werden alle führenden leeren Zeilen und Spalten beim Speichern verworfen.

{{% alert color="primary" %}}

Vor der Veröffentlichung von Aspose.Cells for C++ 20.4 war der Standardwert von [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/) **false**. Seit der Version 20.4 ist der Standardwert von [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/) **true**.

{{% /alert %}}

## **Führende leere Zeilen und Spalten beim Export von Tabellenkalkulationen in das CSV-Format abschneiden**

Der folgende Beispielcode lädt die [Quell-Excel-Datei](sampleTrimBlankColumns.xlsx), die zwei führende leere Spalten hat. Zuerst speichert die Excel-Datei im CSV-Format ohne Änderungen und dann setzt es die [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/)-Eigenschaft auf **true** und speichert sie erneut. Der Screenshot zeigt die [Quell-Excel-Datei](sampleTrimBlankColumns.xlsx), die [Ausgabe-CSV-Datei ohne Abschneiden](outputWithoutTrimBlankColumns.csv) und die [Ausgabe-CSV-Datei mit Abschneiden](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Beispielcode**

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleTrimBlankColumns.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Save in csv format without trimming blank columns
    wb.Save(outDir + u"outputWithoutTrimBlankColumns.csv", SaveFormat::Csv);

    // Create TxtSaveOptions and set TrimLeadingBlankRowAndColumn to true
    TxtSaveOptions opts;
    opts.SetTrimLeadingBlankRowAndColumn(true);

    // Save in csv format with trimming blank columns
    wb.Save(outDir + u"outputTrimBlankColumns.csv", opts);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
