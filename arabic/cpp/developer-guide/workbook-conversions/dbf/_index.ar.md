---
title: قراءة وكتابة ملفات DBF
description: Aspose.Cells هي مكتبة C++ للعمل مع ملفات جداول البيانات، وتدعم قراءة وكتابة ملفات dBASE III وIV (DBF). تشرح هذه المقالة كيفية استيراد البيانات من وتصدير البيانات إلى ملفات DBF باستخدام Aspose.Cells، بما في ذلك تفاصيل تنسيق الملف والميزات المدعومة والأمثلة خطوة بخطوة.
keywords: Aspose.Cells, C++ library, DBF, dBASE, read DBF, write DBF, import DBF, export DBF, file format, .dbf
type: docs
weight: 200
url: /ar/cpp/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

يوفر Aspose.Cells دعمًا كاملاً لقراءة وكتابة ملفات DBF (dBASE). يمكنك تحميل ملفات dBASE III وdBASE IV الموجودة في كائن Workbook، ومعالجة البيانات باستخدام واجهة برمجة التطبيقات الغنية الخاصة بـ Aspose.Cells، ثم حفظ المصنف مرة أخرى بتنسيق DBF للاستخدام مع تطبيقات قواعد البيانات القديمة.

{{% /alert %}}

## **مقدمة**

DBF (DataBase File) هو تنسيق ملف قاعدة بيانات قديم تم تقديمه في الأصل بواسطة dBASE في أوائل الثمانينيات. على الرغم من قدم هذا التنسيق، لا تزال ملفات DBF مستخدمة على نطاق واسع في العديد من الصناعات لتخزين البيانات المنظمة، لا سيما في المحاسبة ونظم المعلومات الجغرافية (GIS) والتطبيقات المتخصصة الأخرى. يتيح لك Aspose.Cells دمج هذه الملفات القديمة بسلاسة في سير العمل الحديث لجداول البيانات بلغة C++.

تدعم المكتبة كلاً من قراءة وكتابة ملفات DBF، مما يمنحك القدرة على:

- استيراد البيانات من ملفات DBF الموجودة إلى كائنات Workbook الخاصة بـ Aspose.Cells لمزيد من المعالجة أو التحويل إلى تنسيقات أخرى.
- إنشاء ملفات DBF جديدة من الصفر أو عن طريق تحويل البيانات من تنسيقات جداول البيانات الأخرى.
- الحفاظ على تعريفات الحقول وأنواع البيانات وهياكل السجلات عند نقل البيانات من وإلى تنسيق DBF.

يمكن أيضًا فتح ملفات DBF مباشرة في Microsoft Excel وتطبيقات جداول البيانات الأخرى، مما يجعلها جسرًا ملائمًا بين الأنظمة القديمة وأدوات جداول البيانات الحديثة.

## **إصدارات وميزات DBF المدعومة**

يدعم Aspose.Cells إصدارات تنسيق DBF التالية:

- **dBASE III** — الصيغة الأصلية والأكثر دعمًا على نطاق واسع من تنسيق DBF.
- **dBASE IV** — نسخة موسعة تدعم أنواع بيانات إضافية وأحجام حقول أكبر.

### الميزات المدعومة

توفر المكتبة دعمًا شاملاً للعمليات التالية:

- قراءة بيانات DBF في كائن Workbook، مع الحفاظ على جميع السجلات وتعريفات الحقول.
- كتابة بيانات المصنف مرة أخرى بتنسيق DBF للتصدير إلى التطبيقات المتوافقة مع dBASE.
- التعامل مع أنواع البيانات الشائعة المستخدمة في ملفات DBF، بما في ذلك الحقول النصية والرقمية والتاريخية والمنطقية.
- الحفاظ على تعريفات الحقول مثل اسم الحقل ونوعه وطوله أثناء عمليات القراءة/الكتابة.

### القيود والاعتبارات

عند العمل مع ملفات DBF، يجب مراعاة القيود التالية:

- الحد الأقصى لعدد الحقول في الملف الواحد هو **128**.
- الحد الأقصى لحجم السجل هو **4000 بايت**.
- أسماء الحقول محدودة بـ **10 أحرف**، ويجب أن تكون بأحرف كبيرة، ولا يمكن أن تحتوي على مسافات.
- يتم تخزين قيم التاريخ في ملفات DBF بتنسيق `YYYYMMDD`.
- قد يختلف ترميز الأحرف حسب التطبيق المصدر (شائعًا Windows-1252 أو صفحات الرموز OEM).

## **قراءة ملف DBF**

يجعل Aspose.Cells عملية تحميل البيانات من ملف DBF في كائن Workbook أمرًا بسيطًا ومباشرًا. تستخدم المكتبة الفئة `LoadOptions` لتحديد تنسيق المصدر، مما يضمن تفسير البيانات بشكل صحيح أثناء عملية التحميل.

### قراءة ملف DBF باستخدام Aspose.Cells

لقراءة ملف DBF، تحتاج إلى إنشاء مثيل من `LoadOptions`، وتعيين خاصية `LoadFormat` الخاصة به إلى `LoadFormat.Dbf`، وتمريره إلى مُنشئ `Workbook` مع مسار الملف. بمجرد التحميل، تصبح البيانات قابلة للوصول من خلال مجموعة `Worksheets`، حيث يمكنك التنقل عبر الخلايا واستخراج القيم ومعالجة البيانات حسب الحاجة.

يوضح المثال التالي كيفية تحميل ملف DBF موجود في Aspose.Cells، والوصول إلى ورقة العمل الأولى الخاصة به، وقراءة قيم الخلايا.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "Data/";
    std::string filePath = dataDir + "example.dbf";

    LoadOptions loadOptions(LoadFormat::Dbf);

    Workbook workbook(U16String(filePath.c_str()), loadOptions);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cells cells = worksheet.GetCells();

    std::string sb = "";

    int maxRow = cells.GetMaxDataRow();
    int maxCol = cells.GetMaxDataColumn();

    for (int i = 0; i <= maxRow; i++) {
        for (int j = 0; j <= maxCol; j++) {
            Cell cell = cells.Get(i, j);
            U16String value = cell.GetStringValue();
            sb += "|";
            sb += value.ToUtf8();
        }
        sb += "|";
        sb += "\n";
    }

    std::cout << sb << std::endl;

    std::string outputPath = dataDir + "output.xlsx";
    workbook.Save(U16String(outputPath.c_str()), SaveFormat::Xlsx);

    std::cout << "DBF file loaded successfully. Converted XLSX saved at: " << outputPath << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

يمكنك فتح ملفات DBF مباشرة في Microsoft Excel عن طريق تحديد الملف في مربع الحوار "فتح". سيعامل Excel ملف DBF كجدول بيانات، ويعرض سجلاته في تخطيط جدولي. يعد هذا مفيدًا للتحقق السريع من البيانات بعد قراءتها أو كتابتها باستخدام Aspose.Cells.

{{% /alert %}}

## **كتابة ملف DBF**

تتبع كتابة البيانات في ملف DBF نمطًا مشابهًا لحفظ أي تنسيق جدول بيانات آخر باستخدام Aspose.Cells. يمكنك إنشاء مصنف أو تحميله، وتعبئة ورقة العمل بالبيانات، ثم استدعاء طريقة `Save` مع تحديد `SaveFormat.Dbf` كتنسيق الهدف.

### كتابة ملف DBF باستخدام Aspose.Cells

لإنشاء ملف DBF، اتبع الخطوات التالية:

1. أنشئ مثيلًا جديدًا من `Workbook`.
2. الوصول إلى ورقة العمل الأولى من مجموعة `Worksheets`.
3. تعبئة ورقة العمل ببياناتك، بما في ذلك الرؤوس في الصف الأول والسجلات في الصفوف اللاحقة.
4. استدعاء طريقة `Workbook.Save`، وتمرير مسار الملف و `SaveFormat.Dbf` كمعلمات.

يوضح المثال التالي كيفية إنشاء ملف DBF جديد من الصفر. حيث يقوم بتعبئة ورقة العمل ببيانات نموذجية تحتوي على أنواع بيانات مختلفة (نصوص وأرقام وتواريخ) لتوضيح كيفية التعامل مع أنواع الحقول عند التصدير إلى تنسيق DBF.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string outputDir = "C:/Output/";
    std::string filePath = outputDir + "output.dbf";

    if (!std::filesystem::exists(outputDir)) {
        std::filesystem::create_directories(outputDir);
    }

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // رؤوس الأعمدة
    cells.Get(0, 0).PutValue(u"ID");
    cells.Get(0, 1).PutValue(u"Name");
    cells.Get(0, 2).PutValue(u"Department");
    cells.Get(0, 3).PutValue(u"Salary");
    cells.Get(0, 4).PutValue(u"HireDate");

    // صف البيانات 1
    cells.Get(1, 0).PutValue(101);
    cells.Get(1, 1).PutValue(u"John Smith");
    cells.Get(1, 2).PutValue(u"Engineering");
    cells.Get(1, 3).PutValue(75000.50);
    Date hireDate1{2020, 3, 15, 0, 0, 0, 0};
    cells.Get(1, 4).PutValue(hireDate1);

    // صف البيانات 2
    cells.Get(2, 0).PutValue(102);
    cells.Get(2, 1).PutValue(u"Jane Doe");
    cells.Get(2, 2).PutValue(u"Marketing");
    cells.Get(2, 3).PutValue(68000.75);
    Date hireDate2{2019, 7, 22, 0, 0, 0, 0};
    cells.Get(2, 4).PutValue(hireDate2);

    // صف البيانات 3
    cells.Get(3, 0).PutValue(103);
    cells.Get(3, 1).PutValue(u"Bob Johnson");
    cells.Get(3, 2).PutValue(u"Finance");
    cells.Get(3, 3).PutValue(82000.00);
    Date hireDate3{2021, 1, 10, 0, 0, 0, 0};
    cells.Get(3, 4).PutValue(hireDate3);

    // صف البيانات 4
    cells.Get(4, 0).PutValue(104);
    cells.Get(4, 1).PutValue(u"Alice Brown");
    cells.Get(4, 2).PutValue(u"Human Resources");
    cells.Get(4, 3).PutValue(71000.25);
    Date hireDate4{2018, 11, 5, 0, 0, 0, 0};
    cells.Get(4, 4).PutValue(hireDate4);

    // صف البيانات 5
    cells.Get(5, 0).PutValue(105);
    cells.Get(5, 1).PutValue(u"Charlie Wilson");
    cells.Get(5, 2).PutValue(u"Operations");
    cells.Get(5, 3).PutValue(79500.80);
    Date hireDate5{2022, 5, 30, 0, 0, 0, 0};
    cells.Get(5, 4).PutValue(hireDate5);

    // تعيين عرض الأعمدة لسهولة القراءة
    worksheet.GetCells().SetColumnWidth(0, 8);
    worksheet.GetCells().SetColumnWidth(1, 20);
    worksheet.GetCells().SetColumnWidth(2, 20);
    worksheet.GetCells().SetColumnWidth(3, 12);
    worksheet.GetCells().SetColumnWidth(4, 14);

    workbook.Save(U16String(filePath.c_str()), SaveFormat::Dbf);

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

