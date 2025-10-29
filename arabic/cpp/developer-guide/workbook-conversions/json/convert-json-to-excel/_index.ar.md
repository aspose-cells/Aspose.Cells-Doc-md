--- 
title: تحويل JSON إلى Excel باستخدام C++ 
linktitle: تحويل JSON إلى Excel 
type: docs 
weight: 300 
url: /ar/cpp/convert-json-to-excel/ 
description: تعلم كيفية تحويل JSON إلى ملف Excel باستخدام Aspose.Cells باستخدام C++. 
keywords: استيراد json بدون مكتب 2013، مكتب 2016، مكتب 2019 ومكتب 365. 
--- 

{{% alert color="primary" %}} 

يدعم Aspose.Cells تحويل ملف Json (ترميز كائن جافا سكريبت) إلى دفتر Excel. 

{{% /alert %}} 

## **تحويل-JSON-إلى-كتاب-عمل-Excel** 
لا حاجة للقلق حول كيفية تحويل JSON إلى ملف Excel، لأن مكتبة Aspose.Cells for C++ تقدم الحل الأفضل. توفر API Aspose.Cells دعمًا لتحويل تنسيق JSON إلى جداول بيانات. يمكنك استخدام فئة [JsonLoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/jsonloadoptions/) لتحديد إعدادات إضافية لاستيراد JSON إلى دفتر العمل. 

يوضح المثال الكودي التالي استيراد JSON إلى دفتر عمل Excel. يرجى الرجوع إلى الكود الخاص بتحويل الملف المصدر إلى ملف xlsx الذي تم إنشاؤه بالكود للإحالة. 

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

يُظهر المثال التالي الذي يستخدم فئة JsonLoadOptions لتحديد إعدادات إضافية التي تظهر استيراد JSON إلى كتاب Excel. يُرجى الاطلاع على الكود لتحويل [الملف المصدر](sample.json) إلى ملف xlsx تم إنشاؤه بواسطة الكود للإشارة. 

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

يوضح المثال البرمجي التالي استيراد سلسلة JSON إلى دفتر عمل Excel. يمكنك أيضًا تحديد مكان التنسيق عند استيراد JSON. يرجى مراجعة الكود لتحويل سلسلة JSON إلى ملف xlsx الناتج بواسطة الكود. 

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
