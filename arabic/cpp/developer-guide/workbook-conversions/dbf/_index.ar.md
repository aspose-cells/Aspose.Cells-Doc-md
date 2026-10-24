---
title: قراءة ملفات DBF وكتابتها
linktitle: قراءة ملفات DBF وكتابتها
description: Aspose.Cells هي مكتبة C++ للعمل مع ملفات جداول البيانات، وتدعم قراءة وكتابة ملفات dBASE III وIV (DBF). توضح هذه المقالة كيفية استيراد البيانات من ملفات DBF وتصدير البيانات إليها باستخدام Aspose.Cells، بما في ذلك تفاصيل تنسيق الملفات والميزات المدعومة والأمثلة خطوة بخطوة.
keywords: Aspose.Cells, مكتبة C++, DBF, dBASE, قراءة DBF, كتابة DBF, استيراد DBF, تصدير DBF, تنسيق الملف, .dbf
type: docs
weight: 200
url: /ar/cpp/reading-and-writing-dbf-files/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
توفر Aspose.Cells دعمًا كاملًا لقراءة ملفات DBF (dBASE) وكتابتها. يمكنك تحميل ملفات dBASE III وdBASE IV الحالية إلى كائن Workbook، ومعالجة البيانات باستخدام واجهة Aspose.Cells API الغنية بالميزات، ثم حفظ المصنف مجددًا بتنسيق DBF لاستخدامه مع تطبيقات قواعد البيانات القديمة.
{{% /alert %}}

## **مقدمة**
DBF (ملف قاعدة البيانات) هو تنسيق قديم لملفات قواعد البيانات استُخدم أول مرة بواسطة dBASE في مطلع الثمانينيات من القرن الماضي. وعلى الرغم من عمر هذا التنسيق، لا تزال ملفات DBF مستخدمة على نطاق واسع في صناعات عديدة لتخزين البيانات المنظمة، ولا سيما في المحاسبة ونظم المعلومات الجغرافية (GIS) والتطبيقات المتخصصة الأخرى. تتيح Aspose.Cells دمج ملفات هذه الأنظمة القديمة بسلاسة ضمن تدفقات عمل C++ الحديثة لجداول البيانات.
تدعم المكتبة قراءة ملفات DBF وكتابتها، مما يتيح لك:
- استيراد البيانات من ملفات DBF الحالية إلى كائنات Workbook الخاصة بـ Aspose.Cells لمزيد من المعالجة أو التحويل إلى تنسيقات أخرى.
- إنشاء ملفات DBF جديدة من الصفر أو من خلال تحويل البيانات من تنسيقات جداول البيانات الأخرى.
- الحفاظ على تعريفات الحقول وأنواع البيانات وبنية السجلات عند نقل البيانات من تنسيق DBF وإليه.
يمكن أيضًا فتح ملفات DBF مباشرةً في Microsoft Excel وتطبيقات جداول البيانات الأخرى، مما يجعلها جسرًا مريحًا بين الأنظمة القديمة وأدوات جداول البيانات الحديثة.

## **إصدارات DBF والميزات المدعومة**
تدعم Aspose.Cells إصدارات تنسيق DBF التالية:
- **dBASE III** — الصنف الأصلي، وهو الأكثر دعمًا لتنسيق DBF.
- **dBASE IV** — إصدار موسّع يدعم أنواع بيانات إضافية وأحجام حقول أكبر.

### الميزات المدعومة
توفر المكتبة دعمًا شاملًا للعمليات التالية:
- قراءة بيانات DBF في كائن Workbook مع الحفاظ على جميع السجلات وتعريفات الحقول.
- كتابة بيانات Workbook مرة أخرى بتنسيق DBF لتصديرها إلى التطبيقات المتوافقة مع dBASE.
- التعامل مع أنواع البيانات الشائعة المستخدمة في ملفات DBF، بما في ذلك حقول الأحرف والحقول الرقمية وحقول التاريخ والحقول المنطقية.
- الحفاظ على تعريفات الحقول مثل اسم الحقل ونوعه وطوله أثناء عمليات القراءة والكتابة.

### القيود والاعتبارات
عند العمل مع ملفات DBF، ضع القيود التالية في الاعتبار:
- الحد الأقصى لعدد الحقول في كل ملف هو **128**.
- الحد الأقصى لحجم السجل هو **4000 بايت**.
- تقتصر أسماء الحقول على **10 أحرف**، ويجب أن تكون بأحرف كبيرة، ولا يمكن أن تحتوي على مسافات.
- تُخزن قيم التاريخ في ملفات DBF بتنسيق `YYYYMMDD`.
- قد يختلف ترميز الأحرف حسب تطبيق المصدر، وهو عادةً Windows-1252 أو صفحات رموز OEM.

## **قراءة ملف DBF**
تتيح Aspose.Cells تحميل البيانات من ملف DBF إلى كائن Workbook بسهولة. تستخدم المكتبة الصنف `LoadOptions` لتحديد تنسيق المصدر، مما يضمن تفسير البيانات تفسيرًا صحيحًا أثناء عملية التحميل.

