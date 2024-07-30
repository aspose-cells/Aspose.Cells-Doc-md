---
title: Copiar Formas entre Hojas de Cálculo
linktitle: Copiar formas
type: docs
weight: 200
url: /es/python-net/copy-shapes-between-worksheets/
description: Este artículo muestra cómo copiar formas entre hojas de cálculo a través de la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Copiar formas entre hojas de cálculo en Python, cómo copiar una imagen de una hoja de cálculo a otra, cómo copiar un gráfico de una hoja de cálculo a otra, cómo copiar controles y otros objetos de dibujo de una hoja de cálculo a otra en Python.
---

{{% alert color="primary" %}}

A veces, necesitas copiar elementos en una hoja de cálculo, como imágenes, gráficos y otros objetos de dibujo, entre hojas de cálculo. Aspose.Cells para Python via .NET admite esta función. Las gráficas, imágenes y otros objetos se pueden copiar con el más alto grado de precisión.

Este artículo te brinda una comprensión detallada de cómo copiar formas entre hojas de cálculo.

{{% /alert %}}

## **Copiar una Imagen de una Hoja de Cálculo a Otra**

Para copiar una imagen de una hoja de cálculo a otra, utiliza el método [**Worksheet.pictures.add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add/#int-int-io.RawIOBase-int-int) como se muestra en el código de ejemplo a continuación.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.py" >}}

## **Copiar un gráfico de una hoja de cálculo a otra**

El siguiente código demuestra el uso del método [**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int) para copiar un gráfico de una hoja de cálculo a otra.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.py" >}}

## **Copiar controles y otros objetos de dibujo de una hoja de cálculo a otra**

Para copiar controles y otros objetos de dibujo, utiliza el método [**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int) como se muestra en el ejemplo a continuación.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.py" >}}
