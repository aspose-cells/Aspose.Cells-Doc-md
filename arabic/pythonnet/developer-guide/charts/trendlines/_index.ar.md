---
title: الحصول على نص المعادلة لخط اتجاه الرسم البياني
description: تعلم كيفية استخدام Aspose.Cells for Python via .NET لاسترداد نص معادلة خط الاتجاه في مخطط تم إنشاؤه في Microsoft Excel. سيُوضح دليلنا كيفية الوصول إلى واستخراج معادلة خط الاتجاه لمزيد من التحليل أو العرض.
keywords: Aspose.Cells for Python via .NET، خط اتجاه المخطط، نص المعادلة، Microsoft Excel، تحليل البيانات، العرض.
linktitle: خطوط الاتجاه
type: docs
weight: 110
url: /ar/python-net/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

يمكنك استرداد نص معادلة خط الاتجاه باستخدام Aspose.Cells for Python via .NET. توفر Aspose.Cells for Python via .NET خاصية ترجع نص معادلة خط الاتجاه للمخطط. لاستخدام هذه الخاصية، عليك أولاً استدعاء الدالة [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate).

{{% /alert %}}

تظهر اللقطة المتصورة التالية الرسم البياني مع خط اتجاه ونص المعادلة له باللون الأحمر. سوف نسترجع هذا النص باستخدام الواجهة البرمجية [**Trendline.data_labels.text**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/datalabels/text) في رمز العينة التالي.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## رمز C# للحصول على نص معادلة خط اتجاه الرسم البياني

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-GetEquationTextOfChartTrendLine-1.py" >}}

## الإخراج الذي تم توليده بواسطة رمز العينة

هذا هو إنتاج الكونسول للكود العيني أعلاه.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
