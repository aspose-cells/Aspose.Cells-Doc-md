---
title: Insertar una imagen basada en una referencia de celda
type: docs
weight: 150
url: /es/net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

A veces tienes una imagen vacía y necesitas mostrar datos o contenidos en la imagen configurando una referencia de celda en la Barra de Fórmulas. Aspose.Cells soporta esta característica (Microsoft Excel 2010).

{{% /alert %}}

## Insertar una imagen basada en una referencia de celda

Aspose.Cells soporta mostrar el contenido de una celda de hoja de cálculo en una forma de imagen. Puedes vincular la imagen a la celda que contiene los datos que deseas mostrar. Debido a que la celda o rango de celdas está vinculado al objeto gráfico, los cambios que realices en los datos de esa celda o rango de celdas aparecerán automáticamente en el objeto gráfico. Agrega una imagen a la hoja de cálculo llamando al método [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) de la colección [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) (encapsulada en el objeto [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). Especifica el rango de celdas usando el atributo [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) del objeto [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture).

### Ejemplo de código

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertPictureCellReference-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
