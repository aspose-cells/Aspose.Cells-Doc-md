---
title: إنشاء مخططات ديناميكية
type: docs
weight: 240
url: /ar/net/create-dynamic-charts/
---
{{% alert color="primary" %}}

تتمتع المخططات الديناميكية (أو التفاعلية) بالقدرة على التغيير عند تغيير نطاق البيانات. بمعنى آخر ، يمكن للمخططات الديناميكية أن تعكس التغييرات تلقائيًا عند تغيير مصدر البيانات. من أجل بدء التغيير في مصدر البيانات ، يمكن للمرء استخدام خيار التصفية في جداول Excel أو استخدام عنصر تحكم مثل ComboBox أو القائمة المنسدلة.

توضح هذه المقالة استخدام واجهات برمجة تطبيقات Aspose.Cells for .NET لإنشاء مخططات ديناميكية باستخدام كل من الطرق المذكورة أعلاه.

{{% /alert %}}

## **استخدام جداول اكسل**

{{% alert color="primary" %}}

 يشار إلى جداول Excel باسم ListObjects في منظور Aspose.Cells ، وبالتالي ، سنستخدم المصطلح "ListObject" بدلاً من "Table" للتوضيح. يرجى القراءة بالتفصيل حول كيفية[إنشاء ListObjects](/cells/ar/net/create-and-format-table/) مع Aspose.Cells for .NET API.

{{% /alert %}}

 توفر ListObjects الوظائف المضمنة لفرز البيانات وتصفيتها عند تفاعل المستخدم. يتم توفير خياري الفرز والتصفية من خلال القوائم المنسدلة التي تتم إضافتها تلقائيًا إلى صف رأس ملف[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) . نظرًا لهذه الميزات (الفرز والتصفية) ، فإن ملف[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)يبدو أنه المرشح المثالي للعمل كمصدر بيانات لمخطط ديناميكي لأنه عند تغيير الفرز أو التصفية ، سيتم تغيير تمثيل البيانات في المخطط ليعكس الحالة الحالية لـ[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

 من أجل الحفاظ على العرض التوضيحي بسيطًا للفهم ، سننشئ ملف[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)من البداية والمضي قدمًا خطوة بخطوة كما هو موضح أدناه.

1.  قم بإنشاء ملف[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  الوصول إلى[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) من الأول[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) في ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. أدخل بعض البيانات في الخلايا.
1.  خلق[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)بناءً على البيانات المدرجة.
1.  خلق[**جدول**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) بناءً على نطاق بيانات[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. احفظ النتيجة على القرص.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

## **استخدام الصيغ الديناميكية**

 في حالة عدم رغبتك في استخدام ملف[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)كمصدر بيانات للمخطط الديناميكي ، فإن الخيار الآخر هو استخدام وظائف Excel (أو الصيغ) لإنشاء نطاق ديناميكي من البيانات ، وعنصر تحكم (مثل ComboBox) لبدء التغيير في البيانات. في هذا السيناريو ، سوف نستخدم وظيفة VLOOKUP لجلب القيم المناسبة بناءً على اختيار ComboBox. عند تغيير التحديد ، ستقوم وظيفة VLOOKUP بتحديث قيمة الخلية. إذا كان نطاق من الخلايا يستخدم وظيفة VLOOKUP ، فيمكن تحديث النطاق بالكامل عند تفاعل المستخدم ، وبالتالي يمكن استخدامه كمصدر للمخطط الديناميكي.

من أجل الحفاظ على العرض التوضيحي بسيطًا للفهم ، سننشئ Workbook من البداية ونتقدم خطوة بخطوة كما هو موضح أدناه.

1.  قم بإنشاء ملف[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  الوصول إلى[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) من الأول[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) في ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. أدخل بعض البيانات في الخلايا عن طريق إنشاء نطاق مسمى. ستعمل هذه البيانات كسلسلة للمخطط الديناميكي.
1.  خلق[**صندوق التحرير**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)استنادًا إلى النطاق المسمى الذي تم إنشاؤه في الخطوة السابقة.
1. أدخل المزيد من البيانات في الخلايا التي ستعمل كمصدر لوظيفة VLOOKUP.
1. أدخل دالة VLOOKUP (مع المعلمات المناسبة) في نطاق من الخلايا. سيعمل هذا النطاق كمصدر للمخطط الديناميكي.
1.  خلق[**جدول**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)بناءً على النطاق الذي تم إنشاؤه في الخطوة السابقة.
1. احفظ النتيجة على القرص.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
