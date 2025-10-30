---
title: Insertar una imagen basada en una referencia de celda
type: docs
weight: 150
url: /es/python-net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

A veces, tienes una imagen vacía y necesitas mostrar datos o contenidos en la imagen configurando una referencia de celda en la barra de fórmulas. Aspose.Cells para Python via .NET soporta esta función (Microsoft Excel 2010).

{{% /alert %}}

## Insertar una imagen basada en una referencia de celda

Aspose.Cells para Python via .NET soporta mostrar el contenido de una celda de hoja en una forma de imagen. Puedes vincular la imagen a la celda que contiene los datos que deseas mostrar. Dado que la celda o el rango de celdas está vinculado al objeto gráfico, los cambios que hagas en los datos en esa celda o rango aparecerán automáticamente en el objeto gráfico. Agrega una imagen a la hoja de cálculo llamando al método [**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture) de la colección [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) (envuelto en el objeto [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). Especifica el rango de celdas usando el atributo [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula) del objeto [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture).

### Ejemplo de código

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertPictureCellReference-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
