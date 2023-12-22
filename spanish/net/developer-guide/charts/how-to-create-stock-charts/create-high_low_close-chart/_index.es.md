---
title: Crear gráfico de acciones de cierre alto-bajo (HLC)
description: Aprenda a crear un gráfico de acciones de cierre alto-bajo usando Aspose.Cells for .NET. Nuestra guía paso a paso demostrará cómo trazar datos del mercado de valores, incluidos los precios máximo, mínimo y de cierre, en un gráfico para un mejor análisis y visualización. .
keywords: Aspose.Cells for .NET, High-Low-Close Stock Chart, Stock Market Data, Analysis, Visualization.
type: docs
weight: 181
url: /es/net/create-high-low-close-stock-chart/
---
##  **Posibles escenarios de uso**
El gráfico de acciones High-Low-Close (HLC) utiliza cuatro columnas de datos. La primera columna es una categoría, normalmente una fecha, pero también se pueden utilizar nombres de acciones. Las siguientes tres columnas en orden son para precios máximos, mínimos y de cierre. El rango de precio para cada categoría se indica mediante una línea vertical de menor a mayor, y el precio de cierre se muestra mediante una marca de verificación que se extiende a la derecha de esta línea.

![todo:image_alt_text](sample.png)
##  **Mejoras de visibilidad en el gráfico.**
veces, para que el gráfico parezca más intuitivo, podemos modificar la apariencia del marcador (cerrar) o hacer que se muestre en el eje secundario.

![todo:image_alt_text](sample2.png)
##  **Código de muestra**
 El siguiente código de muestra carga el[archivo de Excel de muestra](High-Low-Close.xlsx) y genera el[archivo de salida de Excel](out.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-high-low-close-stock-chart.cs" >}}
