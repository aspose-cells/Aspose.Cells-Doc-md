--- 
title: Convertir JSON a Excel con C++ 
linktitle: Convertir JSON a Excel 
type: docs 
weight: 300 
url: /es/cpp/convert-json-to-excel/ 
description: Aprende cómo convertir JSON a archivo de Excel con Aspose.Cells usando C++. 
keywords: Importar JSON sin Office 2013, Office 2016, Office 2019 y Office 365. 
--- 

{{% alert color="primary" %}} 

Aspose.Cells soporta la conversión de un archivo Json (JavaScript Object Notation) a Libro de Excel. 

{{% /alert %}} 

## **Convertir JSON a hoja de cálculo de Excel** 
No hay necesidad de preguntarse cómo convertir JSON a un archivo de Excel, porque la biblioteca Aspose.Cells for C++ tiene la mejor solución. La API de Aspose.Cells proporciona soporte para convertir el formato JSON a hojas de cálculo. Puedes usar la clase [JsonLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/jsonloadoptions/) para especificar configuraciones adicionales al importar JSON a Workbook. 

El siguiente ejemplo de código muestra la importación de JSON a un Libro de Trabajo de Excel. Por favor, vea el código para convertir el [archivo fuente](sample.json) al archivo xlsx generado por el código para referencia. 

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

El siguiente ejemplo de código, que utiliza la clase JsonLoadOptions para especificar configuraciones adicionales, demuestra la importación de JSON a una hoja de cálculo de Excel. Consulte el código para convertir [el archivo fuente](muestra.json) al archivo xlsx generado por el código como referencia. 

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

El siguiente ejemplo de código demuestra cómo importar una cadena JSON a un Libro de Excel. También puedes especificar la ubicación del diseño al importar JSON. Consulta el código para convertir la cadena JSON a un archivo xlsx generado por el código como referencia. 

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
{{< app/cells/assistant language="cpp" >}}
