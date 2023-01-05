---
title: Establecer fuente de datos para el gráfico
linktitle: Fuente de datos
type: docs
weight: 10
url: /es/net/data-formatting-in-charts/
---
En nuestros temas anteriores, ya proporcionamos muchos ejemplos para demostrar cómo puede configurar una fuente de datos para su gráfico, pero en este tema, proporcionaremos más detalles sobre los tipos de datos que se pueden configurar para un gráfico.

## **Configuración de los datos del gráfico**

Hay dos tipos de datos con los que lidiar al trabajar en gráficos usando Aspose.Cells de la siguiente manera:

- Datos del gráfico.
- Datos de la categoría.

### **Datos del gráfico**

Los datos de gráficos son los datos que utilizamos como fuente de datos para crear nuestros gráficos. Podemos agregar un rango de celdas (que contienen datos del gráfico) llamando al[**SerieColección**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) objetos[**Agregar**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add)método.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **Datos de categoría**

 Los datos de categoría se utilizan para el etiquetado de los datos del gráfico y se pueden agregar a[**SerieColección**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) usando su[**CategoríaDatos**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)propiedad. A continuación se proporciona un ejemplo completo para demostrar el uso de datos de gráficos y categorías. Después de ejecutar el código de ejemplo anterior, se agregará un gráfico de columnas a la hoja de trabajo como se muestra a continuación.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **Temas avanzados**
- [Cambie la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango](/cells/es/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Crear gráficos dinámicos](/cells/es/net/create-dynamic-charts/)
- [Manera fácil de configurar el gráfico usando el método Chart.SetChartDataRange](/cells/es/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Buscar tipo de valores X e Y de puntos en series de gráficos](/cells/es/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
