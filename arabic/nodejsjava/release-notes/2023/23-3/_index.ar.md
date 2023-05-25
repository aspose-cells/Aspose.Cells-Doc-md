---
title: Aspose.Cells for Node.js via Java 23.3 ملاحظات الإصدار
type: docs
weight: 10
url: /ar/nodejs-java/aspose-cells-for-node-js-via-java-23-3-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Node.js via Java 23.3](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-23.3/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
| :- | :- | :- |
|CELLSJAVA-45149|قم بتعديل منطق إنشاء كائن "مجموعة" من كائن smartart|
|CELLSJAVA-45172|دعم loadoption لـ GridWeb|
|CELLSJAVA-45173| دعم هوامش علامة img عند تحميل HTML|
|CELLSJAVA-45110|الصورة المحولة ليست مثل MS Excel.|
|CELLSJAVA-45190|لا يتم استرداد قيم الحقول المحسوبة بواسطة دالة getCalculatedValue ().|
|CELLSJAVA-45056|رسم بياني للصورة - لم يتم عرض الحرف وارتفاع مفتاح الرسم بشكل صحيح|
|CELLSJAVA-45089|يظهر PDF المحول تسميات الرسم التخطيطي في مواقع مختلفة ونقاط المحور غير الصحيحة|
|CELLSJAVA-45141| تسميات البيانات مفقودة من المخطط في المصنف المنسوخ في الإصدار 23|
|CELLSJAVA-45178|عند تحويل xlsx إلى html ، سيطالبك البرنامج بأن خلية البداية لكائن المخطط تحتوي على محتوى '}' غير صالح|
|CELLSJAVA-45195|خط المتسلسلة مفقود في مخطط مبعثر|
|CELLSJAVA-45054|لا يمكن تبديل ورقة العمل للملف المحدد من العميل|
|CELLSJAVA-45143|ملف CSV يختلف مع ملف WPS|
|CELLSJAVA-45072|تعذر قراءة PDF المحول بواسطة Aspose.Cells من ملف MS Excel بشكل طبيعي باستخدام iText|
|CELLSJAVA-45200|إظهار "#" للأرقام في PDF المحولة|
|CELLSJAVA-45159|لا تتم محاذاة النص إلى الوسط أثناء العرض على صورة png|
|CELLSJAVA-41794|يكون HTML خطأ عند إخفاء بعض الصفوف|
|CELLSJAVA-45189|حدد حقل البيانات المحورية لجدول محوري لتطبيق التنسيق عليه|
|CELLSJAVA-45197|مشاكل التنسيق في HTML لتحويل Excel|
|CELLSJAVA-45051| كلمة المرور لا تعمل عند فتح ملف LibreOffice Calc (ODS)|
|CELLSJAVA-44070|استثناء "فهرس صف النهاية غير صالح" في عرض CSV إلى PDF|
|CELLSJAVA-45107|يتم إنشاء استثناء IllegalArgumentException عند تصدير الملفات إلى html|

##  **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

###  **إضافة خاصية CalculationOptions.LinkedDataSources**

يسمح للمستخدم بتعيين مصادر البيانات المرتبطة للروابط الخارجية المستخدمة في صيغة الحساب.

###  **فئة Obsoletes SvgSaveOptions**

الرجاء استخدام فئة ImageSaveOptions بدلاً من ذلك.

###  **Obsoletes مُنشئ SvgSaveOptions ()**

الرجاء استخدام ImageSaveOptions (SaveFormat.Svg) بدلاً من ذلك وتعيين ImageSaveOptions.ImageOrPrintOptions.OnePagePerSheet على true.

###  **عفا عليها الزمن خاصية SvgSaveOptions.SheetIndex**

الرجاء استخدام ImageSaveOptions.ImageOrPrintOptions.SheetSet بدلاً من ذلك.

###  **إضافة تعداد StyleModifyFlag.FontVerticalText**

يشير إلى ما إذا كان النص محاذيًا رأسيًا.

###  **إضافة تعداد WarningType.InvalidOperator**

يمثل عامل التحذير غير الصحيح عند تشغيل ملفات Excel.

###  **يدعم إعداد خصائص Row.GroupLevel و Column.GroupLevel**

يدعم تعيين مستوى مجموعة الصفوف والأعمدة.

###  **Obsoletes HtmlLoadOptions.ConvertFormulasData ويضيف خصائص HtmlLoadOptions.HasFormula**

الرجاء استخدام HtmlLoadOptions.HasFormula بدلاً من ذلك.

###  **عطل PivotGlobalizationSettings.GetTextOfProtection () وإضافة طرق PivotGlobalizationSettings.GetTextOfProtectedName (سلسلة)**

الرجاء استخدام PivotGlobalizationSettings.GetTextOfProtectedName (سلسلة) بدلاً من ذلك.

###  **يضيف طريقة Chart.IsReferedByChart (Int32 و Int32)**

يشير إلى ما إذا كان المخطط يشير إلى هذه الخلية أم لا.

###  **إضافة خاصية PasteOptions.IgnoreLinksToOriginalFile**

لا تربط الملف الأصلي عند نسخ النطاق.

###  **إضافة PivotArea و PivotTableSelectionType و PivotTable.Format (Pivot.PivotArea ، Style)**

حدد المنطقة وقم بتنسيقها في PivotTable.

###  **يضيف خاصية SheetSet.Active**

يحصل على مجموعة مع ورقة نشطة من المصنف.
