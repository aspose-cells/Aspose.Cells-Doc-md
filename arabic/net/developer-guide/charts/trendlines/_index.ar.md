---
title: الحصول على نص المعادلة لخط اتجاه الرسم البياني
description: تعرف على كيفية استخدام Aspose.Cells for .NET لاسترجاع نص المعادلة لخط اتجاه في رسم بياني تم إنشاؤه في Microsoft Excel. سيقوم دليلنا بعرض كيفية الوصول إلى واستخراج نص المعادلة لخط الاتجاه للتحليل أو العرض اللاحق.
keywords: Aspose.Cells for .NET، خط اتجاه المخطط، نص المعادلة، Microsoft Excel، تحليل البيانات، العرض.
linktitle: خطوط الاتجاه
type: docs
weight: 110
url: /ar/net/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

يمكنك استرجاع نص المعادلة لخط اتجاه الرسم البياني باستخدام Aspose.Cells. توفر Aspose.Cells الواجهة البرمجية للتطبيقات [**Trendline.DataLabels.Text**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/text) التي تُرجع نص المعادلة لخط اتجاه الرسم البياني. لاستخدام هذه الواجهة البرمجية، سيلزمك أولاً استدعاء الطريقة [**Chart.Calculate()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/calculate).

{{% /alert %}}

تظهر اللقطة المتصورة التالية الرسم البياني مع خط اتجاه ونص المعادلة له باللون الأحمر. سوف نسترجع هذا النص باستخدام الواجهة البرمجية [**Trendline.DataLabels.Text**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/text) في رمز العينة التالي.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## رمز C# للحصول على نص معادلة خط اتجاه الرسم البياني

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GetEquationTextOfChartTrendLine-1.cs" >}}

## الإخراج الذي تم توليده بواسطة رمز العينة

هذا هو إنتاج الكونسول للكود العيني أعلاه.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
