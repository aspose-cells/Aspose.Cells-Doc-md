---
title: إنشاء رسوم بيانية ديناميكية
description: تعلم كيفية إنشاء رسوم بيانية ديناميكية في Aspose.Cells for .NET. سيوضح دليلنا لك كيفية تحديث بيانات الرسم البياني، والسلاسل، والتنسيق بشكل دينامي يستند إلى احتياجاتك، مما يتيح لك تقديم التغييرات في البيانات بصورة بصرية في الأوراق الخاصة بك.
keywords: Aspose.Cells for .NET، الرسوم الديناميكية، البيانات، السلاسل، التنسيق، الأوراق الخاصة، تحديث.
type: docs
weight: 240
url: /ar/net/create-dynamic-charts/
---

{{% alert color="primary" %}}

الرسوم البيانية الديناميكية (أو التفاعلية) لها القدرة على التغيير عند تغيير نطاق البيانات. وبعبارة أخرى، يمكن للرسوم البيانية الديناميكية أن تعكس تلقائيًا التغييرات عند تغيير مصدر البيانات. من أجل تحفيز تغيير مصدر البيانات، يمكن استخدام خيارات التصفية لجداول البيانات في Excel أو استخدام عنصر تحكم مثل مربع القائمة المنسدلة أو قائمة البحث.

يوضح هذا المقال استخدام Aspose.Cells for .NET APIs لإنشاء رسوم بيانية ديناميكية باستخدام الطريقتين المذكورتين.

{{% /alert %}}

## **استخدام جداول Excel**

{{% alert color="primary" %}}

تشير الجداول في Excel إلى ListObjects من وجهة نظر Aspose.Cells، لذلك سنستخدم مصطلح "ListObject" بدلاً من "جدول" للوضوح. يرجى قراءة التفاصيل حول كيفية [إنشاء ListObjects](/cells/ar/net/create-and-format-table/) باستخدام Aspose.Cells for .NET API.

{{% /alert %}}

توفر الـListObjects الوظائف المدمجة لفرز وتصفية البيانات بمشاركة المستخدم. يتم توفير خيارات فرز وتصفية من خلال قوائم القائمة المنسدلة التي تتم إضافتها تلقائيًا إلى الصف الرأسي لـ[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject). بسبب هذه الميزات (الفرز والتصفية)، يبدو أن الـ[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) يبدو كخيار مثالي ليكون مصدر البيانات لرسم بياني ديناميكي لأنه عند تغيير الفرز أو التصفية، سيتم تغيير تمثيل البيانات في الرسم البياني ليعكس الحالة الحالية للـ[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

من أجل الإبقاء على العرض التوضيحي بسيطًا وسهل الفهم، سنقوم بإنشاء الـ[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) من البداية والمضي قدمًا خطوة بخطوة كما هو موضح أدناه.

1. إنشاء [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فارغة.
1. الوصول إلى [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) لأول [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) في [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
3. إدراج بعض البيانات في الخلايا.
1. إنشاء [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) استنادًا إلى البيانات المدرجة.
1. إنشاء [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) استنادًا إلى نطاق البيانات [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. حفظ النتيجة على القرص.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

## **استخدام الصيغ الديناميكية**

في حالة عدم رغبتك في استخدام [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) كمصدر بيانات للمخطط الديناميكي، الخيار الآخر هو استخدام الوظائف (أو الصيغ) في Excel لإنشاء نطاق بيانات ديناميكي، وعنصر تحكم (مثل ComboBox) لتغيير البيانات. في هذ scenar تستخدم الوظيفة VLOOKUP لجلب القيم المناسبة استنادا إلى اختيار ComboBox. عند تغيير التحديد، ستقوم وظيفة VLOOKUP بتحديث قيمة الخلية. إذا كانت مجموعة من الخلايا تستخدم وظيفة VLOOKUP، فيمكن تحديث المجموعة بأكملها عند تفاعل المستخدم، لذا يمكن استخدامها كمصدر للمخطط الديناميكي.

من أجل إبقاء العرض التوضيحي بسيطًا للفهم، سنقوم بإنشاء دفتر العمل من البداية والمضي قدمًا خطوة بخطوة كما هو موضح أدناه.

1. إنشاء [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فارغة.
1. الوصول إلى [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) لأول [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) في [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. إدراج بعض البيانات في الخلايا عن طريق إنشاء نطاق مسمى. ستكون هذه البيانات مصدرًا للمخطط الديناميكي.
1. إنشاء [**ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) استنادًا إلى النطاق المسمى الذي تم إنشاؤه في الخطوة السابقة.
1. إدراج بعض البيانات الإضافية في الخلايا التي ستعتبر مصدرًا لوظيفة VLOOKUP.
1. إدراج وظيفة VLOOKUP (بمعلمات مناسبة) في مجموعة من الخلايا. ستعتبر هذه المجموعة مصدرًا للمخطط الديناميكي.
1. إنشاء [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) استنادًا إلى النطاق الذي تم إنشاؤه في الخطوة السابقة.
1. حفظ النتيجة على القرص.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
