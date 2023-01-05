---
title: Representar elementos de gráficos seleccionados en gráficos de Excel
type: docs
weight: 30
url: /es/reportingservices/render-selected-chart-items-to-excel-charts/
---
{{% alert color="primary" %}} 

Para representar solo algunos gráficos en un informe a gráficos de Excel:

1. Abre el**Aspose.Cells.ReportingServices.xml** expediente.
1.  Modificar los parámetros de configuración del**Aspose.Cells.ReportingServices.xml** expediente.
1. Agregue la información de configuración del informe deseado.
1. Agregue la información de los elementos del gráfico que no desea exportar como gráficos editables. Estos elementos se exportan como imágenes estáticas.

Por ejemplo:

{{< highlight "java" >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**Un gráfico exportado como una imagen** 

![todo:imagen_alternativa_texto](render-selected-chart-items-to-excel-charts_1.png)

**Un gráfico exportado como un gráfico de Excel editable** 

![todo:imagen_alternativa_texto](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
