---
title: قراءة وتلاعب رسومات Excel 2016
description: تعلم كيفية قراءة والتلاعب بمخططات إكسل 2016 باستخدام أسبوست كيلز للبايثون via .NET. دليلنا سيُظهر لك كيفية الوصول إلى وتعديل خصائص المخطط المختلفة، بما في ذلك تسميات البيانات، ألوان السلسلة، والتخطيط.
keywords: أسبوست كيلز للبايثون via .NET، مخططات إكسل 2016، قراءة، تلاعب، تسميات البيانات، ألوان السلسلة، التخطيط، التخطيط الهيكلي، التخطيط الدائري.
type: docs
weight: 48
url: /ar/python-net/read-and-manipulate-excel-2016-charts/
---

## **سيناريوهات الاستخدام المحتملة**
يدعم أسبوست كيلز للبايثون via .NET الآن قراءة وتلاعب مخططات إكسل 2016 والتي غير متوفرة في إكسل مايكروسوفت 2013 أو الإصدارات الأقدم.

## **قراءة وتلاعب شكل بيانات Excel 2016**
يحمل الكود النموذجي التالي [ملف Excel المصدر](22774101.xlsx) الذي يحتوي على رسومات Excel 2016 في الورقة العمل الأولى. يقوم بقراءة جميع الرسومات وتغيير عنوان كل منها حسب نوع الرسم البياني. يوضح اللقطة الشاشية التالية الملف الأصلي لبرنامج Excel قبل تنفيذ الكود. كما تلاحظ، يكون عنوان الرسم متماثل لكل الرسوم.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

تظهر اللقطة الشاشية التالية [ملف Excel الناتج](22774104.xlsx) بعد تنفيذ الكود. كما تلاحظ، تم تغيير عنوان الرسم حسب نوعه.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)

## **الكود المثالي**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ReadAndManipulateExcel2016Charts.py" >}}

## **مخرجات الوحدة**
إليك إخراج وحدة التحكم للشيفرة النموذجية أعلاه عند تنفيذها مع [ملف Excel المصدر المقدم](22774101.xlsx).

{{< highlight java >}}

 Waterfall

Treemap

Sunburst

Histogram

BoxWhisker

{{< /highlight >}}


## **مواضيع متقدمة**
- [إنشاء رسم بياني Waterfall](/cells/ar/python-net/creating-waterfall-chart/)
- [إنشاء رسم بياني TreeMap](/cells/ar/python-net/creating-treemap-chart/)
- [إنشاء رسم بياني Sunburst](/cells/ar/python-net/creating-sunburst-chart/)
{{< app/cells/assistant language="python-net" >}}
