---
title: تحليل سجلات Pivot المؤقتة أثناء تحميل ملف إكسل باستخدام C++
linktitle: تحليل سجلات Pivot المؤقتة
type: docs
weight: 70
url: /ar/cpp/parsing-pivot-cached-records-while-loading-excel-file/
description: تعلم كيفية تحليل سجلات Pivot المؤقتة أثناء تحميل ملفات إكسل باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

عند إنشاء جدول محوري، تقوم Microsoft Excel بنسخ البيانات المصدرية وتخزينها في ذاكرة التخزين المؤقت. تكون ذاكرة التخزين المؤقت موجودة داخل ذاكرة Microsoft Excel. لا يمكنك رؤيتها ولكن هذه هي البيانات التي يشير إليها الجدول المحوري عند بناء الجدول المحوري أو تغيير اختيار Slicer أو تحريك الصفوف/الأعمدة. يمكن لذلك Microsoft Excel أن يكون متجاوبًا جدًا مع التغييرات في الجدول المحوري ولكن يمكنه أيضًا مضاعفة حجم ملفك. بعد كل شيء، ذاكرة التخزين المؤقت مجرد نسخة مكررة من بياناتك المصدرية لذا يبدو منطقيًا أن يكون حجم ملفك مضاعف بشكل محتمل.

عندما تقوم بتحميل ملف الإكسل داخل كائن الدفتر، يمكنك أن تقرر ما إذا كنت تريد أيضًا تحميل سجلات التخزين المؤقت للجدول المحوري أم لا باستخدام خاصية [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/). القيمة الافتراضية لهذه الخاصية هي خاطئة. إذا كان تخزين المحور ضخمًا، فقد يزيد من الأداء. ولكن إذا كنت ترغب أيضًا في تحميل سجلات التخزين المؤقت للجدول المحوري، فيجب عليك ضبط هذه الخاصية على صواب.

## **تحليل السجلات المخزنة في حقول Pivot أثناء تحميل ملف Excel**

الكود العيني التالي يشرح استخدام خاصية [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/). يقوم بتحميل ملف الإكسل العيني مع تحليل السجلات المخزنة المحوري ثم يقوم بتحديث الجدول المحوري وحفظه كملف إكسل جديد.

## **الكود المثالي**

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

    // Create load options
    LoadOptions options;

    // Set ParsingPivotCachedRecords true, default value is false
    options.SetParsingPivotCachedRecords(true);

    // Load the sample Excel file containing pivot table cached records
    U16String inputFilePath = srcDir + u"sampleParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx";
    Workbook wb(inputFilePath, options);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first pivot table
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Set refresh data flag true
    pt.SetRefreshDataFlag(true);

    // Refresh and calculate pivot table
    pt.RefreshData();
    pt.CalculateData();

    // Set refresh data flag false
    pt.SetRefreshDataFlag(false);

    // Save the output Excel file
    U16String outputFilePath = outDir + u"outputParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Pivot table cached records parsed and refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
