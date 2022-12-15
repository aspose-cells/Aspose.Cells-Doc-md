---
title: Aspose.Cells for PHP via Java 22.4 ملاحظات الإصدار
type: docs
weight: 9
url: /ar/php-java/aspose-cells-for-php-via-java-22-4-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for PHP via Java 22.4](https://downloads.aspose.com/cells/php/new-releases/aspose.cells-for-php-via-java-22.4/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-44415|تتسبب الآلاف من مكالمات getResourceAsAStream في ارتفاع تحميل وحدة المعالجة المركزية واستهلاك الذاكرة أثناء إنشاء التقرير|
|CELLSJAVA-44490|إضافة GridWorkbookSetting لـ GridWeb|
|CELLSJAVA-44455|عند تحويل ملف XLSX إلى PDF ، يصبح التاريخ في الجدول المحوري رقمًا تسلسليًا|
|CELLSJAVA-44370|تلف ملف Excel عند فتحه وحفظه باستخدام Aspose.Cells|
|CELLSJAVA-44381|مشكلة في تنسيق الشرط عند حذف الصف أو العمود|
|CELLSJAVA-44442|الفتح والحفظ باستخدام Aspose.Cells يفسد المصنف|
|CELLSJAVA-44356|مشكلة موضع الصورة لطباعة الملف fs.zip في GridWeb|
|CELLSJAVA-44357|قضايا لعرض ofd.zip في GridWeb|
|CELLSJAVA-44398|مشاكل عرض GridWeb من العميل|
|CELLSJAVA-44464|المشكلة الإضافية 1 ، العمود لون الخلفية ليس هو نفسه في Excel لـ yscl.xls في الورقة 4|
|CELLSJAVA-44466| المسألة الإضافية 3 ، لا يعمل setCalculateFormula إلى false|
|CELLSJAVA-44496|قم بتضمين عنصر / علامة التسمية التوضيحية للجدول عند تحميل html|
|CELLSJAVA-44429|يختلف تأثير مخطط Excel في Excel عن تأثير مخطط Excel|
|CELLSJAVA-44414| سيؤدي Unicode في JSON إلى كسر XLSX و CSV اللذين تم إنشاؤهما|
|CELLSJAVA-44404|استثناء "java.lang.IllegalArgumentException: فهرس العمود غير صالح" عند تحميل ملف XLSX في GridWeb|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **يضيف فئة DefaultStyleSettings.**

مجموعة من القيم الافتراضية للخصائص ذات الصلة بالنمط.

### **يضيف خاصية LoadOptions.DefaultStyleSettings.**

دعم لتعيين القيم الافتراضية للخصائص ذات الصلة بالنمط لتهيئة مصنف.

### **يضيف خاصية TxtSaveOptions.TrimTailingBlankCells.**

دعم لإزالة جميع الخلايا الفارغة (الأحرف المتكررة للفاصل مثل "~ ، ~ ، ~ ، ~ ،") في نهاية سجل الصف عند تصدير csv / tsv.

### **يضيف خاصية Style.HasBorders.**

دعم للتحقق مما إذا كانت هناك حدود تم تعيينها للأسلوب.

### **تقادم LoadOptions.StandardFont / StandardFontSize خصائص.**

الرجاء استخدام LoadOptions.DefaultStyleSettings.FontName / FontSize بدلاً من ذلك.

### **يزيل التعداد المتقادم StyleModifyFlag.FontSubscript و FontSuperscript.**

الرجاء استخدام StyleModifyFlag.FontScript بدلاً من ذلك.

### **شكل قديم. خصائص نقاط الاتصال.**

استخدم طريقة GetConnectionPoints () بدلاً من ذلك.

### **يضيف طريقة Shape.GetConnectionPoints ().**

احصل على نقاط الاتصال.

### **يضيف Row.IsCollapsed و Column.IsCollapsed Properties.**

يشير إلى ما إذا كان الصف والعمود مطويًا أم لا.

### **يضيف PasteType.ValuesAndFormats enum.**

يشير فقط إلى نسخ القيم والتنسيقات.

### **يضيف خاصية Shape.IsInGroup.**

يشير إلى ما إذا كان الشكل مجمّعًا أم لا.

### **يضيف طريقة AutoFilter.GetCellArea ().**

يحصل على المنطقة التي ينطبق عليها التصفية التلقائية المحددة.

### **يضيف Cells.GetRowOriginalHeightPoint () طريقة.**

الحصول على ارتفاع الصف الأصلي بوحدة النقاط.

### **يضيف طريقة TimelineCollection.Add (PivotTable pivot ، سلسلة destCellName ، PivotField baseField).**

أضف مخططًا زمنيًا جديدًا باستخدام PivotTable كمصدر بيانات.

### **يضيف طريقة TimelineCollection.Add (PivotTable pivot ، int row ، int عمود ، PivotField baseField).**

أضف مخططًا زمنيًا جديدًا باستخدام PivotTable كمصدر بيانات.

### **يضيف طريقة TimelineCollection.Add (PivotTable pivot ، سلسلة destCellName ، int baseFieldIndex).**

أضف مخططًا زمنيًا جديدًا باستخدام PivotTable كمصدر بيانات.

### **يضيف طريقة TimelineCollection.Add (PivotTable pivot ، int row ، int column ، int baseFieldIndex).**

أضف مخططًا زمنيًا جديدًا باستخدام PivotTable كمصدر بيانات.

### **يضيف طريقة TimelineCollection.Add (PivotTable pivot ، سلسلة destCellName ، سلسلة baseFieldName).**

أضف مخططًا زمنيًا جديدًا باستخدام PivotTable كمصدر بيانات.

### **يضيف DataLabelShapeType.Line enum.**

يمثل شكل الخط. هذا النوع غير متوفر في Excel ، ويستخدم فقط لبعض الملفات الخاصة.
