---
title: إنشاء رسوم بيانية محورية باستخدام Aspose.Cells
type: docs
weight: 40
url: /ar/java/create-pivot-charts-using-aspose-cells/
---

## **Aspose.Cells - إنشاء رسوم بيانية محورية**
الجدول المحوري هو ملخص تفاعلي للسجلات. على سبيل المثال، قد تحتوي على مئات الإدخالات الخاصة بالفواتير في قائمة داخل صفحة العمل. يمكن للجدول المحوري إجمالي الفواتير حسب العميل، المنتج أو التاريخ. باستخدام مايكروسوفت إكسل يمكن بسرعة إعادة ترتيب المعلومات في الجدول المحوري عن طريق سحب الأزرار إلى موقع جديد.
الرسم البياني المحوري هو تمثيل رسومي تفاعلي للبيانات في الجدول المحوري. تم إدخال الرسوم البيانية المحورية في إكسل 2000. باستخدام الرسم البياني المحوري يصبح أسهل فهم البيانات نظرًا لأن الجدول المحوري يقوم تلقائيًا بإنشاء المجاميع الفرعية والمجاميع.

يدعم Aspose.Cells الجداول المحورية والرسوم البيانية المحورية.

**Java**

{{< highlight java >}}

 // Instantiating an Workbook object

Workbook workbook = new Workbook(dataDir + "AsposePivotTable.xls");

// Adding a new sheet

int sheetIndex = workbook.getWorksheets().add(SheetType.CHART);

Worksheet sheet3 = workbook.getWorksheets().get(sheetIndex);

// Naming the sheet

sheet3.setName("PivotChart");

// Adding a column chart

int chartIndex = sheet3.getCharts().add(ChartType.COLUMN, 0, 5, 28, 16);

Chart chart = sheet3.getCharts().get(chartIndex);

// Setting the pivot chart data source

chart.setPivotSource("PivotTable!PivotTable1");

chart.setHidePivotFieldButtons(false);

{{< /highlight >}}
## **تحميل رمز التشغيل**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposePivotChart.java)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [إنشاء جداول محورية ورسوم بيانية محورية](/cells/ar/java/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
