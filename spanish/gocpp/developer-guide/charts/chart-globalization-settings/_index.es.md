---
title: Uso de la clase ChartGlobalizationSettings para establecer diferentes idiomas para el componente de gráficos con Golang a través de C++
linktitle: Uso de la clase ChartGlobalizationSettings
description: Aprenda cómo usar la clase ChartGlobalizationSettings en Aspose.Cells for C++ para establecer diferentes idiomas en los componentes del gráfico. Nuestra guía le ayudará a entender cómo localizar los elementos del gráfico, etiquetas y leyendas a diferentes idiomas, permitiéndole presentar sus datos de manera culturalmente apropiada.
keywords: Aspose.Cells for C++, creación de gráficos, globalización de gráficos, idiomas, localización, ConfiguraciónGlobalizaciónDeGráficos, elementos, etiquetas, leyendas.
type: docs
weight: 2200
url: /es/go-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Escenarios de uso posibles**

Las API de Aspose.Cells han expuesto la clase [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/) para tratar los escenarios en los que el usuario desea establecer el componente del gráfico en un idioma diferente, como etiquetas personalizadas para subtotales en una hoja de cálculo. 

## **Introducción a la clase ChartGlobalizationSettings**

La clase [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/) actualmente ofrece los siguientes 8 métodos que pueden ser sobrescritos en una clase personalizada para traducir, como el nombre del Título del Eje, el nombre de la Unidad del Eje, el nombre del Título del Gráfico, y otros a diferentes idiomas.

1. [**GetAxisTitleName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getaxistitlename/): Obtiene el nombre del Título para el Eje.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getaxisunitname/): Obtiene el nombre de la Unidad del Eje.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getcharttitlename/): Obtiene el nombre del Título del Gráfico.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegenddecreasename/): Obtiene el nombre de Disminución para la Leyenda.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegendincreasename/): Obtiene el nombre de Aumento para la Leyenda.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegendtotalname/): Obtiene el nombre de Total para la Leyenda.
1. [**GetOtherName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getothername/): Obtiene el nombre de las etiquetas "Otro" para el Gráfico.
1. [**GetSeriesName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getseriesname/): Obtiene el nombre de la Serie en el Gráfico.

### **Traducción personalizada de idioma**
Aquí, crearemos un gráfico de cascada basado en los siguientes datos. Los nombres de los componentes del gráfico se mostrarán en inglés en el gráfico. Utilizaremos un ejemplo en idioma turco para mostrar cómo mostrar el Título del Gráfico, los nombres de Aumento/Disminución de la Leyenda, el nombre de Total y el Título del Eje en turco.

![todo:image_alt_text](sample.png)

## **Código de muestra**
El siguiente código de ejemplo carga el [archivo de Excel de muestra](waterfall.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartGlobalizationSettings.go" >}}
Resultado generado por el código de ejemplo

Este es el resultado de consola del código de ejemplo anterior.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
