--- 
title: JSON in Excel mit C++ konvertieren 
linktitle: Konvertieren Sie JSON nach Excel 
type: docs 
weight: 300 
url: /de/cpp/convert-json-to-excel/ 
description: Erfahren Sie, wie Sie JSON mit Aspose.Cells und C++ in Excel Dateien umwandeln. 
keywords: Import von JSON ohne Office 2013, Office 2016, Office 2019 und Office 365. 
--- 

{{% alert color="primary" %}} 

Aspose.Cells unterstützt die Konvertierung einer Json (JavaScript Object Notation)-Datei in Excel-Arbeitsmappe. 

{{% /alert %}} 

## **Konvertieren Sie JSON in Excel-Arbeitsmappe** 
Sie müssen sich keine Sorgen machen, wie man JSON in eine Excel-Datei konvertiert, denn die Aspose.Cells for C++-Bibliothek hat die beste Lösung. Die Aspose.Cells API bietet Unterstützung für die Konvertierung von JSON-Format in Tabellenkalkulationen. Sie können die [JsonLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/jsonloadoptions/) Klasse verwenden, um zusätzliche Einstellungen für das Importieren von JSON in die Arbeitsmappe festzulegen. 

Das folgende Codebeispiel zeigt, wie man JSON in Excel-Arbeitsmappe importiert. Bitte sehen Sie sich den Code zur Konvertierung der [Quelldatei](sample.json) in die von dem Code generierte xlsx-Datei als Referenz an. 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a Workbook object from a JSON file
    Workbook workbook(u"sample.json");

    // Save the file to xlsx format
    workbook.Save(u"sample_out.xlsx");

    std::cout << "File saved successfully in xlsx format!" << std::endl;

    Aspose::Cells::Cleanup();
}
``` 

Das folgende Codebeispiel, das die Klasse JsonLoadOptions verwendet, um zusätzliche Einstellungen festzulegen, zeigt den Import von JSON in Excel-Arbeitsmappe. Bitte sehen Sie sich den Code zur Konvertierung der [Quelldatei](sample.json) in die von dem Code generierte xlsx-Datei als Referenz an. 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an options for loading the file.
    JsonLoadOptions options;

    // Indicates whether importing each attribute of JsonObject object as one worksheet when all child nodes are array nodes.
    options.SetMultipleWorksheets(true);

    // Create a workbook from the JSON file with the specified options.
    U16String inputFilePath(u"sample.json");
    Workbook book(inputFilePath, options);

    // Save file to xlsx format.
    U16String outputFilePath(u"sample_out.xlsx");
    book.Save(outputFilePath);

    std::cout << "File converted successfully to xlsx format!" << std::endl;

    Aspose::Cells::Cleanup();
}
``` 

Das folgende Codebeispiel zeigt das Importieren eines JSON-Strings in eine Excel-Arbeitsmappe. Sie können auch den Ort des Layouts beim Importieren von JSON festlegen. Bitte sehen Sie sich den Code an, um JSON-Strings in die durch den Code generierte xlsx-Datei zu konvertieren. 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // JSON input string
    U16String inputJson = uR"([
                        { BEFORE: 'before cell', TEST: 'asd1', AFTER: 'after cell' },
                        { BEFORE: 'before cell', TEST: 'asd2', AFTER: 'after cell' },
                        { BEFORE: 'before cell', TEST: 'asd3', AFTER: 'after cell' },
                        { BEFORE: 'before cell', TEST: 'asd4', AFTER: 'after cell' }
                    ])";

    U16String sheetName = u"Sheet1";
    int32_t row = 3;
    int32_t column = 2;

    // Create a Workbook object
    Workbook book;
    Worksheet worksheet = book.GetWorksheets().Get(sheetName);

    // Set JsonLayoutOptions to treat Arrays as Table
    JsonLayoutOptions jsonLayoutOptions;
    jsonLayoutOptions.SetArrayAsTable(true);

    // Import JSON data into the worksheet
    JsonUtility::ImportData(inputJson, worksheet.GetCells(), row, column, jsonLayoutOptions);

    // Save the file to xlsx format
    book.Save(u"out.xlsx");

    std::cout << "Data imported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
``` 
