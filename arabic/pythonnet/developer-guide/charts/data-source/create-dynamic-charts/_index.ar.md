---
title: إنشاء رسوم بيانية ديناميكية
description: تعلم كيفية إنشاء رسومات بيانية ديناميكية في Aspose.Cells لبايثون via .NET. سيرينا دليلنا كيف تقوم بتحديث بيانات الرسم البياني، السلاسل، والتنسيقات بشكل ديناميكي استنادًا إلى متطلباتك، مما يتيح لك عرض البيانات المتغيرة بصريًا في أوراق العمل الخاصة بك.
keywords: Aspose.Cells لبايثون via .NET، التصوير البياني، الرسوم البيانية الديناميكية، البيانات، السلاسل، التنسيق، أوراق العمل، التحديث.
type: docs
weight: 240
url: /ar/python-net/create-dynamic-charts/
---

{{% alert color="primary" %}}

الرسوم البيانية الديناميكية (أو التفاعلية) لها القدرة على التغيير عند تغيير نطاق البيانات. وبعبارة أخرى، يمكن للرسوم البيانية الديناميكية أن تعكس تلقائيًا التغييرات عند تغيير مصدر البيانات. من أجل تحفيز تغيير مصدر البيانات، يمكن استخدام خيارات التصفية لجداول البيانات في Excel أو استخدام عنصر تحكم مثل مربع القائمة المنسدلة أو قائمة البحث.

 يوضح هذا المقال استخدام واجهات برمجة التطبيقات Aspose.Cells لبايثون via .NET لإنشاء رسوم بيانية ديناميكية باستخدام كلا من الطريقتين المذكورتين سابقًا.

{{% /alert %}}

## **استخدام جداول Excel**

{{% alert color="primary" %}}

 تُعرف جداول إكسل في Aspose.Cells باسم ListObjects، لذلك، سنستخدم مصطلح "ListObject" بدلاً من "Table" للوضوح. يرجى القراءة بالتفصيل عن كيفية [إنشاء ListObjects]( /cells/ar/python-net/create-and-format-table/) باستخدام واجهة برمجة التطبيقات Aspose.Cells لبايثون via .NET.

{{% /alert %}}

 توفر ListObjects وظيفة مدمجة لفرز وتصفية البيانات عند تفاعل المستخدم. يتم توفير خيارات الفرز والتصفية من خلال القوائم المنسدلة التي تُضاف تلقائيًا إلى صف الرأس للجدول. بفضل هذه الميزات (الفرز والتصفية)، يبدو أن [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) هو المرشح المثالي ليخدم كمصدر بيانات لرسم بياني ديناميكي لأنه عند تغيير الفرز أو التصفية، سيتم تغيير تمثيل البيانات في الرسم البياني ليعكس الحالة الحالية للجدول.

من أجل الإبقاء على العرض التوضيحي بسيطًا وسهل الفهم، سنقوم بإنشاء الـ[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) من البداية والمضي قدمًا خطوة بخطوة كما هو موضح أدناه.

1. إنشاء [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) فارغة.
1. الوصول إلى [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) لأول [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) في [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
3. إدراج بعض البيانات في الخلايا.
1. إنشاء [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) استنادًا إلى البيانات المدرجة.
1. إنشاء [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) استنادًا إلى نطاق البيانات [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject).
1. حفظ النتيجة على القرص.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateDynamicCharts.py" >}}

## **استخدام الصيغ الديناميكية**

في حالة عدم رغبتك في استخدام [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) كمصدر بيانات للمخطط الديناميكي، الخيار الآخر هو استخدام الوظائف (أو الصيغ) في Excel لإنشاء نطاق بيانات ديناميكي، وعنصر تحكم (مثل ComboBox) لتغيير البيانات. في هذ scenar تستخدم الوظيفة VLOOKUP لجلب القيم المناسبة استنادا إلى اختيار ComboBox. عند تغيير التحديد، ستقوم وظيفة VLOOKUP بتحديث قيمة الخلية. إذا كانت مجموعة من الخلايا تستخدم وظيفة VLOOKUP، فيمكن تحديث المجموعة بأكملها عند تفاعل المستخدم، لذا يمكن استخدامها كمصدر للمخطط الديناميكي.

من أجل إبقاء العرض التوضيحي بسيطًا للفهم، سنقوم بإنشاء دفتر العمل من البداية والمضي قدمًا خطوة بخطوة كما هو موضح أدناه.

1. إنشاء [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) فارغة.
1. الوصول إلى [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) لأول [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) في [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
1. إدراج بعض البيانات في الخلايا عن طريق إنشاء نطاق مسمى. ستكون هذه البيانات مصدرًا للمخطط الديناميكي.
1. إنشاء [**ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox) استنادًا إلى النطاق المسمى الذي تم إنشاؤه في الخطوة السابقة.
1. إدراج بعض البيانات الإضافية في الخلايا التي ستعتبر مصدرًا لوظيفة VLOOKUP.
1. إدراج وظيفة VLOOKUP (بمعلمات مناسبة) في مجموعة من الخلايا. ستعتبر هذه المجموعة مصدرًا للمخطط الديناميكي.
1. إنشاء [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) استنادًا إلى النطاق الذي تم إنشاؤه في الخطوة السابقة.
1. حفظ النتيجة على القرص.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateDynamicChartsUsingDynamicFormula.py" >}}
{{< app/cells/assistant language="python-net" >}}
