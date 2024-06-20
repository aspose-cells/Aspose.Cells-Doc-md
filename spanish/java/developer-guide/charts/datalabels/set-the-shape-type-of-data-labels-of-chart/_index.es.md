---
title: Establecer el tipo de forma de las etiquetas de datos del gráfico
type: docs
weight: 70
url: /es/java/set-the-shape-type-of-data-labels-of-chart/
---

## **Escenarios de uso posibles**

Puede cambiar el tipo de forma de las etiquetas de datos del gráfico utilizando la propiedad [**DataLabels.ShapeType**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShapeType). Toma el valor de la enumeración [**DataLabelShapeType**](https://reference.aspose.com/cells/java/com.aspose.cells/DataLabelShapeType) y cambia el tipo de forma de las etiquetas de datos en consecuencia. Algunos de sus valores son

{{< highlight java >}}

DataLabelShapeType.BENT_LINE_CALLOUT

DataLabelShapeType.DOWN_ARROW_CALLOUT

DataLabelShapeType.ELLIPSE

DataLabelShapeType.LINE_CALLOUT

DataLabelShapeType.RECT

etc.

{{< /highlight >}}

## **Establecer el tipo de forma de las etiquetas de datos del gráfico**

El siguiente código de ejemplo cambia el tipo de forma de las etiquetas de datos del gráfico a [**DataLabelShapeType.WEDGE_ELLIPSE_CALLOUT**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabelshapetype#WEDGE_ELLIPSE_CALLOUT). Consulte el [archivo de Excel de ejemplo](60489794.xlsx) utilizado en este código y el [archivo de Excel de salida](60489793.xlsx) generado por él. La captura de pantalla muestra el efecto del código en el archivo de Excel de ejemplo.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-SetShapeTypeOfDataLabelsOfChart.java" >}}
