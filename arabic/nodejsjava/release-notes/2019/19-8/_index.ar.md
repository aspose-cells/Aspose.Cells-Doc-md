---
title: Aspose.Cells for Node.js via Java 19.8 ملاحظات الإصدار
type: docs
weight: 10
url: /ar/nodejs-java/aspose-cells-for-node-js-via-java-19-8-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار Aspose.Cells for Node.js via Java 19.8.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42861|تعذر الحصول على النص البديل للشكل بتنسيق ملف ODS|حشرة|
|CELLSJAVA-42929|يتغير عنوان الرسم البياني عند تحويل XLSX إلى PDF|حشرة|
|CELLSJAVA-42933|يتغير لون الرسومات أثناء تحويل ملف Excel إلى PDF|حشرة|
|CELLSJAVA-42946|عرض خاطئ للمخطط الشريطي المكدس مع سلسلة إلى PDF|حشرة|
|CELLSJAVA-42942|تمت طباعة الصفحات على مستوى ورقة العمل وليس على مستوى المصنف|حشرة|
|CELLSJAVA-42952|مسافة بادئة خاطئة من أعلى الخلية في بعض الكلمات|حشرة|
|CELLSJAVA-42902|لا يتم نسخ نمط المخطط الشلالي بشكل صحيح أثناء نسخ المصنف|حشرة|
|CELLSJAVA-42939|تم رفع تحذير بواسطة Excel إذا استدعينا Workbook.getVbaProject () فقط لمصنف|حشرة|
|CELLSJAVA-42940|تحذير أمني بعد إزالة جميع البرامج النصية لوحدة VBA|حشرة|
|CELLSJAVA-42955|يؤدي فتح VBAProject إلى إتلاف المصنف|حشرة|
|CELLSJAVA-42945|يطرح الحفظ بتنسيق HTML استثناءً إذا تم تعيين ExportImagesAsBase64|استثناء|
|CELLSJAVA-42953|NullPointerException عند تحويل ملفات XLS إلى HTML|استثناء|
|CELLSJAVA-42951|java.lang.NullPointerException تم طرحه بواسطة comment.setHtmlNote ()|استثناء|
|CELLSJAVA-42954|تم رفع الاستثناء أثناء تحميل ملف XLSX وحفظه|استثناء|
|CELLSJAVA-42957|تم طرح قيمة FontUnderlineType غير صالحة عند حفظ ملف XLSX|استثناء|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على via Java for Node.js Aspose.Cells Aspose.Cells. في منتدى الدعم Aspose.Cells.
#### **يقوم بترقية مكتبة BouncyCastle المشار إليها إلى 1.60**
تمت ترقية مكتبة BouncyCastle المرفقة في أرشيف الإصدارات إلى الإصدار 1.60. ومع ذلك ، فإن Aspose.Cells متوافق مع الإصدارات القديمة أيضًا ، لذلك لا يزال بإمكان المستخدم استخدام الإصدارات القديمة مثل 1.46.
#### **يتخلى عن فئة HTMLLoadOptions ويضيف فئة HtmlLoadOptions**
استخدم فئة HtmlLoadOptions بدلاً من ذلك.
#### **يتخلى عن فئة ODSLoadOptions ويضيف فئة OdsLoadOptions**
استخدم فئة OdsLoadOptions بدلاً من ذلك.
#### **يتخلص من فئة Obsolits JSONUtility ويضيف فئة JsonUtility**
استخدم فئة JsonUtility بدلاً من ذلك.
#### **يضيف واجهة IPageSavingCallback**
التحكم / الإشارة إلى التقدم المحرز في عملية حفظ الصفحة.
#### **يضيف فئة PageSavingArgs**
معلومات لعملية حفظ الصفحة.
#### **يضيف فئة PageStartSavingArgs**
تبدأ معلومات الصفحة في عملية الحفظ.
#### **يضيف فئة PageEndSavingArgs**
المعلومات الخاصة بصفحة ما تنتهي من عملية الحفظ.
#### **يضيف خاصية PdfSaveOptions.PageSavingCallback**
التحكم / الإشارة إلى التقدم المحرز في عملية حفظ الصفحة.

