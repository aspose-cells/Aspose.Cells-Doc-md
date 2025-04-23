---
title: تحويل CSV و TSV و TXT إلى Excel باستخدام C++
linktitle: تحويل CSV و TSV و TXT إلى Excel
type: docs
weight: 30
url: /ar/cpp/convert-csv-tsv-and-txt-to-excel/
description: تعلم كيفية تحويل ملفات CSV و TSV و TXT إلى Excel باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

 باستخدام Aspose.Cells for C++، يمكنك تحويل ملفات CSV إلى Excel، OpenOffice، PDF، JSON، والعديد من التنسيقات الأخرى.

{{% /alert %}}

## **فتح ملفات CSV**

ملفات القيم المفصولة بفواصل (CSV) تحتوي على سجلات تفصل بين القيم بواسطة الفاصلة. تُخزن البيانات في جدول حيث يتم فصل كل عمود بواسطة الحرف الفاصلة ويوضع بين علامتي اقتباس مزدوجتين. إذا احتوى حقل على علامة اقتباس مزدوجة، يتم الهروب منها بمزوج من علامتي اقتباس مزدوجتين. يمكنك أيضًا استخدام Microsoft Excel لتصدير بيانات الجدول إلى CSV.

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

## **فتح ملفات CSV واستبدال الأحرف غير الصالحة**

عند فتح ملف CSV في Excel، يتم استبدال الأحرف تلقائيًا. يتم هذا بواسطة API الخاص بـ Aspose.Cells أيضًا، كما هو موضح في المثال البرمجي أدناه.

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

## **باستخدام القارئ المفضل**

ليس من الضروري دائمًا استخدام إعدادات القارئ الافتراضية لفتح ملفات CSV. أحيانًا، استيراد ملف CSV لا يخلق الناتج المتوقع، مثل عندما يكون تنسيق التاريخ غير متوقع أو يتم التعامل مع الحقول الفارغة بشكل مختلف. لهذا الغرض، تتوفر خاصية **TxtLoadOptions.PreferredParsers** لتوفير قاريء مفضل خاص بك لتحليل أنواع البيانات المختلفة حسب متطلباتك. يوضح المثال التالي استخدام قارئ مفضل.

يمكن تنزيل ملف الشفرة المصدري وملفات الإخراج التجريبية من الروابط التالية لاختبار هذه الميزة.

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

### **فتح ملفات النصوص بفاصل مخصص**

تُستخدم ملفات النصوص لاحتواء البيانات الجدولية بدون تنسيق. هذا النوع من الملفات هو نوعٌ من ملفات النصوص البسيطة، وقد تحتوي على بعض محددات التجزئة المخصصة.

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

### **فتح ملفات ذات فاصل علامات التبويب**

ملفات النص المفصولة بعلامات التبويب (TSV) تحتوي على بيانات جداول بيانات ولكن بدون تنسيق. تكون البيانات مرتبة في صفوف وأعمدة كما في الجداول وبرمجيات الجدول. بشكل أساسي، فإن ملف TSV هو نوع خاص من ملفات النص العادي مع فصل بين كل عمود بعلامة تبويب.

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

### **فتح ملفات القيم المفصولة بواسطة الألسنة (TSV)**

ملفات القيم المفصولة بعلامة تبويب (TSV) تحتوي على بيانات جداول بيانات ولكن بدون تنسيق. إنها نفس نوع ملف المفصولة بعلامة تبويب حيث يتم ترتيب البيانات في صفوف وأعمدة كما في الجداول وبرمجيات الجدول.

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

## **مواضيع متقدمة**
- [تحميل أو استيراد ملف CSV مع صيغ](/cells/ar/cpp/load-or-import-csv-file-with-formulas/)
- [قراءة ملف CSV بعدة ترميزات](/cells/ar/cpp/reading-csv-file-with-multiple-encodings/)
