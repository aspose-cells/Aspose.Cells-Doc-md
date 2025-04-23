---
title: Establecer fuente de datos para el gráfico
description: Aprenda sobre las diferentes fuentes de datos admitidas por Aspose.Cells for .NET. Nuestra guía le mostrará los diferentes tipos de fuentes de datos disponibles y le enseñará cómo conectar y recuperar datos de ellas para rellenar sus hojas de cálculo.
keywords: Aspose.Cells for .NET, gráficos, formato de datos, etiquetas, colores, fuentes, apariencia, usabilidad.
linktitle: Fuente de datos
type: docs
weight: 10
url: /es/net/data-formatting-in-charts/
---

En nuestros temas anteriores, ya hemos proporcionado muchos ejemplos para demostrar cómo puede establecer una fuente de datos para su gráfico, pero en este tema, vamos a proporcionar más detalles sobre los tipos de datos que se pueden establecer para un gráfico.

## **Establecer Datos del Gráfico**

Hay dos tipos de datos con los que trabajar al utilizar gráficos con Aspose.Cells como se muestra a continuación:

- Datos del gráfico.
- Datos de categoría.

### **Datos del Gráfico**

Los datos del gráfico son los datos que usamos como fuente de datos para construir nuestros gráficos. Podemos agregar un rango de celdas (que contienen datos del gráfico) llamando al método [**Add**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add) del objeto [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **Datos de Categoría**

Los datos de categoría se utilizan para la etiquetación de los datos del gráfico y se pueden agregar a [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) mediante su propiedad [**CategoryData**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata). A continuación se muestra un ejemplo completo para demostrar el uso de datos del gráfico y de categoría. Después de ejecutar el código de ejemplo anterior, se añadirá un gráfico de columnas a la hoja de cálculo como se muestra a continuación.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **Temas avanzados**
- [Cambiar la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango](/cells/es/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Crear Gráficos Dinámicos](/cells/es/net/create-dynamic-charts/)
- [Forma fácil para la configuración de gráficos utilizando el método Chart.SetChartDataRange](/cells/es/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Encontrar el tipo de valores X e Y de los puntos en la serie del gráfico](/cells/es/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
{{< app/cells/assistant language="csharp" >}}
