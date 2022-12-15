---
title: تغيير موضع المخطط وحجمه
type: docs
weight: 20
url: /ar/java/change-chart-position-and-size/
---
## **Aspose.Cells - تغيير موضع الرسم البياني وحجمه**
لتغيير موضع الرسم البياني (إحداثيات س ، ص) وحجمه (ارتفاع ، عرض) ، استخدم هذه الخصائص باستخدام Aspose.Cells:

1. Chart.getChartObject (). get / setWidth ()
1. Chart.getChartObject (). get / setHeight ()
1. Chart.getChartObject (). get / setX ()
1. Chart.getChartObject (). get / setY ()

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook(dataDir + "AsposeChart.xls");

Worksheet worksheet = workbook.getWorksheets().get(0);

//Load the chart from source worksheet

Chart chart = worksheet.getCharts().get(0);

//Resize the chart

chart.getChartObject().setWidth(400);

chart.getChartObject().setHeight(300);

//Reposition the chart

chart.getChartObject().setX(250);

chart.getChartObject().setY(150);

{{< /highlight >}}
## **تحميل كود الجري**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChangeChartPositionAndSize.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[قم بتغيير موضع المخطط وحجمه](/cells/ar/java/change-chart-position-and-size/).

{{% /alert %}}
