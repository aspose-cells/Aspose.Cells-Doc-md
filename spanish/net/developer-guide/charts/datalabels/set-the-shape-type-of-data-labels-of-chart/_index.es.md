---
title: Establecer el tipo de forma de las etiquetas de datos del gráfico
description: Aprende cómo establecer el tipo de forma de las etiquetas de datos en gráficos usando Aspose.Cells for .NET. Nuestra guía explicará los diferentes tipos de formas disponibles y te mostrará cómo elegir la forma apropiada para tus etiquetas de datos para mejorar la presentación y usabilidad de tus gráficos.
keywords: Aspose.Cells for .NET, gráficos, etiquetas de datos, tipos de formas, presentación, usabilidad.
type: docs
weight: 110
url: /es/net/set-the-shape-type-of-data-labels-of-chart/
---

## **Escenarios de uso posibles**
Puedes cambiar el tipo de forma de las etiquetas de datos del gráfico usando la propiedad DataLabels.ShapeType. Toma el valor de la enumeración DataLabelShapeType y cambia el tipo de forma de las etiquetas de datos en consecuencia. Algunos de sus valores son

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
## **Establecer el tipo de forma de las etiquetas de datos del gráfico**
El siguiente código de muestra cambia el tipo de forma de las etiquetas de datos del gráfico a DataLabelShapeType.WedgeEllipseCallout. Consulta el [archivo Excel de muestra](60489778.xlsx) utilizado en este código y el [archivo Excel de salida](60489779.xlsx) generado por él. La captura de pantalla muestra el efecto del código en el archivo Excel de muestra. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
