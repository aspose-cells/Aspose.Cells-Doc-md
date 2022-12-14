---
title: Aspose.Cells for Java 19.10 ملاحظات الإصدار
type: docs
weight: 30
url: /ar/java/aspose-cells-for-java-19-10-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار for Java Aspose.Cells 19.10.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-41814|دعم فرز البيانات المخصصة لمنطقة معينة في تقرير PivotTable|ميزة جديدة|
|CELLSJAVA-42988|مشكلة في الأداء مع calculateFormula ()|التعزيز|
|CELLSJAVA-41103|لا يتم عرض تلوين وتنسيق بيانات الجدول المحوري بشكل صحيح|حشرة|
|CELLSJAVA-43007|لم يتم إنشاء PDF كما هو متوقع|حشرة|
|CELLSJAVA-43025|Cell.getStyle.getCustom تقوم بإرجاع تنسيق خاطئ للغة الألمانية|حشرة|
|CELLSJAVA-43013|ArrayIndexOutOfBoundsException أثناء تحميل ملف Excel|استثناء|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يضيف Cells.RemoveDuplicates ()**
يزيل البيانات المكررة من النطاق.
### **إضافة خاصية OleObject.FullObjectBin**
الحصول على البيانات الثنائية الكاملة المضمنة في كائن أول في ملف القالب.
### **يضيف خاصية ContentTypeProperty.SNillable**
يشير إلى ما إذا كانت الخاصية يمكن أن تكون خالية.
### **إضافة طريقة WorkbookDesigner.SetDataSource (سلسلة ، ICellsDataTable)**
يعيّن مصدر البيانات لمصمم العلامات الذكية.
### **إضافة خاصية ImageOrPrintOptions.PageSavingCallback**
التحكم / الإشارة إلى التقدم المحرز في عملية حفظ الصفحة.
### **إضافة خاصية ImageOrPrintOptions.IsFontSubstitutionCharGranularity**
الإشارة إلى ما إذا كان سيتم استبدال خط الحرف فقط عندما لا يكون خط الخلية متوافقًا معه.
### **يزيل فئة عفا عليها الزمن HTMLLoadOptions**
استخدم فئة HtmlLoadOptions بدلاً من ذلك.
### **يزيل فئة ODSLoadOptions المتقادمة**
استخدم فئة OdsLoadOptions بدلاً من ذلك.
### **يزيل الفئة المتقادمة JSONUtility**
استخدم class JsonUtility بدلاً من ذلك.
