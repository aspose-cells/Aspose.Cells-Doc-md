---
title: تحويل الرسم البياني إلى صورة للمنطقة الصينية
description: تعرف على كيفية استخدام Aspose.Cells for .NET لضبط التكوين الصيني للمخططات. سيوضح دليلنا كيفية تكوين المخططات لدعم الأحرف والتنسيقات الصينية، بما في ذلك الخطوط والأحجام واتجاهات النص والمزيد.
keywords: Aspose.Cells for .NET, Charts, Chinese Configuration, Fonts, Font Size, Text Direction, Support.
linktitle: تعيين المنطقة الصينية
type: docs
weight: 9
url: /ar/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---
{{% alert color="primary" %}}

في هذا الموضوع، سنوضح لك كيفية تعيين المنطقة الصينية للمخطط.

{{% /alert %}}

##  **يحدد فئة الميراث**

 الخطوة الأولى، تحتاج إلى تحديد فئة "ChartChineseSettings" التي ترث منها[**إعدادات عولمة الرسم البياني**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
بعد ذلك، من خلال إعادة كتابة الوظائف ذات الصلة، يمكنك تعيين نص عناصر المخطط بلغتك الخاصة.
مثال الكود:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

##  **تكوين الإعداد الصيني للرسم البياني**

في هذه الخطوة، ستستخدم الفئة "ChartChineseSettings" التي قمت بتعريفها في الخطوة السابقة.
مثال الكود:

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

ثم يمكنك رؤية التأثير في الصورة الناتجة، وسيتم عرض العناصر الموجودة في المخطط وفقًا لإعداداتك.

##  **خاتمة**

في هذا المثال، إذا لم تقم بتعيين المنطقة الصينية للمخطط، فقد يتم عرض عناصر المخطط التالية باللغة الافتراضية، مثل الإنجليزية.
بعد العملية المذكورة أعلاه، يمكننا الحصول على صورة مخطط الإخراج مع المنطقة الصينية.

|**العناصر المدعومة**|**القيمة في هذا المثال**|**القيمة الافتراضية في البيئة الإنجليزية**|
| :- | :- | :- |
|اسم عنوان المحور|坐标轴标题|عنوان المحور|
|اسم وحدة المحور|百,千...|مئات، آلاف...|
|اسم عنوان المخطط|图表标题|عنوان التخطيط|
|أسطورة زيادة الاسم|增加|يزيد|
|أسطورة إنقاص الاسم|减少|ينقص|
|الاسم الإجمالي للأسطورة|汇总|المجموع|
|اسم آخر|其他|آخر|
|اسم السلسلة|系列|مسلسل|
