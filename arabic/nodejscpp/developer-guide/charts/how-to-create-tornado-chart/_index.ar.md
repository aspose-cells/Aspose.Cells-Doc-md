---
title: كيفية إنشاء مخطط إعصار باستخدام Node.js عبر C++
linktitle: كيفية إنشاء رسم بياني للإعصار
type: docs
weight: 73
url: /ar/nodejs-cpp/create-tornado-chart/
description: تعلم كيفية إنشاء مخطط إعصار باستخدام API Aspose.Cells for Node.js via C++.
keywords: إنشاء رسم بياني على شكل إعصار باستخدام Node.js، إضافة رسم بياني على شكل إعصار، إدراج رسم بياني على شكل إعصار
---

## **مقدمة**
الرسم البياني للإعصار، المعروف أيضًا باسم الرسم البياني للإعصار أو الرسم البياني للتورنادو، هو نوع من تصور البيانات يُستخدم في التحليل الحساسية في برنامج إكسل. يساعدك على فهم تأثير تغيير المتغيرات على نتيجة معينة.

## **كيفية إنشاء رسم بياني للإعصار في إكسل**
يمكنك إنشاء رسم بياني للإعصار في إكسل من خلال اتباع هذه الخطوات:
1. حدد البيانات وانتقل إلى إدراج --> الرسوم البيانية --> إدراج رسم بياني عمودي أو شريطي --> رسم بياني عمودي مكدس. انقر عليه.
<br>
<img src="1.png" width=70% />
2. تغيير محور الصف: انقر بزر الماوس الأيمن فوق محور الصف. انقر على تنسيق المحور. في العلامات، انقر على القائمة المنسدلة لموضع العلامة وحدد العنصر المنخفض.
<br>
<img src="2.png" width=70% />
3. حدد أي شريط وانتقل إلى التنسيق. ضبط عرض الفجوة المناسب.
<br>
<img src="3.png" width=70% />
4. لنقم بإزالة علامة الناقص (-) من رسم بياني الإعصار. حدد محور السين. انتقل إلى التنسيق. في خيارات المحور، انقر على الرقم. في الفئة، حدد مخصص. في رمز التنسيق اكتب ###0،###0. انقر على إضافة.
<br>
<img src="4.png" width=70% />
5. انقر فوق محور الصف وانتقل إلى خيارات المحور. في خيارات المحور، حدد الفئات بترتيب معكوس.
<br>
<img src="5.png" width=70% />

## **كيفية إضافة رسم بياني على شكل إعصار في Aspose.Cells for Node.js via C++**
يرجى الاطلاع على الكود النموذجي التالي. يقوم بتحميل [ملف إكسل نموذجي](sample.xlsx) الذي يحتوي على بعض البيانات النموذجية. ثم يقوم بإنشاء رسم بياني عمودي مكدس بناءً على البيانات الأولية وتعيين الخصائص ذات الصلة. في النهاية، يقوم بحفظ الدفتر إلى [تنسيق XLSX الناتج](out.xlsx). تُظهر اللقطة الشاشية التالية الرسم البياني للإعصار الذي تم إنشاؤه بواسطة Aspose.Cells في ملف الإكسل الناتج.
<br>
<img src="6.png" width=70% />

### **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);
const charts = sheet.getCharts();
// Add bar chart
const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
const chart = charts.get(index);

// Set data for bar chart
chart.setChartDataRange("A1:C7", true);

// Set properties for bar chart
chart.getTitle().setText("Tornado chart");
chart.setStyle(2);
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);
chart.getPlotArea().getBorder().setColor(AsposeCells.Color.White);
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);

chart.getCategoryAxis().setTickLabelPosition(AsposeCells.TickLabelPositionType.Low);
chart.getCategoryAxis().setIsPlotOrderReversed(true);

chart.setGapWidth(10);

const valueAxis = chart.getValueAxis();
valueAxis.getTickLabels().setNumberFormat("#,##0;#,##0");

workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
