---
title: Excel in CSV, TSV und Txt mit C++ konvertieren
linktitle: Als CSV, TSV und Txt speichern
type: docs
weight: 40
url: /de/cpp/convert-excel-to-csv-tsv-and-txt/
description: Einfaches Konvertieren von Excel Dateien in CSV , TSV und TXT Formate mit Aspose.Cells und C++.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht die Konvertierung von Excel-, ODS-, JSON- und anderen Formatdateien in CSV, TSV und TXT.

{{% /alert %}}

## **Arbeitsmappe in Text- oder CSV-Format speichern**

Manchmal möchten Sie eine Arbeitsmappe mit mehreren Arbeitsblättern in Textformat konvertieren oder speichern. Für Textformate (zum Beispiel TXT, TabDelim, CSV usw.) speichern sowohl Microsoft Excel als auch Aspose.Cells standardmäßig nur den Inhalt des aktiven Arbeitsblatts.

Das folgende Codebeispiel erläutert, wie eine gesamte Arbeitsmappe in Textformat gespeichert werden kann. Laden Sie die Quellarbeitsmappe, die eine beliebige Microsoft Excel- oder OpenOffice-Tabellendatei sein kann (also XLS, XLSX, XLSM, XLSB, ODS usw.) mit einer beliebigen Anzahl von Tabellenblättern.

Beim Ausführen des Codes werden die Daten aller Blätter in der Arbeitsmappe in das TXT-Format konvertiert

Sie können das gleiche Beispiel anpassen, um Ihre Datei als CSV zu speichern. Standardmäßig ist [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getseparator/) ein Komma, angeben Sie also keinen Separator, wenn Sie im CSV-Format speichern.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/TxtSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Load your source workbook
    Workbook workbook(inputFilePath);

    // Text save options. You can use any type of separator
    TxtSaveOptions opts;
    opts.SetSeparator(u'\t');
    opts.SetExportAllSheets(true);

    // Save entire workbook data into file
    U16String outputFilePath = srcDir + u"out.txt";
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully as text file!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Textdateien mit benutzerdefiniertem Trennzeichen speichern**

Textdateien enthalten Tabellendaten ohne Formatierung

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/TxtSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and opening the file from its path
    Workbook workbook(filePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Specify the separator
    options.SetSeparator(u';'); // Using U16String for the char

    // Save the file with the options
    workbook.Save(srcDir + u"output.csv", options);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Erweiterte Themen**
- [Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV-Format beibehalten](/cells/de/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Führende leere Zeilen und Spalten beim Export von Tabellenkalkulationen in das CSV-Format abschneiden](/cells/de/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
