---
title: Aspose.Cells for PHP via Java 21.10 ملاحظات الإصدار
type: docs
weight: 3
url: /ar/php-java/aspose-cells-for-php-via-java-21-10-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for PHP via Java 21.10](https://downloads.aspose.com/cells/php/new-releases/aspose.cells-for-php-via-java-21.10/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-43768|Java لوحظ مشكلة مساحة الكومة أثناء تحويل ملف XLSX إلى PDF|
|CELLSJAVA-43875|استثناء "Val FontUnderlineType string غير صالح" عند تحميل ملف XLSX|
|CELLSJAVA-43876|استثناء "java.lang.ArrayIndexOutOfBoundsException" عند تحميل ملف XLSX|
|CELLSJAVA-43646|لم يتم تقديم تأثير الظل للنص بشكل صحيح|
|CELLSJAVA-43760|اتجاه المثلث متساوي الساقين غير صحيح|
|CELLSJAVA-43786|عند تحويل ملف XLS إلى XLSX ، لا يتم تقديم بعض الأجزاء المتعلقة بالأشكال بشكل صحيح|
|CELLSJAVA-43838|بعد تنفيذ XlsToXlsx ، يتم فقد الشكل التلقائي|
|CELLSJAVA-43839|بعد تنفيذ XlsToXlsx ، يتم فقد LeftBracket|
|CELLSJAVA-43842|بعد تنفيذ XlsToXlsx ، يختلف شكل LeftBracket عن الشكل الأصلي|
|CELLSJAVA-43848|تحويل Excel إلى PDF - لا يتم تغليف بعض أحرف WordArt بنفس الطريقة كما في ملف Excel|
|CELLSJAVA-43880|الزوايا الدائرية غير الصحيحة لمربع النص بعد تحويل xls إلى xlsx|
|CELLSJAVA-43867|تختلف أيقونة التنسيق الشرطي عند التصدير إلى html|
|CELLSJAVA-43812|excelToHtml: إزاحة موضع الشكل غير صحيحة|
|CELLSJAVA-43871|لا يتم عرض كائنات Prism 9 OLE في ملف PDF الناتج|
|CELLSJAVA-43883|أحجام الصفحات المعروضة غير صحيحة|
|CELLSJAVA-43881|يؤدي دمج الملفات إلى فقد إعداد لون الخلفية للأوراق|
|CELLSJAVA-43892|حدود Excel المحولة إلى HTML مفقودة|
|CELLSJAVA-43787|استثناء "IllegalArgumentException: أطوال الشرطة كلها صفر ..." في عرض Excel إلى HTML|
|CELLSJAVA-43885|IllegalArgumentException أثناء تحويل ملف Excel|
|CELLSJAVA-43874|يطرح Workbook.save استثناء على ملف معين بواسطة Aspose.Cells فقط عند تطبيق ترخيص Aspose|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **يضيف طريقة التحميل الزائد Name.GetRefersTo ().**

الحصول على تعبير الصيغة بناءً على الخلية المحددة.

### **يضيف طريقة ذات حمل زائد Range.AutoFill ().**

ملء النطاق المستهدف تلقائيًا بنوع التعبئة.

### **يضيف Comment.IsThreadedComment.**

يشير إلى ما إذا كان هذا التعليق هو تعليق مترابط.

### **إضافة الخاصية HtmlSaveOptions.IgnoreInvisibleShapes.**

يشير إلى ما إذا كان يتم إدخال أشكال غير مرئية عند حفظ html.

### **يضيف خاصية Range.CurrentRegion.**

يُرجع نطاقًا محددًا بأي مجموعة من الصفوف الفارغة والأعمدة الفارغة.

### **يضيف فئة AxisBins.**

 يمثل حاويات المحور لمخططات المدرج التكراري.

### **أسلوب قديم ، SheetRender.GetPageSize (int pageIndex)**

استخدم SheetRender.GetPageSizeInch (int pageIndex) بدلاً من ذلك.

### **يضيف طريقة SheetRender.GetPageSizeInch (int pageIndex)**

الحصول على حجم الصفحة من صورة الإخراج؟ في وحدة من البوصة.

### **يضيف طريقة WorkbookRender.GetPageSizeInch (int pageIndex)**

الحصول على صورة حجم الصفحة الإخراج؟ في وحدة من البوصة.

