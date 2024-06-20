---
title: Insertar y Eliminar Filas y Columnas de un archivo de Excel
linktitle: Inserción y Eliminación de Filas y Columnas
type: docs
weight: 70
url: /es/python-net/inserting-and-deleting-rows-and-columns/
description: Este artículo muestra cómo insertar y eliminar filas y columnas mediante la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Aspose.Cells Python administra filas y columnas, Python inserta filas y columnas, Python elimina filas y columnas, Python elimina filas y columnas.
---

## **Introducción**

Ya sea creando una nueva hoja de cálculo desde cero o trabajando en una hoja de cálculo existente, puede ser necesario agregar filas o columnas adicionales para acomodar más datos. Inversamente, también puede ser necesario eliminar filas o columnas de posiciones específicas en la hoja de cálculo.
Para cumplir con estos requisitos, Aspose.Cells para Python via .NET proporciona un conjunto muy simple de clases y métodos, discutidos a continuación.

### **Gestionar Filas y Columnas**

Aspose.Cells para Python via .NET proporciona una clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) que representa todas las celdas en la hoja de cálculo.

La colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) proporciona varios métodos para gestionar filas y columnas en una hoja de cálculo. Algunos de estos se discuten a continuación.

{{% alert color="primary" %}}

Cuando se agregan filas o columnas, el contenido en la hoja de cálculo se desplaza hacia abajo o hacia la derecha, y si se eliminan filas o columnas, el contenido se desplaza hacia arriba o hacia la izquierda.

{{% /alert %}}


## **Insertar Filas y Columnas**

### **Cómo insertar una fila**

Inserte una fila en la hoja de cálculo en cualquier ubicación llamando al método [**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/) de la colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). El método [**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/) toma el índice de la fila donde se insertará la nueva fila.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARow-1.py" >}}

### **Cómo insertar múltiples filas**

Para insertar múltiples filas en una hoja de cálculo, llame al método [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int) de la colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). El método [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int) toma dos parámetros:

- Índice de la fila, el índice de la fila desde donde se insertarán las nuevas filas.
- Número de filas, el número total de filas que se deben insertar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.py" >}}

### **Cómo insertar una fila con formato**

Para insertar una fila con opciones de formato, use la sobrecarga [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int-aspose.cells.InsertOptions) que toma [**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions) como parámetro. Establezca la propiedad [**copy_format_type**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions/copy_format_type/) de la clase [**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions) con la enumeración [**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/). La enumeración [**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/) tiene tres miembros que se enumeran a continuación.

- MISMA_QUE_LA_ANTERIOR: Formatea la fila igual que la fila anterior.
- MISMA_QUE_LA_SIGUIENTE: Formatea la fila igual que la fila siguiente.
- CLARO: Borra el formato.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.py" >}}

### **Cómo Insertar una Columna**

Los desarrolladores también pueden insertar una columna en la hoja de cálculo en cualquier ubicación llamando al método [**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int) de la colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). El método [**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int) toma el índice de la columna donde se insertará la nueva columna.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingAColumn-1.py" >}}

## **Eliminar Filas y Columnas**

### **Cómo borrar múltiples filas**

Para eliminar múltiples filas de una hoja de cálculo, llama al método [**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int) de la colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). El método [**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int) toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se eliminarán las filas.
- Número de filas, el número total de filas que deben ser eliminadas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.py" >}}


### **Cómo eliminar una columna**

Para eliminar una columna de la hoja de cálculo en cualquier ubicación, llama al método [**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int) de la colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). El método [**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int) toma el índice de la columna a eliminar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingAColumn-1.py" >}}
