---
title: Konvertera CSV, TSV och TXT till Excel med C++
linktitle: Konvertera CSV, TSV och TXT till Excel
type: docs
weight: 30
url: /sv/cpp/convert-csv-tsv-and-txt-to-excel/
description: Lär dig att konvertera CSV , TSV och TXT filer till Excel med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Med Aspose.Cells for C++ kan du konvertera CSV-filer till Excel, OpenOffice, PDF, JSON och många andra format.

{{% /alert %}}

## **Öppning av CSV-filer**

Komma-separerade värden (CSV) filer innehåller poster där värdena separeras med kommatecken. Data lagras som en tabell där varje kolumn är separerad av kommatecknet och citerad med dubbla citattecken. Om ett fält innehåller ett dubbelt citattecken, är det undkommet med ett par dubbla citattecken. Du kan också använda Microsoft Excel för att exportera kalkylbladdata till CSV.

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

## **Öppna CSV-filer och ersätt ogiltiga tecken**

När du öppnar en CSV-fil med specialtecken i Excel, ersätts tecknen automatiskt. Samma funktion gör Aspose.Cells API, som demonstreras i kodexemplet nedan.

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

## **Använder föredragen parser**

Det är inte alltid nödvändigt att använda standardinställningar för parser när du öppnar CSV-filer. Ibland skapar import av en CSV-fil inte den förväntade utmatningen, till exempel när datumformatet inte är som förväntat eller tomma fält hanteras annorlunda. För detta ändamål finns **TxtLoadOptions.PreferredParsers** för att tillhandahålla din egen föredragna parser för att analysera olika datatyper enligt dina krav. Följande kodexempel visar användningen av en föredragen parser.

Exempelfilen och utdatafiler kan laddas ner från följande länkar för att testa denna funktion.

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

### **Öppning av Textfiler med Anpassad Separator**

Textfiler används för att hålla kalkylbladsdata utan formatering. Filen är en typ av vanlig textfil som kan ha några anpassade separatorer.

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

### **Öppna flik-begränsade filer**

Tab-begränsade (Text) filer innehåller kalkylbladsdata men utan formatering. Data är ordnade i rader och kolumner som i tabeller och kalkylblad. I princip är en tab-begränsad fil en särskild form av ren textfil med tab mellan varje kolumn.

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

### **Öppning av tabseparatorvärdefiler (TSV-filer)**

Tab-separerade värden (TSV) filer innehåller kalkylbladsdata men utan någon formatering. Det är samma som en tab-begränsad fil där data är ordnad i rader och kolumner som i tabeller och kalkylblad.

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

## **Avancerade ämnen**
- [Ladda eller importera CSV-fil med formler](/cells/sv/cpp/load-or-import-csv-file-with-formulas/)
- [Läsning av CSV-fil med flera teckentabeller](/cells/sv/cpp/reading-csv-file-with-multiple-encodings/)
{{< app/cells/assistant language="cpp" >}}
