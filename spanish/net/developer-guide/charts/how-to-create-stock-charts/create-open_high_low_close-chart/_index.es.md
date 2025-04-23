---
title: Crear Gráfico de Cotizaciones Apertura Alta Baja Cierre (OHLC)
description: Aprende cómo crear un gráfico de cotizaciones apertura alta baja cierre utilizando Aspose.Cells for .NET. Nuestra guía demostrará cómo graficar datos del mercado de valores, incluyendo los precios de apertura, altos, bajos y de cierre, en un gráfico para un mejor análisis y visualización.
keywords: Aspose.Cells for .NET, Gráfico de Cotizaciones Apertura Alta Baja Cierre, Datos del Mercado de Valores, Análisis, Visualización.
type: docs
weight: 182
url: /es/net/create-open-high-low-close-stock-chart/
---

## **Escenarios de uso posibles**
El gráfico de cotizaciones apertura-alta-baja-cierre (OHLC) utiliza cinco columnas de datos, en orden: categoría, apertura, alta, baja y cierre. El rango de precios en cada categoría nuevamente se indica con una línea vertical, mientras que el rango entre la apertura y el cierre se muestra con una barra flotante más ancha; si el precio aumenta en la categoría (el cierre es mayor que la apertura), la barra se llena de un color, mientras que si el precio disminuye, la barra se llena de otro. Este tipo de gráfico a menudo se llama gráfico de velas.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **Mejoras de visibilidad en el gráfico**
A menudo usamos colores en lugar de blanco y negro para indicar precios crecientes y decrecientes. En el primer conjunto de velas a continuación, el rojo muestra precios crecientes y el verde precios decrecientes.

![todo:image_alt_text](sample2.png)
## **Código de muestra**
El siguiente código de muestra carga el [archivo de Excel de ejemplo](Open-High-Low-Close.xlsx) y genera el [archivo de Excel de salida](out.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-open-high-low-close-stock-chart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
