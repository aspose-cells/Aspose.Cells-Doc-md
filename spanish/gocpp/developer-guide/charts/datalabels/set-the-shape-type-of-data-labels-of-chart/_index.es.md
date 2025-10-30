---
title: Establecer el tipo de forma de las etiquetas de datos del gráfico con Golang a través de C++
linktitle: Establecer el tipo de forma de las etiquetas de datos del gráfico
description: Aprenda cómo establecer el tipo de forma de las etiquetas de datos en los gráficos usando Aspose.Cells for C++. Nuestra guía explicará los diferentes tipos de formas disponibles y le mostrará cómo elegir la forma adecuada para sus etiquetas de datos para mejorar la presentación y usabilidad de sus gráficos.
keywords: Aspose.Cells for C++, gráficos, etiquetas de datos, tipos de forma, presentación, usabilidad.
type: docs
weight: 110
url: /es/go-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Escenarios de uso posibles**
Puede cambiar el tipo de forma de las etiquetas de datos del gráfico usando la propiedad `DataLabels.ShapeType`. Toma el valor de la enumeración `DataLabelShapeType` y cambia el tipo de forma de las etiquetas de datos en consecuencia. Algunos de sus valores son:

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}

## **Establecer el tipo de forma de las etiquetas de datos del gráfico**
El siguiente ejemplo cambia el tipo de forma de las etiquetas de datos del gráfico a `DataLabelShapeType.WedgeEllipseCallout`. Por favor, revisa el archivo de Excel de ejemplo ([60489778.xlsx](60489778.xlsx)) usado en este código y el archivo de Excel de salida ([60489779.xlsx](60489779.xlsx)) generado por él. La captura de pantalla muestra el efecto del código en el archivo de ejemplo. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **Código de muestra**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetTheShapeTypeOfDataLabelsOfChart.go" >}}
