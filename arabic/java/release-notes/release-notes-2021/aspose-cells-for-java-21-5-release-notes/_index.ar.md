---
title: Aspose.Cells for Java 21.5 ملاحظات الإصدار
type: docs
weight: 8
url: /ar/java/aspose-cells-for-java-21-5-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 21.5](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.5/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-43452|التقويم الياباني الذي يستخدم وظيفة Excel لا يقرأ بشكل صحيح|
|CELLSJAVA-43420| تمت محاذاة النص الذي تم تدويره بشكل غير صحيح عند حفظه بتنسيق HTML|
|CELLSJAVA-43450|مشكلة تحديث الجدول المحوري|
|CELLSJAVA-43444|الانحدار: ترجع getLastSavedUniversalTime تاريخًا غير صحيح|
|CELLSJAVA-43446|Cells استثناء تعقب التغييرات|
|CELLSJAVA-43448|الانحدار: مرجع غير صالح للقائمة|
|CELLSJAVA-43457|حلقة لا نهائية عند حفظ المصنف المنسوخ|
|CELLSJAVA-43442|مشكلة في فرز البيانات عند النقر على روابط الرأس في العرض التوضيحي لفصل GridWeb|
|CELLSJAVA-43443|مشكلة تتعلق بوضع التحرير في GridWeb Java|
|CELLSJAVA-43455|لا يتم تضمين الخطوط في PDF لحروف غير ASCII أثناء ضبط EmbedStandardWindowsFonts على false|
|CELLSJAVA-43449|تعذر تغيير مجموعة خطوط عناصر المخطط من "Calibri" إلى "Aktiv Grotesk"|
|CELLSJAVA-43454|تسميات المحور السيني مقطوعة|
|CELLSJAVA-43445|الانحدار: بيانات الصف المفقودة لملفات .numbers|
|CELLSJAVA-43459|NullPointerException في getFormulaLocal () مع GlobalizationSettings المخصصة|
|CELLSJAVA-43447| حدث استثناء "java.lang.NullPointerException" عند استخدام ملف نمط مخصص في GridWeb|
|CELLSJAVA-43439|يحدث NegativeArraySizeException عند تحميل المصنف|
|CELLSJAVA-43453|NullPointerException على طريقة Workbook.save|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **يضيف طريقة Slicer.AddPivotConnection (PivotTable pivot).**

يضيف اتصال PivotTable لتقطيع الشرائح.

### **يضيف طريقة Slicer.RemovePivotConnection (PivotTable pivot).**

يزيل اتصال PivotTable من أداة تقطيع الشرائح.

### **يضيف خاصية TxtSaveOptions.ExportAllSheets.**

يشير إلى ما إذا كان سيتم تصدير جميع أوراق العمل إلى الملف أم لا. قيمة dafaut خاطئة مثل MS Excel.

### **يضيف FileFormatType.Numbers09 enum.**

يمثل تنسيق ملف .numbers 09. و FileFormatType.Number سوف يمثل أحدث نوع تنسيق ملف في وقت لاحق.

### **يضيف طريقة WorkbookSettings.SetPageOrientationType ().**

يضبط نوع اتجاه صفحة الطباعة للملف بأكمله.

### **يحذف تعداد DataBarAxisPosition.DataBarAxisAutomatic المتقادم.**

استخدم DataBarAxisPosition. تعداد تلقائي بدلاً من ذلك.

### **حذف عدد DataBarAxisPosition.DataBarAxisMidpointe المتقادم.**

استخدم DataBarAxisPosition.Midpoint enum بدلاً من ذلك.

### **حذف تعداد DataBarAxisPosition.DataBarAxisNone المتقادم.**

استخدم DataBarAxisPosition. لا يوجد تعداد بدلاً منها.

### **حذف تعداد DataBarBorderType.DataBarBorderNone المتقادم.**

استخدم DataBarBorderType. لا يوجد تعداد بدلاً منها.

### **حذف تعداد DataBarBorderType.DataBarBorderSolid المتقادم.**

استخدم DataBarBorderType.Solid تعداد بدلاً من ذلك.

### **حذف تعداد DataBarFillType.DataBarFillGradient المتقادم.**

استخدم DataBarFillType.Gradient enum بدلاً من ذلك.

### **حذف تعداد DataBarFillType.DataBarFillSolid المتقادم.**

استخدم DataBarFillType.Solid التعداد بدلاً من ذلك.

### **حذف تعداد DataBarNegativeColorType.DataBarColor المتقادم.**

استخدم تعداد DataBarNegativeColorTypeColor بدلاً من ذلك.

### **حذف تعداد DataBarNegativeColorType.DataBarSameAsPositive المتقادم.**

استخدم DataBarNegativeColorType.SameAsPositive enum بدلاً من ذلك.

### **حذف تعداد OleObject.FileFormatType المتقادم.**

استخدم تعداد OleObject.FileFormatType بدلاً من ذلك.

### **يحذف DynamicFilterType المتقادم.**

استخدم DynamicFilterType. عد فبراير بدلاً من ذلك.

### **يضيف طريقة GridCells.MoveRange ().**

ينقل النطاق.

### **يضيف طريقة GridCells.InsertRange ().**

يُدرج نطاقًا مع خيار التحول.

### **يضيف طريقة GridCells.DeleteRange ().**

يحذف النطاق مع خيار التحول.
