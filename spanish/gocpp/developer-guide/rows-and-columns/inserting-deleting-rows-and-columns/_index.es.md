---
title: Insertar, eliminar filas y columnas
type: docs
weight: 40
url: /es/go-cpp/inserting-deleting-rows-and-columns/
---

## **Introducción**

Ya sea creando una nueva hoja de cálculo desde cero o trabajando en una hoja de cálculo existente, es posible que necesitemos agregar filas o columnas adicionales para acomodar más datos. Inversamente, es posible que también necesitemos eliminar filas o columnas de posiciones específicas en la hoja de cálculo. Para cumplir con estos requisitos, Aspose.Cells proporciona un conjunto muy simple de clases y métodos, que se discuten a continuación.

### **Gestión de filas y columnas**

Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una colección [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) que permite acceder a cada hoja de cálculo en un archivo Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) proporciona una colección [Cells](https://reference.aspose.com/cells/go-cpp/cells/) que representa todas las celdas en la hoja de cálculo.

La colección [Cells](https://reference.aspose.com/cells/go-cpp/cells/) proporciona varios métodos para gestionar filas y columnas en una hoja de cálculo. Algunos de estos se discuten a continuación.

{{% alert color="primary" %}}

Cuando se agregan filas o columnas, el contenido en la hoja de cálculo se desplaza hacia abajo o hacia la derecha, y si se eliminan filas o columnas, el contenido se desplaza hacia arriba o hacia la izquierda.

{{% /alert %}}

Inserta una fila en la hoja de cálculo en cualquier ubicación llamando al método [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) de la colección [Cells](https://reference.aspose.com/cells/go-cpp/cells/). El método [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) toma el índice de la fila donde se insertará la nueva fila.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertRow.go" >}}

#### **Insertar Múltiples Filas**

Para insertar varias filas en una hoja de cálculo, llame al método [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrows_int_int/) de la colección [Cells](https://reference.aspose.com/cells/go-cpp/cells/). El método [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrowinsertrows_int_ints/) toma dos parámetros:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertingMultipleRows.go" >}}

#### **Eliminar Múltiples Filas**

Para eliminar varias filas de una hoja de cálculo, llame al método [DeleteRows](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/) de la colección [Cells](https://reference.aspose.com/cells/go-cpp/cells/). El método [DeleteRows](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/) toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se eliminarán las filas.
- Número de filas, el número total de filas que deben ser eliminadas.

#### **Insertar una columna**

Los desarrolladores también pueden insertar una columna en la hoja de cálculo en cualquier ubicación llamando al método [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) de la colección [Cells](https://reference.aspose.com/cells/go-cpp/cells/). El método [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) toma el índice de la columna donde se insertará la nueva columna.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertColumn.go" >}}

Para eliminar una columna de la hoja de cálculo en cualquier ubicación, llame al método [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) de la colección [Cells](https://reference.aspose.com/cells/go-cpp/cells/). El método [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) toma el índice de la columna a eliminar.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteColumn.go" >}}
