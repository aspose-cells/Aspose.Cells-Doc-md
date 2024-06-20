---
title: Formateo de datos en gráficos
linktitle: Origen de datos
type: docs
weight: 50
url: /es/java/data-formatting-in-charts/
---

{{% alert color="primary" %}}

En nuestros temas anteriores, ya hemos proporcionado muchos ejemplos para demostrar cómo puede establecer una fuente de datos para su gráfico, pero en este tema, vamos a proporcionar más detalles sobre los tipos de datos que se pueden establecer para un gráfico.

{{% /alert %}}

## **Establecer Datos del Gráfico**

Hay dos tipos de datos con los que trabajar al utilizar gráficos con Aspose.Cells como se muestra a continuación:

- [Datos del gráfico](/cells/es/java/data-formatting-in-charts/#chart-data).
- [Datos de categoría](/cells/es/java/data-formatting-in-charts/#category-data).

### **Datos del Gráfico**

Los datos del gráfico son aquellos datos que utilizamos como origen de datos para construir nuestros gráficos. Podemos agregar un rango de celdas (que contienen datos del gráfico) llamando al método [**Add**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#add(java.lang.Object)) del objeto [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **Datos de Categoría**

Los datos de categoría se utilizan para etiquetar los datos del gráfico y se pueden agregar a [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) mediante su método [**setCategoryData**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#CategoryData).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**Gráfico de columnas con datos de gráfico y categoría** 

![todo:image_alt_text](data-formatting-in-charts_1.png)

## **Temas avanzados**
- [Crear Gráficos Dinámicos](/cells/es/java/create-dynamic-charts/)
- [Forma sencilla de configurar el gráfico usando el método Chart.setChartDataRange](/cells/es/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Encontrar el tipo de valores X e Y de los puntos en la serie del gráfico](/cells/es/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [Establecer el código de formato de valores de la serie del gráfico](/cells/es/java/set-the-values-format-code-of-chart-series/)
