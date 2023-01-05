---
title: قم بإنشاء مخططات محورية باستخدام Aspose.Cells
type: docs
weight: 40
url: /ar/java/create-pivot-charts-using-aspose-cells/
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

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposePivotChart.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[إنشاء جداول محورية ومخططات محورية](/cells/ar/java/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}
