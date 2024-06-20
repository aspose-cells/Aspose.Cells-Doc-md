---
title: استخدام فئة ChartGlobalizationSettings لتعيين لغة مختلفة لعنصر رسم بياني 
description: تعلم كيفية استخدام فئة ChartGlobalizationSettings في Aspose.Cells for .NET لتعيين لغات مختلفة لعناصر الرسم البياني. سيساعدك دليلنا على فهم كيفية توطين عناصر الرسم البياني والتسميات والأساطير إلى لغات مختلفة، مما يتيح لك تقديم بياناتك بطريقة مناسبة ثقافيًا.
keywords: Aspose.Cells for .NET، رسم بياني، تعميم الرسم البياني، لغات، توطين، ChartGlobalizationSettings، عناصر، تسميات، أساطير.
type: docs
weight: 2200
url: /ar/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **سيناريوهات الاستخدام المحتملة**

قد قامت واجهات برمجة التطبيقات Aspose.Cells بفتح فئة [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) للتعامل مع السيناريوهات التي يرغب المستخدم في تعيين عنصر رسم بياني إلى لغة مختلفة وتخصيص التسميات المخصصة للمجموعات الفرعية في جدول بيانات. 

## **مقدمة في فئة ChartGlobalizationSettings**

الفئة [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) تقدم حاليًا 8 طرق يمكن تجاوزها في فئة مخصصة لترجمة مثل اسم عنوان المحور، اسم وحدة المحور، اسم عنوان الرسم البياني وما إلى ذلك إلى لغة مختلفة.
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): يحصل على اسم العنوان للمحور.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): يحصل على اسم وحدة المحور.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): يحصل على اسم عنوان الرسم البياني.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): يحصل على اسم الانخفاض لوحة التفسير.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): يحصل على اسم الزيادة لوحة التفسير.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): يحصل على اسم الإجمالي لوحة التفسير.
1. [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): يحصل على اسم تسميات "أخرى" للرسم البياني.
1. [**GetSeriesName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): يحصل على اسم السلاسل في الرسم البياني.

### **ترجمة لغة مخصصة**
هنا، سنقوم بإنشاء رسم بياني شلالي استنادًا إلى البيانات التالية. سيتم عرض أسماء مكونات الرسم البياني باللغة الإنجليزية في الرسم البياني. سنستخدم مثال باللغة التركية لنريك كيفية عرض عنوان الرسم البياني وأسماء زيادة/انخفاض لوحة التفسير واسم الإجمالي وعنوان المحور باللغة التركية.

![todo:image_alt_text](sample.png)

## **الكود المثالي**
يقوم الكود العيني التالي بتحميل [ملف Excel العيني](waterfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

## الإخراج الذي تم توليده بواسطة رمز العينة

هذا هو إنتاج الكونسول للكود العيني أعلاه.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
