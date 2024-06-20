---
title: Crear Gráfico de Cotizaciones Altas Bajas Cierre (HLC)
description: Aprende cómo crear un gráfico de cotizaciones altas bajas cierre utilizando Aspose.Cells for .NET. Nuestra guía paso a paso demostrará cómo graficar datos del mercado de valores, incluyendo los precios altos, bajos y de cierre, en un gráfico para un mejor análisis y visualización.
keywords: Aspose.Cells for .NET, Gráfico de Cotizaciones Altas Bajas Cierre, Datos del Mercado de Valores, Análisis, Visualización.
type: docs
weight: 181
url: /es/net/create-high-low-close-stock-chart/
---

## **Escenarios de uso posibles**
El gráfico de cotizaciones altas-bajas-cierre (HLC) utiliza cuatro columnas de datos. La primera columna es una categoría, usualmente una fecha pero también se pueden usar nombres de acciones. Las siguientes tres columnas en orden son para los precios altos, bajos y de cierre. El rango de precio para cada categoría se indica mediante una línea vertical de bajo a alto, y el precio de cierre se muestra usando una marca extendiéndose hacia la derecha de esta línea.

![todo:image_alt_text](sample.png)
## **Mejoras de visibilidad en el gráfico**
A veces, para que el gráfico luzca más intuitivo, podemos modificar la apariencia del marcador (cierre), o hacer que se muestre en el eje secundario.

![todo:image_alt_text](sample2.png)
## **Código de muestra**
El siguiente código de ejemplo carga el [archivo de Excel de muestra](High-Low-Close.xlsx) y genera el [archivo de Excel de salida](out.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-high-low-close-stock-chart.cs" >}}
