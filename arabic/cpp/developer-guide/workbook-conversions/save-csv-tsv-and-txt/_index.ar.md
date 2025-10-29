---
title: تحويل Excel إلى CSV و TSV و Txt باستخدام C++
linktitle: حفظ كملف CSV، TSV و Txt
type: docs
weight: 40
url: /ar/cpp/convert-excel-to-csv-tsv-and-txt/
description: تحويل ملفات Excel بسهولة إلى تنسيقات CSV و TSV و TXT باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

يجعل Aspose.Cells من الممكن تحويل ملفات Excel و ODS و JSON والتنسيقات الأخرى إلى CSV و TSV و TXT.

{{% /alert %}}

## **حفظ دفتر العمل إلى تنسيق نصي أو CSV**

في بعض الأحيان ، تريد تحويل أو حفظ دفتر عمل بعدة ورقات عمل إلى تنسيق نصي. بالنسبة لتنسيقات النص (مثل TXT، TabDelim، CSV، إلخ) ، يحفظ كل من Microsoft Excel وAspose.Cells افتراضيًا محتويات الورقة العمل النشطة فقط.

يوضح مثال الكود التالي كيفية حفظ دفتر عمل بأكمله في تنسيق نصي. يُحمّل دفتر العمل المصدري الذي يمكن أن يكون أي ملف جداول بيانات Microsoft Excel أو OpenOffice (مثل XLS وXLSX وXLSM وXLSB وODS وما إلى ذلك) مع أي عدد من ورقات العمل.

عند تنفيذ الكود ، يتم تحويل بيانات كافة الأوراق في دفتر العمل إلى تنسيق TXT.

يمكنك تعديل نفس المثال لحفظ ملفك بصيغة CSV. بشكل افتراضي، [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getseparator/) هو فاصلة، لذا لا تحدد فاصل عند الحفظ بصيغة CSV.

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

## **حفظ ملفات النص بفاصل مخصص**

تحتوي ملفات النص على بيانات جداول بيانات دون تنسيق. الملف هو نوع ملف نصي عادي يمكن أن يحتوي على بعض الفواصل المخصصة بين بياناته.

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

## **مواضيع متقدمة**
- [الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV](/cells/ar/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [تقليص الصفوف والأعمدة الخالية أثناء تصدير جداول البيانات إلى تنسيق CSV](/cells/ar/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
{{< app/cells/assistant language="cpp" >}}
