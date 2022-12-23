---
title: Aspose.Cells for Java 17.8 ملاحظات الإصدار
type: docs
weight: 50
url: /ar/java/aspose-cells-for-java-17-8-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 17.8](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.8/).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42356|أضف خاصية للإشارة إلى ما إذا كنت تريد إخراج صفحة فارغة أم لا في حالة عدم وجود شيء للطباعة|ميزة جديدة|
|CELLSJAVA-42322|دعم ميزة التصفية المتقدمة (MS Excel) لعرض السجلات التي تلبي معايير معقدة|ميزة جديدة|
|CELLSJAVA-42341|يستغرق InterruptMonitor وقتًا أطول لمقاطعة عملية حفظ المصنف لملف كبير يحتوي على PivotTable|التعزيز|
|CELLSJAVA-42358|لم يتم عرض الصيغة في PDF الناتج|التعزيز|
|CELLSJAVA-42351|ترجع صيغة WEEKDAY قيمة خاطئة في حساب صيغة المصنف|التعزيز|
|CELLSJAVA-42332|Aspose.Cells غير قادر على تحويل الملف HTML بشكل صحيح بينما MS-Excel قادر على تحويله بشكل صحيح|خلل برمجي|
|CELLSJAVA-42355|بالنسبة إلى رقم 39 ، تنسيقات MS Excel قيمة سالبة بـ "-" بدلاً من "()" لإيطاليا|خلل برمجي|
|CELLSJAVA-42350|يتم إزاحة نص التسمية للمخطط الدائري|خلل برمجي|
|CELLSJAVA-42343|لا يتم عرض الأنماط المختلفة لمخطط الشلال بشكل صحيح.|خلل برمجي|
|CELLSJAVA-42342|يعرض مخطط الشلال دائمًا خطوط الاتصال|خلل برمجي|
|CELLSJAVA-42352|لم يتم تحديث الشكل بالقيمة الصحيحة|خلل برمجي|
|CELLSJAVA-42349|تم تعليق تحويل Excel إلى PDF لملف XLSX|خلل برمجي|
|CELLSJAVA-42348|تعذر استيراد ملف XLSB (بواسطة واجهات برمجة تطبيقات Aspose.Cells) إلى قاعدة بيانات MS-Access|خلل برمجي|
|CELLSJAVA-42357|يحدث الاستثناء عند حفظ ملف Excel بتنسيق HTML|استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **إضافة الخاصية HtmlSaveOptions.IsExportComments**
يشير إلى ما إذا كان يتم تصدير التعليقات عند حفظ الملف إلى HTML ، فإن القيمة المفترضة هي false.
### **إضافة الخاصية HtmlSaveOptions.DisableDownlevelRevealedComments**
يشير إلى أنه في حالة تعطيل التعليقات الشرطية ذات المستوى الأدنى عند تصدير ملف إلى HTML ، فإن القيمة الافتراضية هي false.
### **يضيف فئة CustomImplementationFactory**
يوفر API للمستخدم لتوسيع / تحسين قدرة المكون من خلال بعض التطبيقات الخاصة لبعض المواقف الخاصة. لا يوجد حاليًا إصدار for Java معتمد لتنفيذ مخصص.
### **يضيف خاصية CellsHelper.CustomImplementationFactory**
الحصول على / تعيين مثيل CustomImplementationFactory الذي يستخدمه مكون الخلايا.
### **إضافة Workbook.AddDigitalSignature (DigitalSignatureCollection digitalSignatureCollection) طريقة**
يضيف توقيعًا رقميًا إلى ملف جدول بيانات OOXML موقع بالفعل (Excel2007 وما بعده).
### **إضافة خاصية ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**
يشير إلى ما إذا كان سيتم إخراج صفحة فارغة في حالة عدم وجود شيء للطباعة.
### **يضيف طريقة GridCell.CreateComment**
ينشئ كائن تعليق لخلية.
### **يضيف طريقة GridCell.RemoveComment**
يزيل كائن التعليق من الخلية.
### **يضيف طريقة GridCell.GetComment**
يحصل على تعليق الكائن على هذه الخلية.


### **أمثلة على الاستخدام**
يرجى التحقق من قائمة مواضيع المساعدة المضافة في Aspose.Cells مستندات Wiki:

- [أضف التوقيع الرقمي إلى ملف Excel موقع بالفعل](/cells/ar/java/add-digital-signature-to-an-already-signed-excel-file/)
- [تعطيل الكشف عن التعليقات ذات المستوى الأدنى أثناء الحفظ في HTML](/cells/ar/java/disable-downlevel-revealed-comments-while-saving-to-html/)
- [تصدير التعليقات أثناء حفظ ملف Excel إلى Html](/cells/ar/java/export-comments-while-saving-excel-file-to-html/)
- [إخراج صفحة فارغة عندما لا يوجد شيء للطباعة](/cells/ar/java/output-blank-page-when-there-is-nothing-to-print/)
- [إنشاء إزالة والحصول على تعليقات GridCell](/cells/ar/java/create-remove-and-get-gridcell-comments/)
