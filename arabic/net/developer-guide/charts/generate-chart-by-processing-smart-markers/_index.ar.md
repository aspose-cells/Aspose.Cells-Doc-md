---
title: إنشاء مخطط عن طريق معالجة العلامات الذكية
type: docs
weight: 2100
url: /ar/net/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}}

 توفر واجهات برمجة التطبيقات Aspose.Cells امتداد[**المصمم المصمم**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)فئة للعمل باستخدام Smart Markers حيث يتم وضع التنسيق والصيغ في جداول بيانات المصمم ثم معالجتها باستخدام[**المصمم المصمم**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)فئة لتعبئة البيانات وفقًا للعلامات الذكية المحددة. من الممكن أيضًا إنشاء مخططات Excel من خلال معالجة Smart Markers ، والتي ستتطلب الخطوات التالية.

- إنشاء جدول بيانات المصمم
- معالجة جدول بيانات المصمم مقابل مصدر البيانات المحدد
- إنشاء مخطط على أساس البيانات المأهولة

{{% /alert %}}

## إنشاء جدول بيانات مصمم

جدول بيانات المصمم هو ملف Excel بسيط تم إنشاؤه باستخدام تطبيق Excel Microsoft أو Aspose.Cells APIs التي تحتوي على التنسيق المرئي والصيغ والعلامات الذكية ، حيث يمكن ملء المحتويات في وقت التشغيل.

من أجل البساطة ، سنقوم بإنشاء جدول بيانات المصمم باستخدام API Aspose.Cells for .NET API ومعالجته لاحقًا مقابل مصدر بيانات تم إنشاؤه ديناميكيًا لأغراض العرض التوضيحي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## معالجة جدول بيانات المصمم

من أجل معالجة جدول بيانات المصمم ، يجب أن يكون لدى المرء مصدر بيانات يتوافق مع العلامات الذكية المستخدمة في جدول بيانات المصمم. على سبيل المثال ، قمنا بإنشاء إدخال Smart Marker كـ & = Sales.Year ، والذي يمثل عمود السنة في مبيعات DataTable. في حالة عدم توفر العمود المقابل في مصدر البيانات ، ستتخطى واجهات برمجة التطبيقات Aspose.Cells المعالجة لهذا المحدد الذكي ، ونتيجة لذلك ، لن يتم ملء البيانات الخاصة بـ Smart Marker المحدد.

لتوضيح حالة الاستخدام هذه ، سننشئ مصدر البيانات من البداية ونعالجها مقابل جدول بيانات المصمم الذي تم إنشاؤه في الخطوة السابقة. ومع ذلك ، في سيناريو الوقت الفعلي ، قد تكون البيانات متاحة بالفعل لمزيد من المعالجة حتى تتمكن من تخطي إنشاء مصدر البيانات إذا كانت البيانات متاحة بالفعل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

تعد معالجة Smart Markers بسيطة للغاية كما هو موضح في مقتطف الشفرة التالي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

 يستخدم مقتطف الشفرة أعلاه المثيل الحالي لملف[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)فئة تم إنشاؤها في الخطوة الأولى. إذا كان لديك بالفعل ملف جدول بيانات المصمم على القرص أو الذاكرة ، فيمكنك إنشاء مثيل لـ[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)فئة عن طريق تحميل جدول بيانات المصمم الحالي.

{{% /alert %}}

## إنشاء الرسم البياني

 بمجرد وضع البيانات في مكانها الصحيح ، كل ما يتعين علينا القيام به هو إنشاء مخطط بناءً على مصدر البيانات. من أجل الحفاظ على المثال بسيطًا ، سنستخدم ملحق[**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)حتى لا نضطر إلى تكوين المخطط بشكل أكبر.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
