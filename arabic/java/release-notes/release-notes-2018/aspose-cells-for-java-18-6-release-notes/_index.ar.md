---
title: Aspose.Cells for Java 18.6 ملاحظات الإصدار
type: docs
weight: 70
url: /ar/java/aspose-cells-for-java-18-6-release-notes/
---
{{% alert color="primary" %}}

تحتوي هذه الصفحة على ملاحظات إصدار for Java Aspose.Cells 18.6.

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42339|تنفيذ فرز البيانات المخصصة في تقرير Pivot Table عبر Aspose.Cells APIs|ميزة جديدة|
|CELLSJAVA-42625|تنفيذ ميزة MS Excel "Watch Window"|ميزة جديدة|
|CELLSJAVA-42612|تعذر استخراج النص من نوع الترس SmartArt|ميزة جديدة|
|CELLSJAVA-42646|استثناء: "FormulaBuild] (/ p صيغة غير معروفة token0" في Name.getRefersTo ()|التعزيز|
|CELLSJAVA-42645|استثناء: "FormulaBuild أكثر من رمز مميز في المكدس ...." في Cell.getFormula ()|التعزيز|
|CELLSJAVA-42516|Aspose.Cells يقبل ويصحح معادلة غير صالحة|التعزيز|
|CELLSJAVA-42636|يتم إزاحة بعض أشكال الرسم أو عرضها بشكل خاطئ في عرض Excel إلى HTML|حشرة|
|CELLSJAVA-42627|CELLSJAVA-42619 - غير قادر على استخراج صور Smart Art بشكل صحيح|حشرة|
|CELLSJAVA-42618|يتم إزاحة الشكل لتغطية البيانات في Excel إلى عرض HTML|حشرة|
|CELLSJAVA-42628|حساب الصيغ خاطئ ، على سبيل المثال أنه يولد # DIV / 0! أخطاء|حشرة|
|CELLSJAVA-42615|تنسيق Cell A3 غير صحيح في HTML الناتج|حشرة|
|CELLSJAVA-42621|أداء ضعيف عند إنشاء ملف PDF من ملف MS Excel|حشرة|
|CELLSJAVA-42620|XLSX إلى TIFF - استثناء NoClassDefFoundError|حشرة|
|CELLSJAVA-42599|تُفقد الصور عند تحويل ملف Excel إلى PDF|حشرة|
|CELLSJAVA-42630|يتسبب أسلوب Chart.calculate في حدوث OutOfMemoryError|حشرة|
|CELLSJAVA-42623|تزداد الذاكرة في تحويل ملف Excel إلى تنسيق ملف PDF|حشرة|
|CELLSJAVA-42592|تم تغيير حجم الخط في عنوان المخطط بسبب طريقة الأحرف ()|حشرة|
|CELLSJAVA-41860|يتغير تأثير الظل أثناء إعادة حفظ XLS|حشرة|
|CELLSJAVA-42654|تحويل Excel إلى PDF - لا يكتمل التحويل أبدًا|حشرة|
|CELLSJAVA-42647|تعذر الحصول على نص بديل أو تعيينه لشكل التعليق|حشرة|
|CELLSJAVA-42644|يتوقف Aspose.Cells عند تحويل ملف مل لجدول بيانات (xml) إلى PDF بعلامة أنماط الإغلاق الذاتي|حشرة|
|CELLSJAVA-42632|تعذر تعيين نص بديل لشكل SmartArt|حشرة|
|CELLSJAVA-42631|يقوم getFirstVisibleRow () و getFirstVisibleColumn () بإرجاع فهارس غير صالحة|حشرة|
|CELLSJAVA-42624|الارتباطات التشعبية ذات الرموز المشفرة (مثل ، "٪ 5c") تقوم بفك تشفيرها بعد إعادة الحفظ|حشرة|
|CELLSJAVA-42638|Cell.getDisplayStringValue () يطرح java.lang.NullPointerException|استثناء|
|CELLSJAVA-42652|java.lang.ArrayIndexOutOfBoundsException حدث أثناء تحميل ملف XLS|استثناء|
|CELLSJAVA-42650|استثناء: "ترميز غير صالح: فارغ" عند تحميل ملف XLS|استثناء|
|CELLSJAVA-42649|استثناء: "لا يمكن أن يكون عدد HPageBreaks أكبر من 1024" عند تحميل ملف XLS|استثناء|
|CELLSJAVA-42648|استثناء: "فشل قراءة بيانات الصورة" على Picture.getData ()|استثناء|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **يضيف فئات Slicer و SlicerCollection و SlicerCache و SlicerCacheItem و SlicerCacheItemCollection**

