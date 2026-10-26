---
title: إنشاء جدول محوري
linktitle: إنشاء جدول محوري
description: إنشاء وتنسيق الجداول المحورية باستخدام Aspose.Cells for C++.
keywords: إنشاء جدول محوري, إدراج جدول محوري, تنسيق جدول محوري.
type: docs
weight: 160
url: /ar/cpp/create-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **ما هو الجدول المحوري؟**
الجدول المحوري هو تقرير ملخص تفاعلي: يختصر مجموعة كبيرة من البيانات الخام المعروضة صفًا تلو صف في مصفوفة موجزة دون الحاجة إلى أي صيغة. تختار الأعمدة التي ستصبح تسميات للصفوف، وتلك التي ستصبح تسميات للأعمدة، وتلك التي ستُجمَّع كقيم؛ ويتولى الجدول المحوري عملية التجميع والحساب:
- **التلخيص** — إجمالي المبيعات لكل منتج أو منطقة أو ربع بدلاً من سلاسل الصيغ الطويلة.
- **المقارنة** — من خلال عرض الفئات في الصفوف والفترات في الأعمدة، تتحول القائمة المسطحة إلى تقرير متقاطع تكشف فيه الاتجاهات بنظرة سريعة.
- **التنقل إلى التفاصيل** — انقر نقرًا مزدوجًا فوق أي قيمة ملخصة لفحص صفوف المصدر التي تقع خلفها.
- **التحديث** — عند تغيير بيانات المصدر، يؤدي تحديث واحد إلى إعادة حساب التقرير بالكامل.
من السيناريوهات المعتادة لوحات معلومات المبيعات، وتفصيلات المصروفات، وتحليلات المخزون، وأي سؤال من صيغة «كيف تتفصل هذه الأرقام حسب الفئة والوقت؟». في Aspose.Cells for C++، يُنشأ الجدول المحوري عبر الطريقة [PivotTableCollection.Add()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/add/) في ورقة العمل. بمجرد إنشاء الجدول المحوري، يمكنك العمل معه باستخدام فئة [PivotTable](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/).

## **إنشاء جدول محوري**
يوضح نموذج التعليمات البرمجية التالي كيفية إنشاء جدول محوري والعمل معه. يُرجى مراجعة [ملف Excel الناتج](23167010.xlsx) الذي تم إنشاؤه باستخدام هذه التعليمات البرمجية، ولقطة الشاشة التالية التي تعرض ملف Excel الناتج في Microsoft Excel.
![todo:image_alt_text](create-pivot-table_1.png)

## **نموذج التعليمات البرمجية**

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // إنشاء مصنف جديد والحصول على ورقة العمل الأولى
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // كتابة بيانات المصدر: المبيعات حسب الرياضة والربع
    cells.Get(u"A1").PutValue(u"Sport");
    cells.Get(u"B1").PutValue(u"Quarter");
    cells.Get(u"C1").PutValue(u"Sales");
    cells.Get(u"A2").PutValue(u"Golf");
    cells.Get(u"B2").PutValue(u"Qtr3");
    cells.Get(u"C2").PutValue(1500);
    cells.Get(u"A3").PutValue(u"Golf");
    cells.Get(u"B3").PutValue(u"Qtr4");
    cells.Get(u"C3").PutValue(2000);
    cells.Get(u"A4").PutValue(u"Tennis");
    cells.Get(u"B4").PutValue(u"Qtr3");
    cells.Get(u"C4").PutValue(600);
    cells.Get(u"A5").PutValue(u"Tennis");
    cells.Get(u"B5").PutValue(u"Qtr4");
    cells.Get(u"C5").PutValue(1500);
    cells.Get(u"A6").PutValue(u"Tennis");
    cells.Get(u"B6").PutValue(u"Qtr3");
    cells.Get(u"C6").PutValue(4070);
    cells.Get(u"A7").PutValue(u"Tennis");
    cells.Get(u"B7").PutValue(u"Qtr4");
    cells.Get(u"C7").PutValue(5000);
    cells.Get(u"A8").PutValue(u"Golf");
    cells.Get(u"B8").PutValue(u"Qtr3");
    cells.Get(u"C8").PutValue(6430);

    // إضافة جدول محوري في الخلية E3 الوجهة، باستخدام A1:C8 كمصدر
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"A1:C8", 2, 4);

    // تعيين حقول الجدول المحوري: الرياضة إلى الصفوف، والربع إلى الأعمدة، والمبيعات إلى البيانات
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Quarter");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");

    // حفظ المصنف
    workbook.Save(u"pivotTable_test_out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{< app/cells/assistant language="cpp" >}}