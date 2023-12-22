---
title: إنشاء مخطط عن طريق معالجة العلامات الذكية
description: تعرف على كيفية إنشاء مخططات باستخدام العلامات الذكية باستخدام Aspose.Cells for .NET. سيوضح لك دليلنا كيفية معالجة العلامات الذكية وخصائصها لتحسين مظهر مخططاتك وسهولة استخدامها.
keywords: Aspose.Cells for .NET, chart generation, smart markers, appearance, usability, processing.
type: docs
weight: 2100
url: /ar/net/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}}

 توفر واجهات برمجة التطبيقات Aspose.Cells[**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) للعمل مع العلامات الذكية حيث يتم وضع التنسيقات والصيغ في جداول بيانات المصمم ثم معالجتها[**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)فئة لملء البيانات وفقا للعلامات الذكية المحددة. من الممكن أيضًا إنشاء مخططات Excel من خلال معالجة العلامات الذكية، الأمر الذي سيتطلب الخطوات التالية.

- إنشاء جدول بيانات المصمم
- معالجة جدول بيانات المصمم مقابل مصدر البيانات المحدد
- إنشاء الرسم البياني على أساس البيانات المملوءة

{{% /alert %}}

##  إنشاء جدول بيانات المصمم

جدول بيانات المصمم هو ملف Excel بسيط تم إنشاؤه باستخدام تطبيق Excel Microsoft أو واجهات برمجة التطبيقات Aspose.Cells التي تحتوي على التنسيق المرئي والصيغ والعلامات الذكية، حيث يمكن ملء المحتويات في وقت التشغيل.

من أجل التبسيط، سنقوم بإنشاء جدول بيانات المصمم باستخدام Aspose.Cells for .NET API ثم نقوم بمعالجته لاحقًا مقابل مصدر بيانات تم إنشاؤه ديناميكيًا لأغراض العرض التوضيحي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

##  معالجة جدول بيانات المصمم

من أجل معالجة جدول بيانات المصمم، يجب أن يكون لدى الشخص مصدر بيانات يتوافق مع العلامات الذكية المستخدمة في جدول بيانات المصمم. على سبيل المثال، قمنا بإنشاء إدخال Smart Marker كـ &=Sales.Year، الذي يمثل عمود السنة في DataTable Sales. في حالة عدم توفر العمود المقابل في مصدر البيانات، ستتخطى واجهات برمجة التطبيقات Aspose.Cells معالجة تلك العلامة الذكية المحددة، ونتيجة لذلك، لن تتم تعبئة البيانات الخاصة بعلامة ذكية معينة.

من أجل توضيح حالة الاستخدام هذه، سنقوم بإنشاء مصدر البيانات من البداية ومعالجته مقابل جدول بيانات المصمم الذي تم إنشاؤه في الخطوة السابقة. ومع ذلك، في سيناريو الوقت الحقيقي، قد تكون البيانات متاحة بالفعل لمزيد من المعالجة حتى تتمكن من تخطي إنشاء مصدر البيانات إذا كانت البيانات متاحة بالفعل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

تعد معالجة العلامات الذكية بسيطة جدًا كما هو موضح في مقتطف التعليمات البرمجية التالي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

 يستخدم مقتطف الكود أعلاه المثيل الموجود لـ[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) تم إنشاء الفصل في الخطوة الأولى. إذا كان لديك بالفعل ملف جدول بيانات المصمم على القرص أو الذاكرة، فيمكنك إنشاء مثيل له[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)الفصل عن طريق تحميل جدول بيانات المصمم الموجود.

{{% /alert %}}

##  إنشاء الرسم البياني

 بمجرد توفر البيانات، كل ما يتعين علينا القيام به هو إنشاء مخطط بناءً على مصدر البيانات. ولتسهيل المثال سنستخدم[**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)الطريقة حتى لا نضطر إلى تكوين المخطط بشكل أكبر.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
