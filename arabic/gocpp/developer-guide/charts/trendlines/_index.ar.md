---
title: الحصول على نص المعادلة لخط الاتجاه في المخطط باستخدام Golang عبر C++
linktitle: خطوط الاتجاه
description: تعلم كيفية استخدام Aspose.Cells for C++ لاسترجاع نص المعادلة لخط الاتجاه في رسم بياني تم إنشاؤه في Microsoft Excel. ستوضح أدلتنا كيفية الوصول إلى واستخراج معادلة خط الاتجاه لمزيد من التحليل أو العرض.
keywords: Aspose.Cells for C++، خط اتجاه الرسم البياني، نص المعادلة، Microsoft Excel، تحليل البيانات، العرض.
type: docs
weight: 110
url: /ar/go-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

يمكنك استرجاع نص المعادلة لخط اتجاه الرسم البياني باستخدام Aspose.Cells. توفر Aspose.Cells الواجهة البرمجية للتطبيقات [**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/) التي تُرجع نص المعادلة لخط اتجاه الرسم البياني. لاستخدام هذه الواجهة البرمجية، سيلزمك أولاً استدعاء الطريقة [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/).

{{% /alert %}}

يعرض لقطة الشاشة التالية المخطط مع خط اتجاه والنص المعادلة الخاص به مرئي باللون الأحمر. سنسترجع هذا النص باستخدام الخاصية [**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/) في الكود التالي.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## كود C++ للحصول على نص معادلة خط الاتجاه في الرسم البياني

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Trendlines.go" >}}
## الإخراج الذي تم توليده بواسطة رمز العينة

هذا هو إنتاج الكونسول للكود العيني أعلاه.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
