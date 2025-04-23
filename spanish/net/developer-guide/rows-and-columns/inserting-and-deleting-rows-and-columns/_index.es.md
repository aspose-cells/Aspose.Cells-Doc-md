---
title: Insertar y Eliminar Filas y Columnas de un archivo de Excel
linktitle: Inserción y Eliminación de Filas y Columnas
type: docs
weight: 70
url: /es/net/inserting-and-deleting-rows-and-columns/
description: Este artículo muestra cómo insertar y eliminar filas y columnas mediante la API Aspose.Cells for .NET de Aspose.Cells.
keywords: Aspose.Cells C# manejar filas y columnas, insertar filas y columnas, eliminar filas y columnas
---

## **Introducción**

Ya sea creando una nueva hoja de cálculo desde cero o trabajando en una hoja de cálculo existente, puede ser necesario agregar filas o columnas adicionales para acomodar más datos. Inversamente, también puede ser necesario eliminar filas o columnas de posiciones específicas en la hoja de cálculo.
Para cumplir con estos requisitos, Aspose.Cells proporciona un conjunto muy simple de clases y métodos, discutidos a continuación.

### **Gestionar Filas y Columnas**

Aspose.Cells proporciona una clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) que representa todas las celdas en la hoja de cálculo.

La colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) proporciona varios métodos para gestionar filas y columnas en una hoja de cálculo. Algunos de estos se discuten a continuación.

{{% alert color="primary" %}}

Cuando se agregan filas o columnas, el contenido en la hoja de cálculo se desplaza hacia abajo o hacia la derecha, y si se eliminan filas o columnas, el contenido se desplaza hacia arriba o hacia la izquierda.

{{% /alert %}}


## **Insertar Filas y Columnas**

### **Cómo insertar una fila**

Inserte una fila en la hoja de cálculo en cualquier ubicación llamando al método [**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). El método [**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) toma el índice de la fila donde se insertará la nueva fila.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **Cómo insertar múltiples filas**

Para insertar múltiples filas en una hoja de cálculo, llame al método [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). El método [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) toma dos parámetros:

- Índice de la fila, el índice de la fila desde donde se insertarán las nuevas filas.
- Número de filas, el número total de filas que se deben insertar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **Cómo insertar una fila con formato**

Para insertar una fila con opciones de formato, use la sobrecarga [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) que toma [**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) como parámetro. Establezca la propiedad [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) de la clase [**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) con la enumeración [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype). La enumeración [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) tiene tres miembros que se enumeran a continuación.

- SameAsAbove: Formatea la fila igual que la fila superior.
- SameAsBelow: Formatea la fila igual que la fila inferior.
- Clear: Borra el formato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **Cómo Insertar una Columna**

Los desarrolladores también pueden insertar una columna en la hoja de cálculo en cualquier ubicación llamando al método [**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). El método [**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) toma el índice de la columna donde se insertará la nueva columna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **Eliminar Filas y Columnas**

### **Cómo borrar múltiples filas**

Para eliminar múltiples filas de una hoja de cálculo, llama al método [**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). El método [**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se eliminarán las filas.
- Número de filas, el número total de filas que deben ser eliminadas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **Cómo eliminar una columna**

Para eliminar una columna de la hoja de cálculo en cualquier ubicación, llama al método [**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). El método [**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) toma el índice de la columna a eliminar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
