---
title: Aspose.Cells for Java 20.1 ملاحظات الإصدار
type: docs
weight: 60
url: /ar/java/aspose-cells-for-java-20-1-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 20.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.1/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-41325|تقوم طريقة التحقق من صحة Cell.getValidation بإرجاع قيمة خالية لـ ODS|ميزة جديدة|
|CELLSJAVA-43074|XLSX إلى PDF ، الفرق في الإخراج PDF عند استخدام Oracle JDK مقابل Open JDK|التعزيز|
|CELLSJAVA-43083|لا يتم تطبيق التعتيم على المخططات العمودية|خلل برمجي|
|CELLSJAVA-41879|٪ of و٪ من الصف و٪ من ParentRowTotal و٪ ParentTotal وما إلى ذلك لا تعمل في إخراج Excel المحوري|خلل برمجي|
|CELLSJAVA-43062|لون الخلفية الافتراضي لـ Cell غير صحيح في الإخراج HTML|خلل برمجي|
|CELLSJAVA-43063|إخراج SheetRender.toImage () غير صحيح|خلل برمجي|
|CELLSJAVA-43070|calculateFormula () لا يحسب القيمة|خلل برمجي|
|CELLSJAVA-43086|تم تطبيق نمط تنسيق النسبة المئوية بشكل غير صحيح ضمن اللغة النرويجية|خلل برمجي|
|CELLSJAVA-43082|يتم عرض خط أصغر في كل صف أول من الجدول|خلل برمجي|
|CELLSJAVA-41360|يتم عرض Cells بالصيغ داخل PDF بينما لا يتم عرضها داخل ODS|خلل برمجي|
|CELLSJAVA-42786|ODS إلى XLSX - يفقد الرسم البياني الخطي إدخالات الخطوط ومفاتيح الرسم البياني|خلل برمجي|
|CELLSJAVA-42788|ODS إلى XLSX - تصبح الدائرة مربعة|خلل برمجي|
|CELLSJAVA-43073|لا يمكن الوصول إلى معلومات DataMashup في المصنف|خلل برمجي|
|CELLSJAVA-43092|لا يمكن معالجة ملف Excel|خلل برمجي|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يضيف خاصية ReplaceOptions.RegexKey.**
 يشير إلى ما إذا كان المفتاح الذي تم البحث عنه هو regex أم لا. إذا**حقيقي**ثم سيتم اعتبار المفتاح الذي تم البحث عنه (الذي سيتم استبدال جزء منه) بمثابة regex محدد من قبل المستخدم.
### **يحذف طريقة ValidationCollection.Add (Aspose.Cells.Validation) القديمة.**
استخدم طريقة ValidationCollection.Add (CellArea) بدلاً من ذلك.
### **إضافة خاصية PowerQueryFormula.FormulaDefinition.**
يحصل على تعريف صيغة استعلام الطاقة.
### **إضافة خاصية DBConnection.PowerQueryFormula.**
يحصل على تعريف صيغة استعلام الطاقة.
### **إضافة الخاصية HtmlSaveOptions.ExportHeadings.**
يشير إلى ما إذا كان تصدير العناوين عند حفظ الملف في HTML. القيمة المفترضة هي false. إذا كنت تريد استيراد ملف HTML إلى Excel ، فيرجى الاحتفاظ بالقيمة الافتراضية.
### **يضيف فئة XAdESType**
نوع التوقيع الإلكتروني المتقدم بتنسيق XML (XAdES).
### **يضيف خاصية DigitalSignature.XAdESType**
الحصول على نوع التوقيع الإلكتروني المتقدم لـ XML (XAdES) وتعيينه. القيمة الافتراضية هي بلا (XAdES قيد إيقاف التشغيل).
