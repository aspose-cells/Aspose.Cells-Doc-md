---
title: Insertar una Imagen Basada en la Referencia de la Celda con Golang a través de C++
linktitle: Insertar una imagen basada en una referencia de celda
type: docs
weight: 150
url: /es/go-cpp/insert-a-picture-based-on-cell-reference/
description: Aprenda cómo insertar una imagen basada en la referencia de celda usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A veces tienes una imagen vacía y necesitas mostrar datos o contenidos en la imagen configurando una referencia de celda en la Barra de Fórmulas. Aspose.Cells soporta esta característica (Microsoft Excel 2010).

{{% /alert %}}

## Insertar una imagen basada en una referencia de celda

Aspose.Cells soporta mostrar el contenido de una celda de hoja de cálculo en una forma de imagen. Puedes vincular la imagen a la celda que contiene los datos que deseas mostrar. Debido a que la celda o rango de celdas está vinculado al objeto gráfico, los cambios que realices en los datos de esa celda o rango de celdas aparecerán automáticamente en el objeto gráfico. Agrega una imagen a la hoja de cálculo llamando al método [**AddPicture**](https://reference.aspose.com/cells/go-cpp/shapecollection/addpicture_int_int_int_int_stream/) de la colección [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) (encapsulada en el objeto [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). Especifica el rango de celdas usando el atributo [**Formula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) del objeto [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

### Ejemplo de código

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertAPictureBasedOnCellReference.go" >}}
