---
title: قم بإنشاء مخططات Pivot في xlsx4j
type: docs
weight: 30
url: /ar/java/create-pivot-charts-in-xlsx4j/
---
## **Aspose.Cells - تكوين مخططات محورية**
الجدول المحوري هو ملخص تفاعلي للسجلات. على سبيل المثال ، قد يكون لديك المئات من إدخالات الفاتورة في قائمة بورقة عمل. يمكن للجدول المحوري إجمالي الفواتير حسب العميل أو المنتج أو التاريخ. باستخدام Microsoft Excel ، من الممكن إعادة ترتيب المعلومات في الجدول المحوري بسرعة عن طريق سحب الأزرار إلى موضع جديد.
المخطط المحوري هو تمثيل رسومي تفاعلي للبيانات في جدول محوري. تم تقديم المخططات المحورية في Excel 2000. ويسهل استخدام المخطط المحوري فهم البيانات نظرًا لأن الجدول المحوري ينشئ الإجماليات الفرعية والإجماليات تلقائيًا.

يدعم Aspose.Cells الجداول المحورية والمخططات المحورية.

**Java**

{{< highlight "java" >}}

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

// Saving the Excel file

workbook.save(dataDir + "Aspose_PivotChart_Out.xls");


{{< /highlight >}}
## **تحميل كود الجري**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/createpivotcharts/AsposePivotChart.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[إنشاء الجداول المحورية والمخططات المحورية](/cells/ar/java/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}
