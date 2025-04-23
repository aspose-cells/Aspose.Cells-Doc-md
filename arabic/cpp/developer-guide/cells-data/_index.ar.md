---
title: إدارة بيانات ملفات إكسل باستخدام C++
linktitle: بيانات الخلايا
type: docs
weight: 110
url: /ar/cpp/view-and-edit-excel-data/
description: تصف هذه المقالة كيفية عرض وتحرير بيانات ملفات إكسل باستخدام مكتبة Aspose.Cells باستخدام C++.
keywords: Aspose.Cells C++ إدارة بيانات ملفات إكسل، إضافة بيانات إلى ملف إكسل، الحصول على البيانات من ملف إكسل، كيفية تحسين كفاءة إضافة البيانات، إدارة بيانات الخلايا، تحديث بيانات الخلايا، الحصول على بيانات الخلايا، إدراج بيانات الخلايا
---

{{% alert color="primary" %}}

في [الوصول إلى الخلايا في ورقة العمل](/cells/ar/cpp/accessing-cells-of-a-worksheet/)، تمت مناقشة النهج الأساسي للوصول إلى الخلايا في ورقة عمل. تستخدم هذه المقالة أحد تلك النهج لإضافة أنواع مختلفة من البيانات إلى الخلايا.

{{% /alert %}}

## **كيفية إضافة بيانات إلى الخلايا**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)، التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بالفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). يمثل كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) كائنًا من الفئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

تسمح Aspose.Cells للمطورين بإضافة بيانات إلى الخلايا في ورقات العمل عن طريق استدعاء طريقة [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) لفئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). توفر Aspose.Cells إصدارات متعددة من الطريقة [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) التي تتيح للمطورين إضافة أنواع مختلفة من البيانات إلى الخلايا. باستخدام هذه الإصدارات المتعددة للطريقة [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)، يمكن إضافة قيم بوليانية، نصية، مزدوجة، صحيحة أو تاريخ / وقت،إلى الخلية.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);


    worksheet.GetCells().Get(U16String(u"A1")).PutValue(U16String(u"Hello World"));
    worksheet.GetCells().Get(U16String(u"A2")).PutValue(20.5);
    worksheet.GetCells().Get(U16String(u"A3")).PutValue((int32_t)15);
    worksheet.GetCells().Get(U16String(u"A4")).PutValue(true);

    Cell cellA1 = worksheet.GetCells().Get(U16String(u"A4"));
    Style style = cellA1.GetStyle();
    style.SetNumber(15);
    cellA1.SetStyle(style);

    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Data inserted and workbook saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **كيفية تحسين الكفاءة**

إذا استخدمت الطريقة [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) لوضع كمية كبيرة من البيانات في ورقة عمل، يجب أولاً إضافة القيم إلى الخلايا حسب الصفوف ثم حسب الأعمدة. هذا النهج يحسن بشكل كبير كفاءة تطبيقاتك.

## **كيفية استرداد البيانات من الخلايا**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تسمح بالوصول إلى أوراق العمل في الملف. تمثل ورقة العمل بالفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) يمثل كائنًا من الفئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

توفر الفئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) خصائصًا عدة تسمح للمطورين باسترداد القيم من الخلايا وفقًا لأنواع بياناتها. تتضمن هذه الخصائص:

- [**StringValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/): يعيد قيمة السلسلة للخلية.
- [**DoubleValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/): يعيد قيمة مزدوجة للخلية.
- [**BoolValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/): يعيد قيمة Boolean للخلية.
- [**DateTimeValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/): يعيد قيمة تاريخ / وقت للخلية.
- [**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/): يعيد قيمة عائمة للخلية.
- [**IntValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/): يعيد قيمة العدد الصحيح للخلية.

عندما لا يتم ملؤها، تثير الخلايا مع [**DoubleValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) أو [**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/) استثناء.

يمكن أيضًا فحص نوع البيانات الموجود في خلية باستخدام خاصية [**Type**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) لفئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) . في الواقع، تعتمد خاصية [**Type**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) لفئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) على تعداد [**CellValueType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/) والذي تم سرده أسفله:

