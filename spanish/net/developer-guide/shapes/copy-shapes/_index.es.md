---
title: Copiar Formas entre Hojas de Cálculo
linktitle: Copiar formas
type: docs
weight: 200
url: /es/net/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

A veces, necesitas copiar elementos en una hoja de cálculo, por ejemplo, imágenes, gráficos y otros objetos de dibujo, entre hojas de cálculo. Aspose.Cells admite esta función. Los gráficos, imágenes y otros objetos se pueden copiar con el más alto grado de precisión.

Este artículo te brinda una comprensión detallada de cómo copiar formas entre hojas de cálculo.

{{% /alert %}}

## **Copiar una Imagen de una Hoja de Cálculo a Otra**

Para copiar una imagen de una hoja de cálculo a otra, utiliza el método [**Worksheet.Pictures.Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) como se muestra en el código de ejemplo a continuación.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.cs" >}}

## **Copiar un gráfico de una hoja de cálculo a otra**

El siguiente código demuestra el uso del método [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy) para copiar un gráfico de una hoja de cálculo a otra.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.cs" >}}

## **Copiar controles y otros objetos de dibujo de una hoja de cálculo a otra**

Para copiar controles y otros objetos de dibujo, utiliza el método [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy) como se muestra en el ejemplo a continuación.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.cs" >}}
{{< app/cells/assistant language="csharp" >}}