### قراءة ملف DBF باستخدام Aspose.Cells
لقراءة ملف DBF، تحتاج إلى إنشاء كائن `LoadOptions`، ثم تعيين خاصية `LoadFormat` الخاصة به إلى `LoadFormat.Dbf`، وتمريره مع مسار الملف إلى مُنشئ `Workbook`. وبمجرد التحميل، تصبح البيانات متاحة عبر مجموعة `Worksheets`، حيث يمكنك المرور على الخلايا واستخراج القيم أو معالجة البيانات حسب الحاجة.
يوضح المثال التالي كيفية تحميل ملف DBF موجود باستخدام Aspose.Cells، ثم الوصول إلى ورقة العمل الأولى فيه وقراءة قيم الخلايا.

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
يمكنك فتح ملفات DBF مباشرةً في Microsoft Excel عن طريق تحديد الملف في مربع الحوار فتح. ستتعامل Excel مع ملف DBF بصفه جدول بيانات وتعرض سجلاته في تنسيق جدولي. وهذا مفيد للتحقق سريعًا من البيانات بعد قراءتها أو كتابتها باستخدام Aspose.Cells.
{{% /alert %}}

## **كتابة ملف DBF**
تتبع كتابة البيانات في ملف DBF نمطًا مشابهًا لحفظ أي تنسيق آخر لجداول البيانات باستخدام Aspose.Cells. تنشئ كائن Workbook أو تحمّله، ثم تملأ ورقة العمل بالبيانات، وتستدعي طريقة `Save` مع تحديد `SaveFormat.Dbf` كتنسيق للحفظ.

### كتابة ملف DBF باستخدام Aspose.Cells
لإنشاء ملف DBF، اتبع الخطوات التالية:
1. أنشئ كائن `Workbook` جديدًا.
2. احصل على ورقة العمل الأولى من مجموعة `Worksheets`.
3. املأ ورقة العمل ببياناتك، بما في ذلك رؤوس الأعمدة في الصف الأول والسجلات في الصفوف التالية.
4. استدعِ طريقة `Workbook.Save`، مع تمرير مسار الملف و`SaveFormat.Dbf` كمعلمتين.
يوضح المثال التالي كيفية إنشاء ملف DBF جديد من الصفر. يملأ المثال ورقة العمل ببيانات نموذجية تحتوي على أنواع بيانات مختلفة (النصوص والأرقام والتواريخ) لتوضيح كيفية التعامل مع أنواع الحقول عند التصدير إلى تنسيق DBF.

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
    // تعيين عرض الأعمدة لتحسين القراءة
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
عند كتابة البيانات في ملف DBF، تأكد من توافقها مع قيود التنسيق. يجب ألا يزيد طول أسماء الحقول على 10 أحرف، كما يجب ألا تحتوي على مسافات. لن تُحفظ السجلات التي يتجاوز حجمها الإجمالي 4000 بايت بصورة صحيحة. يجب أن تكون قيم التاريخ صالحة ويمكن تمثيلها بتنسيق YYYYMMDD.
{{% /alert %}}

## **اعتبارات أنواع البيانات والتنسيق**
عند نقل البيانات بين Aspose.Cells وتنسيق DBF، من المهم فهم كيفية مطابقة أنواع البيانات بين النظامين لضمان سلامة البيانات.

### أنواع الخلايا إلى أنواع حقول DBF
يتم تحويل قيم الخلايا في Aspose.Cells تلقائيًا إلى أنواع حقول DBF المناسبة عند الحفظ:
- **النصوص** تُعيَّن إلى حقول الأحرف (C).
- **القيم الرقمية**، بما في ذلك الأعداد الصحيحة والعشرية، تُعيَّن إلى حقول الأرقام (N).
- **قيم التاريخ** تُعيَّن إلى حقول التاريخ (D) بتنسيق `YYYYMMDD`.
- **القيم المنطقية** تُعيَّن إلى الحقول المنطقية (L).

### الترميز
قد تستخدم ملفات DBF ترميزات مختلفة للأحرف اعتمادًا على التطبيق الذي أنشأها. تتعامل Aspose.Cells مع الترميز بصورة شفافة في معظم الحالات، لكن إذا واجهت مشكلات في عرض الأحرف، فقد تحتاج إلى التحقق من ترميز الملف المصدر.

### قواعد أسماء الحقول
يجب أن تلتزم أسماء حقول DBF بالقواعد التالية:
- الحد الأقصى لطول اسم الحقل هو 10 أحرف.
- يجب أن يبدأ اسم الحقل بحرف.
- لا يمكن أن يحتوي اسم الحقل على مسافات أو أحرف خاصة.
- يُخزن اسم الحقل بأحرف كبيرة بغض النظر عن حالة الأحرف المستخدمة في الإدخال.

### التحقق من الناتج
بعد كتابة ملف DBF، يمكنك التحقق من الناتج بفتحه في Microsoft Excel أو أي تطبيق متوافق مع dBASE. يجب أن تظهر البيانات في تنسيق جدولي، وتكون أسماء الحقول رؤوسًا للأعمدة، مع ملء السجلات بالبيانات التي قدتها.

## **التحويل بين DBF والتنسيقات الأخرى**
يُعدّ تحويل البيانات بين تنسيق DBF وتنسيقات جداول البيانات الحديثة مثل XLSX وXLS وCSV من أكثر حالات الاستخدام عمليةً لقراءة ملفات DBF وكتابتها باستخدام Aspose.Cells. وبما أن مكتبة Aspose.Cells تدعم مجموعة واسعة من التنسيقات، يمكنك بسهولة تحميل ملف DBF وإعادة حفظه بأي تنسيق مدعوم آخر، أو إجراء العملية العكسية.

{{< app/cells/assistant language="cpp" >}}