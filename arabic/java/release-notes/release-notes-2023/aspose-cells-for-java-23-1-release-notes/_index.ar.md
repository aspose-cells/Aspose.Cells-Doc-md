---
title: Aspose.Cells for Java 23.1 ملاحظات الإصدار
type: docs
weight: 12
url: /ar/java/aspose-cells-for-java-23-1-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 23.1](https://releases.aspose.com/cells/java/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
| :- | :- | :- |
|CELLSJAVA-44172|دعم الانقطاع أثناء حساب الصيغ لخلية واحدة|
|CELLSJAVA-45029|دعم تكبير الورقة وتجميد الأجزاء عند تصدير واستيراد html|
|CELLSJAVA-45034|كيفية ترميز / استخدام خيار علامة مرشح الصف 1|
|CELLSJAVA-45003|XLS إلى HTML: شكل المستطيل مشوه|
|CELLSJAVA-45004|XLS إلى HTML: تم قص الصورة ونقلها من مكانها|
|CELLSJAVA-44364|الفرق في القيم بين ملف Excel والملف PDF المحول (عبر Aspose.Cells)|
|CELLSJAVA-45026|علامات الاقتباس المزدوجة "من ملف XLSX غير معروض في الملف PDF المحول|
|CELLSJAVA-45035|لا تعمل وظيفة DATEDIF بشكل صحيح مع السنوات الكبيسة|
|CELLSJAVA-45008|تم قطع عناصر وسيلة إيضاح الرسم البياني في صورة الإخراج|
|CELLSJAVA-45036|الانحدار: تم تغيير حجم المخطط بشكل غير صحيح|
|CELLSJAVA-45017|لا يمكن تبديل ورقة العمل في مشروع جافا التجريبي للملف بكلمة مرور|
|CELLSJAVA-44942|فقدت الألوان عند تصدير مخطط إلى EMF|
|CELLSJAVA-45005|لم يتم اختيار الخط مع الاسم الكامل للخط أثناء التحويل إلى pdf|
|CELLSJAVA-45033|ورقة العمل إلى صورة Emf ليست صحيحة بعد تعيين خيار الدقة|
|CELLSJAVA-44971|لا يمكن عرض الصور عند تحميل دفق html|
|CELLSJAVA-45020|HTML إلى EXCEL: تم تغيير الأنماط|
|CELLSJAVA-45021|"com.aspose.cells.CellsException: مرجع ورقة غير صالح للاسم المحدد" عند تقديم ملف Excel إلى PDF|
|CELLSJAVA-45025|ArrayIndexOutOfBoundsException عند حفظ المصنف|

##  **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

###  **يضيف فئة PivotGlobalizationSettings.**

يدير الفصل كل إعدادات العولمة حول الجدول المحوري.

###  **يزيل أسلوب GlobalizationSettings.GetOtherName ().**

لم تتم الإشارة إلى هذه الطريقة بعد الآن ، ولا تؤثر حتى على قيام المستخدم بتنفيذها في GlobalizationSettings. لذلك نقوم بإزالته الآن. يجب على المستخدم استخدام طريقة ChartGlobalizationSettings.GetOtherName () بدلاً من ذلك.

###  **يزيل أساليب GlobalizationSettings.GetColumnLablesName () / GetRowLablesName ().**

الرجاء استخدام PivotGlobalizationSettings.GetTextOfColumnLabels () / GetTextOfRowLabels ().

###  **تقادم جميع الطرق حول الجدول المحوري في إعدادات العولمة.**

الرجاء استخدام الطرق المتوافقة في PivotGlobalizationSettings.

###  **يضيف طريقة SetStyle () لفئة الصف والعمود.**

يدعم تعيين نمط مخصص للصف / العمود بأكمله. لتعيين النمط المخصص ، فإن الاختلاف بين SetStyle () و ApplyStyle () هو أن SetStyle () لا يغير إعدادات النمط للخلايا الموجودة.

###  **إضافة خاصية HasCustomStyle لفئات الصفوف والعمود Cell.**

يشير إلى ما إذا كان قد تم تعيين الخلية أو الصف أو العمود بإعدادات نمط مخصصة (تختلف عن الإعداد الافتراضي الذي يرثه).

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