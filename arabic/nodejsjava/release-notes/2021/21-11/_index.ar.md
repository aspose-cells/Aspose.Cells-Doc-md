---
title: Aspose.Cells for Node.js via Java 21.11 ملاحظات الإصدار
type: docs
weight: 2
url: /ar/nodejs-java/aspose-cells-for-node-js-via-java-21-11-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Node.js via Java 21.11](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-21.11/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-43844| هناك حاجة إلى تحسين تنسيق الأرقام المحاسبية|
|CELLSJAVA-43953|تقديم نص / جزء محدد "Cell" و "تعليق" ليتم ترجمته إلى اليابانية في Excel إلى تحويل PDF|
|CELLSJAVA-43935|مشكلة في حجم خط نص الشكل أثناء حفظ وتحميل ملف XLS|
|CELLSJAVA-43952|إصدار انتهاء صلاحية الترخيص المؤقت|
|CELLSJAVA-43954|XLSX إلى PDF: تسبب الصورة استثناء "java.lang.OutOfMemoryError: Java heap space"|
|CELLSJAVA-43902|بعض حدود Excel المحولة إلى HTML زائدة عن الحاجة|
|CELLSJAVA-43933|عند التصدير إلى HTML ببيانات واحدة فقط ، فإن التنسيق الشرطي يختلف عن Excel|
|CELLSJAVA-43878| الموضع غير الصحيح لتسميات بيانات مخطط شريط المجموعة في Excel|
|CELLSJAVA-43895|لا يتم عرض شكل الخط وأشكال المخططات الأخرى بشكل صحيح عند تحويل XLS إلى XLSX|
|CELLSJAVA-43932|مشكلة تتعلق بتعيين موضع تسميات البيانات للمخططات الدائرية المجوفة المنفصلة في صورة الإخراج|
|CELLSJAVA-43934|تسميات المخطط الدائري غير متطابقة مع Excel بعد معالجة المخطط أو تحديثه|
|CELLSJAVA-43519|تنتج الخلايا المدمجة المتضمنة في الصفوف أو الأعمدة المخفية جدول HTML غير متساو|
|CELLSJAVA-43962|التأثير غير متناسق بعد تحويل التنسيق الشرطي في Excel إلى HTML|
|CELLSJAVA-43969|ينتج عن الاسم الذي يحتوي على دالة COUNTIF والمرجع الخارجي NullPointerException|
|CELLSJAVA-43903|java.lang.NumberFormatException: لسلسلة الإدخال عند تقديم ملف Excel إلى HTML|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **يضيف تعداد CellValueFormatStrategy.DisplayString.**

باستخدام هذه الإستراتيجية ، ستأخذ Cell.GetStringValue (CellValueFormatStrategy) في الاعتبار حد عرض العمود عند تنسيق قيم الخلية بنمط العرض. إذا تجاوزت النتيجة المنسقة العرض المتاح ، فقد يتم إرجاع "#" واحد أو أكثر ، تمامًا مثل ما يظهره ms excel لمثل هذا النوع من الخلايا.

### **إضافة خاصية WorksheetCollection.ActiveSheetName.**

الحصول على اسم الورقة النشط للمصنف وتعيينه.

### **يضيف فئات JsonLoadOptions و JsonSaveOptions.**

يمثل خيارات تحميل الملفات أو حفظها.

### **يضيف خاصية ImageSaveOptions.StreamProvider.**

قم بتوفير التدفقات إذا كان هناك صفحتان أو أكثر.

### **يضيف LoadFormat.Image و LoadFormat.Json enum.**

يمثل الصورة ونوع json.

### **إضافة تعداد SaveFormat.Bmp و SaveFormat.Emf و SaveFormat.Gif و SaveFormat.Jpg و SaveFormat.Json و SaveFormat.Png**

تنسيقات حفظ جديدة مدعومة.

### **يضيف FileFormatType.Emf ، FileFormatType.Gif ، FileFormatType.Jpg ، FileFormatType.Json ، FileFormatType.Png ، FileFormatType.Wmf enum**

أنواع تنسيقات الملفات المدعومة الجديدة.


