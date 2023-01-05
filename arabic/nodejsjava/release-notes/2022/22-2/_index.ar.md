---
title: Aspose.Cells for Node.js via Java 22.2 ملاحظات الإصدار
type: docs
weight: 11
url: /ar/nodejs-java/aspose-cells-for-node-js-via-java-22-2-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Node.js via Java 22.2](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-22.2/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-44317|النص الموجود في ملف xlsx هذا غير صحيح|
|CELLSJAVA-44271|عند تحويل Excel إلى PDF ، يتغير موضع الإخراج مقارنة بحالة التحويل اليدوي|
|CELLSJAVA-44197|عند تحويل XLSX إلى PDF ، لا يتم عرض شكل الجدول الزمني للجدول المحوري (نافذة)|
|CELLSJAVA-44267|تلف المصنف الذي يحتوي على جدول محوري|
|CELLSJAVA-44114|XLSX إلى PDF: البيانات في تنسيق الأرقام العلمية من ملف XLSX لا تتطابق مع البيانات الموجودة في ملف الإخراج PDF|
|CELLSJAVA-44293|يجب استرداد ملف Excel الذي تم إعادة حفظه عند فتحه في MS Excel|
|CELLSJAVA-43194|تظهر الصور بشكل غير صحيح|
|CELLSJAVA-44243|فشل حفظ ملف GridWeb الربيع التجريبي في jdk1.8|
|CELLSJAVA-44276|ارتفاع رأس الصف غير متطابق مع محتوى الصف بعد تحرير خلية الملف 249.xls|
|CELLSJAVA-44284|رفع استثناء الذاكرة لملف bug.xlsx|
|CELLSJAVA-44229|تُفقد الصيغة عندما يتم تغليف محتوى td بعلامة div|
|CELLSJAVA-44247|يتم التفاف نص سطر واحد أثناء التحويل إلى pdf|
|CELLSJAVA-44175| مشكلة في تداخل تسميات المخطط الدائري المجوف|
|CELLSJAVA-44192|تم قطع اسم عنصر محور الفئة في الرسم البياني في Excel لتحويل PDF|
|CELLSJAVA-44233|حلقة لانهائية عند تحويل ملف XLSX|
|CELLSJAVA-44263|لا يتم تفعيل تعيين اتجاه نص تسمية المخطط إلى الوضع الرأسي|
|CELLSJAVA-44268| استثناء "java.lang.NullPointerException" في طريقة Chart.toPdf|
|CELLSJAVA-44302|اتجاه النص لمحور الإحداثيات خاطئ بعد تحويل ملف Excel إلى HTML|
|CELLSJAVA-44314|تسميات محور فئة المخطط خاطئة في عرض الرسم البياني للصورة|
|CELLSJAVA-44274|هو تنسيق SVG مدعوم للقراءة أو التقديم إلى PDF|
|CELLSJAVA-44311|استثناء "java.lang.OutOfMemoryError: Java heap space" عند التقديم إلى تنسيق ملف HTML|
|CELLSJAVA-44285|استثناء "java.lang.ClassCastException: لا يمكن تحويل com.aspose.cells.n2f إلى com.aspose.cells.o90" عند استدعاء Workbook.calculateFormula ()|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **تقادم Cells.AddAddInFunction ().**

الرجاء استخدام أساليب WorksheetCollection.RegisterAddInFunction () بدلاً من ذلك.

### **إضافة طريقة NameCollection.Filter () وتعداد NameScopeType.**

يحصل على الأسماء المحددة حسب النطاق.

### **يضيف MsoDrawingType.Timeline تعداد.**

يمثل نوع الكائنات الرسومية للخط الزمني.

