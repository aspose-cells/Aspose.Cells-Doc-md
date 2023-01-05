---
title: Establecer el tipo de forma de las etiquetas de datos del gráfico
type: docs
weight: 110
url: /es/net/set-the-shape-type-of-data-labels-of-chart/
---
## **Posibles escenarios de uso**
Puede cambiar el tipo de forma de las etiquetas de datos del gráfico mediante la propiedad DataLabels.ShapeType. Toma el valor de la enumeración DataLabelShapeType y cambia el tipo de forma de las etiquetas de datos en consecuencia. Algunos de sus valores son

{{< highlight "java" >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
## **Establecer el tipo de forma de las etiquetas de datos del gráfico**
 El siguiente código de ejemplo cambia el tipo de forma de las etiquetas de datos del gráfico a DataLabelShapeType.WedgeEllipseCallout. Por favor vea el[ejemplo de archivo de Excel](60489778.xlsx) utilizado en este código y el[archivo de salida de Excel](60489779.xlsx) generada por ella. La captura de pantalla muestra el efecto del código en un archivo de muestra de Excel.

![todo:imagen_alternativa_texto](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
