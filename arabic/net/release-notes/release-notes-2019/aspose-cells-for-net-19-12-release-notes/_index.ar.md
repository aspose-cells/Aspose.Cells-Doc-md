---
title: Aspose.Cells for .NET 19.12 ملاحظات الإصدار
type: docs
weight: 10
url: /ar/net/aspose-cells-for-net-19-12-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 19.12](https://www.nuget.org/packages/Aspose.Cells/19.12.0).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-44451|تطبيق فرز البيانات لحقل البيانات فيما يتعلق بحقل الصف في PivotTable - تقليد النتائج وفقًا لملف المستخدم المتوقع|ميزة جديدة|
|CELLSNETCORE-45|تحميل البيانات من Datasource مع خيار تخطي بعض الأحرف مثل الفاصلة العليا|ميزة جديدة|
|CELLSNET-47018|يمكن أن يؤدي حساب بعض مخططات التحرير والسرد إلى طرح استثناء|التعزيز|
|CELLSNET-47016|يختلف التفاف النص في أحدث إصدار من Aspose.Cells|التعزيز|
|CELLSNET-47023|فقد الرسم البياني أثناء تحميل وحفظ ملف ODS|التعزيز|
|CELLSNET-47056|لم يتم تقديم المخططات أثناء تحميل وحفظ ملف ODS|التعزيز|
|CELLSNET-46679|عرض غير صحيح عند تصدير XLSX إلى PDF|خلل برمجي|
|CELLSNET-46680|رمز الجناح مفقود عند التحويل XLSX إلى PDF|خلل برمجي|
|CELLSNET-46740|خطأ في الصور أثناء تحويل ملف Excel إلى PDF|خلل برمجي|
|CELLSNET-46901|يتغير موضع النموذج ثلاثي الأبعاد|خلل برمجي|
|CELLSNET-46936|لم يتم تقديم الخط بشكل جيد في HTML|خلل برمجي|
|CELLSNET-47013|يختفي Numbers على الرسم البياني القمعي أثناء تحويل ملف Excel إلى PDF|خلل برمجي|
|CELLSNET-43846|يفقد Pivot Table أسماء الحقول المخصصة والإعداد "إظهار القيمة باسم ..."|خلل برمجي|
|CELLSNET-46444|تم تغيير قيمة الجدول المحوري بعد استدعاء PivotTable.CalculateData|خلل برمجي|
|CELLSNET-46484|لا يقوم RefreshData بفرز البيانات قبل فتح الملف في Excel|خلل برمجي|
|CELLSNET-47010|مشكلة في تنسيق رؤوس مجموعات الجدول المحوري|خلل برمجي|
|CELLSNET-47024|ترتيب فرز الصفوف غير صحيح في الجداول المحورية مع صف القيم|خلل برمجي|
|CELLSNET-47034|تم ضغط عرض العمود وارتفاع الصفوف أثناء تحويل HTML إلى Excel|خلل برمجي|
|CELLSNET-47007|يظهر خطأ القيمة أثناء تقييم الصيغة|خلل برمجي|
|CELLSNET-47029|تم استرداد قيمة غير صحيحة TRUE من Cell بدلاً من القيمة FALSE|خلل برمجي|
|CELLSNET-47052|عطب DateTimeFormat أثناء تحويل Excel إلى PDF|خلل برمجي|
|CELLSNET-46757|مشاكل أثناء تحويل XLSX إلى PDF|خلل برمجي|
|CELLSNET-46976|تختفي بعض خطوط الحدود في Excel إلى عرض PDF|خلل برمجي|
|CELLSNET-47000|صورة نتيجة غير ملائمة بواسطة SheetRender من ملف ods المحمي بكلمة مرور|خلل برمجي|
|CELLSNET-47025|لم يتم الكشف عن وحدات الماكرو لـ XLSM|خلل برمجي|
|CELLSNET-47038|لا يتم عرض المخططات الخطية في ملف ODS بشكل جيد عند فتحها أو حفظها عبر Aspose.Cells|خلل برمجي|
|CELLSNET-47045|تعطل تغيير اسم الوحدة النمطية لـ VBA|خلل برمجي|
|CELLSNET-47051|لا يزال المخطط مرتبطًا بورقة العمل الأولى بعد النسخ|خلل برمجي|
|CELLSNET-47053|اكتشاف تنسيق ملف غير صحيح وتعطل العملية أثناء فتح الملف|خلل برمجي|
|CELLSNET-46922|استثناء أثناء تحميل الملف XLS|استثناء|
|CELLSNET-46999|تم طرح استثناء عند عرض ملف ods. "المعلمة غير صالحة."|استثناء|
|CELLSNET-47017|يطرح OpenXML SDK استثناءً عند فتح الملف المحول|استثناء|
|CELLSNET-47022|استثناء عند تحميل تنسيق ملف XLSX|استثناء|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **حذف خاصية DataLabels.BaseField القديمة**
الرجاء استخدام PivotField.BaseFieldIndex بدلاً من ذلك.
#### **يحذف خاصية DataLabels.BaseItem القديمة**
الرجاء استخدام PivotField.BaseItemIndex بدلاً من ذلك.
#### **حذف خاصية DataLabels.IsValueShown القديمة**
استخدم خاصية DataLabels.ShowValue بدلاً من ذلك.
#### **حذف خاصية DataLabels.IsPercentageShown المتقادمة**
استخدم خاصية DataLabels.ShowPercentage بدلاً من ذلك.
#### **حذف خاصية DataLabels.IsBubbleSizeShown القديمة**
استخدم خاصية DataLabels.ShowBubbleSize بدلاً من ذلك.
#### **حذف خاصية DataLabels.IsCategoryNameShown القديمة**
استخدم خاصية DataLabels.ShowCategoryName بدلاً من ذلك.
#### **حذف خاصية DataLabels.IsSeriesNameShown القديمة**
استخدم خاصية DataLabels.ShowSeriesName بدلاً من ذلك.
#### **حذف خاصية DataLabels.IsLegendKeyShown القديمة**
استخدم خاصية DataLabels.ShowLegendKey بدلاً من ذلك.
#### **يضيف خيار LoadOptions.KeepUnparsedData**
يشير الخيار إلى ما إذا كان سيتم الاحتفاظ بالبيانات التي لم يتم تحليلها في الذاكرة للمصنف عند تحميله من ملف القالب. إذا لم يكن المستخدمون بحاجة إلى إعادة حفظ المصنف بالكامل ، خاصةً عندما يحتاجون فقط إلى قراءة بعض المحتوى الخاص بالمصنف (على سبيل المثال بواسطة نوع من LoadFilter) ، فلن تكون هناك حاجة إلى هذه البيانات التي لم يتم تحليلها بعد الآن وقد يقومون بتعيين هذه الخاصية على أنها خاطئة للحصول على أداء أفضل. بالنسبة للإصدارات القديمة ، عند تحميل المصنف من ملف قالب باستخدام LoadFilter المحدد من قبل المستخدم ، لم يتم الاحتفاظ بهذه البيانات غير المحللة للنظر في الأداء. نقدم الآن هذا الخيار ونجعل قيمته الافتراضية صحيحة ، فقد يؤثر ذلك على أداء حالات المستخدمين لاستخدام LoadFilter. إذا كان الأمر كذلك ، يجب على المستخدمين تعيين هذه الخاصية على أنها خطأ بشكل صريح في تطبيقاتهم.
#### **يضيف خيار LoadDataFilterOptions.Picture**
الخيار الذي يشير إلى ما إذا كان يجب تحميل الصورة.
#### **يضيف خيار LoadDataFilterOptions.OleObject**
الخيار الذي يشير إلى ما إذا كان يجب تحميل OleObject.
#### **يضيف خيار LoadDataFilterOptions.Drawing**
الخيار الذي يشير إلى ما إذا كان يجب تحميل الكائنات الرسومية (بما في ذلك التخطيط والصورة و OleObject وكافة الكائنات الرسومية الأخرى).
#### **يتخلى عن خيار LoadDataFilterOptions.Shape**
الرجاء استخدام (LoadDataFilterOptions.Drawing & ~ LoadDataFilterOptions.Chart) بدلاً من LoadDataFilterOptions.Shape.
#### **يضيف فئة FormulaParseOptions**
يوفر خيارات للمستخدم لإعداد الصيغ.
#### **يضيف طرقًا: Cell.SetFormula (صيغة سلسلة ، خيارات FormulaParseOptions ، قيمة الكائن) ، SetArrayFormula (سلسلة مصفوفة ، صيغة int ، rowNumber ، int عمود ، FormulaParseOptions options) ، SetSharedFormula (سلسلة sharedFormula ، int rowNumber ، int columnNumber ، FormionsParse)**
يضبط الصيغ مع الخيارات.
#### **الطرق القديمة: Cell.SetFormula (صيغة سلسلة ، منطقي هو R1C1 ، منطقي isLocal ، قيمة الكائن) ، SetArrayFormula (string arrayFormula ، int rowNumber ، int columnNumber ، bool isR1C1 ، bool isLocal) ، SetSharedFormula (string sharedFormula، int rowNumber ، int row) isR1C1 ، منطقي isLocal)**
استخدم الطرق المقابلة مع FormulaParseOptions بدلاً من ذلك.
#### **يضيف FileFormatType.OTP التعداد**
يدعم الكشف عن تنسيق ملف .OTP.
#### **إضافة خاصية AutoFitterOptions.AutoFitWrappedTextType وتعداد AutoFitWrappedTextType.**
الحصول على نوع النص المغلف المناسب تلقائيًا وتعيينه.
#### **يضيف فئة EmfRenderSetting**
مجموعات لعرض ملف تعريف Emf.
#### **يضيف خاصية PdfSaveOptions.EmfRenderSetting**
مجموعات لتقديم ملف تعريف EMF أثناء التقديم إلى ملف PDF.
#### **يضيف طريقة ShapeCollection.AddSvg ()**
يضيف SVG صورة.
#### **يضيف خاصية WorkbookSettings.QuotePrefixToStyle**
الإشارة إلى ما إذا كان إعداد خاصية Style.QuotePrefix عند إدخال قيمة السلسلة (التي تبدأ بعلامة اقتباس مفردة) في الخلية
#### **إضافة خاصية HtmlSaveOptions.AddTooltipText**
يشير إلى ما إذا كانت إضافة نص تلميح أداة عندما يتعذر عرض البيانات بالكامل. القيمة الافتراضية هي كاذبة.
