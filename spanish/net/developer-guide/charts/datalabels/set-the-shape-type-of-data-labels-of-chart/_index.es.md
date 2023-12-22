---
title: Establecer el tipo de forma de las etiquetas de datos del gráfico
description: Aprenda a configurar el tipo de forma de las etiquetas de datos en los gráficos usando Aspose.Cells for .NET. Nuestra guía explicará los diferentes tipos de formas disponibles y le mostrará cómo elegir la forma adecuada para sus etiquetas de datos para mejorar la presentación y usabilidad de sus gráficos.
keywords: Aspose.Cells for .NET, charting, data labels, shape types, presentation, usability.
type: docs
weight: 110
url: /es/net/set-the-shape-type-of-data-labels-of-chart/
---
##  **Posibles escenarios de uso**
Puede cambiar el tipo de forma de las etiquetas de datos del gráfico utilizando la propiedad DataLabels.ShapeType. Toma el valor de la enumeración DataLabelShapeType y cambia el tipo de forma de las etiquetas de datos en consecuencia. Algunos de sus valores son

{{< highlight "java" >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
##  **Establecer el tipo de forma de las etiquetas de datos del gráfico**
 El siguiente código de ejemplo cambia el tipo de forma de las etiquetas de datos del gráfico a DataLabelShapeType.WedgeEllipseCallout. Por favor vea el[archivo de Excel de muestra](60489778.xlsx) utilizado en este código y el[archivo de salida de Excel](60489779.xlsx)generado por ello. La captura de pantalla muestra el efecto del código en un archivo de Excel de muestra.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
##  **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
