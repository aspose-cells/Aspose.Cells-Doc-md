---
title: إنشاء رسم بياني عن طريق معالجة العلامات الذكية
description: تعلم كيفية إنشاء رسوم بيانية باستخدام العلامات الذكية باستخدام Aspose.Cells for .NET. سيوضح دليلنا لك كيفية معالجة العلامات الذكية وخصائصها لتعزيز مظهر رسومك البيانية وقابليتها للاستخدام.
keywords: Aspose.Cells for .NET، إنشاء الرسم البياني، العلامات الذكية، المظهر، الاستخدام، المعالجة.
type: docs
weight: 2100
url: /ar/net/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}}

توفر واجهات برمجة التطبيقات Aspose.Cells [**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) للعمل مع العلامات الذكية حيث يتم وضع التنسيقات والصيغ في جداول البيانات التصميمية ثم معالجتها بواسطة فئة [**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) لملء البيانات وفقًا للعلامات الذكية المحددة. كما يمكن إنشاء رسوم بيانية في Excel عن طريق معالجة العلامات الذكية، مما سيتطلب الخطوات التالية.

- إنشاء جدول بيانات المصمم
- معالجة جدول البيانات التصميمي مقابل مصدر البيانات المحدد
- إنشاء رسم بياني بناءً على البيانات المحددة

{{% /alert %}}

## إنشاء جدول بيانات مصمم

جدول بيانات المصمم هو ملف Excel بسيط تم إنشاؤه باستخدام تطبيق Microsoft Excel أو واجهات برمجة التطبيقات Aspose.Cells، يحتوي على التنسيق البصري، الصيغ والعلامات الذكية، حيث يمكن ملأ المحتويات في وقت التشغيل.

لأسباب بساطة، سنقوم بإنشاء جدول البيانات المصمم باستخدام واجهات البرمجة Aspose.Cells for .NET ومن ثم معالجته ضد مصدر بيانات تم إنشاؤه ديناميكيًا لأغراض العرض.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## معالجة جدول البيانات المصمم

لمعالجة جدول البيانات المصمم، يجب أن يكون لدى المستخدم مصدر بيانات يتوافق مع العلامات الذكية المستخدمة في جدول البيانات المصمم. على سبيل المثال، قمنا بإنشاء مدخل علامة ذكية كـ &=Sales.Year، الذي يمثل عمود السنة في جدول البيانات Sales. في حالة عدم توفر عمود مقابل في مصدر البيانات، ستقوم واجهات برمجة التطبيقات Aspose.Cells بتخطي المعالجة لتلك العلامة الذكية بشكل محدد، ونتيجة لذلك، لن يتم ملأ البيانات للعلامة الذكية بشكل محدد.

لتوضيح هذه الحالة الاستخدام، سنقوم بإنشاء مصدر البيانات من البداية ومعالجته ضد جدول البيانات المصمم الذي تم إنشاؤه في الخطوة السابقة. ومع ذلك، في حالة الوقت الحقيقي، قد تكون البيانات متاحة بالفعل لمزيد من المعالجة، لذلك يمكنك تخطي إنشاء مصدر البيانات إذا كانت البيانات متاحة بالفعل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

معالجة العلامات الذكية بسيطة كما هو موضح في مقتطف الكود التالي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

يستخدم مقتطف الكود أعلاه النسخة الحالية ل [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) الكائن التي تم إنشاؤها في الخطوة الأولى. إذا كان لديك بالفعل ملف جدول البيانات المصمم على القرص أو الذاكرة، فيمكنك إنشاء نسخة لـ [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) الكائن عن طريق تحميل جدول البيانات المصمم الحالي.

{{% /alert %}}

## إنشاء الشارت

بمجرد توفر البيانات، كل ما علينا فعله هو إنشاء شارت استنادًا إلى مصدر البيانات. من أجل تبسيط المثال، سنستخدم ال [**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange) الطريقة حتى لا يتعين علينا تكوين الشارت بشكل أكبر.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
