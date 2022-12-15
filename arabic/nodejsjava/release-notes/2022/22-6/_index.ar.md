---
title: Aspose.Cells for Node.js via Java 22.6 ملاحظات الإصدار
type: docs
weight: 7
url: /ar/nodejs-java/aspose-cells-for-node-js-via-java-22-6-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Node.js via Java 22.6](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-22.6/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-44632|يدعم تنسيق صف البيانات بالكامل في PivotTable|
|CELLSJAVA-44611|تحسين قراءة الخلايا الفارغة من ملف xlsx|
|CELLSJAVA-44616|يجب إزالة الإعدادات الأصلية للتنسيق الشرطي في نطاق الوجهة عند نسخ النطاق|
|CELLSJAVA-44658|دعم BouncyCastle v1.71|
|CELLSJAVA-44628|كيفية الاحتفاظ بتنسيق النسبة المئوية لصفوف محورية معينة عند توسيع بيانات العقدة لعمود / حقل محوري|
|CELLSJAVA-44483|الفرز لا يعمل بعد تجميع الصفوف|
|CELLSJAVA-44609|نسخ بطيء بتنسيق شرطي باستخدام إصدار أحدث|
|CELLSJAVA-44622|عند فرز مجموعات كبيرة بمفاتيح متعددة ، يتم إلقاء "java.lang.ArrayIndexOutOfBoundsException"|
|CELLSJAVA-44630|مشكلة في ميزة العلامات الذكية منذ 22.5 Aspose Cells|
|CELLSJAVA-44646|يؤدي مسح المحتوى على الورقة المنسوخة إلى ظهور NullPointerException|
|CELLSJAVA-44656|يقوم Cells.getMaxDataColumn بإرجاع قيمة مختلفة (خاطئة) في 22.5|
|CELLSJAVA-44650|صفحة مستند Excel غير مرتبة عند التحميل في Aspose.Cells.GridWeb (Java)|
|CELLSJAVA-44660|مشكلة في محاذاة البيانات عند تحميل XLS في Aspose.Cells.GridWeb (Java)|
|CELLSJAVA-44661|مشكلة عند تحميل ملف et في Aspose.Cells.GridWeb (Java)|
|CELLSJAVA-44584|يتم تدوير عنوان المحور في المخطط في صورة الإخراج - تحويل الرسم البياني إلى الصورة|
|CELLSJAVA-44615|خط رمادي مرسوم في صورة الإخراج من ملف XLS|
|CELLSJAVA-44665|توقف تحميل ملف ODS|
|CELLSJAVA-44651|خطأ "ليست قيمة رقمية" عند تحويل ورقة Excel إلى HTML / PDF|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **يضيف فئة CellsDataTableFactory**

توفر هذه الفئة واجهات برمجة تطبيقات لإنشاء مثيل لـ ICellsDataTable من كائنات مخصصة لراحة المستخدم.

### **يضيف خاصية Workbook.CellsDataTableFactory**

قم بتوفير CellsDataTableFactory للمستخدم لإنشاء مثيل ICellsDataTable من الكائنات المخصصة.

### **يضيف Cell.GetDependentsInCalculation (bool) method**

وفقًا لسلسلة الحساب الحالية ، احصل على جميع الخلايا التي تعتمد نتيجتها المحسوبة على هذه الخلية.

### **يضيف Cell.GetPrecedentsInCalculation () طريقة**

وفقًا لسلسلة الحساب الحالية ، احصل على جميع السابقات (مرجع للخلايا في المصنف الحالي) المستخدمة بواسطة صيغة هذه الخلية أثناء حسابها.

### **عفا عليها الزمن Cell. GetLeafs () و Cell.**

الرجاء استخدام طريقة Cell.GetDependentsInCalculation (منطقي) بدلاً من ذلك.

### **يضيف طريقة PivotTable.FormatRow (الصف int ، نمط النمط)**

قم بتنسيق بيانات الصف في المنطقة المحورية.

### **يضيف خاصية Shapes.CreateId**

يحصل على إنشاء معرف الشكل.

### **إضافة تعداد WarningType.InvalidData**

يمثل نوع البيانات غير صالح.

### **يضيف طريقة ChartCollection.Add () الزائد**

يضيف مخططًا بمصدر البيانات.

### **يضيف طريقة Chart.GetActualSize ()**

الحصول على الحجم الفعلي للرسم البياني بوحدة البكسل.

### **عفا عليها الزمن Chart.ActualChartSize خاصية**

الرجاء استخدام طريقة Chart.GetActualSize () بدلاً من ذلك.

### **عفا عليها الزمن خاصية PdfSaveOptions.ImageType**

يتم تقديم الرسم البياني والشكل دائمًا كعناصر متجهة (على سبيل المثال ، نقطة ، خط) لتقديم الجودة.

### **عفا عليها الزمن خاصية ImageOrPrintOptions.ChartImageType**

يتم تقديم الرسم البياني والشكل دائمًا كعناصر متجهة (على سبيل المثال ، نقطة ، خط) لتقديم الجودة.

### **حذف الخاصية القديمة ImageOrPrintOptions.ImageFormat الخاصية**

الرجاء استخدام خاصية ImageOrPrintOptions.ImageType بدلاً من ذلك.

### **حذف الخاصية القديمة ImageOrPrintOptions.SImageFitToPage الخاصية**

الخاصية غير مجدية.

