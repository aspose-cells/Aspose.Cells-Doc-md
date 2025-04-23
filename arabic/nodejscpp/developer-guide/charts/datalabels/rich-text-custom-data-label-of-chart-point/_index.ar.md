---
title: تسمية بيانات مخصصة غنية مع نص مخصّص على نقطة المخطط باستخدام Node.js عبر C++
description: تعلم كيفية إضافة تسميات مخصصة غنية بالنص إلى نقاط المخطط في Aspose.Cells for Node.js via C++. سيرينا دليلنا كيفية تنسيق التسميات باستخدام خطوط وألوان وخيارات محاذاة مختلفة لتعزيز مظهر وقراءة مخططاتك.
keywords: Aspose.Cells for Node.js via C++، رسم بياني، نص منسق، تسميات بيانات مخصصة، خطوط، ألوان، محاذاة، مظهر، سهولة القراءة.
type: docs
weight: 10
url: /ar/nodejs-cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

يمكنك استخدام Aspose.Cells لإنشاء تسميات بيانات مخصصة غنية للنقاط على المخططات. يوفر Aspose.Cells طريقة [**ChartTextFrame.characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#characters-number-number-) لإرجاع كائن [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) الذي يمكن استخدامه لتعيين خصائص الخط للنص مثل لونه، عريضته، إلخ.

{{% /alert %}}

## تسمية بيانات مخصصة بتنسيق نص غني لنقطة الرسم البياني

يسمح الكود التالي بالوصول إلى نقطة المخطط الأولى من السلسلة الأولى، تعيين نصها ثم تعيين خط العشرة أحرف الأولى من خلال ضبط لونها إلى الأحمر وعرضها إلى **صحيح**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_custom_datalabel.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = worksheet.getCharts().get(0);

// Access the data label of first series first point
const dlbls = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

// Set data label text
dlbls.setText("Rich Text Label");

// Set the font setting of the first 10 characters
const fntSetting = dlbls.characters(0, 10);
fntSetting.getFont().setColor(AsposeCells.Color.Red);
fntSetting.getFont().setIsBold(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
