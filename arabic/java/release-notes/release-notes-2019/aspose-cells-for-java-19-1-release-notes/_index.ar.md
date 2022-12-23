---
title: Aspose.Cells for Java 19.1 ملاحظات الإصدار
type: docs
weight: 120
url: /ar/java/aspose-cells-for-java-19-1-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار Aspose.Cells for Java 19.1.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-41026|دعم Excel 95 / 5.0 (ملفات XLS)|ميزة جديدة|
|CELLSJAVA-42778|استثناء "نمط النص يجب أن يكون التدوير بين 0 و 180" أثناء تحميل XLSM|التعزيز|
|CELLSJAVA-42290|لا يتم عرض Mdash و ndash المدرجة في مربعات النص في المخططات بشكل صحيح في PDF الرسم البياني|خلل برمجي|
|CELLSJAVA-42750|تعذر استرداد عناصر حقول الصفحة في تقرير PivotTable|خلل برمجي|
|CELLSJAVA-42783|مشكلة في نص يتوسطه خط في تنسيق ملف HTML الذي تم إنشاؤه|خلل برمجي|
|CELLSJAVA-42784|لا يتم عرض البيانات في بعض الخلايا (مثل G7 و H7 وما إلى ذلك) بالطريقة نفسها الواردة في الملف الأصلي في Excel إلى HTML / تحويل الصورة|خلل برمجي|
|CELLSJAVA-42797|لا يتم عرض بعض الأنماط في إدخال HTML|خلل برمجي|
|CELLSJAVA-42807|صيغة / دالة حساب "ISOWEEKNUM" ليست مثل MS Excel|خلل برمجي|
|CELLSJAVA-42794|ODS إلى XLSX - تم تغيير لون النص|خلل برمجي|
|CELLSJAVA-42795|ODS إلى XLSX - لم يتم الاحتفاظ بخط يتوسطه خط بشكل صحيح|خلل برمجي|
|CELLSJAVA-42796|ODS إلى XLSX - تم تغيير أبعاد مربع النص|خلل برمجي|
|CELLSJAVA-42798|ODS -> XLSX - الارتباط التشعبي وظيفي ولكنه يظهر كنص عادي|خلل برمجي|
|CELLSJAVA-42802|ODS إلى XLSX ، يتم فقدان النسب المئوية في مخطط الرسم البياني الشريطي|خلل برمجي|
|CELLSJAVA-42803|لم يتأثر المخطط التفصيلي "SummaryRowBelow" عند الحفظ بتنسيق ملف XLSB|خلل برمجي|
|CELLSJAVA-42757|CellsException أثناء تحويل الملفات|استثناء|
|CELLSJAVA-42799|استثناء "java.lang.ArrayIndexOutOfBoundsException: -32768" عند تحميل تنسيق ملف XLSX|استثناء|
|CELLSJAVA-42800|ArrayIndexOutOfBoundsException عند تحميل مصنف|استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يضيف أسلوب PivotTable.ShowReportFilterPageByName (سلسلة fieldName)**
إظهار كافة صفحات عامل تصفية التقرير وفقًا لاسم PivotField ، ويجب أن يكون PivotField موجودًا في PageFields.
### **إضافة طريقة PivotTable.ShowReportFilterPageByIndex (int posIndex)**
يعرض كل صفحات تصفية التقرير وفقًا لفهرس الموضع في PageFields.
### **يضيف أسلوب PivotTable.ShowReportFilterPage (PivotField pageField)**
إظهار كافة صفحات عامل تصفية التقرير وفقًا لـ PivotField ، يجب أن يكون PivotField موجودًا في PageFields.
### **يضيف فئة DataSorterKey و DataSorterKeyCollection**
يمثل مفتاح فارز البيانات.
### **يضيف طريقة DataSorter.AddKey (Int32 ، SortOnType ، SortOrder ، كائن)**
يضيف مفتاح الفرز مثل لون خلفية الخلية ولون الخط.
### **يضيف Aspose.Cells.DataSorter.Keys خاصية**
يحصل على جميع مفاتيح فارز البيانات.
### **يضيف تعداد SortOnType**
يمثل نوع البيانات التي تم فرزها.
### **يضيف فئة ODSLoadOptions**
يمثل خيارات تحميل ملف ODS.
### **يضيف خاصية HTMLLoadOptions.ProgId**
يحصل على معرف البرنامج الخاص بإنشاء الملف. تستخدم فقط لملفات MHT.
### **يضيف خاصية PdfSaveOptions.TextCrossType**
الحصول على عرض نوع النص أو تعيينه عندما يكون عرض النص أكبر من عرض الخلية.
### **يضيف فئة تعداد TextCrossType**
تعداد عرض نوع النص عندما يكون عرض النص أكبر من عرض الخلية.
### **يضيف أساليب WorksheetCollection.RegisterAddInFunction ()**
استبدال Cell.SetAddInFormula () ، طريقة أكثر ملاءمة وفعالية للمستخدمين لإضافة واستخدام الوظائف الإضافية.
### **عفا عليها الزمن Cell.SetAddInFormula () طريقة**
يرجى تسجيل الدالات الإضافية أولاً بواسطة WorksheetCollection.RegisterAddInFunction () ثم قم بتعيين الصيغة لـ Cell بواسطة Cell.Formula / Cell.SetFormula () بدلاً من ذلك.
