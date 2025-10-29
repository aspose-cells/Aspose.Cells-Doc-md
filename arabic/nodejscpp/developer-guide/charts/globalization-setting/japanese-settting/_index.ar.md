---  
title: تحويل الرسم البياني إلى صورة للمنطقة اليابانية باستخدام Node.js عبر C++  
description: تعلم كيفية استخدام Aspose.Cells for Node.js via C++ لضبط إعدادات اللغة اليابانية في الرسم البياني. سيرينا دليلنا كيف يمكن تكوين الرسوم البيانية لدعم الأحرف اليابانية والتنسيقات، بما في ذلك الخطوط، الحجم، اتجاه النص، والمزيد.  
keywords: Aspose.Cells for Node.js via C++، الرسوم البيانية، إعدادات اللغة اليابانية، الخط، حجم الخط، اتجاه النص، الدعم.  
linktitle: تعيين منطقة يابانية  
type: docs  
weight: 10  
url: /ar/nodejs-cpp/convert-chart-to-image-for-japanese-region/  
alias: [/nodejs-cpp/set-japanese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
في هذا الموضوع، سنوضح لك كيفية تعيين المنطقة اليابانية للرسم البياني.  
{{% /alert %}}  

## **تحديد فئة الإرث**  

الخطوة الأولى، تحتاج إلى تعريف فئة "ChartJapaneseSettings" الوريثة من [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/).  
ثم، من خلال إعادة كتابة الوظائف ذات الصلة، يمكنك تعيين نص عناصر الرسم البياني بلغتك.  
مثال على الكود:  
```javascript
const AsposeCells = require("aspose.cells.node");

class ChartJapaneseSettings extends AsposeCells.ChartGlobalizationSettings {
getAxisTitleName() {
return "軸タイトル";
}

getAxisUnitName(type) {
switch (type) {
case AsposeCells.DisplayUnitType.None:
return '';
case AsposeCells.DisplayUnitType.Hundreds:
return "百";
case AsposeCells.DisplayUnitType.Thousands:
return "千";
case AsposeCells.DisplayUnitType.TenThousands:
return "万";
case AsposeCells.DisplayUnitType.HundredThousands:
return "10万";
case AsposeCells.DisplayUnitType.Millions:
return "百万";
case AsposeCells.DisplayUnitType.TenMillions:
return "千万";
case AsposeCells.DisplayUnitType.HundredMillions:
return "億";
case AsposeCells.DisplayUnitType.Billions:
return "10億";
case AsposeCells.DisplayUnitType.Trillions:
return "兆";
default:
return '';
}
}

getChartTitleName() {
return "グラフ タイトル";
}

getLegendDecreaseName() {
return "削減";
}

getLegendIncreaseName() {
return "ぞうか";
}

getLegendTotalName() {
return "すべての";
}

getOtherName() {
return "その他";
}

getSeriesName() {
return "シリーズ";
}
}
```  

## **تكوين إعدادات اللغة اليابانية للرسم البياني**  

 في هذه الخطوة، ستستخدم فئة "ChartJapaneseSettings" التي قمت بتعريفها في الخطوة السابقة.  
مثال على الكود:  

```javascript  
const { Workbook } = require('aspose.cells');

let wb = new Workbook("Japanese.xls");
wb.settings.globalizationSettings.chartSettings = new ChartJapaneseSettings();
let chart0 = wb.worksheets[0].charts[0];
chart0.toImage("Output.png");
```

ثم يمكنك رؤية التأثير في الصورة الناتجة، حيث سيتم تقديم عناصر الرسم البياني وفقًا لإعداداتك.  

## **الاستنتاج**  

في هذا المثال ، إذا لم تقم بتعيين المنطقة اليابانية للرسم البياني ، فقد يتم رسم عناصر الرسم البياني التالية باللغة الافتراضية ، مثل الإنجليزية.  
بعد العملية أعلاه ، يمكننا الحصول على صورة رسم بياني مخرجات مع منطقة يابانية.  

| ** العناصر المدعومة ** | ** القيمة في هذا المثال ** | ** القيمة الافتراضية في بيئة اللغة الإنجليزية ** |  
| :- | :- | :- |  
| اسم عنوان المحور | 軸タイトル | عنوان المحور |  
| اسم وحدة المحور | 百,千... | مئات ، آلاف ... |  
| اسم عنوان الرسم البياني | グラフ タイトル | عنوان الرسم البياني |  
| اسم زيادة الوسيلة | ぞうか | زيادة |  
| اسم نقصان الوسيلة | 削減 | نقص |  
| اسم المجموع الأسطوري | すべての | مجموع |  
| اسم آخر | その他 | آخر |  
| اسم السلسلة | シリーズ | السلسلة |  

{{< app/cells/assistant language="nodejs-cpp" >}}
