---
title: Aspose.Cells for .NET 22.11 ملاحظات الإصدار
type: docs
weight: 2
url: /ar/net/aspose-cells-for-net-22-11-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 22.11](https://www.nuget.org/packages/Aspose.Cells/22.11.0).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-52026|دعم نسخ الجدول الزمني|
|CELLSNET-52022|التمييز أو التمييز بين صيغة الصفيف القديمة لمحرك البحث المخصص وصيغة الصفيف العادية|
|CELLSNET-52156|تعطيل خلايا الجدول المدمجة عند حفظ XLSX إلى HTML|
|CELLSNET-52159|دعم تحليل الممتلكات المنهارة عند تحويل HTML إلى Excel|
|CELLSNET-51939|XLSX إلى PDF: اختلال المحتوى|
|CELLSNET-51940|XLS إلى PDF: عدم محاذاة المحتوى في الخلايا|
|CELLSNET-52068|XLSX إلى PDF: الأشكال مفقودة / انهيار الشكل|
|CELLSNET-52092|تم قطع طباعة الأحرف والتباعد في أشكال Excel|
|CELLSNET-52186|تكون الأشكال / المربعات فارغة عند تحويل مستند XLSX إلى PDF|
|CELLSNET-52225|XLSX إلى PDF تم عكس الحروف في مربعات النص|
|CELLSNET-52086|تلف الاتصالات الخارجية في الملف الذي تم إنشاؤه|
|CELLSNET-52133|يتم تغليف صيغ Excel بأقواس معقوفة في ملف xlsb المعاد حفظه|
|CELLSNET-52158|كشف مرجعي دائري غير صحيح|
|CELLSNET-52174|Cell.IsArrayFormula خطأ في صيغة مصفوفة بعد قراءتها من ملف قالب xlsb|
|CELLSNET-52217|تم حساب دالات البحث بشكل غير صحيح لبعض الأرقام الكبيرة|
|CELLSNET-52221|لم يتم سكب صيغة الصفيف الديناميكي بشكل صحيح لـ XLOOKUP|
|CELLSNET-52232|تتم إزالة علامات الاقتباس المفردة من اسم ورقة الارتباط الخارجي|
|CELLSNET-52198|مشكلة متداخلة عند تحويل المخططات إلى ملفات صور|
|CELLSNET-52043|مشكلة عند حساب "PageSetup.Zoom" باستخدام HorizontalPageBreaks|
|CELLSNET-52157|يتداخل حد الصفحة مع النص أثناء التحويل إلى pdf|
|CELLSNET-52118|نتيجة غير متسقة عبر تنسيقات مختلفة عند تعيين html على خلية في OpenOffice و LibreCalc|
|CELLSNET-52125|كان الفهرس خارج النطاق لـ range.copy with picture|
|CELLSNET-52143| يتم تغيير نوع علاقة الارتباط عند تحويل ملف XLS إلى XLSM|
|CELLSNET-52144|من XLS إلى XLSM تحويل نوع علاقة تغيير الارتباط|
|CELLSNET-52151|استبدل حفظ xlsb جميع التعليقات بالتعليق الأخير|
|CELLSNET-52152|قيمة ارتفاع الصف غير صحيحة عند تطبيق عملية صف الاحتواء التلقائي من خلال Aspose.Cells|
|CELLSNET-52155|فقد التنسيق الشرطي بعد نسخ النطاق|
|CELLSNET-52181|XLSX إلى HTML: لم يتم تصدير النطاق Cells بشكل صحيح|
|CELLSNET-52214|يتم اقتطاع محتوى الصف الأخير في ملف Excel الناتج|
|CELLSNET-52236| العلامة الذكية (مجموعة: دمج) لا تعمل للخلايا المدمجة|
|CELLSNET-52241|لا تظهر المربعات (الأشكال) الموجودة في المستند في الإخراج PDF|
|CELLSNET-52243|سيؤدي تعديل مشروع VBA إلى ظهور خطأ عند حفظ المصنف|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **إضافة Cell. خاصية IsDynamicArrayFormula**

الإشارة إلى ما إذا كانت صيغة الخلية هي صيغة صفيف ديناميكية (صواب) أو صيغة صفيف قديمة (خطأ).

### **Obsoletes SparklineGroup.SparklineCollection property ويضيف خاصية SparklineGroup.Sparklines**

استخدم خاصية SparklineGroup.Sparklines بدلاً من ذلك.

### **Obsoletes Worksheet.SparklineGroupCollection وتضيف الخاصية Worksheet.SparklineGroups**

استخدم الخاصية Worksheet.SparklineGroups بدلاً من ذلك.
