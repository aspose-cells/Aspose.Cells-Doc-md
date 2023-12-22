---
title: Crear gráfico de acciones de volumen-alto-bajo-cierre (VHLC)
type: docs
weight: 183
url: /es/java/create-volume-high-low-close-stock-chart/
description: Cómo crear un gráfico de acciones de volumen-alto-bajo-cierre (VHLC), cómo agregar un gráfico de acciones de volumen-alto-bajo-cierre (VHLC), cómo generar un gráfico de acciones de volumen-alto-bajo-cierre (VHLC) .
keywords: Add Volume-High-Low-Close(VHLC) Stock Chart, Create Volume-High-Low-Close(VHLC) Stock Chart, Generate Volume-High-Low-Close(VHLC) Stock Chart.
---
##  **Posibles escenarios de uso**
El tercer gráfico de acciones que veremos es el gráfico de cierre de volumen máximo y mínimo. Nuevamente es importante repetir que debes tener los datos en el orden correcto. Si necesita reorganizar su tabla de datos, debe hacerlo antes de configurar su gráfico.
Este gráfico incluye una columna para el volumen inmediatamente después de la primera columna (categoría), y los gráficos incluyen un gráfico de columnas en el eje principal que muestra este volumen, mientras que los precios se mueven al eje secundario.

![todo:image_alt_text](data.png)
##  **Gráfico de acciones de Volumen-Alto-Bajo-Cierre (VHLC)**

![todo:image_alt_text](sample.png)
##  **Código de muestra**
 El siguiente código de muestra carga el[archivo de Excel de muestra](Volume-High-Low-Close.xlsx) y genera el[archivo de salida de Excel](out.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-create-volume-high-low-close-stock-chart.java" >}}
