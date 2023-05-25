---
title:  استخدام فئة ChartGlobalizationSettings لتعيين لغة مختلفة لمكون الرسم البياني
type: docs
weight: 2200
url: /ar/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---
##  **سيناريوهات الاستخدام الممكنة**

 كشفت واجهات برمجة التطبيقات Aspose.Cells ملف[**إعدادات العولمة**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) class من أجل التعامل مع السيناريوهات التي يرغب فيها المستخدم في ضبط مكون الرسم البياني على لغة مختلفة. تسميات مخصصة للإجماليات الفرعية في جدول بيانات.

##  **مقدمة إلى فئة ChartGlobalizationSettings**

 ال[**إعدادات العولمة**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)تقدم class حاليًا الطرق الثمانية التالية التي يمكن تجاوزها في فئة مخصصة للترجمة مثل اسم AxisTitle واسم AxisUnit واسم ChartTitle وما إلى ذلك إلى لغة مختلفة.
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): الحصول على اسم العنوان للمحور.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): الحصول على اسم وحدة المحور.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): الحصول على اسم عنوان المخطط.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): الحصول على اسم Decrease for Legend.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): الحصول على اسم الزيادة لـ Legend.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): الحصول على اسم Total for Legend.
1. [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): الحصول على اسم تسميات "أخرى" للمخطط.
1. [**GetSeriesName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): الحصول على اسم السلسلة في المخطط.

###  **ترجمة لغة مخصصة**
هنا ، سننشئ مخططًا شلالًا بناءً على البيانات التالية. سيتم عرض أسماء مكونات المخطط باللغة الإنجليزية في المخطط. سنستخدم مثالًا باللغة التركية لإظهار كيفية عرض عنوان المخطط ، وزيادة / تقليل الأسماء في الأسطورة ، والاسم الإجمالي ، وعنوان المحور باللغة التركية.

![ما يجب القيام به: image_alt_text](sample.png)

##  **عينة من الرموز**
 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](waterfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

##  الناتج الناتج عن نموذج التعليمات البرمجية

هذا هو إخراج وحدة التحكم لعينة التعليمات البرمجية أعلاه.

{{< highlight "java" >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
