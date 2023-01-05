---
title: Aspose.Cells for Android via Java 19.6 ملاحظات الإصدار
type: docs
weight: 30
url: /ar/java/aspose-cells-for-android-via-java-19-6-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار Aspose.Cells for Android via Java 19.6.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42914|تتسبب التنسيقات الشرطية الكبيرة في استثناء OOM|التعزيز|
|CELLSJAVA-42916|مشكلة تنسيق البيانات بعد Workbook.save ()|التعزيز|
|CELLSJAVA-42930|فشل تحميل Excel95|التعزيز|
|CELLSJAVA-42927|يفتح الملف المحفوظ ببطء في Excel بعد حذف الأعمدة|التعزيز|
|CELLSJAVA-42857|تم عرض قيمة خاطئة للأشكال في PDF المُصدَّر|خلل برمجي|
|CELLSJAVA-42890|الصورة معتمة وغير شفافة بعد التحويل - Excel إلى HTML التقديم|خلل برمجي|
|CELLSJAVA-42893|المخطط مفقود في Excel حتى عرض HTML|خلل برمجي|
|CELLSJAVA-42899|Excel مشكلة HTML|خلل برمجي|
|CELLSJAVA-42903|Excel إلى HTML مشكلة التقديم على CentOS|خلل برمجي|
|CELLSJAVA-42882|تعذر استخراج البيانات من ملف MS Excel 95 XLS|خلل برمجي|
|CELLSJAVA-42887|فرق الحساب بين MS Excel و Aspose.Cells|خلل برمجي|
|CELLSJAVA-42891|تعطي الدالة XIRR خطأ رقميًا في حالة وجود أي قيمة فارغة في النطاق|خلل برمجي|
|CELLSJAVA-42909|مشكلة متعلقة بوظيفة DATEVALUE|خلل برمجي|
|CELLSJAVA-42910|مشكلة في وظيفة VLOOKUP عند وجود حرف في السلسلة|خلل برمجي|
|CELLSJAVA-42911|مشكلة أثناء استخدام دالة TEXT للتواريخ|خلل برمجي|
|CELLSJAVA-42896|التحويل إلى PDF يحول أرقام الهواتف|خلل برمجي|
|CELLSJAVA-42900|التحويل إلى PDF يغير ترتيب النص|خلل برمجي|
|CELLSJAVA-42932|خطأ في التنسيق الشرطي في أسلوب Style.getDisplayStyle|خلل برمجي|
|CELLSJAVA-42928|لا تنعكس بعض الأسطر في التحويل XLSX إلى PDF|خلل برمجي|
|CELLSJAVA-42904|يبدو أن صورة العنوان تفسد الملف|خلل برمجي|
|CELLSJAVA-42907|تم فقد عامل التصفية بعد حفظ المصنف|خلل برمجي|
|CELLSJAVA-42915|يتم تغيير عوامل التصفية بعد إضافة ورقة إلى المصنف|خلل برمجي|
|CELLSJAVA-42918|تم تسوية مخطط الملف المحول (تحويل XLS إلى XLSX)|خلل برمجي|
|CELLSJAVA-42938|يؤدي تحميل ملف XLSX إلى توقف التطبيق|خلل برمجي|
|CELLSJAVA-42881|استثناء "java.lang.IllegalStateException: ترميز غير صالح: فارغ" عند تحميل ملف MS Excel 5.0 / 95 XLS|استثناء|
|CELLSJAVA-42884|استثناء "java.lang.ArrayIndexOutOfBoundsException" عند تحميل ملف MS Excel 5.0 / 95 XLS|استثناء|
|CELLSJAVA-42859|CellsException لتحميل الاسم من ملف ODS|استثناء|
|CELLSJAVA-42908|استثناء أثناء استدعاء Name.getRefersTo ()|استثناء|
|CELLSJAVA-42926|IllegalStateException عند تحميل المصنف|استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على via Java for Android Aspose.Cells Aspose.Cells. في منتدى الدعم Aspose.Cells.
### **يضيف مُنشئ StreamProviderOptions**
خيارات StreamProviderOptions الجديدة.
### **إضافة تعداد FileFormatType.GraphChart**
يمثل ملف الرسم البياني المضمن.
### **يضيف خصائص ImportTableOptions.CheckMergedCells**
يشير إلى ما إذا كان التحقق من الخلايا المدمجة عند استيراد البيانات.
### **إضافة فئات ODSCellFieldCollection و ODSCellField و ODSCellFieldType enum**
يمثل حقل الخلية ODS.
### **يضيف Cells.ODSCellFields Properties**
الحصول على كشف حقول الخلايا للرقم ODS.
### **إضافة فئة ODSPageBackground وخاصية PageSetup.ODSPageBackground**
يمثل خلفية ODS.
### **إضافة enum FileFormatType.FODS و FileFormatType.SXC و LoadFormat.FODS و LoadFormat.SXC و SaveFormat.FODS و SaveFormat.SXC**
يمثل نوعي تنسيقات الملف .FODS و .SXC.
### **إضافة نوع WarningType.UnsupportedFileFormat**
يمثل تنسيق ملف غير مدعوم لأنواع التحذير.
### **يضيف تعداد ODSGeneratorType**
يمثل نوع مولد الآود.
### **OoxmlSaveOptions.EmbedOoxmlAsOleObject**
الإشارة إلى ما إذا كان يتم تضمين ملف OOXML على هيئة OleObject.
### **إضافة Row.CopySettings (Aspose.Cells.Row ، System.Boolean)**
نسخ إعدادات الصف ، مثل النمط ، الارتفاع ، الرؤية ، ... إلخ.
