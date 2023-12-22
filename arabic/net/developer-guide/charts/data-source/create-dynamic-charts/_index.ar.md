---
title: إنشاء الرسوم البيانية الديناميكية
description: تعرف على كيفية إنشاء مخططات ديناميكية في Aspose.Cells for .NET. سيوضح لك دليلنا كيفية تحديث بيانات المخطط والسلاسل والتنسيق ديناميكيًا بناءً على متطلباتك، مما يسمح لك بتقديم البيانات المتغيرة بشكل مرئي في أوراق العمل الخاصة بك.
keywords: Aspose.Cells for .NET, charting, dynamic charts, data, series, formatting, worksheets, updating.
type: docs
weight: 240
url: /ar/net/create-dynamic-charts/
---
{{% alert color="primary" %}}

تتمتع المخططات الديناميكية (أو التفاعلية) بالقدرة على التغيير عند تغيير نطاق البيانات. بمعنى آخر، يمكن أن تعكس المخططات الديناميكية التغييرات تلقائيًا عند تغيير مصدر البيانات. من أجل إحداث التغيير في مصدر البيانات، يمكن للمرء استخدام خيار التصفية في جداول Excel أو استخدام عنصر تحكم مثل ComboBox أو القائمة المنسدلة.

توضح هذه المقالة استخدام واجهات برمجة التطبيقات Aspose.Cells for .NET لإنشاء مخططات ديناميكية باستخدام كلا الطريقتين المذكورتين أعلاه.

{{% /alert %}}

##  **استخدام جداول إكسل**

{{% alert color="primary" %}}

 يُشار إلى جداول Excel باسم ListObjects في المنظور Aspose.Cells، لذلك، سنستخدم المصطلح "ListObject" بدلاً من "Table" للتوضيح. يرجى القراءة بالتفصيل حول كيفية القيام بذلك[إنشاء كائنات القائمة](/cells/ar/net/create-and-format-table/)مع Aspose.Cells for .NET API.

{{% /alert %}}

 توفر ListObjects وظيفة مدمجة لفرز البيانات وتصفيتها عند تفاعل المستخدم. يتم توفير كل من خيارات الفرز والتصفية من خلال القوائم المنسدلة التي تتم إضافتها تلقائيًا إلى صف رأس الصفحة[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) . ونظرًا لهذه الميزات (الفرز والتصفية)، فإن[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) يبدو أنه المرشح المثالي ليكون بمثابة مصدر البيانات لمخطط ديناميكي لأنه عند تغيير الفرز أو التصفية، سيتم تغيير تمثيل البيانات في المخطط ليعكس الحالة الحالية للمخطط[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

 من أجل إبقاء العرض التوضيحي سهل الفهم، سنقوم بإنشاء[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)من الصفر والمضي قدمًا خطوة بخطوة كما هو موضح أدناه.

1.  إنشاء فارغة[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  الوصول إلى[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) من الأول[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) في ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. أدخل بعض البيانات في الخلايا.
1.  يخلق[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)بناء على البيانات المدرجة.
1.  يخلق[**جدول**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) استنادا إلى نطاق البيانات[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. احفظ النتيجة على القرص.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

##  **استخدام الصيغ الديناميكية**

في حالة عدم رغبتك في استخدام[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)كمصدر بيانات للمخطط الديناميكي، فإن الخيار الآخر هو استخدام وظائف Excel (أو الصيغ) لإنشاء نطاق ديناميكي من البيانات، وعنصر تحكم (مثل ComboBox) لتشغيل التغيير في البيانات. في هذا السيناريو، سوف نستخدم الدالة VLOOKUP لجلب القيم المناسبة بناءً على تحديد ComboBox. عند تغيير التحديد، ستقوم وظيفة VLOOKUP بتحديث قيمة الخلية. إذا كان نطاق من الخلايا يستخدم وظيفة VLOOKUP، فيمكن تحديث النطاق بأكمله عند تفاعل المستخدم، وبالتالي يمكن استخدامه كمصدر للمخطط الديناميكي.

من أجل إبقاء العرض التوضيحي سهل الفهم، سنقوم بإنشاء المصنف من البداية والمضي قدمًا خطوة بخطوة كما هو موضح أدناه.

1.  إنشاء فارغة[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  الوصول إلى[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) من الأول[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) في ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. قم بإدراج بعض البيانات في الخلايا عن طريق إنشاء نطاق مسمى. ستكون هذه البيانات بمثابة سلسلة للمخطط الديناميكي.
1.  يخلق[**صندوق التحرير**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)استنادًا إلى النطاق المسمى الذي تم إنشاؤه في الخطوة السابقة.
1. أدخل المزيد من البيانات في الخلايا التي ستكون بمثابة مصدر لوظيفة VLOOKUP.
1. أدخل وظيفة VLOOKUP (مع المعلمات المناسبة) في نطاق من الخلايا. سيكون هذا النطاق بمثابة مصدر للمخطط الديناميكي.
1.  يخلق[**جدول**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)بناءً على النطاق الذي تم إنشاؤه في الخطوة السابقة.
1. احفظ النتيجة على القرص.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
