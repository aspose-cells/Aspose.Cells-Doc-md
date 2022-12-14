---
title: Aspose.Cells for Java 17.7 ملاحظات الإصدار
type: docs
weight: 60
url: /ar/java/aspose-cells-for-java-17-7-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 17.7](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.7/).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42322|دعم ميزة التصفية المتقدمة (MS Excel) لعرض السجلات التي تلبي معايير معقدة|ميزة جديدة|
|CELLSJAVA-42336|تقوم ResultSet باستيراد صفر بدلاً من قيمة خالية في ملف XLSX|التعزيز|
|CELLSJAVA-42329|التحسينات المطلوبة لمرشحات البيانات وميزات الترحيل - Aspose.Cells.GridWeb (Java)|التعزيز|
|CELLSJAVA-41616|SaveCustomStyleFile غير موجود في GridWeb (Java)|التعزيز|
|CELLSJAVA-42321|يجب ألا تكون CellsHelper.setSignificantDigits () دالة ثابتة (عامة)|التعزيز|
|CELLSJAVA-42327|يتم تشويه بعض الأشكال وتغييرها في عرض Excel إلى PDF|حشرة|
|CELLSJAVA-42290|لا يتم عرض Mdash و ndash المدرجة في TextBoxes في المخططات بشكل صحيح في ملف PDF للمخطط|حشرة|
|CELLSJAVA-42338|نتائج خاطئة عند استخدام صيغ SUMIFS|حشرة|
|CELLSJAVA-42337|Aspose.Cells غير قادر على حساب قيمة الخلية B4 من ورقة عمل العمليات الحسابية|حشرة|
|CELLSJAVA-42330|نتيجة غريبة عند التحويل من Excel إلى PDF أو PDF / A باستخدام المواضيع|حشرة|
|CELLSJAVA-42331|لا يتم الاحتفاظ بالتغييرات في حقل مؤلف التعليق|حشرة|
|CELLSJAVA-42328|تم إرجاع IconSet الخاطئة|حشرة|
|CELLSJAVA-42324|خلفية الرسم البياني مفقودة بعد تعيين بيانات الصورة|حشرة|
|CELLSJAVA-42340|استثناء في مؤشر الترابط "Thread-2" java.lang.OutOfMemoryError: تم تجاوز حد الحمل الزائد لـ GC|استثناء|
|CELLSJAVA-42334|تم طرح استثناء "Error for ZipFile" عند استخدام OutputFileStream|استثناء|
|CELLSJAVA-42326|com.aspose.cells.CellsException: كلمة مرور غير صالحة عند فتح ملف Excel|استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يضيف طرق GlobalizationSettings.GetBooleanValueString () / GetErrorValueString ()**
الحصول على قيمة سلسلة عرض مخصصة للخلية قيمة منطقية وقيمة خطأ عند التنسيق / العرض.
### **يزيل طريقة ValidationCollection.Add () القديمة**
استخدم طريقة ValidationCollection.Add (CellArea) بدلاً من ذلك.
### **يضيف خاصية PdfSaveOptions.CheckWorkbookDefaultFont**
يشير إلى ما إذا كنت ستحاول استخدام الخط الافتراضي للمصنف أولاً لإظهار الأحرف التي لم يتم تعيين الخط بشكل صحيح.
### **إضافة خاصية ImageOrPrintOptions.CheckWorkbookDefaultFont**
يشير إلى ما إذا كنت ستحاول استخدام الخط الافتراضي للمصنف أولاً لإظهار الأحرف التي لم يتم تعيين الخط بشكل صحيح.
### **إضافة FileFormatType.Numbers و LoadFormat.Numbers و SaveFormat.Numbers enum**
يمثل تنسيق ملف جدول بيانات Numbers بواسطة Apple Inc /.
### **يضيف طريقة Worksheet.AdvancedFilter ()**
يقوم بتصفية البيانات باستخدام معايير معقدة.
### **يضيف خاصية WorkbookSettings.SignificantDigits**
الحصول على عدد الخانات المعنوية وتعيينها.
### **Obsoletes Validation.AreaList ويضيف خاصية Validation.Areas**
يحصل على كل المنطقة التي تحتوي على إعدادات التحقق من صحة البيانات.
### **إضافة خاصية PageSetup.IsAutomaticPaperSize**
يشير إلى ما إذا كان حجم الورق تلقائيًا.
### **يضيف طريقة FontSettingCollection.Replace ()**
يستبدل نص الشكل.
### **يضيف Cells.importResultSet (ResultSet rs، int rowIndex، int columnIndex، ImportTableOptions options) /Cells.importResultSet (ResultSet rs، String startCell، ImportTableOptions options)**
يدعم استيراد ResultSet بمزيد من الخيارات.
### **يضيف خاصية GridWorksheet.CustomColumnCaption**
الحصول على أو تعيين تسمية العمود المخصصة لورقة العمل - Aspose.Cells.GridDesktop.
### **يضيف خاصية GridWorksheet.CustomRowCaption**
الحصول على أو تعيين التسمية التوضيحية للصف المخصص لورقة العمل - Aspose.Cells.GridDesktop.
### **يضيف طريقة GridDesktop.GetVersion ()**
احصل على نسخة الإصدار.
### **يضيف وظيفة GridWebInstance.resize () في GridWeb client js ، (GridWebInstance هو كائن التحكم GridWeb)**
جعل عنصر التحكم GridWeb متوافقًا مع حجم نافذة المستعرض الحالي.


### **أمثلة على الاستخدام**
يرجى التحقق من قائمة مواضيع المساعدة المضافة في Aspose.Cells مستندات Wiki:

- [اقرأ جدول بيانات الأرقام الذي طورته شركة Apple Inc. باستخدام Aspose.Cells](/cells/ar/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [قم بتعيين خاصية DefaultFont لـ PdfSaveOptions و ImageOrPrintOptions ليكون لها الأولوية](/cells/ar/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [استيراد البيانات من Microsoft Access Database ResultSet Object إلى ورقة العمل](/cells/ar/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [تطبيق عامل التصفية المتقدم لـ Microsoft Excel لعرض السجلات التي تفي بالمعايير المعقدة](/cells/ar/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [تنفيذ الأخطاء والقيمة المنطقية باللغة الروسية أو أي لغة أخرى](/cells/ar/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/)
- [حدد ما إذا كان حجم الورق الخاص بورقة العمل تلقائيًا](/cells/ar/java/determine-if-paper-size-of-worksheet-is-automatic/)


