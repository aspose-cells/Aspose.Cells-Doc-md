---
title: Renderizar elementos del gráfico seleccionado como gráficos de Excel
type: docs
weight: 30
url: /es/reportingservices/render-selected-chart-items-to-excel-charts/
---

{{% alert color="primary" %}} 

Para renderizar solo algunos gráficos en un informe a gráficos de Excel:

1. Abrir el archivo **Aspose.Cells.ReportingServices.xml**.
1. Modificar los parámetros de configuración del archivo **Aspose.Cells.ReportingServices.xml**.
1. Agregar la información de configuración del informe deseado.
1. Agregar la información para los elementos del gráfico que no desea exportar como gráficos editables. Estos elementos se exportan como imágenes estáticas.

Por ejemplo:

{{< highlight java >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**Un gráfico exportado como imagen** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_1.png)

**Un gráfico exportado como gráfico editable de Excel** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
