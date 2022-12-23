---
title: Aspose.Cells for .NET 8.5.1 ملاحظات الإصدار
type: docs
weight: 60
url: /ar/net/aspose-cells-for-net-8-5-1-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 8.5.1](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.5.1/)

{{% /alert %}}

فيما يلي قائمة بالتحسينات والتغييرات في هذا الإصدار من Aspose.Cells

## 1) Aspose.Cells

### **تحسينات وتغييرات أخرى**

### **ميزات جديدة**

(CELLSNET-43703) - وظيفة ICustomFunction - إرجاع نطاق بدلاً من خلية واحدة

(CELLSNET-43777) - Cell. GetHeightOfValue () مماثلة لـ Cell. GetWidthOfValue () needed

### **البق**

(CELLSNET-43744) - لا يتم تحديث PivotTable عند الحفظ في PDF

(CELLSNET-43735) - تم فقد خيار الصفوف ذات النطاق المحوري للجدول المحوري

(CELLSNET-43759) - الجدول المحوري لا يحتفظ بالفرز عند الدمج

(CELLSNET-43721) - تنبثق رسالة الخطأ بعد حفظ المصنف

(CELLSNET-43724) - القيم غير صحيحة عندما تتغير البيانات

(CELLSNET-43719) - قيمة مختلفة بعد حساب الصيغة

(CELLSNET-43713) - مصنف لا يحسب القيم الصحيحة

(CELLSNET-43708) - استدعاء ورقة العمل. يغير GetPrintingPageBreaks عرض مربع النص

(CELLSNET-43695) - Cell.RemoveArrayFormula لا يزيل صيغة الصفيف

(CELLSNET-41874) - بناء جملة Excel غير مدعوم للصيغ

(CELLSNET-43753) - Aspose.Cells يتم عرض صفحتين

(CELLSNET-43731) - يتم قطع النص أثناء تقديم ورقة العمل إلى صورة EMF

(CELLSNET-43756) - لا تحتوي صورة الرسم البياني على نفس قيم المحور x من مخطط Excel

(CELLSNET-43728) - يؤدي تحديث PivotTable ببيانات جديدة إلى تغيير نمط لون المخطط

(CELLSNET-43726) - يؤدي دمج مصنفات العمل إلى تغيير نمط المخطط

(CELLSNET-43700) - يبدو لون الصورة مختلفًا بعد التحويل إلى PDF

(CELLSNET-43199) - تتغير المحتويات والأشكال عندما يتم حفظ Excel في PDF

(CELLSNET-43767) - يعرض Excel طريقة العرض المحمية على Aspose.Cells جدول البيانات المحفوظ

(CELLSNET-43762) - Cell.GetPrecedents () لا يقوم بإرجاع اسم ورقة العمل الصحيح

(CELLSNET-43761) - يتغير لون الخلفية للخلايا المنسقة شرطيًا

(CELLSNET-43760) - قواعد التنسيق الشرطي تالفة

(CELLSNET-43742) - سلوك حماية مصنف غير متسق

(CELLSNET-43734) - لا يمكن لبرنامج Excel فتح الملف بعد التحويل من XLSM إلى XLS

(CELLSNET-43727) - يتسبب دمج المصنفات في ظهور تحذير Excel "لا يمكن تحرير PivotTable في وضع تحرير المجموعة"

### **استثناءات**

(CELLSNET-43768) - حدث خطأ غير معروف أثناء نسخ ورقة العمل من مصنف آخر

(CELLSNET-43716) - خطأ من شكل إلى صورة عند التحويل إلى PDF

(CELLSNET-43764) - NullReferenceException at Workbook ctor مع جدول بيانات محفوظ كـ Strict OpenXML

(CELLSNET-43740) - System.IndexOutOfRangeException at Workbook.Save

## 2) مجموعة الشبكة Aspose.Cells

### **تحسينات وتغييرات أخرى**

### **ميزات جديدة**

(CELLSNET-42783) - يؤدي الارتباط بالمصنف الخارجي إلى إنشاء #REF! في GridDesktop

(CELLSNET-41744) - شاشة من اليمين إلى اليسار

### **البق**

(CELLSNET-43730) - الفرق بين GridWeb.ActiveCell و GridWeb.WorkSheets [0] .ActiveCell

(CELLSNET-43175) - خطأ X أحمر عشوائي في GridDesktop

(CELLSNET-42321) - تنسيق رقم مخصص غير مطابق لـ Excel في Aspose.Cells.GridDesktop

(CELLSNET-43763) - طرق مفقودة في Aspose.Cells.GridDesktop

(CELLSNET-43774) - الوضع الجديد GridDesktop: عدم عرض الحدود بشكل صحيح في الخلايا المدمجة

### **استثناءات**

(CELLSNET-43670) - استثناء System.Argument في GridDesktop. ImportExcelFile

### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

إضافة تعداد TableDataSourceType و ListObject.DataSourceType

يتم استخدامه للحصول على نوع مصدر البيانات للجدول.

يضيف طريقة Workbook.Dispose ().

يتم استخدامه لتحرير الموارد غير المدارة.

يضيف Cell.GetHeightOfValue () طريقة.

يتم استخدامه للحصول على ارتفاع القيمة بوحدة البكسل.
