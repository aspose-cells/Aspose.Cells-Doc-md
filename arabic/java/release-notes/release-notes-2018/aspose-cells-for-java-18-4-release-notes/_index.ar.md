---
title: Aspose.Cells for Java 18.4 ملاحظات الإصدار
type: docs
weight: 90
url: /ar/java/aspose-cells-for-java-18-4-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار Aspose.Cells for Java 18.4.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42523|استخدم إصدارًا متوافقًا مع FIPS من Bouncy Castle في Aspose.Cells APIs|ميزة جديدة|
|CELLSJAVA-42572|يجب ألا تحتوي الصيغة على أكثر من 8192 حرفًا|التعزيز|
|CELLSJAVA-42569|تعذر الوصول إلى عناصر تسميات محور الفئة الأفقية في المخطط في XLS|التعزيز|
|CELLSJAVA-42580|الحصول على / تعيين خاصية مستند اللغة|التعزيز|
|CELLSJAVA-42565|لون المقدمة مقابل لون الخلفية مقابل لون التعبئة - استخدم طريقة واحدة تأخذ وسيطتين|التعزيز|
|CELLSJAVA-42528|"<Font>"ليست علامة HTML5 صالحة ، كما أن علامة الإغلاق الذاتي ومتصفحات الويب تحرف محتوياتها|التعزيز|
|CELLSJAVA-42413|أدخل نوع صورة SVG في خلايا ورقة العمل بواسطة Aspose.Cells|التعزيز|
|CELLSJAVA-42551|بعض الأشكال غير صحيحة في الإخراج PDF|خلل برمجي|
|CELLSJAVA-42578|يتم فقد التنسيق الشرطي أثناء حفظ Excel بالرقم HTML|خلل برمجي|
|CELLSJAVA-42571|الإخراج HTML لا يتطابق مع MS-Excel|خلل برمجي|
|CELLSJAVA-42553|الروابط إلى المنطقة المحددة خاطئة بعد التصدير إلى HTML|خلل برمجي|
|CELLSJAVA-42530|لا تحتوي الجداول المحورية والمخططات المقابلة لها على تنسيق تاريخ صحيح|خلل برمجي|
|CELLSJAVA-42527|يحتوي الرسم البياني على العديد من القيم في المحور x وتتداخل القيم مع بعضها البعض|خلل برمجي|
|CELLSJAVA-42581|تقوم Aspose.Cells بإرجاع قيمة خاطئة للخلية A2|خلل برمجي|
|CELLSJAVA-42583|لا يُنشئ مخطط XML الجدول بشكل صحيح|خلل برمجي|
|CELLSJAVA-42577|الحصول على / استخراج القيم (0 لـ 0 وفارغ للفراغ) باستخدام طريقة DataPoint.getYValue () لمخطط معين|خلل برمجي|
|CELLSJAVA-42566|عكس الترجمات (إدخالات وسيلة الإيضاح) في مخطط MS Excel|خلل برمجي|
|CELLSJAVA-42560|الأسهم مفقودة في إخراج PNG من مخطط Excel|خلل برمجي|
|CELLSJAVA-42508|تعمل طريقة Java 'Shape.toImage' بشكل مختلف بنفس الطريقة في .NET|خلل برمجي|
|CELLSJAVA-42573|Aspose.Cells 18.3 دوران مربع نص لا يعمل مع EXCEL_97_TO_2003 حفظ التنسيق|خلل برمجي|
|CELLSJAVA-42570|يظهر سطر جديد فارغ داخل TextBox بعد معالجة ملف Excel وحفظه|خلل برمجي|
|CELLSJAVA-42563|استثناء "java.lang.NullPointerException" عند التوقيع الرقمي على ملف XLSX|استثناء|
# **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **إضافة عنصر جديد "CrossHideRight" لتعداد HtmlCrossType**
يعرض HTML السلسلة المتقاطعة ويخفي السلسلة اليمنى عند تراكب النص.
#### **إضافة عنصر جديد "TSV" لتعدادات LoadFormat و SaveFormat و FileFormatType**
يمثل ملف TSV (قيم مفصولة بعلامات جدولة) ، مثله مع "TabDelimited".
#### **يضيف تعداد ImageType**
يمثل نوع الصورة.
#### **إضافة خصائص MsoTextFrame.RotateTextWithShape و ShapeTextAlignment.RotateTextWithShape**
يشير إلى ما إذا كان النص سيتم تدويره مع الشكل.
#### **إضافة خصائص OleObject.ImageType و Picture.ImageType**
يحصل على تنسيق صورة الصورة.
#### **عفا عليها الزمن OleObject.ImageFormat و Picture.ImageFormat خصائص**
استخدم خصائص OleObject.ImageType و Picture.ImageType بدلاً من ذلك.
#### **يضيف طريقة التحميل الزائد AutoFilter.Refresh (System.Boolean)**
يحصل على جميع فهارس الصفوف المخفية ويقوم بتحديث التصفية التلقائية.
#### **يضيف طريقة التحميل الزائد Cell.GetHtmlString (System.Boolean)**
الحصول على السلسلة HTML التي تحتوي على بيانات وبعض التنسيقات في هذه الخلية.
#### **إضافة خاصية BuiltInDocumentPropertyCollection.Language**
الحصول على لغة الملف وتعيينها.
#### **يضيف Style.SetPatternColor (Aspose.Cells.BackgroundType ، System.Drawing.Color ، System.Drawing.Color)**
يضبط نمط الخلية ولونها
#### **إضافة خاصية ChartPoint.XValueType**
يحصل على نوع القيمة X لنقطة المخطط.
#### **إضافة خاصية ChartPoint.YValueType**
الحصول على نوع القيمة Y لنقطة المخطط.
#### **إضافة تعداد PageLayoutAlignmentType**
يمثل أنواع محاذاة تخطيط الصفحة.
#### **إضافة طريقة Chart.ToPdf (System.IO.Stream، System.Single، System.Single، Aspose.Cells.PageLayoutAlignmentType، Aspose.Cells.PageLayoutAlignmentType)**
لتكوين PDF الرسم البياني بحجم الصفحة المطلوب وحفظه في التدفق.
#### **إضافة طريقة Chart.ToPdf (System.String، System.Single، System.Single، Aspose.Cells.PageLayoutAlignmentType، Aspose.Cells.PageLayoutAlignmentType)**
لتكوين PDF الرسم البياني بحجم الصفحة المطلوب وحفظه في ملف.
#### **يضيف خاصية PdfSaveOptions.OutputBlankPageWhenNothingToPrint**
يشير إلى ما إذا كان سيتم إخراج صفحة فارغة في حالة عدم وجود شيء للطباعة.
