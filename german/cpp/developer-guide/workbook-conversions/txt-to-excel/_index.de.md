---
title: CSV, TSV und TXT in Excel konvertieren mit C++
linktitle: CSV, TSV und TXT in Excel konvertieren
type: docs
weight: 30
url: /de/cpp/convert-csv-tsv-and-txt-to-excel/
description: Erfahren Sie, wie Sie CSV , TSV und TXT Dateien mit Aspose.Cells for C++ in Excel umwandeln.
---

{{% alert color="primary" %}}

Mit Aspose.Cells for C++ können Sie CSV-Dateien in Excel, OpenOffice, PDF, JSON und viele andere Formate konvertieren.

{{% /alert %}}

## **Öffnen von CSV-Dateien**

Comma Separated Values (CSV)-Dateien enthalten Datensätze, bei denen die Werte durch Kommas getrennt sind. Die Daten werden als Tabelle gespeichert, wobei jede Spalte durch das Kommazeichen getrennt und durch doppelte Anführungszeichen eingeschlossen ist. Wenn ein Feldwert ein doppelt-anklicken Zeichen enthält, wird es mit einem Paar doppelter Anführungszeichen maskiert. Sie können auch Microsoft Excel verwenden, um Tabellenkalkulationsdaten in CSV zu exportieren.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate LoadOptions specified by the LoadFormat
    LoadOptions loadOptions4(LoadFormat::Csv);

    // Create a Workbook object and open the file from its path
    Workbook wbCSV(srcDir + u"Book_CSV.csv", loadOptions4);

    std::cout << "CSV file opened successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **CSV-Dateien öffnen und ungültige Zeichen ersetzen**

In Excel werden beim Öffnen einer CSV-Datei mit Sonderzeichen die Zeichen automatisch ersetzt. Dies wird auch von der Aspose.Cells-API durchgeführt, wie im folgenden Code-Beispiel gezeigt.

```c++
// Fix BOM issue
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String filename = srcDir + u"[20180220142533][ASPOSE_CELLS_TEST].csv";

    TxtLoadOptions options;
    options.SetSeparator(u';');
    options.SetCheckExcelRestriction(false);
    options.SetConvertNumericData(false);
    options.SetConvertDateTimeData(false);

    LoadFilter* filter = new LoadFilter(LoadDataFilterOptions::CellData);
    options.SetLoadFilter(filter);

    Workbook workbook(filename, options);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    std::cout << worksheet.GetName().ToUtf8() << std::endl;
    std::cout << worksheet.GetName().GetLength() << std::endl;
    std::cout << "CSV file opened successfully!" << std::endl;

    delete filter;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Mit bevorzugtem Parser verwenden**

Es ist nicht immer notwendig, die Standardeinstellungen für den Parser beim Öffnen von CSV-Dateien zu verwenden. Manchmal führt der Import einer CSV-Datei nicht zum erwarteten Ergebnis, z.B. wenn das Datumsformat nicht wie erwartet ist oder leere Felder anders behandelt werden. Hierfür steht **TxtLoadOptions.PreferredParsers** zur Verfügung, mit dem Sie Ihren eigenen bevorzugten Parser verwenden können, um unterschiedliche Datentypen entsprechend Ihren Anforderungen zu analysieren. Das folgende Beispiel zeigt die Verwendung eines bevorzugten Parsers.

Die Quell- und Ausgabedateien können von den folgenden Links heruntergeladen werden, um diese Funktion zu testen.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
	Aspose::Cells::Startup();

	U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
	U16String outDir(u"..\\Data\\02_OutputDirectory\\");

	TxtLoadOptions loadOptions(LoadFormat::Csv);
	loadOptions.SetSeparator(u',');
	loadOptions.SetConvertDateTimeData(true);

	Workbook workbook(srcDir + u"sample.csv", loadOptions);

	Worksheet worksheet = workbook.GetWorksheets().Get(0);
	Cells cells = worksheet.GetCells();

	Cell cell = cells.Get(u"A1");
	std::cout << "A1: " << static_cast<int>(cell.GetType())
		<< " - " << cell.GetDisplayStringValue().ToUtf8() << std::endl;

	cell = cells.Get(u"B1");
	std::cout << "B1: " << static_cast<int>(cell.GetType())
		<< " - " << cell.GetDisplayStringValue().ToUtf8() << std::endl;

	workbook.Save(outDir + u"outputsample.xlsx");

	std::cout << "OpeningCSVFilesWith executed successfully." << std::endl;

	Aspose::Cells::Cleanup();
	return 0;
}
```

### **Öffnen von Textdateien mit benutzerdefiniertem Trennzeichen**

Textdateien werden verwendet, um Tabellendaten ohne Formatierung zu halten. Die Datei ist eine Art reine Textdatei, die einige benutzerdefinierte Trennzeichen haben kann.

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

    // Path of input CSV file
    U16String filePath = srcDir + u"Book11.csv";

    // Instantiate Text File's LoadOptions
    TxtLoadOptions txtLoadOptions;

    // Specify the separator
    txtLoadOptions.SetSeparator(u',');

    // Create a Workbook object and open the file from its path
    Workbook wb(filePath, txtLoadOptions);

    // Save file
    wb.Save(outDir + u"output.txt");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Tabulator-getrennte Dateien öffnen**

Tabulator-getrennte (Text-)Dateien enthalten Tabellen und Spaltendaten, jedoch ohne Formatierung. Daten sind in Zeilen und Spalten wie in Tabellen und Tabellenkalkulationen angeordnet. Im Wesentlichen ist eine tabulator-getrennte Datei eine spezielle Art der Klartextdatei mit einem Tabulator zwischen den Spalten.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate LoadOptions specified by the LoadFormat
    LoadOptions loadOptions(LoadFormat::TabDelimited);

    // Create a Workbook object and open the file from its path
    Workbook wbTabDelimited(srcDir + u"Book1TabDelimited.txt", loadOptions);

    std::cout << "Tab delimited file opened successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Öffnen von tabstoppgetrennten Werten (TSV) Dateien**

Tabulator-separierte Werte (TSV) Dateien enthalten Tabellen- und Spaltendaten, ohne Formatierung. Es ist dasselbe wie eine tabulator-getrennte Datei, bei der Daten in Zeilen und Spalten wie in Tabellen angeordnet sind.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate LoadOptions specified by the LoadFormat
    LoadOptions loadOptions(LoadFormat::Tsv);

    // Create a Workbook object and open the file from its path
    Workbook workbook(srcDir + u"SampleTSVFile.tsv", loadOptions);

    // Using the Sheet 1 in Workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing a cell using its name
    Cell cell = worksheet.GetCells().Get(u"C3");

    // Output the cell name and value
    std::cout << "Cell Name: " << cell.GetName().ToUtf8() << " Value: " << cell.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Erweiterte Themen**
- [CSV-Datei mit Formeln laden oder importieren](/cells/de/cpp/load-or-import-csv-file-with-formulas/)
- [Lesen von CSV-Dateien mit verschiedenen Codierungen](/cells/de/cpp/reading-csv-file-with-multiple-encodings/)
