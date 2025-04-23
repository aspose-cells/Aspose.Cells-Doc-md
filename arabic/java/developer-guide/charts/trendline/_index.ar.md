---
title: الحصول على نص المعادلة لخط اتجاه الرسم البياني
linktitle: خط الاتجاه
type: docs
weight: 90
url: /ar/java/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

يمكنك استرجاع نص المعادلة لخط اتجاه الرسم البياني باستخدام Aspose.Cells. توفر Aspose.Cells الواجهة البرمجية للتطبيقات [**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) التي تُرجع نص المعادلة لخط اتجاه الرسم البياني. لاستخدام هذه الواجهة البرمجية، سيلزمك أولاً استدعاء الطريقة [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--).

{{% /alert %}}

## **مثال**

تظهر اللقطة المتصورة التالية الرسم البياني مع خط اتجاه ونص المعادلة له باللون الأحمر. سوف نسترجع هذا النص باستخدام الواجهة البرمجية [**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) في رمز العينة التالي.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

### جافا كود للحصول على نص معادلة اتجاه الخط في المخطط

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetEquationText-GetEquationText.java" >}}

### الناتج الذي تم استخراجه بواسطة الشفرة العينية

هذا هو إنتاج الكونسول للكود العيني أعلاه.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
