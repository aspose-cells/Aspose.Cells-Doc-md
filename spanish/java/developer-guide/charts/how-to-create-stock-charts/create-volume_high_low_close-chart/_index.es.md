---
title: Crear Gráfico de la bolsa de valores con Volumen Alto Bajo Cierre (VHLC)
type: docs
weight: 183
url: /es/java/create-volume-high-low-close-stock-chart/
description: Cómo crear un Gráfico de la bolsa de valores con Volumen Alto Bajo Cierre (VHLC), cómo agregar un Gráfico de la bolsa de valores con Volumen Alto Bajo Cierre (VHLC), cómo generar un Gráfico de la bolsa de valores con Volumen Alto Bajo Cierre (VHLC).
keywords: Añadir Gráfico de la bolsa de valores con Volumen Alto Bajo Cierre (VHLC), Crear Gráfico de la bolsa de valores con Volumen Alto Bajo Cierre (VHLC), Generar Gráfico de la bolsa de valores con Volumen Alto Bajo Cierre (VHLC).
---

## **Escenarios de uso posibles**
El tercer gráfico de la bolsa de valores que veremos es el gráfico de Volumen Alto Bajo Cierre. Nuevamente es importante repetir que debe tener los datos en el orden correcto. Si necesita reorganizar su tabla de datos, debe hacerlo antes de configurar su gráfico.
Este gráfico incluye una columna para el volumen inmediatamente después de la primera columna (categoría), y los gráficos incluyen un gráfico de columnas en el eje primario mostrando este volumen, mientras que los precios se mueven al eje secundario.

![todo:image_alt_text](data.png)
## **Gráfico de bolsa de valores Volumen-Alto-Bajo-Cierre (VHLC)**

![todo:image_alt_text](sample.png)
## **Código de muestra**
El siguiente código de muestra carga el [archivo Excel de muestra](Volume-High-Low-Close.xlsx) y genera el [archivo Excel de salida](out.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-create-volume-high-low-close-stock-chart.java" >}}
