--- 
title: Converti JSON in Excel con C++ 
linktitle: Converti JSON in Excel 
type: docs 
weight: 300 
url: /it/cpp/convert-json-to-excel/ 
description: Impara come convertire un file json in file excel con Aspose.Cells usando C++. 
keywords: Importare JSON senza Office 2013, Office 2016, Office 2019 e Office 365. 
--- 

{{% alert color="primary" %}} 

Aspose.Cells supporta la conversione di un file Json (JavaScript Object Notation) in Workbook Excel. 

{{% /alert %}} 

## **Converti JSON in Excel Workbook** 
Non c'è bisogno di chiedersi come convertire JSON in un file Excel, perché la libreria Aspose.Cells for C++ ha la soluzione migliore. L'API Aspose.Cells supporta la conversione del formato JSON in fogli di calcolo. Puoi usare la classe [JsonLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/jsonloadoptions/) per specificare impostazioni aggiuntive durante l'importazione di JSON in Workbook. 

Il seguente esempio di codice dimostra l'importazione del JSON nel foglio di lavoro di Excel. Si prega di vedere il codice per convertire il [file di origine](sample.json) nel file xlsx generato dal codice a titolo di riferimento. 

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

L'esempio di codice seguente che utilizza la classe JsonLoadOptions per specificare impostazioni aggiuntive dimostra l'importazione di JSON in Excel Workbook. Si prega di consultare il codice per convertire [file di origine](sample.json) nel file xlsx generato dal codice per riferimento. 

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

Il seguente esempio di codice mostra come importare una stringa JSON in un Workbook Excel. È possibile anche specificare la posizione del layout durante l'importazione di JSON. Consulta il codice per convertire la stringa JSON nel file xlsx generato come riferimento. 

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
