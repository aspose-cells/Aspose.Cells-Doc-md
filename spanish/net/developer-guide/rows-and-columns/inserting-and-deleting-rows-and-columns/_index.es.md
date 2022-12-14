---
title: Insertar y eliminar filas y columnas de un archivo de Excel
linktitle: Insertar y eliminar filas y columnas
type: docs
weight: 70
url: /es/net/inserting-and-deleting-rows-and-columns/
---
## **Introducción**

Ya sea creando una nueva hoja de trabajo desde cero o trabajando en una hoja de trabajo existente, es posible que necesitemos agregar filas o columnas adicionales para acomodar más datos. A la inversa, es posible que también necesitemos eliminar filas o columnas de posiciones específicas en la hoja de trabajo.
Para cumplir con estos requisitos, Aspose.Cells proporciona un conjunto de clases y métodos muy simple, que se analiza a continuación.

### **Administrar filas y columnas**

Aspose.Cells proporciona una clase[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) colección que permite el acceso a cada hoja de trabajo en un archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)colección que representa todas las celdas de la hoja de trabajo.

 los[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)La colección proporciona varios métodos para administrar filas y columnas en una hoja de cálculo. Algunos de éstos se discuten a continuación.

{{% alert color="primary" %}}

Cuando se agregan filas o columnas, el contenido de la hoja de cálculo se desplaza hacia abajo o hacia la derecha, y si se eliminan filas o columnas, el contenido se desplaza hacia arriba o hacia la izquierda.

{{% /alert %}}


## **Insertar filas y columnas**

### **Insertar una fila**

 Inserte una fila en la hoja de trabajo en cualquier lugar llamando al[**Insertar fila**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) metodo de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. los[**Insertar fila**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)El método toma el índice de la fila donde se insertará la nueva fila.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **Insertar varias filas**

 Para insertar varias filas en una hoja de trabajo, llame al[**Insertar filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) metodo de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. los[**Insertar filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)El método toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se insertarán las nuevas filas.
- Número de filas, el número total de filas que deben insertarse.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **Insertar una fila con formato**

Para insertar una fila con opciones de formato, use el[**Insertar filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)sobrecarga que toma[**Opciones de inserción**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) como parámetro. Selecciona el[**Tipo de formato de copia**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) propiedad de[**Opciones de inserción**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) clase con[**Tipo de formato de copia**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) Enumeración. los[**Tipo de formato de copia**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)La enumeración tiene tres miembros, como se indica a continuación.

- SameAsAbove: da formato a la fila igual que la fila anterior.
- SameAsBelow: da formato a la fila igual que la fila de abajo.
- Borrar: Borra el formato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **Insertar una columna**

 Los desarrolladores también pueden insertar una columna en la hoja de trabajo en cualquier ubicación llamando al[**InsertarColumna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) metodo de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)recopilación. los[**InsertarColumna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)El método toma el índice de la columna donde se insertará la nueva columna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **Eliminar filas y columnas**

### **Eliminar varias filas**

Para eliminar varias filas de una hoja de trabajo, llame al[**Eliminar filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) metodo de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. los[**Eliminar filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)El método toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se eliminarán las filas.
- Número de filas, el número total de filas que deben eliminarse.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **Eliminar una columna**

 Para eliminar una columna de la hoja de cálculo en cualquier lugar, llame al[**EliminarColumna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) metodo de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. los[**EliminarColumna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)El método toma el índice de la columna a eliminar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
