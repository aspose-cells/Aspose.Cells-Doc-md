---
title: Aspose.Cells for Java 8.8.1 ملاحظات الإصدار
type: docs
weight: 100
url: /ar/java/aspose-cells-for-java-8-8-1-release-notes/
---
## **1) Aspose.Cells**

|**مفتاح** |**ملخص** |**فئة** |
|:- |:- |:- |
|CELLSJAVA-41664 |تصدير أشرطة البيانات على أساس التنسيق الشرطي إلى HTML| ميزة جديدة|
|CELLSJAVA-40746 | دعم ColorScale و DataBar و IconSet أثناء تصدير XLSX إلى HTML| ميزة جديدة|
|CELLSJAVA-41820 | لا تحتوي ورقة العمل على طريقة calcualteFormula (صيغة سلسلة ، خيارات CalculationOptions)| ميزة جديدة|
|CELLSJAVA-40544 | اختناق الأداء في Workbook.calculateFormula| التعزيز|
|CELLSJAVA-41817 | يبدو أن إعداد ShowAllItems لـ PivotField غير ساري المفعول| حشرة|
|CELLSJAVA-41810 | يصبح النص مزدحمًا ومتداخلاً في صورة EMF| حشرة|
|CELLSJAVA-41801 | تتداخل تسميات النص في صورة EMF| حشرة|
|CELLSJAVA-41834 | تم طرح استثناء عند نسخ المصنف| حشرة|
|CELLSJAVA-41819 | جدول بيانات إلى HTML: تعد محاذاة النص في شكل خاطئة بعد نسخ السمة من جدول البيانات المصدر| حشرة|
|CELLSJAVA-41824 | لا يتم تقديم الرسم البياني في ملف PDF الناتج| حشرة|
|CELLSJAVA-41805 | تسميات المحور X مفقودة في ملف PDF للمخطط| حشرة|
|CELLSJAVA-41767 | تنسيق رقم غير صحيح لتسميات المحور X في ملف PDF للمخطط| حشرة|
|CELLSJAVA-41640 | لا يتم عرض الواصلات الطويلة بشكل مناسب في ملف PDF / صورة للمخطط| حشرة|
|CELLSJAVA-41604 | لا تظهر خطوط الشبكة الأفقية للمخطط بشكل صحيح في ملف PDF الناتج| حشرة|
|CELLSJAVA-41832 |بعض أشرطة المخطط مفقودة أثناء عرض ورقة العمل على صورة| حشرة|
|CELLSJAVA-41837 | أضف Chart.toPDF (java.io.OutputStream ، com.aspose.cells.PdfSaveOptions)| حشرة|
|CELLSJAVA-41839 | يتم إنشاء نطاق مسمى عند استخدام أسلوب Cells.copyRow () داخل نطاق مسمى| حشرة|
|CELLSJAVA-41838 | عند تطبيق autoSizeColumns على الورقة ، لا يتم توسيع العمود بشكل صحيح| حشرة|
|CELLSJAVA-41835 | CellsException أثناء حفظ جدول البيانات في PDF| استثناء|
|CELLSJAVA-41826 | استثناء NaN| استثناء|
## **2) مجموعة الشبكة Aspose.Cells**

|**مفتاح** |**ملخص** |**فئة** |
|:- |:- |:- |
|CELLSJAVA-41719 | كيفية إنشاء أزرار أوامر مخصصة في GridWeb (جافا)| ميزة جديدة|
|CELLSJAVA-41718 | أسلوب GridCell.createValidation () مفقود في GridWeb| التعزيز|
|CELLSJAVA-41649 | لا يتوقف التمرير أحيانًا - Aspose.Cells.GridWeb لـ JAVA| حشرة|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يضيف خاصية WorkbookSettings.PaperSize.**
يتم استخدامه لتعيين حجم ورق الطابعة الافتراضية كحجم ورق افتراضي للمصنف.
### **إضافة فئة LoadDataFilterOptions وخاصية LoadOptions.LoadDataFilterOptions.**
يتم استخدامه لتحديد نوع البيانات التي يجب تحميلها عند إنشاء المصنف من ملف القالب. يمكن أن تؤدي تصفية البيانات المحملة إلى تحسين الأداء للأغراض الخاصة للمستخدم ، لا سيما عند استخدام واجهات برمجة تطبيقات LightCells.
### **يضيف طريقة Worksheet.CalculateFormula (صيغة سلسلة ، CalculationOptions).**
يتم استخدامه لحساب صيغة معينة مباشرة باستخدام خيارات مخصصة للمستخدم.
### **إضافة فئات من مساحة الاسم Aspose.Cells.Drawing.Texts.**
يتم استخدامه لتعيين خصائص خط نص الشكل.
### **خاصية Shape.TextFrame قديمة.**
استخدم خاصية Shape.TextBody.TextAlignment بدلاً من ذلك.
### **يضيف خاصية Shape.TextBody.**
يقدم إعداد نص الشكل.
### **يضيف أسلوب GridCell.CreateValidation (GridValidationType ValidationType ، bool isRequired).**
ينشئ كائن تحقق لخلية شبكة.
### **يضيف أسلوب GridCell.RemoveValidation ().**
يزيل كائن التحقق من الصحة من خلية شبكة.
### **يضيف طريقة Chart.ToPdf (دفق System.IO.Stream).**
يضيف حفظ الرسم البياني إلى PDF كتدفق.

{{% alert color="primary" %}} 

نظرًا لأن قاعدة الكود Aspose.Cells for Java تطابق رمز إصدار .NET ذي الصلة ، فإن معظم التغييرات والتحسينات والإصلاحات المضمنة في Aspose.Cells for .NET v8.8.1 مدرجة أيضًا في Aspose.Cells for Java v8.8.1.

{{% /alert %}}
