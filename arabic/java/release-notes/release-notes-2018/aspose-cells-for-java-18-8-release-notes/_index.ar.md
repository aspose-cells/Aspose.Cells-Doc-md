---
title: Aspose.Cells for Java 18.8 ملاحظات الإصدار
type: docs
weight: 50
url: /ar/java/aspose-cells-for-java-18-8-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار Aspose.Cells for Java 18.8.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42680|تعطيل Pivot Table Ribbon|ميزة جديدة|
|CELLSJAVA-42568|حماية المصنف وورقة العمل في ملف ODS|ميزة جديدة|
|CELLSJAVA-42677|مشكلة انقطاع في حفظ عملية ملف XLSX|التعزيز|
|CELLSJAVA-42687|الارتباط التشعبي لا يعمل عند الرجوع إليه من ورقة أخرى|التعزيز|
|CELLSJAVA-41176|محاذاة غير صحيحة أثناء تحويل جدول البيانات إلى تنسيق PDF|حشرة|
|CELLSJAVA-42676|تحولت بيانات الجدول إلى صف وعمود خاطئين أثناء التحويل من تنسيق ملف HTML إلى MS Excel|حشرة|
|CELLSJAVA-41670|موضع صورة المخطط خاطئ في Chrome و FireFox أثناء التحويل إلى HTML|حشرة|
|CELLSJAVA-41245|لا يتم عرض التحكم في أداة تقطيع الشرائح عند تحويل ملف Excel إلى تنسيق ملف HTML|حشرة|
|CELLSJAVA-42684|لم يتم رسم الخط العمودي في وسط المخطط بشكل صحيح في الصورة المعروضة|حشرة|
|CELLSJAVA-42682|لا يتم تطبيق لون التدرج للفقاعات السلبية في إخراج PDF|حشرة|
|CELLSJAVA-42681|عنوان فئة المخطط غير معروض بشكل صحيح في الصورة|حشرة|
|CELLSJAVA-42695|تم إرجاع نمط حد خاطئ للخلية المدمجة|حشرة|
|CELLSJAVA-42694|قراءة العلامة المائية من ملف Excel|حشرة|
|CELLSJAVA-42686|يحتوي تعليق الخاصية على نص غير ضروري|حشرة|
|CELLSJAVA-42685|الخاصية "رقم المراجعة" لم يتم فحصها بشكل صحيح|حشرة|
|CELLSJAVA-41485|لا يتم الاحتفاظ بوحدات الماكرو في ملف ODS في تنسيق ملف ODS الذي تم إنشاؤه|حشرة|
|CELLSJAVA-42691|NegativeArraySizeException أثناء تحويل XLSX إلى HTML|استثناء|
|CELLSJAVA-42675|تم رفع NumberFormatException أثناء تحميل ملف HTML في المصنف|استثناء|
|CELLSJAVA-42689|تم تشغيل استثناء NullPointerException أثناء استدعاء CalculateFormula|استثناء|
|CELLSJAVA-42678|استثناء عند تحويل ورقة العمل إلى تنسيق ملف PNG|استثناء|
|CELLSJAVA-42411|خطأ في Cell: E22 - صيغة غير صالحة - استثناء عند فتح ملف MS Excel|استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يضيف خاصية PdfSecurityOptions.AccessibilityExtractContent**
إذن لنسخ المحتوى أو استخراجه (لدعم إمكانية الوصول للمستخدمين المعوقين أو لأغراض أخرى).
### **يضيف فئة SubtotalSetting**
يمثل تحديد المجموع الفرعي.
### **يضيف Cells.RetrieveSubtotalSetting (CellArea)**
يسترجع إعداد المجموع الفرعي.
### **يضيف طريقة التحميل الزائد Range.ExportDataTable (Aspose.Cells.ExportTableOptions).**
يدعم خيارات تصدير النطاق.
### **إضافة خاصية WebQueryConnection.IsSameSetting وحذف خاصية WebQueryConnection.IsFirstRow**
استخدم خاصية WebQueryConnection.IsSameSetting بدلاً من ذلك.
### **إضافة خاصية WebQueryConnection.IsXmlSourceData وحذف خاصية WebQueryConnection.IsSourceData**
استخدم خاصية WebQueryConnection.IsXmlSourceData بدلاً من ذلك.
### **يضيف خاصية Shape.IsEquation**
يشير إلى ما إذا كان الشكل يحتوي على معادلة.
### **إضافة تحميل زائد Cells.CopyColumns (Int32 ، Int32 ، PasteOptions) وطريقة Cels.CopyRows (Int32 ، Int32 ، PasteOptions)**
يدعم خيارات اللصق عند نسخ الصفوف والأعمدة.
### **إضافة خاصية Axis.IsAutoTickLabelSpacing**
يشير إلى ما إذا كان تباعد تسمية التجزئة تلقائيًا.
