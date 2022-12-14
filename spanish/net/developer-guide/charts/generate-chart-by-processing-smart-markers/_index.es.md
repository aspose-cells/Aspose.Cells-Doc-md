---
title: Generar gráfico procesando marcadores inteligentes
type: docs
weight: 2100
url: /es/net/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}}

 Aspose.Cells Las API proporcionan la[**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)clase para trabajar con Smart Markers donde el formato y las fórmulas se colocan en las hojas de cálculo del diseñador y luego se procesan con[**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)clase para completar los datos de acuerdo con los marcadores inteligentes especificados. También es posible crear gráficos de Excel mediante el procesamiento de marcadores inteligentes, lo que requerirá los siguientes pasos.

- Creación de hoja de cálculo de diseñador.
- Hoja de cálculo del diseñador de procesamiento contra la fuente de datos especificada
- Creación de gráfico basado en datos poblados

{{% /alert %}}

## Creación de la hoja de cálculo del diseñador

Una hoja de cálculo de diseñador es un archivo de Excel simple creado con la aplicación de Excel Microsoft o las API Aspose.Cells que contiene el formato visual, las fórmulas y los marcadores inteligentes, donde los contenidos se pueden completar en tiempo de ejecución.

En aras de la simplicidad, crearemos la hoja de cálculo del diseñador utilizando Aspose.Cells for .NET API y luego la procesaremos contra una fuente de datos creada dinámicamente con fines de demostración.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## Hoja de cálculo del diseñador de procesamiento

Para procesar la hoja de cálculo del diseñador, se debe tener una fuente de datos que corresponda a los marcadores inteligentes utilizados en la hoja de cálculo del diseñador. Por ejemplo, hemos creado una entrada de marcador inteligente como &=Sales.Year, que representa la columna Year en DataTable Sales. En caso de que una columna correspondiente no esté disponible en la fuente de datos, las API Aspose.Cells omitirán el procesamiento para ese marcador inteligente en particular y, como resultado, los datos para ese marcador inteligente en particular no se completarán.

Para demostrar este caso de uso, crearemos la fuente de datos desde cero y la procesaremos contra la hoja de cálculo del diseñador creada en el paso anterior. Sin embargo, en un escenario en tiempo real, los datos ya podrían estar disponibles para su posterior procesamiento, por lo que puede omitir la creación de la fuente de datos si los datos ya están disponibles.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

El procesamiento de Smart Markers es bastante simple, como lo demuestra el siguiente fragmento de código.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

 El fragmento de código anterior utiliza la instancia existente de la[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)clase creada en el primer paso. Si ya tiene el archivo de hoja de cálculo del diseñador en el disco o en la memoria, puede crear una instancia de[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)clase cargando la hoja de cálculo del diseñador existente.

{{% /alert %}}

## Creación de gráfico

 Una vez que los datos están en su lugar, todo lo que tenemos que hacer es crear un gráfico basado en la fuente de datos. Para simplificar el ejemplo, utilizaremos el[**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)para que no tengamos que configurar más el gráfico.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
