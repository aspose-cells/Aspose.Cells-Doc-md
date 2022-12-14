---
title: Aspose.Cells for Java 21.3 ملاحظات الإصدار
type: docs
weight: 10
url: /ar/java/aspose-cells-for-java-21-3-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 21.3](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.3/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-43400|دعم وظيفة UNIQUE ()|
|CELLSJAVA-42863|إحضار العنوان الفرعي للمخطط|
|CELLSJAVA-43401|دعم نتيجة التنسيق الموحدة للعصر الياباني لجميع JDKs|
|CELLSJAVA-43398|لا يتم تقديم التنسيق الشرطي بشكل صحيح في تحويل ODS إلى HTML|
|CELLSJAVA-43388|ملف الإخراج تالف بعد نسخ المصنف|
|CELLSJAVA-43406|مشاكل أثناء تحويل HTML إلى Excel|
|CELLSJAVA-43399|تنشئ CalculateFormula () الكثير من قيم نوع الخطأ #VALUE|
|CELLSJAVA-43362|مشكلة النسبة المئوية للملصقات عند طباعة المخططات|
|CELLSJAVA-43384|مشكلة النسب المئوية لبعض الملصقات عند التقديم إلى PDF وطباعة المخططات|
|CELLSJAVA-43402|قم بإنشاء صورة مخطط دقيقة من ملف Excel|
|CELLSJAVA-43408|يتم قطع الجزء العلوي من الرسم البياني ويرتفع الخط المائل|
|CELLSJAVA-43412|CellsException في تحويل xlsx إلى html|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **يضيف خاصية SignatureLine.Id.**

الحصول على أو تعيين معرف لسطر التوقيع هذا.

### **يضيف خاصية DigitalSignature.Id.**

يحدد UUID الذي يمكن الرجوع إليه باستخدام UUID الخاص بسطر التوقيع المخزن في محتوى المستند.

### **يضيف خاصية DigitalSignature.ProviderId.**

يحدد معرف فئة موفر التوقيع.

### **يضيف خاصية DigitalSignature.Image.**

يحدد صورة للتوقيع الرقمي.

### **يضيف خاصية DigitalSignature.Text.**

يحدد نص التوقيع الفعلي في التوقيع الرقمي.

### **يضيف Cells.ClearMergedCells () طريقة.**

يزيل كل الخلايا المدمجة.

### **يضيف طريقة Workbook.RemovePersonalInformation ().**

يزيل جميع المعلومات الشخصية.

### **إضافة خاصية WorkbookSettings.ForceFullCalculate.**

ترشد الخاصية ms excel إلى الحساب بالكامل في كل مرة يتم فيها تشغيل عملية حسابية.

### **يضيف مُنشئ DocxSaveOptions (منطقي).**

يمثل خيارات حفظ ملفات .docx.

### **يحذف خاصية WorkbookSettings.IsWriteProtected القديمة.**

استخدم خاصية WorkbookSettings.WriteProtection.IsWriteProtected بدلاً من ذلك.

### **يحذف WorkbookSettings القديمة.**

استخدم خاصية WorkbookSettings.WriteProtection.RecommendReadOnly بدلاً من ذلك.

### **يحذف WorkbookSettings.WriteProtectedPassword الخاصية القديمة.**

استخدم خاصية WorkbookSettings.WriteProtection.Password بدلاً من ذلك.