تُستخدم واجهات برمجة التطبيقات هذه لإنشاء أداة تقطيع الشرائح وتعديلها في الملف.

### **يضيف SlicerCacheItemSortType و SlicerStyleType**

تُستخدم واجهات برمجة التطبيقات هذه لإنشاء أداة تقطيع الشرائح وتعديلها في الملف.

### **يضيف فئات CellWatchCollection و CellWatch ، ويضيف خاصية Worksheet.CellWatches**

يضيف Cell عنصر المشاهدة في "نافذة الساعة".

### **يضيف فئة CustomXmlShape و MsoDrawingType.CustomXml enum**

يدعم الحفاظ على شكل xml المخصص.

### **إضافة تعداد MsoDrawingType.SmartArt**

يمثل نوع الشكل الفني الذكي.

### **يضيف خاصية Font.SchemeType وتعدادات FontSchemeType**

الحصول على نوع مخطط الخط وتعيينه.

### **يضيف خاصية CustomXmlPart.ID**

الحصول على معرف جزء xml المخصص وتعيينه.

### **يضيف أسلوب CustomXmlPartCollection.SelectByID ()**

يحصل على جزء xml مخصص بواسطة المعرف.

### **يضيف Range.Address و Range.CellCount و EntireColumn و Range.EntireRow و Range.GetOffset (System.Int32 و System.Int32)**

تحسين نطاق المعالجة.

### **إضافة تعداد ColorDepth وخاصية ImageOrPrintOptions.TiffColorDepth**

الحصول على عمق البت أو تعيينه ليتم تطبيقه فقط عند حفظ الصفحات بتنسيق Tiff.

### **طريقة التحميل الزائد WorkbookRender.ToImage ()**

يعرض صورة المصنف من خلال فهرس الصفحة.

### **يضيف طريقة Legend.LegendEntriesLabels ()**

الحصول على تسميات إدخالات وسيلة الإيضاح بعد استدعاء طريقة Chart.Calculate ().

### **يضيف طريقة CustomFilter.SetCriteria (FilterOperatorType filterOperator ، معايير الكائن)**

يحدد معايير التصفية.

### **يوفر واجهات برمجة تطبيقات جديدة لدعم الحصول على / تعيين الصيغ في تنسيق يعتمد على اللغة المحلية (وظيفة FormulaLocal من Microsoft Interop)**

Cell.GetFormula (منطقي isR1C1 ، منطقي isLocal)
Cell.SetFormula (صيغة سلسلة ، منطقي هو R1C1 ، منطقي isLocal ، قيمة الكائن)
Name.GetRefersTo (منطقي هو R1C1 ، منطقي isLocal)
Name.SetRefersTo (سلسلة تشير إلى ، منطقي هو R1C1 ، منطقي هو محلي)
FormatCondition.GetFormula1 (منطقي هو R1C1 ، منطقي isLocal)
FormatCondition.SetFormula1 (صيغة سلسلة ، منطقي هو R1C1 ، منطقي isLocal)
FormatCondition.GetFormula2 (منطقي هوR1C1 ، منطقي isLocal)
FormatCondition.SetFormula2 (صيغة سلسلة ، منطقي هو R1C1 ، منطقي isLocal)
FormatCondition.GetFormula1 (منطقي هو R1C1 ، منطقي isLocal ، صف int ، عمود int)
FormatCondition.GetFormula2 (منطقي هو R1C1 ، منطقي isLocal ، صف int ، عمود int)
GlobalizationSettings.GetTableRowTypeOfHeaders ()
GlobalizationSettings.GetTableRowTypeOfData ()
GlobalizationSettings.GetTableRowTypeOfAll ()
GlobalizationSettings.GetTableRowTypeOfTotals ()
GlobalizationSettings.GetTableRowTypeOfCurrent ()
GlobalizationSettings.GetErrorValueString (سلسلة خاطئة)
GlobalizationSettings.GetBooleanValueString (bool bv)
GlobalizationSettings.GetLocalFunctionName (سلسلة معايير اسم)
GlobalizationSettings.GetStandardFunctionName (سلسلة localName)
GlobalizationSettings.GetLocalBuiltInName (سلسلة معيارية اسم)
GlobalizationSettings.GetStandardBuiltInName (سلسلة localName)
إعدادات العولمة
إعدادات العولمة
إعدادات العولمة
