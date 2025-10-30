---
title: Crear un gráfico de acciones de tipo Open High Low Close (OHLC) con Golang a través de C++
description: Aprenda a crear un gráfico de acciones open high low close usando Aspose.Cells for C++. Nuestra guía demostrará cómo trazar datos del mercado de valores, incluyendo los precios de apertura, altos, bajos y de cierre, en un gráfico para un mejor análisis y visualización.
keywords: Aspose.Cells for C++, Gráfico de Acciones Open High Low Close, Datos del Mercado de Valores, Análisis, Visualización.
type: docs
weight: 182
url: /es/go-cpp/create-open-high-low-close-stock-chart/
---

## **Escenarios de uso posibles**
El gráfico de cotizaciones apertura-alta-baja-cierre (OHLC) utiliza cinco columnas de datos, en orden: categoría, apertura, alta, baja y cierre. El rango de precios en cada categoría nuevamente se indica con una línea vertical, mientras que el rango entre la apertura y el cierre se muestra con una barra flotante más ancha; si el precio aumenta en la categoría (el cierre es mayor que la apertura), la barra se llena de un color, mientras que si el precio disminuye, la barra se llena de otro. Este tipo de gráfico a menudo se llama gráfico de velas.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)

## **Mejoras de visibilidad en el gráfico**
A menudo usamos colores en lugar de blanco y negro para indicar precios en aumento y en disminución. En el primer conjunto de velas abajo, el rojo muestra precios en aumento y el verde en disminución.

![todo:image_alt_text](sample2.png)

## **Código de muestra**
El siguiente código de muestra carga el [archivo de Excel de ejemplo](Open-High-Low-Close.xlsx) y genera el [archivo de Excel de salida](out.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreateOpenHighLowCloseChart.go" >}}
