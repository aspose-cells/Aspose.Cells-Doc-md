---
title: تحويل الرسم البياني إلى صورة للمنطقة اليابانية
description: تعرف على كيفية استخدام Aspose.Cells for .NET لتعيين التكوين الياباني للمخطط. سيوضح دليلنا كيفية تكوين المخططات لدعم الأحرف والتنسيقات اليابانية، بما في ذلك الخطوط والحجم واتجاه النص والمزيد.
keywords: Aspose.Cells for .NET, Charts, Japanese configuration, font, font size, text direction, support.
linktitle: تعيين المنطقة اليابانية
type: docs
weight: 10
url: /ar/net/convert-chart-to-image-for-japanese-region/
alias: [/net/set-japanese-configuration-for-chart/]
---
{{% alert color="primary" %}}

في هذا الموضوع، سنوضح لك كيفية تعيين المنطقة اليابانية للمخطط.

{{% /alert %}}

##  **يحدد فئة الميراث**

 الخطوة الأولى، تحتاج إلى تحديد فئة "ChartJapaneseSettings" التي ترث منها[**إعدادات عولمة الرسم البياني**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
بعد ذلك، من خلال إعادة كتابة الوظائف ذات الصلة، يمكنك تعيين نص عناصر المخطط بلغتك الخاصة.
مثال الكود:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

##  **تكوين الإعداد الياباني للرسم البياني**

في هذه الخطوة، ستستخدم الفئة "ChartJapaneseSettings" التي حددتها في الخطوة السابقة.
مثال الكود:

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

ثم يمكنك رؤية التأثير في الصورة الناتجة، وسيتم عرض العناصر الموجودة في المخطط وفقًا لإعداداتك.

##  **خاتمة**

في هذا المثال، إذا لم تقم بتعيين المنطقة اليابانية للمخطط، فقد يتم عرض عناصر المخطط التالية باللغة الافتراضية، مثل الإنجليزية.
بعد العملية المذكورة أعلاه، يمكننا الحصول على صورة مخطط الإخراج مع المنطقة اليابانية.

|**العناصر المدعومة**|**القيمة في هذا المثال**|**القيمة الافتراضية في البيئة الإنجليزية**|
| :- | :- | :- |
|اسم عنوان المحور|軸タイトル|عنوان المحور|
|اسم وحدة المحور|百,千...|مئات، آلاف...|
|اسم عنوان المخطط|グラフ タイトル|عنوان التخطيط|
|أسطورة زيادة الاسم|ぞうか|يزيد|
|أسطورة إنقاص الاسم|削減|ينقص|
|الاسم الإجمالي للأسطورة|すべての|المجموع|
|اسم آخر|その他|آخر|
|اسم السلسلة|シリーズ|مسلسل|
