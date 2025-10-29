---
title: استخدام فئة ChartGlobalizationSettings لضبط لغة مكونات المخطط مع Golang عبر C++
linktitle: استخدام فئة ChartGlobalizationSettings
description: تعلم كيفية استخدام فئة ChartGlobalizationSettings في Aspose.Cells for C++ لضبط لغات مختلفة لمكونات المخطط. د دليلنا سيساعدك على فهم كيفية توطين عناصر المخطط، التسميات، والأساطير إلى لغات مختلفة، مما يتيح لك عرض بياناتك بطريقة ملائمة ثقافيًا.
keywords: Aspose.Cells for C++، الرسوم البيانية، توطين المخططات، اللغات، التوطين، ChartGlobalizationSettings، العناصر، التسميات، الأساطير.
type: docs
weight: 2200
url: /ar/go-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **سيناريوهات الاستخدام المحتملة**

قد قامت واجهات برمجة التطبيقات Aspose.Cells بفتح فئة [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/) للتعامل مع السيناريوهات التي يرغب المستخدم في تعيين عنصر رسم بياني إلى لغة مختلفة وتخصيص التسميات المخصصة للمجموعات الفرعية في جدول بيانات. 

## **مقدمة في فئة ChartGlobalizationSettings**

تقدم فئة [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/) حاليًا الطرق التالية الثمانية التي يمكن تجاوزها في فئة مخصصة لترجمة مثل اسم AxisTitle، واسم AxisUnit، واسم ChartTitle، وما إلى ذلك إلى لغات مختلفة.

1. [**GetAxisTitleName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getaxistitlename/): يحصل على اسم العنوان للمحور.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getaxisunitname/): يحصل على اسم وحدة المحور.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getcharttitlename/): يحصل على اسم عنوان الرسم البياني.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegenddecreasename/): يحصل على اسم الانخفاض لوحة التفسير.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegendincreasename/): يحصل على اسم الزيادة لوحة التفسير.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegendtotalname/): يحصل على اسم الإجمالي لوحة التفسير.
1. [**GetOtherName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getothername/): يحصل على اسم تسميات "أخرى" للرسم البياني.
1. [**GetSeriesName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getseriesname/): يحصل على اسم السلاسل في الرسم البياني.

### **ترجمة لغة مخصصة**
هنا، سنقوم بإنشاء رسم بياني شلالي استنادًا إلى البيانات التالية. سيتم عرض أسماء مكونات الرسم البياني باللغة الإنجليزية في الرسم البياني. سنستخدم مثال باللغة التركية لنريك كيفية عرض عنوان الرسم البياني وأسماء زيادة/انخفاض لوحة التفسير واسم الإجمالي وعنوان المحور باللغة التركية.

![todo:image_alt_text](sample.png)

## **الكود المثالي**
يقوم الكود العيني التالي بتحميل [ملف Excel العيني](waterfall.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartGlobalizationSettings.go" >}}
## الإخراج الذي تم توليده بواسطة رمز العينة

هذا هو إنتاج الكونسول للكود العيني أعلاه.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
