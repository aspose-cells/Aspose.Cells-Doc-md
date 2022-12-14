---
title: Formato de datos en gráficos
linktitle: Fuente de datos
type: docs
weight: 50
url: /es/java/data-formatting-in-charts/
---
{{% alert color="primary" %}}

En nuestros temas anteriores, ya proporcionamos muchos ejemplos para demostrar cómo puede configurar una fuente de datos para su gráfico, pero en este tema, proporcionaremos más detalles sobre los tipos de datos que se pueden configurar para un gráfico.

{{% /alert %}}

## **Configuración de los datos del gráfico**

Hay dos tipos de datos con los que lidiar al trabajar en gráficos usando Aspose.Cells de la siguiente manera:

- [Datos del gráfico](/cells/es/java/data-formatting-in-charts/#chart-data).
- [Datos de categoría](/cells/es/java/data-formatting-in-charts/#category-data).

### **Datos del gráfico**

 Los datos de gráficos son los datos que usamos como fuente de datos para construir nuestros gráficos. Podemos agregar un rango de celdas (que contienen datos del gráfico) llamando al[**SerieColección**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) objetos[**Agregar**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#add(java.lang.Object)) método.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **Datos de categoría**

 Los datos de categoría se utilizan para el etiquetado de los datos del gráfico y se pueden agregar a[**SerieColección**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) usando su[**setCategoryData**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#CategoryData)método.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**Gráfico de columnas con datos de gráfico y categoría** 

![todo:imagen_alternativa_texto](data-formatting-in-charts_1.png)

## **Temas avanzados**
- [Crear gráficos dinámicos](/cells/es/java/create-dynamic-charts/)
- [Manera fácil de configurar el gráfico usando el método Chart.setChartDataRange](/cells/es/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Buscar tipo de valores X e Y de puntos en series de gráficos](/cells/es/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [Establecer el código de formato de valores de la serie de gráficos](/cells/es/java/set-the-values-format-code-of-chart-series/)
