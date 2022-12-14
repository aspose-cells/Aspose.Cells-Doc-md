---
title: Aspose.Cells for Java 20.3 ملاحظات الإصدار
type: docs
weight: 40
url: /ar/java/aspose-cells-for-java-20-3-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 20.3](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.3/).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-43137|ضوء Cells API: معالجة الأوراق بترتيب معين|ميزة جديدة|
|CELLSJAVA-43135|قم بإزالة ActiveXControl من شكل الصورة|ميزة جديدة|
|CELLSJAVA-43141|إضافة خاصية ThreadedComment.CreatedTime|ميزة جديدة|
|CELLSJAVA-42068|ملف GIF في ورقة العمل خاطئ عند تحويل المصنف إلى HTML|حشرة|
|CELLSJAVA-43127|لا يتم تحديث Excel Pivot Table تلقائيًا أثناء فتح الملف لأول مرة|حشرة|
|CELLSJAVA-43129|النص الصيني مشوه في تحويل HTML إلى XLS|حشرة|
|CELLSJAVA-43139|لا يتم تحديث المخططات الموجودة في الورقة عند تحويل ورقة العمل إلى صورة|حشرة|
|CELLSJAVA-43148|خطأ في موضع تسمية المخطط|حشرة|
|CELLSJAVA-43124|عند التحويل إلى PDF ، يتم قطع عمودين من الجدول|حشرة|
|CELLSJAVA-43091|تتداخل تسميات البيانات على مخطط الكعك في ملف PDF|حشرة|
|CELLSJAVA-43132|تسميات البيانات مفقودة من بعض المخططات أثناء تصدير مخطط إلى صورة|حشرة|
|CELLSJAVA-43143|بعد WorkbookDesigner.process ، خرج المخطط فارغًا في HTML|حشرة|
|CELLSJAVA-43098|استبدال الكائن المضمن بصورة لا يعمل مع تنسيق ملف XLS|حشرة|
|CELLSJAVA-43122|مشكلة في طلب التعليقات المترابطة بعد الاستيراد إلى تنسيق ملف Office365 XLSX|حشرة|
|CELLSJAVA-43134|قيمة سلسلة الخلية فارغة في Apple Numbers'09|حشرة|
|CELLSJAVA-43144|تم اكتشاف خاصية IsItalic بشكل مختلف عن MS Excel (Java)|حشرة|
|CELLSJAVA-43140|IllegalArgumentException أثناء استدعاء calculateFormula ()|استثناء|
|CELLSJAVA-43110|التحويل إلى ملف PDF - java.lang.NullPointerException|استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **أضف خاصية LoadFilter.SheetsInLoadingOrder**
يمكن للمستخدمين تجاوز هذه الخاصية لتحديد الأوراق وترتيب تحميلها أثناء استيراد المصنفات من ملفات القوالب.
### **يحذف خاصية TickLabels القديمة**
استخدم خاصية TickLabels.BackgroundMode بدلاً من ذلك.
### **Obsoletes TickLabels.TextDirection ويضيف خاصية TickLabels.ReadingOrder**
استخدم خاصية TickLabels.ReadingOrder بدلاً من ذلك.
### **عفا عليها الزمن TickLabels.DirectionTypeproperty ويضيف مخطط التعدادات TextDirectionType**
يمثل اتجاه النص.
### **يضيف طريقة Shape.RemoveActiveXControl ().**
يزيل بيانات ActiveX من الشكل.
### **يضيف خاصية ThreadedComment.CreatedTime.**
الحصول على وقت إنشاء التعليقات المترابطة وتعيينه.
### **يضيف خاصية Worksheet.UniqueId.**
الحصول على المعرف الفريد لورقة العمل وتعيينه.
### **إضافة تعداد IconSetType.ColorSmilies3 و IconSetType.Smilies3.**
يمثل رمز 3 Smiles مجموعة التنسيقات الشرطية. فقط لملفات ods
### **إضافة تعداد TimePeriodType.LastYear و TimePeriodType.NextYear و ThisYear.**
يمثل العام الماضي والعام المقبل وتنسيقات هذا العام الشرطية. فقط لملفات ods.
### **يضيف طريقة WorksheetCollection.RefreshPivotTables ().**
تحديث كل الجداول المحورية في الملف.
