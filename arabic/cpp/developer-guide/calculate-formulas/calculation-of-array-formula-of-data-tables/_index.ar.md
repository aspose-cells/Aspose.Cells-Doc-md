---
title: حساب صيغ المصفوفة لجدول البيانات باستخدام C++
linktitle: حساب الصيغة الصفيفية لجداول البيانات
description: كيفية استخدام مكتبة Aspose.Cells لحساب صيغ المصفوفة لجدول بيانات في إكسل باستخدام C++. عن طريق تحميل ملف إكسل موجود أو إنشاء ملف جديد، يمكننا استخدام الطريقة التي تقدمها Aspose.Cells لحساب صيغة المصفوفة والحصول على النتيجة. وأخيرًا، نحفظ ملف إكسل المعدل على القرص.
keywords: Aspose.Cells، إكسل، جداول البيانات، صيغ المصفوفة، الحسابات، C++
type: docs
weight: 70
url: /ar/cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

يمكنك إنشاء جدول بيانات في Microsoft Excel باستخدام البيانات > تحليل الـ What-If > جدول البيانات. تسمح Aspose.Cells الآن بحساب الصيغة الصفيفية لجدول البيانات. يرجى استخدام [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) كالمعتاد لحساب أي نوع من الصيغ.

{{% /alert %}}

في الكود النموذجي التالي، استخدمنا الملف المصدر (ملف Excel مصدر)5115535.xlsx. إذا قمت بتغيير قيمة الخلية B1 إلى 100، ستصبح قيم جدول البيانات المحددة باللون الأصفر 120 كما هو موضح في الصور التالية. يولد الكود النموذجي الملف [PDF الناتج](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

هنا الكود النموذجي المستخدم لإنشاء الملف [PDF الناتج](5115538.pdf) من الملف المصدر (ملف Excel مصدر)5115535.xlsx. يرجى قراءة التعليقات للحصول على مزيد من المعلومات.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"DataTable.xlsx";

    // Create workbook from source excel file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
    worksheet.GetCells().Get(u"B1").PutValue(100);

    // Calculate formula, now it also calculates Data Table array formula
    workbook.CalculateFormula();

    // Save the workbook in pdf format
    workbook.Save(outDir + u"output_out.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