|**أنواع قيم الخلية**|**الوصف**|
| :- | :- |
|IsBool| يحدد أن قيمة الخلية هي بولية.
|IsDateTime| يحدد أن قيمة الخلية هي تاريخ/وقت.
|IsNull| تمثل خلية فارغة.
|IsNumeric| يحدد أن قيمة الخلية هي رقمية.
|IsString| يحدد أن قيمة الخلية هي نصية.
|IsUnknown| يحدد أن قيمة الخلية غير معروفة.

يمكنك أيضًا استخدام أنواع قيم الخلية المحددة مسبقًا أعلاه للمقارنة مع نوع البيانات الحاضرة في كل خلية.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"book1.xls";

    Workbook workbook(inputFilePath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    int maxRow = worksheet.GetCells().GetMaxDataRow();
    int maxCol = worksheet.GetCells().GetMaxDataColumn();

    for (int row = 0; row <= maxRow; row++)
    {
        for (int col = 0; col <= maxCol; col++)
        {
            Cell cell = worksheet.GetCells().Get(row, col);

            U16String stringValue;
            double doubleValue = 0.0;
            bool boolValue = false;

            switch (cell.GetType())
            {
                case CellValueType::IsString:
                    stringValue = cell.GetStringValue();
                    std::cout << "String Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsNumeric:
                    doubleValue = cell.GetDoubleValue();
                    std::cout << "Double Value: " << doubleValue << std::endl;
                    break;

                case CellValueType::IsBool:
                    boolValue = cell.GetBoolValue();
                    std::cout << "Bool Value: " << boolValue << std::endl;
                    break;

                case CellValueType::IsDateTime:
                    stringValue = cell.GetStringValue();
                    std::cout << "DateTime Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsUnknown:
                    stringValue = cell.GetStringValue();
                    std::cout << "Unknown Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsNull:
                    break;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

أثناء العمل على أوراق العمل، قد يضيف المستخدمون أنواعًا مختلفة من البيانات في الخلايا. يمكن أن تشمل هذه الأنواع البيانية بولية وأعدادية ونقطية عائمة ونصية وقيم التاريخ/الوقت. باستخدام Aspose.Cells، يمكنك الحصول على القيم المناسبة من الخلايا وفقًا لأنواعها.

{{% /alert %}}

## **مواضيع متقدمة**
- [الوصول إلى الخلايا في ورقة العمل](/cells/ar/cpp/accessing-cells-of-a-worksheet/)
- [تحويل بيانات النص الرقمية إلى رقم](/cells/ar/cpp/convert-text-numeric-data-to-number/)
- [إنشاء المجاميع الفرعية](/cells/ar/cpp/creating-subtotals/)
- [تصفية البيانات](/cells/ar/cpp/data-filtering/)
- [فرز البيانات](/cells/ar/cpp/sort-data-of-excel/)
- [التحقق من البيانات](/cells/ar/cpp/data-validation/)
- [العثور على البيانات أو البحث](/cells/ar/cpp/find-or-search-data/)
- [الحصول على قيمة سلسلة الخلية بتنسيق وبدون تنسيق](/cells/ar/cpp/get-cell-string-value-with-and-without-formatting/)
- [إضافة نص فائق النص الغني HTML داخل الخلية](/cells/ar/cpp/adding-html-rich-text-inside-the-cell/)
- [إدراج الروابط التشعبية في إكسل أو أوبن أوفيس](/cells/ar/cpp/insert-hyperlinks-to-excel/)
- [كيفية استخدام العدادات وأين استخدامها](/cells/ar/cpp/how-and-where-to-use-enumerators/)
- [قياس عرض وارتفاع قيمة الخلية بوحدة البكسل](/cells/ar/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [قراءة قيم الخلية في مواضيع متعددة بشكل متزامن](/cells/ar/cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [التحويل بين اسم الخلية وفهرس الصف/العمود](/cells/ar/cpp/names-and-indices/)
- [ملء البيانات أولاً حسب الصف ثم حسب العمود](/cells/ar/cpp/populate-data-first-by-row-then-by-column/)
- [الحفاظ على بادئة اقتباس واحدة لقيمة الخلية أو النطاق](/cells/ar/cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [الوصول إلى وتحديث أجزاء النص الغني للخلية](/cells/ar/cpp/access-and-update-the-portions-of-rich-text-of-cell/)