عند كتابة البيانات في ملف DBF، تأكد من أن بياناتك تتوافق مع قيود التنسيق. يجب ألا يتجاوز طول أسماء الحقول 10 أحرف وألا تحتوي على مسافات. لن يتم حفظ السجلات التي يتجاوز حجمها الإجمالي 4000 بايت بشكل صحيح. يجب أن تكون التواريخ قيم تاريخ صالحة يمكن تمثيلها بتنسيق YYYYMMDD.

{{% /alert %}}

## **اعتبارات نوع البيانات والتنسيق**

عند نقل البيانات بين Aspose.Cells وتنسيق DBF، فإن فهم كيفية تعيين أنواع البيانات بين النظامين أمر مهم لضمان سلامة البيانات.

### أنواع الخلايا إلى أنواع حقول DBF

يتم تحويل قيم خلايا Aspose.Cells تلقائيًا إلى أنواع حقول DBF المناسبة عند الحفظ:

- يتم تعيين **النصوص** إلى حقول الأحرف (C).
- يتم تعيين **القيم الرقمية** (الأعداد الصحيحة والعشرية) إلى حقول رقمية (N).
- يتم تعيين **قيم التاريخ** إلى حقول التاريخ (D) بتنسيق `YYYYMMDD`.
- يتم تعيين **القيم المنطقية** إلى حقول منطقية (L).

### الترميز

قد تستخدم ملفات DBF ترميزات أحرف مختلفة اعتمادًا على التطبيق الذي أنشأها. يتعامل Aspose.Cells مع الترميز بشفافية في معظم الحالات، ولكن إذا واجهت مشكلات في عرض الأحرف، فقد تحتاج إلى التحقق من ترميز الملف المصدر.

### قواعد أسماء الحقول

يجب أن تلتزم أسماء حقول DBF بالقواعد التالية:

- الحد الأقصى للطول هو 10 أحرف.
- يجب أن يبدأ بحرف.
- لا يمكن أن يحتوي على مسافات أو أحرف خاصة.
- يتم تخزينها بأحرف كبيرة بغض النظر عن حالة الأحرف المستخدمة في الإدخال.

### التحقق من المخرجات

بعد كتابة ملف DBF، يمكنك التحقق من النتيجة عن طريق فتحه في Microsoft Excel أو أي تطبيق متوافق مع dBASE. يجب أن تظهر البيانات في تخطيط جدولي مع أسماء الحقول كرؤوس أعمدة، والسجلات معبأة وفقًا للبيانات التي قدمتها.

## **التحويل بين DBF والتنسيقات الأخرى**

تتمثل إحدى أكثر حالات الاستخدام العملية لقراءة وكتابة ملفات DBF باستخدام Aspose.Cells في تحويل البيانات بين تنسيق DBF وتنسيقات جداول البيانات الحديثة مثل XLSX أو XLS أو CSV. نظرًا لأن Aspose.Cells يدعم مجموعة واسعة من التنسيقات، يمكنك بسهولة تحميل ملف DBF وإعادة حفظه بأي تنسيق مدعوم آخر، أو العكس.

على سبيل المثال، يمكنك قراءة ملف DBF، وتطبيق التنسيق أو الحسابات باستخدام واجهة برمجة التطبيقات الخاصة بـ Aspose.Cells، ثم حفظ النتيجة كملف XLSX لتوزيعها على المستخدمين الذين يعملون مع تطبيقات جداول البيانات الحديثة. وعلى العكس من ذلك، يمكنك أخذ البيانات من ملف XLSX أو CSV وتصديرها إلى تنسيق DBF للتكامل مع الأنظمة القديمة.



{{< app/cells/assistant language="cpp" >}}