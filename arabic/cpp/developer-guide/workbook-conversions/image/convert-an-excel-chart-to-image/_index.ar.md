---
title: تحويل مخطط Excel إلى صورة باستخدام C++
linktitle: تحويل مخطط Excel إلى صورة
type: docs
weight: 20
url: /ar/cpp/convert-an-excel-chart-to-image/
description: تعلم كيفية تحويل مخططات Excel إلى صور باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

الرسوم البيانية جذابة بصريًا وتسهّل على المستخدمين رؤية المقارنات والأنماط والاتجاهات في البيانات. على سبيل المثال، بدلاً من تحليل أعمدة من أرقام الورقة، يُظهر رسم بياني بسرعة ما إذا كانت المبيعات تتراجع أو ترتفع، أو كيف تقارن المبيعات الفعلية بالمبيعات المتوقعة. يُطلب من الناس بشكل متكرر تقديم المعلومات الإحصائية والبيانية بطريقة سهلة الفهم وسهلة الصيانة. تساعد الصورة.

أحيانًا، تكون الحاجة إلى الرسوم البيانية في تطبيق أو صفحات ويب. أو قد تكون ضرورية لمستند Word، ملف PDF، عرض PowerPoint، أو تطبيق آخر. في كل حالة، تريد عرض المخطط كصورة لاستخدامها في مكان آخر.

{{% /alert %}}

## **تحويل الرسوم البيانية إلى صور**

في الأمثلة هنا، يتم تحويل مخطط دائري ومخطط عمود إلى صور.

### **تحويل مخطط دائري إلى ملف صورة**

أولاً، أنشئ مخطط دائري في Microsoft Excel ثم قم بتحويله إلى ملف صورة باستخدام Aspose.Cells. يقوم الكود في هذا المثال بإنشاء صورة EMF استنادًا إلى مخطط الدائرة في ملف Microsoft Excel النموذجي.

|**الإخراج: صورة مخطط دائري**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. أنشئ مخطط دائري في Microsoft Excel:
   1. افتح برنامج Excel الجديد في Microsoft Excel.
   1. إدخال بعض البيانات في ورقة العمل.
   1. أنشئ مخطط دائري بناءً على البيانات.
   4. حفظ الملف.

|**الملف المدخل.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. قم بتنزيل وتثبيت Aspose.Cells:
   1. [تحميل Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
   1. قم بتثبيته على كمبيوتر التطوير الخاص بك.

جميع مكونات [Aspose](http://www.aspose.com/) تعمل في وضع التقييم عند التثبيت الأول. وضع التقييم ليس له حد زمني ويضيف فقط علامات مائية إلى مستندات الإخراج.

1. أنشئ مشروعًا:
   ابدأ بيئة تطوير C++ الخاصة بك (مثل Visual Studio).
   1. أنشئ تطبيقًا جديدًا على الكونسول.
   أضف مرجعاً إلى Aspose.Cells. يستخدم هذا المشروع Aspose.Cells، لذا أضف مرجعاً إلى مكتبة Aspose.Cells.
   1. كتابة الكود الذي يجد الرسم البياني ويحوله. أدناه الكود المستخدم من قِبَل المكون لإنجاز المهمة. يتم استخدام عدد قليل جدًا من السطور من الكود.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the pie chart.
    Workbook workbook(srcDir + u"PieChart.xlsx");

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Chart chart = workbook.GetWorksheets().Get(0).GetCharts().Get(0);

    // Convert the chart to an image file.
    chart.ToImage(srcDir + u"PieChart.out.emf", Aspose::Cells::Drawing::ImageType::Emf);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **تحويل رسم بياني الأعمدة إلى ملف صورة**

أولاً، أنشئ مخطط عمودي في Microsoft Excel وقم بتحويله إلى ملف صورة، كما هو موضح أعلاه. بعد تنفيذ الشفرة النموذجية، يتم إنشاء ملف JPEG بناءً على المخطط العمودي في ملف Excel النموذجي.

|**ملف الإخراج: صورة رسم بياني للأعمدة.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. إنشاء رسم بياني للأعمدة في Microsoft Excel:
   1. افتح برنامج Excel الجديد في Microsoft Excel.
   1. إدخال بعض البيانات في ورقة العمل.
   1. إنشاء رسم بياني للأعمدة بناءً على البيانات.
   4. حفظ الملف.

|**ملف الإدخال.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. إعداد مشروع، بالمراجع كما هو موضح أعلاه.
1. تحويل الرسم البياني إلى صورة ديناميكياً. يلي الكود المستخدم من قِبَل المكون لإنجاز المهمة. الكود مماثل للكود السابق:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the column chart.
    U16String inputFilePath = srcDir + u"ColumnChart.xlsx";
    Workbook workbook(inputFilePath);

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Chart chart = worksheet.GetCharts().Get(0);

    // Convert the chart to an image file.
    U16String outputImagePath = srcDir + u"ColumnChart.out.jpeg";
    chart.ToImage(outputImagePath, ImageType::Jpeg);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
