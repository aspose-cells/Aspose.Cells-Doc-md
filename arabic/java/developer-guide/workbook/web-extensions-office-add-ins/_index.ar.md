---
title: الإضافات الإلكترونية للويب  إضافات Office
type: docs
weight: 120
url: /ar/java/web-extensions-office-add-ins/
---

ملحقات الويب توسع تطبيقات Office وتتفاعل مع محتوى مستندات Office. تضيف ملحقات الويب وظائف إضافية إلى عميل Office لتحسين تجربة المستخدم وزيادة الإنتاجية.

توفر Aspose.Cells أيضًا القدرة على العمل مع ملحقات الويب.

## **إضافة ملحق ويب**

يمكنك إضافة توسيعات الويب (واضافات مكتبية) في Excel عن طريق النقر على علامة التبويب **إدراج** ثم النقر على الرابط **متجر**/**الحصول على الواضافات**. في مربع الواضافات، تصفح الواضافة المطلوبة وأضفها.

توفر Aspose.Cells أيضًا ميزة إضافة توسيعات الويب باستخدام فئات WebExtension و WebExtensionTaskPane. يوضح الكود النموذجي التالي استخدام فئات WebExtension و WebExtensionTaskPane لإضافة توسيع ويب إلى ملف Excel. يرجى الاطلاع على [ملف Excel الناتج](AddWebExtension_Out.xlsx) الذي تم إنشاؤه بواسطة الكود للرجوع إليه.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddWebExtension-1.java" >}}

## **الوصول إلى معلومات ملحق الويب**

يوفر Aspose.Cells القدرة على الوصول إلى معلومات توسيعات الويب في ملف Excel. يوضح الكود النموذجي التالي كيفية الوصول إلى معلومات توسيع الويب من خلال تحميل [ملف Excel عيني](WebExtensionsSample.xlsx). يرجى الاطلاع على الإخراج في وحدة التحكم الذي تم إنشاؤه بواسطة الكود للرجوع إليه.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AccessWebExtensionInformation-1.java" >}}

### **مخرجات الوحدة**

{{< highlight java >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}
