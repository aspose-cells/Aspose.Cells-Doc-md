---
title: Insertar una imagen basada en la referencia Cell
type: docs
weight: 150
url: /es/net/insert-a-picture-based-on-cell-reference/
---
{{% alert color="primary" %}}

A veces tiene una imagen vacía y necesita mostrar datos o contenidos en la imagen estableciendo una referencia de celda en la barra de fórmulas. Aspose.Cells admite esta función (Microsoft Excel 2010).

{{% /alert %}}

## Insertar una imagen basada en la referencia Cell

Aspose.Cells admite la visualización del contenido de una celda de la hoja de trabajo en forma de imagen. Puede vincular la imagen a la celda que contiene los datos que desea mostrar. Dado que la celda o el rango de celdas está vinculado al objeto gráfico, los cambios que realice en los datos de esa celda o rango de celdas aparecerán automáticamente en el objeto gráfico. Agregue una imagen a la hoja de trabajo llamando al[**Añade una foto**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) metodo de la[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) colección (encapsulada en el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) objeto). Especifique el rango de celdas usando el[**Fórmula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) atributo de la[**Imagen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)objeto.

### Ejemplo de código

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertPictureCellReference-1.cs" >}}
