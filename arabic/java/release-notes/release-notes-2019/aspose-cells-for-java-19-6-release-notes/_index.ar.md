---
title: Aspose.Cells for Java 19.6 ملاحظات الإصدار
type: docs
weight: 70
url: /ar/java/aspose-cells-for-java-19-6-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار for Java Aspose.Cells 19.6.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42914|تتسبب التنسيقات الشرطية الكبيرة في استثناء OOM|التعزيز|
|CELLSJAVA-42916|مشكلة تنسيق البيانات بعد Workbook.save ()|التعزيز|
|CELLSJAVA-42930|فشل تحميل Excel95|التعزيز|
|CELLSJAVA-42927|يفتح الملف المحفوظ ببطء في Excel بعد حذف الأعمدة|التعزيز|
|CELLSJAVA-42932|خطأ في التنسيق الشرطي في أسلوب Style.getDisplayStyle|خلل برمجي|
|CELLSJAVA-42928|لا تنعكس بعض الأسطر في التحويل XLSX إلى PDF|خلل برمجي|
|CELLSJAVA-42904|يبدو أن صورة العنوان تفسد الملف|خلل برمجي|
|CELLSJAVA-42907|تم فقد عامل التصفية بعد حفظ المصنف|خلل برمجي|
|CELLSJAVA-42915|يتم تغيير عوامل التصفية بعد إضافة ورقة إلى المصنف|خلل برمجي|
|CELLSJAVA-42918|تم تسوية مخطط الملف المحول (تحويل XLS إلى XLSX)|خلل برمجي|
|CELLSJAVA-42938|يؤدي تحميل ملف XLSX إلى توقف التطبيق|خلل برمجي|
|CELLSJAVA-42859|CellsException لتحميل الاسم من ملف ODS|استثناء|
|CELLSJAVA-42908|استثناء أثناء استدعاء Name.getRefersTo ()|استثناء|
|CELLSJAVA-42926|IllegalStateException عند تحميل المصنف|استثناء|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
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
