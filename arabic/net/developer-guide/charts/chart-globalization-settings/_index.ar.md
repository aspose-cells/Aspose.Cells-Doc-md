---
title:  استخدام فئة ChartGlobalizationSettings لتعيين لغة مختلفة لمكون المخطط
description: تعرف على كيفية استخدام فئة ChartGlobalizationSettings في Aspose.Cells for .NET لتعيين لغات مختلفة لمكونات المخطط. سيساعدك دليلنا على فهم كيفية ترجمة عناصر المخطط والتسميات ووسائل الإيضاح إلى لغات مختلفة، مما يسمح لك بتقديم بياناتك بطريقة مناسبة ثقافيًا.
keywords: Aspose.Cells for .NET, charting, chart globalization, languages, localization, ChartGlobalizationSettings, elements, labels, legends.
type: docs
weight: 2200
url: /ar/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---
##  **سيناريوهات الاستخدام المحتملة**

 Aspose.Cells كشفت واجهات برمجة التطبيقات (APIs) عن[**إعدادات عولمة الرسم البياني**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) فئة من أجل التعامل مع السيناريوهات التي يرغب فيها المستخدم في تعيين مكون المخطط إلى لغة مختلفة. تسميات مخصصة للإجماليات الفرعية في جدول بيانات.

##  **مقدمة إلى فئة إعدادات ChartGlobalization**

 ال[**إعدادات عولمة الرسم البياني**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)تقدم الفئة حاليًا الطرق الثمانية التالية التي يمكن تجاوزها في فئة مخصصة للترجمة مثل اسم AxisTitle واسم AxisUnit واسم ChartTitle وما إلى ذلك إلى لغة مختلفة.
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): يحصل على اسم عنوان المحور.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): الحصول على اسم وحدة المحور.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): يحصل على اسم عنوان المخطط.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): يحصل على اسم التخفيض للأسطورة.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): يحصل على اسم الزيادة للأسطورة.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): يحصل على اسم Total للأسطورة.
1. [**احصل على اسم آخر**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): يحصل على اسم التصنيفات "أخرى" للمخطط.
1. [**GetSeriesName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): يحصل على اسم السلسلة في المخطط.

###  **ترجمة لغة مخصصة**
هنا، سنقوم بإنشاء مخطط شلالي بناءً على البيانات التالية. سيتم عرض أسماء مكونات المخطط باللغة الإنجليزية في المخطط. سوف نستخدم مثالاً باللغة التركية لإظهار كيفية عرض عنوان المخطط وأسماء زيادة/تقليل وسيلة الإيضاح والاسم الإجمالي وعنوان المحور باللغة التركية.

![ما يجب القيام به:image_alt_text](sample.png)

##  **عينة من الرموز**
 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[عينة من ملف إكسل](waterfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

##  الإخراج الناتج عن نموذج التعليمات البرمجية

هذا هو إخراج وحدة التحكم لنموذج التعليمات البرمجية أعلاه.

{{< highlight "java" >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
