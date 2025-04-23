---
title: Usar la clase ChartGlobalizationSettings para establecer un idioma diferente para el componente del gráfico 
description: Aprenda a usar la clase ChartGlobalizationSettings en Aspose.Cells for .NET para establecer diferentes idiomas para los componentes del gráfico. Nuestra guía le ayudará a comprender cómo localizar elementos de gráficos, etiquetas y leyendas en diferentes idiomas, lo que le permitirá presentar sus datos de una manera culturalmente apropiada.
keywords: Aspose.Cells for .NET, gráficos, globalización de gráficos, idiomas, localización, ChartGlobalizationSettings, elementos, etiquetas, leyendas.
type: docs
weight: 2200
url: /es/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Escenarios de uso posibles**

Las API de Aspose.Cells han expuesto la clase [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) para tratar los escenarios en los que el usuario desea establecer el componente del gráfico en un idioma diferente, como etiquetas personalizadas para subtotales en una hoja de cálculo. 

## **Introducción a la clase ChartGlobalizationSettings**

La clase [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) ofrece actualmente los siguientes 8 métodos que se pueden sobrescribir en una clase personalizada para traducir, por ejemplo, el nombre de AxisTitle, AxisUnit y ChartTitle a un idioma diferente.
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Obtiene el nombre del Título para el Eje.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Obtiene el nombre de la Unidad del Eje.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Obtiene el nombre del Título del Gráfico.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Obtiene el nombre de Disminución para la Leyenda.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Obtiene el nombre de Aumento para la Leyenda.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Obtiene el nombre de Total para la Leyenda.
1. [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): Obtiene el nombre de las etiquetas "Otro" para el Gráfico.
1. [**GetSeriesName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Obtiene el nombre de la Serie en el Gráfico.

### **Traducción personalizada de idioma**
Aquí, crearemos un gráfico de cascada basado en los siguientes datos. Los nombres de los componentes del gráfico se mostrarán en inglés en el gráfico. Utilizaremos un ejemplo en idioma turco para mostrar cómo mostrar el Título del Gráfico, los nombres de Aumento/Disminución de la Leyenda, el nombre de Total y el Título del Eje en turco.

![todo:image_alt_text](sample.png)

## **Código de muestra**
El siguiente código de ejemplo carga el [archivo de Excel de muestra](waterfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

Resultado generado por el código de ejemplo

Este es el resultado de consola del código de ejemplo anterior.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
