---
title: Aspose.Cells for Java 20.7 ملاحظات الإصدار
type: docs
weight: 9
url: /ar/java/aspose-cells-for-java-20-7-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 20.7](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.7/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-43221|استثناء "java.lang.NullPointerException" عند تحميل ملف XLT|التعزيز|
|CELLSJAVA-43222|استثناء "com.aspose.cells.CellsException: يجب أن تكون بيانات الصيغة تالفة ...." عند تحميل ملف XLS|التعزيز|
|CELLSJAVA-43223|استثناء "java.lang.IllegalStateException: ترميز غير صالح: فارغ" عند تحميل ملف XLS|التعزيز|
|CELLSJAVA-43226|استثناء "java.lang.ArrayIndexOutOfBoundsException" عند استرداد بيانات الصورة|التعزيز|
|CELLSJAVA-43234|لا تتم قراءة البيانات قبل عام 2014 من الجدول المحوري|خلل برمجي|
|CELLSJAVA-43210|تمت قراءة قيمة خاطئة #Value بواسطة Aspose.Cells|خلل برمجي|
|CELLSJAVA-43215|تعذر تحويل الملف XLSM إلى PDF|خلل برمجي|
|CELLSJAVA-43219|إضافة مرجع الصيغة إلى نتائج ورقة مختلفة في مصنف Excel تالف|خلل برمجي|
|CELLSJAVA-43232|مشكلة دالة ROUNDUP|خلل برمجي|
|CELLSJAVA-43243|لا يمكن استرداد الصيغة أثناء تغيير صيغة الخلية المجاورة|خلل برمجي|
|CELLSJAVA-43217|تفقد الطباعة XLSX إلى XPS تنسيق الخلفية|خلل برمجي|
|CELLSJAVA-43224|مشكلة أثناء الطباعة على طابعة فعلية|خلل برمجي|
|CELLSJAVA-43241|مشكلة في ارتفاع الخط والحدود أثناء إنشاء صورة من منطقة Excel|خلل برمجي|
|CELLSJAVA-43209|setRepeatFormulaWithSubtotal (صواب) لا ينتج عنه النتائج المتوقعة أثناء استخدام SmartMarkers|خلل برمجي|
|CELLSJAVA-43213|Aspose.Cells 20.6 لا يعمل بشكل جيد مع عناصر تحكم النموذج في Office 365 (الإصدار 2005 Build 12827.20268)|خلل برمجي|
|CELLSJAVA-43214|عند ترجمة XLS إلى XLSX ، ينتج عنه ملف XLSX مكسور|خلل برمجي|
|CELLSJAVA-43216|تحويل XLS إلى XLSX - تم تغيير خط غامق وموضع للشكل|خلل برمجي|
|CELLSJAVA-43228|تم إنشاء XLS في طريقة العرض المحمية|خلل برمجي|
|CELLSJAVA-43231|خطأ في ملف الإخراج بعد الاستبدالات|خلل برمجي|
|CELLSJAVA-43225|استثناء "java.lang.NullPointerException" عند استرداد قيمة سلسلة من الخلية|استثناء|
|CELLSJAVA-43229|استثناء أثناء تحميل ملف XLSM مع مجموعة الخيارات|استثناء|
|CELLSJAVA-43238|فشل الحساب مع NPE (java.lang.NullPointerException)|استثناء|
|CELLSJAVA-43199|استثناء "java.lang.NegativeArraySizeException" عند الحفظ في HTML|استثناء|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **يضيف Cells.RemoveDuplicates ().**

طريقة التحميل الزائد Cells.RemoveDuplicates (...) لراحة المستخدم لإزالة الصفوف المكررة في الورقة بأكملها.

### **يضيف خاصية TickLabels.DisplayNumberFormat.**

الحصول على تنسيق رقم العرض الخاص بعلامات التجزئة وتعيينه.

### **يضيف Cells.GetViewRowHeight () و Cells.GetViewRowHeightInch ().**

الحصول على ارتفاع صف العرض.

### **يضيف نوع ورقة التعداد.**

يضيف نوع ورقة جديدًا: ماكرو دولي.

### **يضيف طريقة PivotFieldCollection.iterator ().**

يحصل على عداد على العناصر الموجودة في هذه المجموعة بالتسلسل الصحيح.

### **يضيف طريقة PivotItemCollection.iterator ().**

يحصل على عداد على العناصر الموجودة في هذه المجموعة بالتسلسل الصحيح.

### **يضيف خاصية Workbook.IsWorkbookProtectedWithPassword.**

يشير إلى ما إذا كانت البنية والنافذة محمية بكلمة مرور.

### **إضافة PowerQueryFormulaParameters وفئات PowerQueryFormulaParameter**

يمثل معلمات صيغة استعلام الطاقة.
