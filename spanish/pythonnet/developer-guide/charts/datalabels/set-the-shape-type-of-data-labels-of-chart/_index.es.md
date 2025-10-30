---
title: Establecer el tipo de forma de las etiquetas de datos del gráfico
description: Aprenda cómo establecer el tipo de forma de las etiquetas de datos en los gráficos usando Aspose.Cells para Python via .NET. Nuestra guía explicará los diferentes tipos de formas disponibles y le mostrará cómo elegir la forma adecuada para sus etiquetas de datos para mejorar la presentación y usabilidad de sus gráficos.
keywords: Aspose.Cells para Python via .NET, graficación, etiquetas de datos, tipos de formas, presentación, usabilidad.
type: docs
weight: 110
url: /es/python-net/set-the-shape-type-of-data-labels-of-chart/
---

## **Escenarios de uso posibles**
Puedes cambiar el tipo de forma de las etiquetas de datos del gráfico usando la propiedad DataLabels.ShapeType. Toma el valor de la enumeración DataLabelShapeType y cambia el tipo de forma de las etiquetas de datos en consecuencia. Algunos de sus valores son

{{< highlight java >}}

DataLabelShapeType.BENT_LINE_CALLOUT

DataLabelShapeType.DOWN_ARROW_CALLOUT

DataLabelShapeType.ELLIPSE

DataLabelShapeType.LINE_CALLOUT

DataLabelShapeType.RECT

etc.

{{< /highlight >}}

## **Establecer el tipo de forma de las etiquetas de datos del gráfico**
El siguiente código de muestra cambia el tipo de forma de las etiquetas de datos del gráfico a DataLabelShapeType.WedgeEllipseCallout. Consulta el [archivo Excel de muestra](60489778.xlsx) utilizado en este código y el [archivo Excel de salida](60489779.xlsx) generado por él. La captura de pantalla muestra el efecto del código en el archivo Excel de muestra. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **Código de muestra**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SetShapeTypeOfDataLabelsOfChart.py" >}}
{{< app/cells/assistant language="python-net" >}}
