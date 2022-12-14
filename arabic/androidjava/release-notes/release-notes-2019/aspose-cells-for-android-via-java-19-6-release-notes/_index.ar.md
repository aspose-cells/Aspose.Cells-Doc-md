---
title: Aspose.Cells لنظام Android عبر Java 19.6 Release Notes
type: docs
weight: 30
url: /ar/java/aspose-cells-for-android-via-java-19-6-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار Aspose.Cells لنظام Android عبر Java 19.6.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42914|تتسبب التنسيقات الشرطية الكبيرة في استثناء OOM|التعزيز|
|CELLSJAVA-42916|مشكلة تنسيق البيانات بعد Workbook.save ()|التعزيز|
|CELLSJAVA-42930|فشل تحميل Excel95|التعزيز|
|CELLSJAVA-42927|يفتح الملف المحفوظ ببطء في Excel بعد حذف الأعمدة|التعزيز|
|CELLSJAVA-42857|يتم عرض قيمة خاطئة للأشكال في ملف PDF المُصدَّر|حشرة|
|CELLSJAVA-42890|الصورة معتمة وغير شفافة بعد التحويل - تحويل Excel إلى HTML|حشرة|
|CELLSJAVA-42893|المخطط مفقود في عرض Excel إلى HTML|حشرة|
|CELLSJAVA-42899|Excel إلى مشكلة HTML|حشرة|
|CELLSJAVA-42903|مشكلة عرض Excel إلى HTML على CentOS|حشرة|
|CELLSJAVA-42882|تعذر استخراج البيانات من ملف MS Excel 95 XLS|حشرة|
|CELLSJAVA-42887|فرق الحساب بين MS Excel و Aspose.Cells|حشرة|
|CELLSJAVA-42891|تعطي الدالة XIRR خطأ رقميًا في حالة وجود أي قيمة فارغة في النطاق|حشرة|
|CELLSJAVA-42909|مشكلة متعلقة بوظيفة DATEVALUE|حشرة|
|CELLSJAVA-42910|مشكلة في وظيفة VLOOKUP عند وجود حرف في السلسلة|حشرة|
|CELLSJAVA-42911|مشكلة أثناء استخدام دالة TEXT للتواريخ|حشرة|
|CELLSJAVA-42896|التحويل إلى PDF يحول أرقام الهواتف|حشرة|
|CELLSJAVA-42900|التحويل إلى PDF يغير ترتيب النص|حشرة|
|CELLSJAVA-42932|خطأ في التنسيق الشرطي في أسلوب Style.getDisplayStyle|حشرة|
|CELLSJAVA-42928|لا تنعكس بعض الأسطر في تحويل XLSX إلى PDF|حشرة|
|CELLSJAVA-42904|يبدو أن صورة العنوان تفسد الملف|حشرة|
|CELLSJAVA-42907|تم فقد عامل التصفية بعد حفظ المصنف|حشرة|
|CELLSJAVA-42915|يتم تغيير عوامل التصفية بعد إضافة ورقة إلى المصنف|حشرة|
|CELLSJAVA-42918|مخطط الملف المحول بالارض (تحويل XLS إلى XLSX)|حشرة|
|CELLSJAVA-42938|تحميل ملف XLSX توقف التطبيق|حشرة|
|CELLSJAVA-42881|استثناء "java.lang.IllegalStateException: ترميز غير صالح: فارغ" عند تحميل ملف MS Excel 5.0 / 95 XLS|استثناء|
|CELLSJAVA-42884|استثناء "java.lang.ArrayIndexOutOfBoundsException" عند تحميل ملف MS Excel 5.0 / 95 XLS|استثناء|
|CELLSJAVA-42859|CellsException لتحميل الاسم من ملف ODS|استثناء|
|CELLSJAVA-42908|استثناء أثناء استدعاء Name.getRefersTo ()|استثناء|
|CELLSJAVA-42926|IllegalStateException عند تحميل المصنف|استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأية تغييرات تم إجراؤها على API العام مثل الأعضاء الذين تمت إضافتهم أو إعادة تسميتهم أو إزالة أو إهمالهم بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells لنظام Android عبر Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى ارفعه في منتدى الدعم Aspose.Cells.
### **يضيف مُنشئ StreamProviderOptions**
خيارات StreamProviderOptions الجديدة.
### **إضافة تعداد FileFormatType.GraphChart**
يمثل ملف الرسم البياني المضمن.
### **يضيف خصائص ImportTableOptions.CheckMergedCells**
يشير إلى ما إذا كان التحقق من الخلايا المدمجة عند استيراد البيانات.
### **إضافة فئات ODSCellFieldCollection و ODSCellField و ODSCellFieldType enum**
يمثل مجال الخلية في المواد المستنفدة للأوزون.
### **يضيف Cells.ODSCellFields Properties**
يحصل على قائمة حقول الخلايا في نظام الوثائق الرسمية.
### **إضافة فئة ODSPageBackground وخاصية PageSetup.ODSPageBackground**
يمثل خلفية نظام الوثائق الرسمية.
### **إضافة enum FileFormatType.FODS و FileFormatType.SXC و LoadFormat.FODS و LoadFormat.SXC و SaveFormat.FODS و SaveFormat.SXC**
يمثل نوعي تنسيقات الملفات .FODS و .SXC.
### **إضافة نوع WarningType.UnsupportedFileFormat**
يمثل تنسيق ملف غير مدعوم لأنواع التحذير.
### **يضيف تعداد ODSGeneratorType**
يمثل نوع مولد الآود.
### **OoxmlSaveOptions.EmbedOoxmlAsOleObject**
الإشارة إلى ما إذا كان يتم تضمين ملف OOXML على هيئة OleObject.
### **إضافة Row.CopySettings (Aspose.Cells.Row ، System.Boolean)**
نسخ إعدادات الصف ، مثل النمط ، الارتفاع ، الرؤية ، ... إلخ.
