---
title: Aspose.Cells for Node.js via Java 21.12 ملاحظات الإصدار
type: docs
weight: 1
url: /ar/nodejs-java/aspose-cells-for-node-js-via-java-21-12-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Node.js via Java 21.12](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-21.12/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-43994|دعم لمقاطعة تنفيذ WorkbookDesigner.process في SmarkMarker|
|CELLSJAVA-44039|قم بتعديل سمة PDF Producer من ملف PDF الذي تم إنشاؤه|
|CELLSJAVA-43469|الانحدار المحتمل: تدهور أداء FormatConditionCollection.addArea ()|
|CELLSJAVA-43983|الانحدار: حلقة لا نهائية عند تحويل XLSX إلى PDF|
|CELLSJAVA-44029|XLSX إلى PDF: لم يتم تحويل الصورة|
|CELLSJAVA-44093| مشكلة اقتطاع النص مع أشكال المستطيل عند التقديم للصورة في الإصدارات الأحدث Aspose.Cells for Java|
|CELLSJAVA-44089|DataLabels.setShadow () غير متوفر ولا يساوي طريقة Series.setShadow ()|
|CELLSJAVA-44000|نمط Cells غير صحيح في HTML عند استخدام مجموعة الرموز والتنسيقات الشرطية الأخرى في نفس الوقت|
|CELLSJAVA-43932|مشكلة تتعلق بتعيين موضع تسميات البيانات للمخططات الدائرية المجوفة المنفصلة في صورة الإخراج|
|CELLSJAVA-43934|تسميات المخطط الدائري غير متطابقة مع Excel بعد معالجة المخطط أو تحديثه|
|CELLSJAVA-44094|تم قطع عنوان المخطط عند التصدير إلى PDF|
|CELLSJAVA-43533|XLSX إلى مشكلة إنشاء Html في أوبونتو|
|CELLSJAVA-43987|يتم فقدان الحد الأيمن للخلايا المدمجة في لغة تأشير النص الفائق|
|CELLSJAVA-44016|مشكلة عند تحويل ملف Excel الذي يحتوي على عنوان URL للصورة إلى HTML|
|CELLSJAVA-44071|com.aspose.cells.CellsException: لقد أدخلت عددًا قليلاً جدًا من المعلمات للوظيفة IF عند استدعاء Workbook.calculateFormula ()|
|CELLSJAVA-44104|NullPointerException عند استيراد SpreadSheetML|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **المزيد من القيود لإضافة مناطق للتحقق من الصحة.**

لقد قمنا بتغيير نموذج المنطقة للتحقق من الصحة والتنسيق الشرطي للنظر في الأداء. يتطلب النموذج الجديد مزيدًا من القيود لتسلسل المناطق المضافة. من أجل Validation.AddArea (CellArea cellArea ، bool checkIntersection ، bool checkEdge) and Validation.AddAreas (CellArea [] area ، bool checkIntersection ، bool checkEdge) ، إذا كانت معلمتا "check" خاطئة ، يحتاج المستخدم للتأكد من أن المناطق المضافة مرتبة ترتيبًا تصاعديًا حسب الزوايا العلوية اليسرى. وإلا فقد يتم الحصول على نتيجة غير متوقعة لعمليات أخرى. في الإصدار الجديد ، نظرًا لأن أداء إضافة كمية كبيرة من المناطق قد تم تحسينه بشكل كبير ، لا نعتقد أن ميزة Validation. لذلك نعتقد أن المستخدمين يمكنهم فقط الاتصال بـ AddArea (CellArea cellArea) مباشرة ، دون الحاجة إلى استخدام هاتين الطريقتين الخاصتين.

### **تم تغيير السلوك لتغيير مناطق التحقق من الصحة / التنسيق الشرطي.**

للتحقق من الصحة و ConditionalFormatting ، في الإصدارات القديمة ، قد يتم دعم مناطقهم بواسطة كائن CellArea الذي تم الحصول عليه منه أو تعيينه لهم. لذلك إذا قام المستخدم بتغيير قيمة حقل كائن CellArea ، فقد تتغير المناطق أيضًا ، والعكس صحيح. في الواقع هذه نتيجة غير متوقعة من وجهة نظر تصميم API. من هذا الإصدار ، تمت إزالة هذا التأثير الجانبي ولا يمكن للمستخدم تغيير المناطق عن طريق تغيير كائن CellArea بعد الآن.

### **تم تغيير سلوك إضافة شرط التنسيق إلى FormatConditionCollection.**

بالنسبة إلى طرق FormatConditionCollection.AddCondition (...) ، فإن الإصدارات القديمة تجعل أولوية الأسلوب المُضاف حديثًا هي الأقل. إنه يختلف عن سلوك ms excel. من هذا الإصدار ، تمامًا مثل ما ستحصل عليه للعملية في ms excel ، نجعل أولوية شرط التنسيق المضافة حديثًا هي الأعلى.

### **إضافة خاصية AbstractInterruptMonitor.TerminateWithoutException.**

تشير هذه الخاصية إلى وقت الحاجة إلى مقاطعة لإحدى العمليات ، وما إذا كان يجب إنهاء العملية بواسطة استثناء أو الخروج بهدوء. بشكل افتراضي ، تكون هذه الخاصية خاطئة ، أي أنه سيتم إنهاء العملية بواسطة استثناء عند مقاطعتها.

### **يضيف خاصية WorkbookSettings.ResourceProvider.**

تمت إعادة تسمية خاصية WorkbookSettings.StreamProvider لجعلها أكثر ملاءمة لوظيفتها وتسهيل فهمها على المستخدمين.

### **يضيف خيار LoadDataFilterOptions.Revision.**

قد تحتوي بعض ملفات القوالب على كمية كبيرة من سجلات المراجعة مما يتسبب في ضعف أداء تحميل المصنف. يمكن للمستخدم استخدام هذا الخيار للتحكم في ما إذا كان يجب تحميل سجلات المراجعة أم لا.

### **خاصية Obsoletes WorkbookSettings.StreamProvider.**

الرجاء استخدام الخاصية WorkbookSettings.ResourceProvider بدلاً من ذلك.

### **يحذف الخاصية القديمة PdfSaveOptions.StreamProvider.**

الرجاء استخدام الخاصية WorkbookSettings.ResourceProvider بدلاً من ذلك.

### **يضيف خاصية JsonLoadOptions.MultipleWorksheets.**

الإشارة إلى ما إذا كان استيراد كل سمة من سمات كائن JsonObject كورقة عمل واحدة عندما تكون جميع العقد الفرعية عبارة عن عقد صفيف.

### **يضيف FileFormatType.SqlScript و SaveFormat.SqlScript و SqlScriptSaveOptions**

يمثل خيارات حفظ سكربت SQL.

### **يضيف SaveFormat.Xml و LoadFormat.Xml و XmlSaveOptions و XmlLoadOptions**

يمثل خيارات ملفات R / W xml.

### **إضافة خاصية HtmlSaveOptions.SaveAsSingleFile.**

 يشير إلى ما إذا كان حفظ Excel كملف واحد.

### **يضيف خاصية JsonLoadOptions.MultipleWorksheets.**

 يشير إلى ما إذا كان يتم تحميل بيانات ملف Json إلى أوراق عمل متعددة

### **يضيف PdfSaveOptions.Producer خاصية.**

 الحصول على وتعيين منتج مستند pdf الذي تم إنشاؤه.

### **إضافة أساليب ListColumn.GetCustomTotalsRowFormula () و ListColumn.SetCustomTotalsRowFormula ()**

 الحصول على الصيغة المخصصة لصف الإجماليات في الجدول وتعيينها.

