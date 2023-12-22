---
title: Insertar y eliminar filas y columnas de un archivo Excel
linktitle: Insertar y eliminar filas y columnas
type: docs
weight: 70
url: /es/net/inserting-and-deleting-rows-and-columns/
description: Este artículo muestra cómo insertar y eliminar filas y columnas mediante Aspose.Cells for .NET API.
keywords: Aspose.Cells C# manage rows and columns, insert rows and columns, delete rows and columns
---
##  **Introducción**

Ya sea que creemos una nueva hoja de trabajo desde cero o trabajemos en una hoja de trabajo existente, es posible que necesitemos agregar filas o columnas adicionales para acomodar más datos. A la inversa, es posible que también necesitemos eliminar filas o columnas de posiciones específicas en la hoja de trabajo.
Para cumplir con estos requisitos, Aspose.Cells proporciona un conjunto de clases y métodos muy simple, que se analiza a continuación.

###  **Administrar filas y columnas**

Aspose.Cells proporciona una clase[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo Excel Microsoft. El[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)colección que permite el acceso a cada hoja de cálculo en un archivo Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. El[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)colección que representa todas las celdas de la hoja de trabajo.

 El[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)La colección proporciona varios métodos para administrar filas y columnas en una hoja de trabajo. Algunos de éstos se discuten a continuación.

{{% alert color="primary" %}}

Cuando se agregan filas o columnas, el contenido de la hoja de cálculo se desplaza hacia abajo o hacia la derecha, y si se eliminan filas o columnas, el contenido se desplaza hacia arriba o hacia la izquierda.

{{% /alert %}}


##  **Insertar filas y columnas**

###  **Cómo insertar una fila**

 Inserte una fila en la hoja de trabajo en cualquier ubicación llamando al[**Insertar fila**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) método de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. El[**Insertar fila**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)El método toma el índice de la fila donde se insertará la nueva fila.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

###  **Cómo insertar varias filas**

 Para insertar varias filas en una hoja de trabajo, llame al[**Insertar filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) método de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. El[**Insertar filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)El método toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se insertarán las nuevas filas.
- Número de filas, el número total de filas que deben insertarse.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

###  **Cómo insertar una fila con formato**

Para insertar una fila con opciones de formato, utilice el[**Insertar filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)sobrecarga que lleva[**Insertar opciones**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) como parámetro. Selecciona el[**Tipo de formato de copia**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) propiedad de[**Insertar opciones**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) clase con[**Tipo de formato de copia**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) Enumeración. El[**Tipo de formato de copia**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)La enumeración tiene tres miembros como se enumeran a continuación.

- Igual que arriba: formatea la fila igual que la fila anterior.
- Igual que abajo: formatea la fila igual que la fila siguiente.
- Borrar: borra el formato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

###  **Cómo insertar una columna**

 Los desarrolladores también pueden insertar una columna en la hoja de trabajo en cualquier ubicación llamando al[**Insertar columna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) método de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)recopilación. El[**Insertar columna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)El método toma el índice de la columna donde se insertará la nueva columna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

##  **Eliminar filas y columnas**

###  **Cómo eliminar varias filas**

 Para eliminar varias filas de una hoja de cálculo, llame al[**Eliminar filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) método de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. El[**Eliminar filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)El método toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se eliminarán las filas.
- Número de filas, el número total de filas que deben eliminarse.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


###  **Cómo eliminar una columna**

 Para eliminar una columna de la hoja de cálculo en cualquier ubicación, llame al[**Eliminar columna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) método de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. El[**Eliminar columna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)El método toma el índice de la columna a eliminar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
