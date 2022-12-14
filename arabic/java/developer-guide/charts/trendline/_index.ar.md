---
title: احصل على نص معادلة خط اتجاه المخطط
linktitle: خط الاتجاه
type: docs
weight: 90
url: /ar/java/get-equation-text-of-chart-trendline/
---
{{% alert color="primary" %}}

 يمكنك استرداد نص المعادلة لخط اتجاه المخطط باستخدام Aspose.Cells. يوفر Aspose.Cells[**Trendline.getDataLabels (). getText ()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) الخاصية التي تُرجع نص المعادلة لخط اتجاه المخطط. للاستفادة من هذه الخاصية ، سيتعين عليك الاتصال أولاً[**Chart.calculate ()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()) طريقة.

{{% /alert %}}

## **مثال**

 تُظهر لقطة الشاشة التالية المخطط الذي يحتوي على خط اتجاه ويظهر نص المعادلة باللون الأحمر. سنقوم باسترداد هذا النص باستخدام[**Trendline.getDataLabels (). getText ()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text)الخاصية في نموذج التعليمات البرمجية التالي.

![ما يجب القيام به: image_بديل_نص](get-equation-text-of-chart-trendline_1.png)

### كود Java للحصول على نص معادلة خط اتجاه المخطط

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetEquationText-GetEquationText.java" >}}

### الناتج الناتج عن نموذج التعليمات البرمجية

هذا هو إخراج وحدة التحكم لعينة التعليمات البرمجية أعلاه.

{{< highlight "java" >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
