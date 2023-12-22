---
title: Crear gráfico de acciones de apertura-alto-bajo-cierre (OHLC)
description: Aprenda a crear un gráfico de acciones de apertura, máximo, mínimo y cierre utilizando Aspose.Cells for .NET. Nuestra guía le demostrará cómo trazar datos del mercado de valores, incluidos los precios de apertura, máximo, mínimo y cierre, en un gráfico para un mejor análisis y visualización.
keywords: Aspose.Cells for .NET, Open-High-Low-Close Stock Chart, Stock Market Data, Analysis, Visualization.
type: docs
weight: 182
url: /es/net/create-open-high-low-close-stock-chart/
---
##  **Posibles escenarios de uso**
El gráfico Apertura-Alto-Bajo-Cierre (OHLC) utiliza cinco columnas de datos, en orden: categoría, apertura, máximo, mínimo y cierre. El rango de precios en cada categoría se indica nuevamente mediante una línea vertical, mientras que el rango entre apertura y cierre se indica mediante una barra flotante más amplia; si el precio aumenta en la categoría (el cierre es mayor que la apertura), la barra se llena con un color, mientras que si el precio disminuye, la barra se llena con otro. Este tipo de gráfico a menudo se denomina gráfico de velas.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
##  **Mejoras de visibilidad en el gráfico.**
menudo utilizamos colores en lugar de blanco y negro para indicar precios crecientes y decrecientes. En el primer conjunto de velas a continuación, el rojo muestra precios crecientes y verdes decrecientes.

![todo:image_alt_text](sample2.png)
##  **Código de muestra**
 El siguiente código de muestra carga el[archivo de Excel de muestra](Open-High-Low-Close.xlsx) y genera el[archivo de salida de Excel](out.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-open-high-low-close-stock-chart.cs" >}}
