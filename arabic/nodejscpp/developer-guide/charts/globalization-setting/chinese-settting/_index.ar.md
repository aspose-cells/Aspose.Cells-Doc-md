---  
title: تحويل الرسم البياني إلى صورة للمنطقة الصينية باستخدام Node.js عبر C++  
description: تعلم كيفية استخدام Aspose.Cells for Node.js via C++ لضبط إعدادات الرسوم البيانية للغات الصينية، بما في ذلك الخطوط والأحجام واتجاهات النص والمزيد.  
keywords: Aspose.Cells لـ Node.js، الرسوم البيانية، إعدادات اللغة الصينية، الخطوط، حجم الخط، اتجاه النص، الدعم.  
linktitle: تحديد المنطقة الصينية  
type: docs  
weight: 9  
url: /ar/nodejs-cpp/convert-chart-to-image-for-chinese-region/  
alias: [/nodejs-cpp/set-chinese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
في هذا الموضوع، سنوضح لك كيفية تعيين المنطقة الصينية لرسم بياني.  
{{% /alert %}}  

## **تحديد فئة الإرث**  

الخطوة الأولى، تحتاج إلى تعريف فئة "ChartChineseSetttings" الوريثة من [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/).  
ثم، من خلال إعادة كتابة الوظائف ذات الصلة، يمكنك تعيين نص عناصر الرسم البياني بلغتك.  
مثال على الكود:  
```javascript
const AsposeCells = require("aspose.cells.node");

class ChartChineseSettings extends AsposeCells.ChartGlobalizationSettings {
getAxisTitleName() {
return "坐标轴标题";
}

getAxisUnitName(type) {
switch (type) {
case AsposeCells.DisplayUnitType.None:
return '';
case AsposeCells.DisplayUnitType.Hundreds:
return '百';
case AsposeCells.DisplayUnitType.Thousands:
return '千';
case AsposeCells.DisplayUnitType.TenThousands:
return '万';
case AsposeCells.DisplayUnitType.HundredThousands:
return '十万';
case AsposeCells.DisplayUnitType.Millions:
return '百万';
case AsposeCells.DisplayUnitType.TenMillions:
return '千万';
case AsposeCells.DisplayUnitType.HundredMillions:
return '亿';
case AsposeCells.DisplayUnitType.Billions:
return '十亿';
case AsposeCells.DisplayUnitType.Trillions:
return '兆';
default:
return '';
}
}

getChartTitleName() {
return "图表标题";
}

getLegendDecreaseName() {
return "减少";
}

getLegendIncreaseName() {
return "增加";
}

getLegendTotalName() {
return "汇总";
}

getOtherName() {
return "其他";
}

getSeriesName() {
return "系列";
}
}
```  

## **تهيئة إعدادات اللغة الصينية للرسم البياني**  

في هذه الخطوة، ستستخدم فئة "ChartChineseSetttings" التي قمت بتعريفها في الخطوة السابقة.  
مثال على الكود:  

```javascript  
const Workbook = require('aspose.cells');  
const wb = new Workbook("Chinese.xls");  
wb.settings.globalizationSettings.chartSettings = new ChartChineseSetttings();  
const chart0 = wb.worksheets[0].charts[0];  
chart0.toImage("Output.png");  
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

{{< app/cells/assistant language="nodejs-cpp" >}}
