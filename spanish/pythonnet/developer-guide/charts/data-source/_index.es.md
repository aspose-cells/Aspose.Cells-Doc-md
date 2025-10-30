---
title: Establecer fuente de datos para el gráfico
description: Aprende sobre las diferentes fuentes de datos admitidas por Aspose.Cells para Python via .NET. Nuestra guía te guiará a través de los diferentes tipos de fuentes de datos disponibles y te mostrará cómo conectarte y recuperar datos de ellas para rellenar tus hojas de cálculo.
keywords: Aspose.Cells para Python via .NET, gráficos, formato de datos, etiquetas, colores, fuentes, apariencia, usabilidad.
linktitle: Fuente de datos
type: docs
weight: 10
url: /es/python-net/data-formatting-in-charts/
---

En nuestros temas anteriores, ya hemos proporcionado muchos ejemplos para demostrar cómo puede establecer una fuente de datos para su gráfico, pero en este tema, vamos a proporcionar más detalles sobre los tipos de datos que se pueden establecer para un gráfico.

## **Establecer Datos del Gráfico**

Hay dos tipos de datos con los que trabajar al crear gráficos usando Aspose.Cells para Python via .NET:

- Datos del gráfico.
- Datos de categoría.

### **Datos del Gráfico**

Los datos del gráfico son los datos que usamos como fuente de datos para construir nuestros gráficos. Podemos agregar un rango de celdas (que contienen datos del gráfico) llamando al método [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/add) del objeto [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsData-1.py" >}}

### **Datos de Categoría**

Los datos de categoría se utilizan para la etiquetación de los datos del gráfico y se pueden agregar a [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) mediante su propiedad [**category_data**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/category_data). A continuación se muestra un ejemplo completo para demostrar el uso de datos del gráfico y de categoría. Después de ejecutar el código de ejemplo anterior, se añadirá un gráfico de columnas a la hoja de cálculo como se muestra a continuación.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingCategoryData-1.py" >}}

## **Temas avanzados**
- [Cambiar la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango](/cells/es/python-net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Crear Gráficos Dinámicos](/cells/es/python-net/create-dynamic-charts/)
- [Forma fácil para la configuración de gráficos utilizando el método Chart.SetChartDataRange](/cells/es/python-net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Encontrar el tipo de valores X e Y de los puntos en la serie del gráfico](/cells/es/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/)
{{< app/cells/assistant language="python-net" >}}
