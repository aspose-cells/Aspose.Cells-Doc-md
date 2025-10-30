--- 
title: JSON dan Excel e Dönüştürme C++ ile 
linktitle: JSON u Excel dosyasına Dönüştürme 
type: docs 
weight: 300 
url: /tr/cpp/convert-json-to-excel/ 
description: Aspose.Cells kullanarak JSON dan excel dosyasına nasıl dönüştürüleceğini C++ ile öğrenin. 
keywords: Office 2013, office 2016, office 2019 ve office 365 olmadan json içe aktarma 
--- 

{{% alert color="primary" %}} 

Aspose.Cells, Json (JavaScript Nesne Gösterimi) dosyasını Excel İş Kitabına dönüştürmeyi destekler. 

{{% /alert %}} 

## **JSON'u Excel Workbook'e dönüştür** 
JSON'u Excel dosyasına dönüştürmenin en iyi çözümünü aramaya gerek yok, çünkü Aspose.Cells for C++ kütüphanesi en iyi çözümü sunar. Aspose.Cells API'si, JSON formatını elektronik tablolara dönüştürmeyi destekler. JSON'u İş Kitabına içe aktarmak için [JsonLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/jsonloadoptions/) sınıfını kullanabilirsiniz. 

Aşağıdaki kod örneği, JSON'u Excel Çalışma Kitabına içe aktarmayı göstermektedir. Lütfen başvuru için kodu inceleyin [kaynak dosyası](örnek.json) kod tarafından oluşturulan xlsx dosyası. 

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

Ek ayarları belirtmek için JsonLoadOptions sınıfını kullanan JSON'u Excel Workbook'e içe aktarmanın bir örneğini gösteren aşağıdaki kod örneğini inceleyin. Referans için kodu görmek için [kaynak dosyayı](sample.json) kodla üretilen xlsx dosyası ile birlikte inceleyin. 

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

Aşağıdaki kod örneği, bir JSON dizesini Excel İş Kitabına içe aktarmayı gösterir. JSON içe aktarma sırasında düzenin konumunu da belirtebilirsiniz. JSON dizesini xlsx dosyasına dönüştürmek için kodu inceleyebilirsiniz. 

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
