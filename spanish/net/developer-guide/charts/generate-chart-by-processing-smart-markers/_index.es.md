---
title: Generar gráfico mediante el procesamiento de marcadores inteligentes
description: Aprenda cómo generar gráficos con marcadores inteligentes utilizando Aspose.Cells for .NET. Nuestra guía le mostrará cómo procesar marcadores inteligentes y sus propiedades para mejorar la apariencia y usabilidad de sus gráficos.
keywords: Aspose.Cells for .NET, generación de gráficos, marcadores inteligentes, apariencia, usabilidad, procesamiento.
type: docs
weight: 2100
url: /es/net/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}}

Las API de Aspose.Cells proporcionan la clase [**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) para trabajar con Marcadores Inteligentes, donde el formato y las fórmulas se colocan en las hojas de cálculo del diseñador y luego se procesan con la clase [**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) para rellenar los datos según los Marcadores Inteligentes especificados. También es posible crear gráficos de Excel mediante el procesamiento de Marcadores Inteligentes, lo que requerirá los siguientes pasos.

- Creación de hoja de cálculo de diseñador
- Procesamiento de hoja de cálculo del diseñador contra la fuente de datos especificada
- Creación de gráfico basada en datos poblados

{{% /alert %}}

## Creación de hoja de cálculo del diseñador

Una hoja de cálculo del diseñador es un archivo Excel simple creado con la aplicación Microsoft Excel o las API de Aspose.Cells que contiene el formato visual, fórmulas y marcadores inteligentes, cuyo contenido puede ser poblado en tiempo de ejecución.

Por simplicidad, crearemos la hoja de cálculo del diseñador utilizando la API Aspose.Cells for .NET y luego la procesaremos contra una fuente de datos creada dinámicamente con fines de demostración.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## Procesamiento de hoja de cálculo del diseñador

Para procesar la hoja de cálculo del diseñador, se debe contar con una fuente de datos que corresponda a los marcadores inteligentes utilizados en la hoja de cálculo del diseñador. Por ejemplo, hemos creado una entrada de marcador inteligente como &=Ventas.Año, que representa la columna de Año en la tabla de datos Ventas. En caso de que no esté disponible una columna correspondiente en la fuente de datos, las API de Aspose.Cells omitirán el procesamiento para ese marcador inteligente en particular y, como resultado, los datos para ese marcador inteligente en particular no se poblarán.

Para demostrar este caso de uso, crearemos la fuente de datos desde cero y la procesaremos contra la hoja de cálculo del diseñador creada en el paso anterior. Sin embargo, en un escenario en tiempo real, los datos podrían estar disponibles para su procesamiento posterior, por lo que puedes omitir la creación de la fuente de datos si los datos ya están disponibles.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

El procesamiento de marcadores inteligentes es bastante sencillo, como se muestra en el siguiente fragmento de código.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

El fragmento de código anterior utiliza la instancia existente de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) creada en el primer paso. Si ya tienes el archivo de hoja de cálculo del diseñador en el disco o en la memoria, puedes crear una instancia de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) cargando la hoja de cálculo del diseñador existente.

{{% /alert %}}

## Creación de gráfico

Una vez que los datos estén en su lugar, todo lo que necesitamos hacer es crear un gráfico basado en la fuente de datos. Para mantener el ejemplo simple, usaremos el método [**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange) para que no tengamos que configurar el gráfico más adelante.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
