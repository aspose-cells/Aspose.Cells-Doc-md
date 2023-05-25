---
title:  Uso de la clase ChartGlobalizationSettings para establecer un idioma diferente para el componente de gráfico
type: docs
weight: 2200
url: /es/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---
##  **Posibles escenarios de uso**

 Aspose.Cells Las API han expuesto el[**GráficoGlobalizaciónConfiguración**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) class para manejar los escenarios en los que el usuario desea configurar el componente del gráfico en un idioma diferente. etiquetas personalizadas para subtotales en una hoja de cálculo.

##  **Introducción a la clase ChartGlobalizationSettings**

 El[**GráficoGlobalizaciónConfiguración**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)class actualmente ofrece los siguientes 8 métodos que se pueden anular en una clase personalizada para traducir, como el nombre de AxisTitle, el nombre de AxisUnit, el nombre de ChartTitle, etc., a un idioma diferente.
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Obtiene el nombre del Título para Axis.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Obtiene el Nombre de la Unidad del Eje.
1. [**ObtenerNombreTítuloGráfico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Obtiene el nombre del Título del gráfico.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Obtiene el nombre de Decrease for Legend.
1. [**ObtenerLeyendaIncrementarNombre**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Obtiene el nombre de aumento de Leyenda.
1. [**ObtenerLeyendaTotalNombre**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Obtiene el nombre de Total para Legend.
1. [**ObtenerOtroNombre**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): Obtiene el nombre de las etiquetas "Otros" para Chart.
1. [**ObtenerNombreSerie**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Obtiene el nombre de la Serie en el Gráfico.

###  **Traducción personalizada de idiomas**
Aquí, crearemos un gráfico de cascada basado en los siguientes datos. Los nombres de los componentes del gráfico se mostrarán en inglés en el gráfico. Usaremos un ejemplo de idioma turco para mostrar cómo mostrar el título del gráfico, los nombres de aumento/disminución de la leyenda, el nombre total y el título del eje en turco.

![todo:imagen_alt_texto](sample.png)

##  **Código de muestra**
 El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](waterfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

##  Salida generada por el código de muestra

Esta es la salida de la consola del código de muestra anterior.

{{< highlight "java" >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
