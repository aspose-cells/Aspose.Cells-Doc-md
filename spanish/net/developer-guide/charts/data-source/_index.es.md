---
title: Establecer fuente de datos para el gráfico
description: Conozca las diversas fuentes de datos admitidas por Aspose.Cells for .NET. Nuestra guía lo guiará a través de los diferentes tipos de fuentes de datos disponibles y le mostrará cómo conectarse y recuperar datos de ellas para completar sus hojas de trabajo.
keywords: Aspose.Cells for .NET, charting, data formatting, labels, colors, fonts, appearance, usability.
linktitle: Fuente de datos
type: docs
weight: 10
url: /es/net/data-formatting-in-charts/
---
En nuestros temas anteriores, ya proporcionamos muchos ejemplos para demostrar cómo se puede configurar una fuente de datos para su gráfico, pero en este tema, brindaremos más detalles sobre los tipos de datos que se pueden configurar para un gráfico.

##  **Configuración de datos del gráfico**

Hay dos tipos de datos con los que trabajar mientras se trabaja en gráficos utilizando Aspose.Cells de la siguiente manera:

- Datos del gráfico.
- Datos de categoría.

###  **Datos del gráfico**

 Los datos de los gráficos son los datos que utilizamos como fuente de datos para crear nuestros gráficos. Podemos agregar un rango de celdas (que contienen datos del gráfico) llamando al[**SerieColección**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) objetos[**Agregar**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add)método.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

###  **Datos de categoría**

 Los datos de categoría se utilizan para etiquetar los datos del gráfico y se pueden agregar a[**SerieColección**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) usando su[**CategoríaDatos**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)propiedad. A continuación se proporciona un ejemplo completo para demostrar el uso de datos de gráficos y categorías. Después de ejecutar el código de ejemplo anterior, se agregará un gráfico de columnas a la hoja de trabajo como se muestra a continuación.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

##  **Temas avanzados**
- [Cambie la fuente de datos del gráfico a la hoja de trabajo de destino mientras copia filas o rango](/cells/es/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Crear gráficos dinámicos](/cells/es/net/create-dynamic-charts/)
- [Manera sencilla de configurar el gráfico utilizando el método Chart.SetChartDataRange](/cells/es/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Encuentre el tipo de valores X e Y de puntos en series de gráficos](/cells/es/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
