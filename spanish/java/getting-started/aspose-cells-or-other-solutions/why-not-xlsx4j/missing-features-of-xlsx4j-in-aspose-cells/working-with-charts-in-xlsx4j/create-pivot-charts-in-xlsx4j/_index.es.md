---
title: Crear gráficos dinámicos en xlsx4j
type: docs
weight: 30
url: /es/java/create-pivot-charts-in-xlsx4j/
---

## **Aspose.Cells - Crear gráficos dinámicos**
Una tabla dinámica es un resumen interactivo de registros. Por ejemplo, puede tener cientos de entradas de factura en una lista en una hoja de cálculo. Una tabla dinámica puede totalizar las facturas por cliente, producto o fecha. Con Microsoft Excel es posible reorganizar rápidamente la información en la tabla dinámica arrastrando botones a una nueva posición.
Un gráfico dinámico es una representación gráfica interactiva de los datos en una tabla dinámica. Los gráficos dinámicos se introdujeron en Excel 2000. El uso de un gráfico dinámico facilita aún más la comprensión de los datos, ya que la tabla dinámica crea subtotales y totales automáticamente.

Aspose.Cells admite tablas dinámicas y gráficos dinámicos.

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

// Saving the Excel file

workbook.save(dataDir + "Aspose_PivotChart_Out.xls");


{{< /highlight >}}
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/createpivotcharts/AsposePivotChart.java)

{{% alert color="primary" %}} 

Para más detalles, visita [Crear tablas dinámicas y gráficos dinámicos](/cells/es/java/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
