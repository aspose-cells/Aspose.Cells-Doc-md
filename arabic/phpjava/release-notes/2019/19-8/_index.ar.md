---
title: Aspose.Cells for PHP via Java 19.8 ملاحظات الإصدار
type: docs
weight: 10
url: /ar/php-java/aspose-cells-for-php-via-java-19-8-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار Aspose.Cells for PHP via Java 19.8.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42861|تعذر الحصول على النص البديل للشكل بتنسيق ملف ODS|خلل برمجي|
|CELLSJAVA-42929|يتغير عنوان الرسم البياني في التحويل XLSX إلى PDF|خلل برمجي|
|CELLSJAVA-42933|يتغير لون الرسومات أثناء تحويل ملف Excel إلى PDF|خلل برمجي|
|CELLSJAVA-42946|عرض خاطئ للمخطط الشريطي المكدس مع المتسلسلة إلى PDF|خلل برمجي|
|CELLSJAVA-42942|تمت طباعة الصفحات على مستوى ورقة العمل وليس على مستوى المصنف|خلل برمجي|
|CELLSJAVA-42952|مسافة بادئة خاطئة من أعلى الخلية في بعض الكلمات|خلل برمجي|
|CELLSJAVA-42902|لا يتم نسخ نمط المخطط الشلالي بشكل صحيح أثناء نسخ المصنف|خلل برمجي|
|CELLSJAVA-42939|تم رفع تحذير بواسطة Excel إذا استدعينا Workbook.getVbaProject () فقط لمصنف|خلل برمجي|
|CELLSJAVA-42940|تحذير أمني بعد إزالة جميع البرامج النصية لوحدة VBA|خلل برمجي|
|CELLSJAVA-42955|يؤدي فتح VBAProject إلى إتلاف المصنف|خلل برمجي|
|CELLSJAVA-42945|يؤدي الحفظ باسم HTML إلى ظهور استثناء إذا تم تعيين ExportImagesAsBase64|استثناء|
|CELLSJAVA-42953|NullPointerException عند تحويل ملفات XLS إلى HTML|استثناء|
|CELLSJAVA-42951|تم طرح java.lang.NullPointerException بواسطة comment.setHtmlNote ()|استثناء|
|CELLSJAVA-42954|تم رفع الاستثناء أثناء تحميل وحفظ XLSX|استثناء|
|CELLSJAVA-42957|تم طرح قيمة FontUnderlineType غير صالحة عند حفظ XLSX|استثناء|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على via Java for PHP Aspose.Cells Aspose.Cells. في منتدى الدعم Aspose.Cells.
#### **يقوم بترقية مكتبة BouncyCastle المشار إليها إلى 1.60**
تمت ترقية مكتبة BouncyCastle المرفقة في أرشيف الإصدارات إلى الإصدار 1.60. ومع ذلك ، فإن Aspose.Cells متوافق مع الإصدارات القديمة أيضًا ، لذلك لا يزال بإمكان المستخدم استخدام الإصدارات القديمة مثل 1.46.
#### **يتخلى عن فئة HTMLLoadOptions ويضيف فئة HtmlLoadOptions**
استخدم فئة HtmlLoadOptions بدلاً من ذلك.
#### **يتخلى عن فئة ODSLoadOptions ويضيف فئة OdsLoadOptions**
استخدم فئة OdsLoadOptions بدلاً من ذلك.
#### **يتخلى عن فئة JSONUtility ويضيف JsonUtilityclass**
استخدم فئة JsonUtilityclass بدلاً من ذلك.
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

