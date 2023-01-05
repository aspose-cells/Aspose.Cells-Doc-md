---
title: Aspose.Cells for .NET 19.7 ملاحظات الإصدار
type: docs
weight: 60
url: /ar/net/aspose-cells-for-net-19-7-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 19.7](https://www.nuget.org/packages/Aspose.Cells/19.7.0).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-42029|دعم لإضافة نوع من حدث / آلية رد الاتصال التي تُعلمك بتقدم التحويل|ميزة جديدة|
|CELLSNET-46791|دعم المزيد من وجهات النظر ولكن ليس العرض المخصص|ميزة جديدة|
|CELLSNET-46808|دعم جدول القراءة خلايا مفردة من ملف XLS.|ميزة جديدة|
|CELLSNET-46775|لا يمكن تعيين عرض الشكل المجمع|التعزيز|
|CELLSNET-46785|تختلف حالة الاختصار عن نفس الكلمات: HtmlSaveOptions و HTMLLoadOptions و JsonLayoutOptions و JSONUtility و ODSLoadOptions و OdsSaveOptions.|التعزيز|
|CELLSNET-46811|دعم علامات HeadingPairs و TitlesOfParts لملف XLS.|التعزيز|
|CELLSNET-46783|CalculateFormula بطيء جدًا|أداء|
|CELLSNET-46746|CalculateFormula - لا تؤثر الصيغ على المخططات|خلل برمجي|
|CELLSNET-46772|تم إنشاء PDF خاطئ بفقدان الرسومات|خلل برمجي|
|CELLSNET-46802|تم عرض الرسم البياني بشكل مختلف في XLS عن PDF|خلل برمجي|
|CELLSNET-46806|يتم عرض مخطط التحرير والسرد إلى PDF بشكل غير صحيح|خلل برمجي|
|CELLSNET-41449|XLSB بملفات PivotTable المعقدة|خلل برمجي|
|CELLSNET-43921|ينتج عن التقديم XLSX إلى XLSB ملف تالف|خلل برمجي|
|CELLSNET-44593|إخراج ملف Excel ليس جيدًا أثناء تحويل HTML إلى Excel|خلل برمجي|
|CELLSNET-46794|Cells تحول عند تحويل HTML إلى XLSX|خلل برمجي|
|CELLSNET-46809|ألغت التنسيقات الشرطية جميع الخلايا في العمود (الأعمدة B و C و D)|خلل برمجي|
|CELLSNET-46778|CalculateFormula () يكسر تصوير UNICHAR ()|خلل برمجي|
|CELLSNET-46781|تم تعديل System.Globalization.CultureInfo.CurrentCulture|خلل برمجي|
|CELLSNET-46244|GridDesktop انسخ والصق مع خروج أخطاء التعليق|خلل برمجي|
|CELLSNET-46774|تم تشويه النص في الصفوف أثناء تحويل ملف كبير إلى PDF|خلل برمجي|
|CELLSNET-46798|مشكلة في تحويل Excel إلى PDF|خلل برمجي|
|CELLSNET-46797|يتم تجاهل نمط الخط المسطر أثناء تقديم ورقة Excel إلى BMP / Tiff|خلل برمجي|
|CELLSNET-46664|تتم استعادة علامات HeadingPairs و TitlesOfParts مرة أخرى بعد تحويل تنسيق الملف المنظف XLS إلى تنسيق ملف XLSM|خلل برمجي|
|CELLSNET-46782|لا تقوم Smart Marker بتحديث مرجع صيغة الورقة المتقاطعة|خلل برمجي|
|CELLSNET-46784|العلامات الذكية - إصدار عرض JSON كائنات قائمة بخصائصها|خلل برمجي|
|CELLSNET-46800|فتح / حفظ يزيل CheckBox.AlternativeText|خلل برمجي|
|CELLSNET-46807|جزء مفقود من النص أثناء التحويل XLS إلى PDF|خلل برمجي|
|CELLSNET-42168|IndexOutOfRangeException: في Workbook.SaveToStream|استثناء|
|CELLSNET-46248|تم طرح استثناء عند قراءة ملف HTML.|استثناء|
|CELLSNET-46792|استثناء عند محاولة حذف أعمدة فارغة في مصنف معين|استثناء|
|CELLSNET-46799|تم رفع الاستثناء أثناء تحويل ملف XLSX إلى PDF|استثناء|
|CELLSNET-46803|استثناء "لم يتم تعيين مرجع الكائن إلى مثيل لكائن" عند تحميل ملف XLSX|استثناء|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **يتخلى عن فئة HTMLLoadOptions ويضيف فئة HtmlLoadOptions**
استخدم فئة HtmlLoadOptions ، بدلاً من ذلك.
#### **يتخلى عن فئة ODSLoadOptions ويضيف فئة OdsLoadOptions**
استخدم فئة OdsLoadOptions ، بدلاً من ذلك.
#### **يتخلص من فئة Obsolits JSONUtility ويضيف فئة JsonUtility**
استخدم فئة JsonUtility بدلاً من ذلك.
#### **تحديث مساحة الاسم Aspose.Cells.ODS كـ Aspose.Cells.Ods وتحديث ODS * الفئات / التعدادات / الخصائص كـ Ods**
استخدم فئات / تعدادات / خصائص محدثة ، بدلاً من ذلك.
#### **يضيف واجهة IPageSavingCallback**
التحكم / الإشارة إلى التقدم المحرز في عملية حفظ الصفحة.
#### **يضيف فئة PageSavingArgs**
معلومات لعملية حفظ الصفحة.
#### **يضيف فئة PageStartSavingArgs**
تبدأ معلومات الصفحة في عملية الحفظ.
#### **يضيف فئة PageEndSavingArgs**
معلومات لصفحة تنتهي عملية الحفظ.
#### **يضيف خاصية PdfSaveOptions.PageSavingCallback**
التحكم / الإشارة إلى التقدم المحرز في عملية حفظ الصفحة.
