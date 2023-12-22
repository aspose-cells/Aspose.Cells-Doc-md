---
title:  Uso de la clase ChartGlobalizationSettings para establecer un idioma diferente para el componente del gráfico
description: Aprenda a utilizar la clase ChartGlobalizationSettings en Aspose.Cells for .NET para configurar diferentes idiomas para los componentes del gráfico. Nuestra guía lo ayudará a comprender cómo localizar elementos, etiquetas y leyendas de gráficos a diferentes idiomas, lo que le permitirá presentar sus datos de una manera culturalmente apropiada.
keywords: Aspose.Cells for .NET, charting, chart globalization, languages, localization, ChartGlobalizationSettings, elements, labels, legends.
type: docs
weight: 2200
url: /es/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---
##  **Posibles escenarios de uso**

 Aspose.Cells Las API han expuesto el[**GráficoGlobalizaciónConfiguración**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) clase para hacer frente a los escenarios en los que el usuario desea configurar el componente del gráfico en un idioma diferente. etiquetas personalizadas para subtotales en una hoja de cálculo.

##  **Introducción a la clase ChartGlobalizationSettings**

 El[**GráficoGlobalizaciónConfiguración**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)La clase ofrece actualmente los siguientes 8 métodos que se pueden anular en una clase personalizada para traducir, como el nombre de AxisTitle, el nombre de AxisUnit, el nombre de ChartTitle, etc., a diferentes idiomas.
1. [**Obtener nombre del título del eje**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Obtiene el nombre del Título del Eje.
1. [**Obtener nombre de unidad del eje**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Obtiene el nombre de la unidad del eje.
1. [**Obtener nombre del título del gráfico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Obtiene el nombre del título del gráfico.
1. [**ObtenerLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Obtiene el nombre de Disminución para Leyenda.
1. [**ObtenerLegendAumentarNombre**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Obtiene el nombre del aumento de Leyenda.
1. [**ObtenerLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Obtiene el nombre de Total para Leyenda.
1. [**Obtener otro nombre**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): Obtiene el nombre de las etiquetas "Otras" para el gráfico.
1. [**Obtener nombre de serie**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Obtiene el nombre de la Serie en el Gráfico.

###  **Traducción de idiomas personalizada**
Aquí, crearemos un gráfico en cascada basado en los siguientes datos. Los nombres de los componentes del gráfico se mostrarán en inglés en el gráfico. Usaremos un ejemplo en turco para mostrar cómo mostrar el título del gráfico, los nombres de aumento/disminución de la leyenda, el nombre total y el título del eje en turco.

![todo:image_alt_text](sample.png)

##  **Código de muestra**
 El siguiente código de muestra carga el[archivo de Excel de muestra](waterfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

##  Salida generada por el código de muestra.

Esta es la salida de consola del código de muestra anterior.

{{< highlight "java" >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
