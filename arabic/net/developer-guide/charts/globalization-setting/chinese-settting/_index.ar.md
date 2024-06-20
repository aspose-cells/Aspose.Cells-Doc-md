---
title: تحويل الرسم البياني إلى صورة للمنطقة الصينية
description: تعرف على كيفية استخدام مجموعة Aspose.Cells for .NET لضبط تكوين الرسوم البيانية الصينية. سيقدم دليلنا كيفية ضبط الرسوم البيانية لدعم الحروف والصيغ والحجوم واتجاهات النصوص الصينية، وأكثر من ذلك.
keywords: Aspose.Cells for .NET, رسوم بيانية, تكوين صيني, خطوط, حجم الخط, اتجاه النص, دعم.
linktitle: تحديد المنطقة الصينية
type: docs
weight: 9
url: /ar/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

في هذا الموضوع، سنوضح لك كيفية تعيين المنطقة الصينية لرسم بياني.

{{% /alert %}}

## **تحديد فئة الإرث**

الخطوة الأولى، تحتاج إلى تعريف فئة "ChartChineseSetttings" التي ترث من [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
ثم، من خلال إعادة كتابة الوظائف ذات الصلة، يمكنك تعيين نص عناصر الرسم البياني بلغتك.
مثال على الكود:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

## **تهيئة إعدادات اللغة الصينية للرسم البياني**

في هذه الخطوة، ستستخدم فئة "ChartChineseSetttings" التي قمت بتعريفها في الخطوة السابقة.
مثال على الكود:

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

ثم يمكنك رؤية التأثير في الصورة الناتجة، حيث سيتم تقديم عناصر الرسم البياني وفقًا لإعداداتك.

## **الاستنتاج**

في هذا المثال، إذا لم تقم بتحديد المنطقة الصينية لرسم بياني، فقد يتم عرض عناصر الرسم البياني التالية باللغة الافتراضية، مثل الإنجليزية.
بعد العملية المذكورة أعلاه، يمكننا الحصول على صورة رسم بياني إخراجية مع المنطقة الصينية.

| ** العناصر المدعومة ** | ** القيمة في هذا المثال ** | ** القيمة الافتراضية في بيئة اللغة الإنجليزية ** |
| :- | :- | :- |
|اسم عنوان المحور|坐标轴标题|عنوان المحور|
| اسم وحدة المحور | 百,千... | مئات ، آلاف ... |
|Chart Title Name|اسم عنوان الرسم البياني|اسم عنوان الرسم البياني|
|Legend Increase Name|زيادة|زيادة|
|Legend Decrease Name|انخفاض|انخفاض|
|Legend Total Name|الإجمالي|الإجمالي|
|Other Name|آخر|آخر|
|Series Name|سلسلة|سلسلة|
