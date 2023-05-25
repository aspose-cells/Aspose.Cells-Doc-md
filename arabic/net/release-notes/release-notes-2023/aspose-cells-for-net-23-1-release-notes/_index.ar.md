---
title: Aspose.Cells for .NET 23.1 ملاحظات الإصدار
type: docs
weight: 12
url: /ar/net/aspose-cells-for-net-23-1-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 23.1](https://www.nuget.org/packages/Aspose.Cells/23.1.0).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
| :- | :- | :- |
|CELLSNET-50111|دعم الانقطاع أثناء حساب الصيغ|
|CELLSNET-52496|دعم لتغيير النمط الافتراضي للصف / العمود دون تغيير إعدادات النمط للخلايا الموجودة|
|CELLSNET-52505|دعم وظائف جديدة HSTACK / VSTACK|
|CELLSNET-52429|دعم للحصول على المؤلف وتاريخ وقت المراجعات|
|CELLSNET-52337|دعم CHOOSECOLS و CHOOSEROWS Excel 365 الصيغ|
|CELLSNET-52498| تحسين SaveOptions.HasHeaderRow عند تحويل xlsx إلى json|
|CELLSNET-52499|تكون قيمة JSON مفقودة عندما تكون الورقة فارغة|
|CELLSNET-52500|JsonSaveOptions.SkipEmptyRows لا يعمل بشكل صحيح|
|CELLSNET-52502|قم دائمًا بتصدير excel كـ JObject عند تحويل excel إلى json|
|CELLSNET-52418|تعبئة الشكل غير صحيحة أثناء التحويل إلى pdf|
|CELLSNET-52420| تم تشويه الأشكال والصور في Excel إلى تقديم PDF بعد نسخ الورقة|
|CELLSNET-52437|ظل غير صحيح عند تحويل الصورة إلى pdf|
|CELLSNET-52494|خطأ في إزاحة علامة السهم عند تحويل ملف Excel إلى PDF|
|CELLSNET-52442|تُرجع SUMIF محرك حساب الصيغة 4 بدلاً من 0 في Aspose.Cells|
|CELLSNET-52441|الصورة المحولة من خلال الرسم البياني ليست مثل MS excel|
|CELLSNET-52486|ثغرة أمنية - CVE-2021-24112|
|CELLSNET-52410|صورة إلى SVG - النص متراكب للشريط الأفقي لعناوين التاريخ لصورة المخطط|
|CELLSNET-52366| خطوط أكثر سمكًا وحدود مفقودة عند حفظ XLSB في صورة|
|CELLSNET-52395|ملف Excel (XLS) تالف عند إعادة الحفظ عبر Aspose.Cells|
|CELLSNET-52435|دعم معايير التصفية عند فتح وحفظ html|
|CELLSNET-52440|نطاق pivottable ليس مثل MS Excel عند تحويل pivittable إلى pdf|
|CELLSNET-52458|يتم تغيير محتويات الأوراق وتنسيقها أثناء النسخ|
|CELLSNET-52493|استثناء "تمت إضافة العنصر بالفعل." عند حفظ XLS إلى XLSX|
|CELLSNET-48991|مرجع كائن لم يتم تعيين إلى مثيل كائن. استثناء عند فتح ملف ODS|
|CELLSNET-52419|يحدث استثناء خارج النطاق للفهرس بعد نسخ الورقة والتحويل إلى pdf|
|CELLSNET-52433|استثناء "الملف تالف" عند تحميل ملف XLSX به ارتباط تشعبي|

##  **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

###  **يضيف فئة PivotGlobalizationSettings.**

يدير الفصل كل إعدادات العولمة حول الجدول المحوري.

###  **يزيل أسلوب GlobalizationSettings.GetOtherName ().**

لم تتم الإشارة إلى هذه الطريقة بعد الآن ، ولا تؤثر حتى على قيام المستخدم بتنفيذها في GlobalizationSettings. لذلك نقوم بإزالته الآن. يجب على المستخدم استخدام طريقة ChartGlobalizationSettings.GetOtherName () بدلاً من ذلك.

###  **يزيل أساليب GlobalizationSettings.GetColumnLablesName () / GetRowLablesName ().**

الرجاء استخدام PivotGlobalizationSettings.GetTextOfColumnLabels () / GetTextOfRowLabels ().

###  **تقادم جميع الطرق حول الجدول المحوري في إعدادات العولمة.**

الرجاء استخدام الطرق المتوافقة في PivotGlobalizationSettings.

###  **يضيف أساليب GetStyle () / SetStyle () لفئة الصف والعمود.**

يدعم الحصول على / تعيين نمط مخصص للصف / العمود بالكامل. لتعيين النمط المخصص ، فإن الاختلاف بين SetStyle () و ApplyStyle () هو أن SetStyle () لا يغير إعدادات النمط للخلايا الموجودة.

###  **إضافة خاصية HasCustomStyle لفئات الصفوف والعمود Cell.**

يشير إلى ما إذا كان قد تم تعيين الخلية أو الصف أو العمود بإعدادات نمط مخصصة (تختلف عن الإعداد الافتراضي الذي يرثه).

###  **تقادم الصف.النمط والعمود.خصائص النمط**

الرجاء استخدام Row.GetStyle () و Column.GetStyle () بدلاً من ذلك.

###  **يضيف خاصية JsonSaveOptions.AlwaysExportAsJsonObject.**

يشير إلى ما إذا كان يتم دائمًا تصدير ملفات Excel ككائن Json حتى إذا كانت هناك ورقة عمل واحدة فقط.

###  **إضافة فئة RevisionHeader وخاصية RevisionLog.MetadataTable.**

يدعم الحصول على خصائص سجل المراجعة وتعيينها.

###  **يضيف أسلوب Style.GetTwoColorGradientSetting () ويقضي على أسلوب Style.GetTwoColorGradient ().**

استخدم أسلوب Style.GetTwoColorGradientSetting () بدلاً من ذلك.

###  **Obsoletes JsonUtility.ExportRangeToJson (Range، ExportRangeToJsonOptions) ويضيف JsonUtility.ExportRangeToJson (Range، JsonSaveOptions)**

استخدم طريقة ExportRangeToJson (Range ، JsonSaveOptions) بدلاً من ذلك.

###  **يضيف خاصية Charts.Axis.CustomUnit.**

يحدد قيمة مخصصة لوحدة العرض.

###  **الرسوم البيانية المتقادمة. خاصية Axis.CustUnit.**

الرجاء استخدام Charts.Axis.CustomUnit بدلاً من ذلك.

###  **يضيف خاصية Charts.Chart.PlotVisibleCellsOnly.**

يشير إلى ما إذا كان يتم رسم الخلايا المرئية فقط.

###  **الرسوم البيانية القديمة. خاصية Chart.PlotVisibleCells.**

الرجاء استخدام Charts.Chart.PlotVisibleCellsOnly بدلاً من ذلك.

###  **يزيل خاصية ShapeFormat.FillFormat.**

الرجاء استخدام خاصية ShapeFormat.Fill بدلاً من ذلك.

###  **يزيل خاصية ShapeFormat.Outline.**

الرجاء استخدام خاصية ShapeFormat.Line بدلاً من ذلك.
