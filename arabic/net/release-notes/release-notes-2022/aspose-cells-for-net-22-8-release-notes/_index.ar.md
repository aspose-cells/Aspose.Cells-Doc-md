---
title: Aspose.Cells for .NET 22.8 ملاحظات الإصدار
type: docs
weight: 5
url: /ar/net/aspose-cells-for-net-22-8-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 22.8](https://www.nuget.org/packages/Aspose.Cells/22.8.0).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-51589|دعم نمط زر التوسيع / الطي لـ PivotTable|
|CELLSNET-51473|تحويل التعليقات المترابطة إلى html|
|CELLSNET-51570|انسخ ارتفاع الصف عند معالجة العلامات الذكية للجدول|
|CELLSNET-51590|حذف الأشكال المجمعة من المجموعة|
|CELLSNET-51595|محاذاة رأسية خاطئة لنص الخلية عند التحويل إلى PDF من ملف Excel مع جدول محوري|
|CELLSNET-51621|تم نسخ الصيغ المشتركة بشكل غير صحيح لتنسيقات ملفات مختلفة|
|CELLSNET-51524|التفاف كلمة خاطئ عند التحويل إلى PDF من ملف Excel مع جدول محوري|
|CELLSNET-51675|يتم فقد الشكل أثناء التحويل إلى pdf|
|CELLSNET-51435|تتم إضافة علاقات ورقة عمل جديدة عند تحويل مصنف XLSB إلى XLSM|
|CELLSNET-51545|فشل تحميل المصنف مع أوراق حوار MS Excel 5.0 بحلول Aspose.Cells|
|CELLSNET-51546|يتم تكرار المخططات بعد الفتح والحفظ باستخدام Aspose خلية ، ثم عرضها في Excel|
|CELLSNET-51550|يتم حذف الروابط الموجودة في النطاقات المسماة في التحويل XLS إلى XLSM|
|CELLSNET-51551|تلف الملفات وتغير الارتباط الخارجي إلى ارتباط DDE عند تحويل ملفات XLS إلى XLSM|
|CELLSNET-51558|يؤدي تحويل ملفات XLS باستخدام ارتباط نوع xlAlternateStartup إلى XLSM إلى إخراج ملفات تالفة|
|CELLSNET-51564|بيانات مكررة للعلامة الذكية|
|CELLSNET-51574|يتم عرض مربع النص الذي يحتوي على عمودين بداخله بعمود واحد فقط عند إعادة حفظ ملف XLSX|
|CELLSNET-51580|تم تغيير ارتباط خارجي من النوع xlPathMissing إلى نوع ExternalLinkPath عادي في تحويل XLS إلى XLSM|
|CELLSNET-51599|أسماء طويلة جدًا لمصادر نوع الصورة أثناء الحفظ بتنسيق Html|
|CELLSNET-51627|لا يمكن تحميل ملف XLSM محدد|
|CELLSNET-51632|RibbonXml لا يعمل|
|CELLSNET-51696|يؤدي تحويل XLS إلى XLSM إلى تغيير خاصية تعريف اتصال البيانات "حفظ كلمة المرور"|
|CELLSNET-51559|تحويل ملف XLSB إلى XLSM طرح استثناء "لا يمكن أن يكون startIndex أكبر من طول السلسلة"|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **أضف طريقة FontSettingCollection.Replace ().**

استبدل نص الشكل.

### **أضف خاصية ShapeTextAlignment.NumberOfColumns.**

الحصول على عدد أعمدة نص الشكل وتعيينه.

### **أضف خاصية HtmlSaveOptions.ExportCommentsType.**

الحصول على نوع تعليقات التصدير إلى html وتعيينه.

### **أضف فئة أساسية PaginatedSaveOptions لـ PdfSaveOptions و XpsSaveOptions.**

يمثل خيارات ترقيم الصفحات.

### **أضف مجموعة أوراق الفصل.**

يصف مجموعة من الأوراق.

### **إضافة خاصية PaginatedSaveOptions.SheetSet.**

الحصول على الأوراق أو تعيينها للعرض.

### **إضافة خاصية ImageOrPrintOptions.SheetSet.**

الحصول على الأوراق أو تعيينها للعرض.

### **إضافة خاصية GridWeb.IgnoreStyleWithNoData.**

الحصول على أو تعيين ما إذا كان GridWeb يتجاهل إظهار الصفوف أو الأعمدة التي لا تحتوي على قيم خلية ولكنها لا تزال ذات نمط

### **خاصية ImageOrPrintOptions.SaveFormat قديمة.**

بالنسبة لـ Tiff / Svg ، الرجاء استخدام ImageType ؛ بالنسبة إلى Xps ، يرجى استخدام Workbook.Save (سلسلة ، SaveOptions) مع XpsSaveOptions.

### **مُنشئ قديم XpsSaveOptions (Aspose.Cells.SaveFormat saveFormat).**

الرجاء استخدام المُنشئ XpsSaveOptions () بدلاً من ذلك.

### **مُنشئ قديم SvgSaveOptions (Aspose.Cells.SaveFormat saveFormat).**

الرجاء استخدام المُنشئ SvgSaveOptions () بدلاً من ذلك.

### **إزالة المُنشئ PdfSaveOptions (Aspose.Cells.SaveFormat saveFormat).**

يُرجى استخدام المُنشئ PdfSaveOptions () بدلاً من ذلك.
