---
title: Establecer origen de datos para el gráfico con Golang mediante C++
linktitle: Origen de datos
type: docs
weight: 10
url: /es/go-cpp/data-formatting-in-charts/
description: Conoce las diversas fuentes de datos soportadas por Aspose.Cells for C++. Nuestra guía te enseñará los diferentes tipos de fuentes de datos disponibles y cómo conectarte y recuperar datos de ellas para llenar tus hojas de cálculo.
keywords: Aspose.Cells for C++, creación de gráficos, formato de datos, etiquetas, colores, fuentes, apariencia, usabilidad.
---

En nuestros temas anteriores, ya hemos proporcionado muchos ejemplos para demostrar cómo puedes establecer una fuente de datos para tu gráfico. En este tema, proporcionaremos más detalles sobre los tipos de datos que se pueden establecer para un gráfico.

## **Establecer Datos del Gráfico**

Hay dos tipos de datos con los que trabajar al utilizar gráficos con Aspose.Cells como se muestra a continuación:

- Datos del gráfico.
- Datos de categoría.

### **Datos del Gráfico**

Los datos del gráfico son los datos que usamos como fuente de datos para construir nuestros gráficos. Podemos agregar un rango de celdas (que contienen datos del gráfico) llamando al método [**Add**](https://reference.aspose.com/cells/go-cpp/seriescollection/add/) del objeto [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource.go" >}}
### **Datos de Categoría**

Los datos de categoría se utilizan para la etiquetación de los datos del gráfico y se pueden agregar a [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/) mediante su propiedad [**GetCategoryData()**](https://reference.aspose.com/cells/go-cpp/seriescollection/getcategorydata/). A continuación se muestra un ejemplo completo para demostrar el uso de datos del gráfico y de categoría. Después de ejecutar el código de ejemplo anterior, se añadirá un gráfico de columnas a la hoja de cálculo como se muestra a continuación.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource-1.go" >}}
## **Temas Avanzados**
- [Cambiar la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango](/cells/es/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Crear Gráficos Dinámicos](/cells/es/cpp/create-dynamic-charts/)
- [Forma fácil para la configuración de gráficos utilizando el método Chart.SetChartDataRange](/cells/es/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Encontrar el tipo de valores X e Y de los puntos en la serie del gráfico](/cells/es/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
