---
title: Verschiedene Möglichkeiten, Dateien mit C++ zu speichern
linktitle: Dateien speichern
type: docs
weight: 40
url: /de/cpp/different-ways-to-save-files/
description: Aspose.Cells for C++ kann Dateien in verschiedene Formate speichern. Dateien im PDF Format speichern. Dateien im HTML Format speichern. Dateien im DOCX Format speichern. Dateien im PPTX Format speichern. Dateien im JSON Format speichern. Dateien im MHTML Format speichern.
keywords: Aspose.Cells speichert Excel in PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML und weitere Formate mit C++, speichert oder konvertiert Arbeitsmappen nach PDF, HTML, JSON, TXT, SQL in C++.
---

{{% alert color="primary" %}}

Mit Aspose.Cells ist es möglich, Dateien zu erstellen und zu speichern. Dieser Artikel erklärt die verschiedenen Möglichkeiten, wie Dateien gespeichert werden können.

{{% /alert %}}

## **Verschiedene Möglichkeiten, Dateien zu speichern**

Aspose.Cells bietet die Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Microsoft Excel-Datei darstellt und die für die Arbeit mit Excel-Dateien notwendigen Eigenschaften und Methoden bereitstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) bietet die [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-Methode, die zum Speichern von Excel-Dateien verwendet wird. Die Methode [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) hat viele Überladungen, die verwendet werden, um Dateien auf verschiedene Weisen zu speichern.

Das Dateiformat, in das die Datei gespeichert wird, wird durch die Enumeration [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) entschieden.

|**Dateiformat-Typen**|**Beschreibung**|
| :- | :- |
|CSV|Repräsentiert eine CSV-Datei|
|Excel97To2003|Stellt eine Excel 97 - 2003-Datei dar|
|Xlsx|Repräsentiert eine Excel 2007 XLSX Datei|
|Xlsm|Repräsentiert eine Excel 2007 XLSM Datei|
|Xltx|Repräsentiert eine Excel 2007 Vorlagen XLTX Datei|
|Xltm|Repräsentiert eine Excel 2007 makrofähige XLTM Datei|
|Xlsb|Repräsentiert eine Excel 2007 binäre XLSB Datei|
|SpreadsheetML|Repräsentiert eine Tabellenkalkulation XML-Datei|
|TSV|Repräsentiert eine durch Tabulatoren getrennte Werte-Datei|
|TabDelimited|Stellt eine tabulatorgetrennte Textdatei dar|
|ODS|Repräsentiert eine ODS-Datei|
|Html|Repräsentiert HTM L-Datei(en)|
|MHtml|Repräsentiert eine MHTML Datei(en)|
|Pdf|Repräsentiert eine PDF-Datei|
|XPS|Repräsentiert ein XPS-Dokument|
|TIFF|Repräsentiert das Dateiformat für markierte Bilddatei (TIFF)|

## **Wie man Datei in verschiedenen Formaten speichert**

Um Dateien an einen Speicherort zu speichern, geben Sie beim Aufrufen der Methode [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) des Objekts [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) den Dateinamen (vollständig mit Speicherpfad) und das gewünschte Dateiformat (aus der Enumeration [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)) an.

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
    U16String filePath = srcDir + u"Book1.xls";

    // Load your source workbook
    Workbook workbook(filePath);

    // Save in Excel 97 to 2003 format
    workbook.Save(outDir + u".output.xls");
    // OR
    XlsSaveOptions xlsSaveOptions;
    workbook.Save(outDir + u".output.xls", xlsSaveOptions);

    // Save in Excel2007 xlsx format
    workbook.Save(outDir + u".output.xlsx", SaveFormat::Xlsx);

    // Save in Excel2007 xlsb format
    workbook.Save(outDir + u".output.xlsb", SaveFormat::Xlsb);

    // Save in ODS format
    workbook.Save(outDir + u".output.ods", SaveFormat::Ods);

    // Save in Pdf format
    workbook.Save(outDir + u".output.pdf", SaveFormat::Pdf);

    // Save in Html format
    workbook.Save(outDir + u".output.html", SaveFormat::Html);

    // Save in SpreadsheetML format
    workbook.Save(outDir + u".output.xml", SaveFormat::SpreadsheetML);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Wie man eine Arbeitsmappe als PDF speichert**
Portable Document Format (PDF) ist ein Dokumententyp, der von Adobe in den 1990er Jahren erstellt wurde. Der Zweck dieses Dateiformats war es, einen Standard für die Darstellung von Dokumenten und anderen Referenzmaterialien in einem Format einzuführen, das unabhängig von Anwendungssoftware, Hardware sowie Betriebssystem ist. Das PDF-Dateiformat kann vollständige Informationen wie Text, Bilder, Hyperlinks, Formularfelder, Rich-Media-Inhalte, digitale Signaturen, Anhänge, Metadaten, Geodaten und 3D-Objekte enthalten, die als Teil des Quelldokuments fungieren können.

Der folgende Code zeigt, wie man eine Arbeitsmappe mit Aspose.Cells als PDF-Datei speichert:
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate the Workbook object
    Workbook workbook;

    // Set value to Cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"Hello World!");

    // Save the workbook to PDF
    workbook.Save(u"pdf1.pdf");

    // Save as Pdf format compatible with PDFA-1a
    PdfSaveOptions saveOptions;
    saveOptions.SetCompliance(PdfCompliance::PdfA1a);

    workbook.Save(u"pdfa1a.pdf", saveOptions);

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Wie man eine Arbeitsmappe im Text- oder CSV-Format speichert**

Manchmal möchten Sie eine Arbeitsmappe mit mehreren Arbeitsblättern in Textformat konvertieren oder speichern. Für Textformate (zum Beispiel TXT, TabDelim, CSV usw.) speichern sowohl Microsoft Excel als auch Aspose.Cells standardmäßig nur den Inhalt des aktiven Arbeitsblatts.

Das folgende Codebeispiel erläutert, wie eine gesamte Arbeitsmappe in Textformat gespeichert werden kann. Laden Sie die Quellarbeitsmappe, die eine beliebige Microsoft Excel- oder OpenOffice-Tabellendatei sein kann (also XLS, XLSX, XLSM, XLSB, ODS usw.) mit einer beliebigen Anzahl von Tabellenblättern.

Beim Ausführen des Codes werden die Daten aller Blätter in der Arbeitsmappe in das TXT-Format konvertiert

Sie können das gleiche Beispiel anpassen, um Ihre Datei als CSV zu speichern. Standardmäßig ist [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getseparator/) das Komma, also geben Sie keinen Trennzeichen an, wenn Sie im CSV-Format speichern. Bitte beachten Sie: Wenn Sie die Evaluierungsversion verwenden und selbst wenn die Eigenschaft [**TxtSaveOptions.GetExportAllSheets()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getexportallsheets/) auf true gesetzt ist, exportiert das Programm weiterhin nur ein Arbeitsblatt.

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

    // Path of output text file
    U16String outputFilePath = outDir + u"out.txt";

    // Load your source workbook
    Workbook workbook(inputFilePath);

    // Text save options. You can use any type of separator
    TxtSaveOptions opts;
    opts.SetSeparator(u'\t');
    opts.SetExportAllSheets(true);

    // Save entire workbook data into file
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook data saved to text file successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Wie man eine Datei in Textdateien mit benutzerdefiniertem Trennzeichen speichert**

Textdateien enthalten Tabellendaten ohne Formatierung

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and open the file from its path
    Workbook wb(filePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Specify the separator
    options.SetSeparator(u';');

    // Save the file with the options
    wb.Save(srcDir + u"output.csv", options);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Wie man eine Datei in einen Stream speichert**

Um Dateien in einen Stream zu speichern, erstellen Sie ein *MemoryStream* oder *FileStream*-Objekt und speichern Sie die Datei in diesem Stream-Objekt, indem Sie die [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-Methode des Objekts [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) aufrufen. Geben Sie das gewünschte Dateiformat mithilfe der Enumeration [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) an, wenn Sie die [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-Methode aufrufen.

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save workbook to memory stream with explicit FileFormatType
    Vector<uint8_t> data = workbook.SaveToStream();

    std::cout << "File size: " << data.GetLength() << std::endl;

    Cleanup();

    return 0;
}
```

## **Wie man eine Excel-Datei in Html- und Mht-Dateien speichert**
Aspose.Cells kann eine Excel-, JSON-, CSV- oder andere Dateien einfach als .html- und .mht-Dateien speichern.
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"Book1.xlsx");
    Workbook workbook(inputFilePath);

    // Save file to MHTML format
    U16String outputFilePath(u"out.mht");
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully to MHTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


## **Wie man eine Excel-Datei in das OpenOffice-Format (ODS, SXC, FODS, OTS) speichert**
Wir können die Dateien als OpenOffice-Format speichern: ODS, SXC, FODS, OTS usw.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"book1.xlsx");

    // Save as ods file
    workbook.Save(u"Out.ods");

    // Save as sxc file
    workbook.Save(u"Out.sxc");

    // Save as fods file
    workbook.Save(u"Out.fods");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Wie man eine Excel-Datei in JSON- oder XML-Dateien speichert**

JSON (JavaScript Object Notation) ist ein offenes Standarddateiformat zum Austausch von Daten, das menschenlesbaren Text zur Speicherung und Übertragung von Daten verwendet. JSON-Dateien werden mit der Erweiterung .json gespeichert. JSON erfordert weniger Formatierung und ist eine gute Alternative für XML. JSON leitet sich von JavaScript ab, ist jedoch ein sprachunabhängiges Datenformat. Die Generierung und Analyse von JSON wird von vielen modernen Programmiersprachen unterstützt. application/json ist der Medientyp, der für JSON verwendet wird.

Aspose.Cells unterstützt das Speichern von Dateien als JSON oder XML.

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output json file
    U16String outputFilePath = outDir + u"book1.json";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the workbook as JSON
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


## **Erweiterte Themen**
- [Anpassen des Arbeitsmappe-Komprimierungsgrads](/cells/de/cpp/adjust-workbook-compression-level/)
- [Arbeitsmappe im Strict Open XML-Tabellenkalkulationsformat speichern](/cells/de/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Speichern der Datei im Antwortobjekt](/cells/de/cpp/saving-file-to-response-object/)
