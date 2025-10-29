---
title: تلاعب بموقع وحجم ومصمم المخطط باستخدام Golang عبر C++
linktitle: تلاعب بموقع الرسمة وحجمها وتصميم الرسم البياني
description: تعلم كيفية استخدام Aspose.Cells for C++ للتلاعب الفعال بموقع، وحجم، وتصميم المخطط في Microsoft Excel. سيظهر دليلنا كيف تعدل هذه الخصائص لتحسين التخطيط والتصور.
keywords: Aspose.Cells for C++، الموقع، الحجم، تصميم المخطط، Microsoft Excel، التخطيط، التصور.
type: docs
weight: 45
url: /ar/go-cpp/manipulate-position-size-and-designer-chart/
---

## **الموقع والحجم للرسم البياني**
 أحيانًا، تريد تغيير موقع أو حجم المخطط الجديد أو الموجود داخل ورقة العمل. يوفر Aspose.Cells الخاصية [Chart.GetChartObject()](https://reference.aspose.com/cells/go-cpp/chart/getchartobject/) لتحقيق ذلك. يمكنك استخدام خصائصها الفرعية لإعادة حجم المخطط بـ **الارتفاع** و **العرض** الجديد أو لإعادة وضعه بالإحداثيات الجديدة **X** و **Y**.

### **التحكم في موقع الرسم البياني وحجمه**
لاستخدام هذه الخصائص وتغيير موقع الرسم البياني (إحداثيات X و Y) أو حجمه (ارتفاع وعرض):

1. [Chart.GetX()](https://reference.aspose.com/cells/go-cpp/shape/getx/)
1. [Chart.GetY()](https://reference.aspose.com/cells/go-cpp/shape/gety/)
1. [Chart.GetHeight()](https://reference.aspose.com/cells/go-cpp/shape/getheight/)
1. [Chart.GetWidth()](https://reference.aspose.com/cells/go-cpp/shape/getwidth/)

المثال التالي يشرح استخدام الواجهات البرمجية التطبيقية المذكورة أعلاه، حيث يقوم بتحميل دفتر العمل الحالي الذي يحتوي على رسم بياني في ورقة العمل الأولى. ثم يقوم بتغيير حجم وموضع الرسم البياني باستخدام Aspose.Cells.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart.go" >}}
## **تلاعب الرسوم البيانية للمصمم**
هناك أوقات عندما تحتاج إلى تلاعب أو تعديل الرسوم البيانية في ملفات القوالب المصممة. Aspose.Cells يدعم بشكل كامل تغير محتويات وعناصر الرسم البياني المصممة. يمكن الاحتفاظ بالبيانات ومحتويات الرسم البياني والصورة الخلفية والتنسيقات بدقة.

### **تلاعب الرسوم البيانية لملفات القوالب المصممة**
لتلاعب الرسوم البيانية لملفات القالب المصممة، استخدم واجهة برمجة التطبيق للرسم البياني. على سبيل المثال، يمكنك استخدام خاصية Worksheet.Charts للحصول على مجموعة الرسوم البيانية الحالية في ملف القالب.

#### **إنشاء رسم بياني**
المثال التالي يوضح كيفية إنشاء رسم بياني هرمي. سوف نقوم بتلاعب بهذا الرسم لاحقًا.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-1.go" >}}
#### **تلاعب الرسم البياني**
المثال التالي يوضح كيفية تلاعب الرسم البياني الحالي. في هذا المثال، نقوم بتعديل الرسم البياني الذي تم إنشاؤه أعلاه. في الناتج المولد، لاحظ أن تسمية التاريخ لأحد نقاط البيانات تم تعيينها إلى 'المملكة المتحدة، 30 ألف'.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-2.go" >}}
#### **تلاعب رسم بياني الخط في القالب المصمم**
في هذا المثال، سنقوم بتلاعب رسم بياني خطي. سنضيف بعض سلاسل البيانات إلى الرسم البياني الحالي وتغيير ألوان خطوطها.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-3.go" >}}
