---
title: Aspose.Cells for Java 22.11 ملاحظات الإصدار
type: docs
weight: 2
url: /ar/java/aspose-cells-for-java-22-11-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 22.11](https://releases.aspose.com/cells/java/new-releases/aspose.cells-for-java-22.11/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-44888|اختفت "+" و "-" بعد التحويل - Excel إلى عرض HTML|
|CELLSJAVA-44775|تتداخل تسميات المخطط في الرسم البياني مع عرض الصورة|
|CELLSJAVA-44882|عرض الرسم البياني للصورة - توجد إحدى التسميات داخل المخطط الدائري المجوف|
|CELLSJAVA-44943|XLSX إلى PDF: لم يتم تقديم عناوين المخططات بشكل صحيح|
|CELLSJAVA-44928|XLS إلى PDF: بيانات غير كافية لصورة|
|CELLSJAVA-44910|تحويل Excel إلى HTML ينتج عنه آلاف الصور الصغيرة المتشابهة|
|CELLSJAVA-44944|يؤدي تغيير حجم الجداول إلى تغيير تنسيق الخلايا|
|CELLSJAVA-44948| لا يمكن عرض الصور في الورقة عند تحويل HTML إلى Excel|
|CELLSJAVA-44908|استثناء "java.lang.OutOfMemoryError: Java heap space" عند تحميل ملفات XLSB كبيرة|
|CELLSJAVA-44929|الانحدار: "java.lang.NullPointerException" على Workbook.calculateFormula ()|
|CELLSJAVA-44927|استثناء "java.lang.IndexOutOfBoundsException: الفهرس: 5 ، الحجم: 5" عند تحويل ملف Excel إلى HTML|
|CELLSJAVA-44939|خطأ "java.lang.StringIndexOutOfBoundsException: فهرس السلسلة خارج النطاق: 0" أثناء محاولة قراءة ملف Excel|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **إضافة Cell. خاصية IsDynamicArrayFormula**

الإشارة إلى ما إذا كانت صيغة الخلية هي صيغة صفيف ديناميكية (صواب) أو صيغة صفيف قديمة (خطأ).

### **Obsoletes SparklineGroup.SparklineCollection property ويضيف خاصية SparklineGroup.Sparklines**

استخدم خاصية SparklineGroup.Sparklines بدلاً من ذلك.

### **Obsoletes Worksheet.SparklineGroupCollection وتضيف الخاصية Worksheet.SparklineGroups**

استخدم الخاصية Worksheet.SparklineGroups بدلاً من ذلك.