---
title: Ocultar y mostrar filas y columnas
type: docs
weight: 60
url: /es/net/hiding-and-showing-rows-and-columns/
---
{{% alert color="primary" %}}

A veces, tiene sentido ocultar ciertas filas o columnas en una hoja de cálculo y mostrarlas más tarde. Microsoft Excel proporciona esta característica y también Aspose.Cells.

{{% /alert %}}

## **Control de la visibilidad de filas y columnas**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel Microsoft. Él[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) que permite a los desarrolladores acceder a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. Él[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) colección que representa todas las celdas de la hoja de trabajo. Él[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)colección proporciona varios métodos para administrar filas o columnas en una hoja de trabajo. Algunos de estos se discuten a continuación.

### **Ocultar filas y columnas**

 Los desarrolladores pueden ocultar una fila o columna llamando al[**Ocultarfila**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) y[**OcultarColumna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) métodos de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)colección respectivamente. Ambos métodos toman el índice de fila y columna como parámetro para ocultar la fila o columna específica.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

También es posible ocultar una fila o columna configurando la altura de la fila o el ancho de la columna en 0 respectivamente.

{{% /alert %}}

### **Mostrar filas y columnas**

 Los desarrolladores pueden mostrar cualquier fila o columna oculta llamando al[**Mostrar Fila**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) y[**Mostrar columna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) métodos de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)colección respectivamente. Ambos métodos toman dos parámetros:

- **Índice de fila o columna** - el índice de una fila o columna que se utiliza para mostrar la fila o columna específica.
- **Alto de fila o ancho de columna** - la altura de fila o el ancho de columna asignado a la fila o columna después de mostrarse.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Al hacer visible una columna oculta, si necesita restaurarla al ancho previamente asignado o al ancho original, muestre la columna con un ancho negativo. Por ejemplo: hoja de trabajo.Cells.MostrarColumna(5, -1)

{{% /alert %}}

### **Ocultar varias filas y columnas**

 Los desarrolladores pueden ocultar varias filas o columnas a la vez llamando al[**Ocultar Filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) y[**Ocultar columnas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) métodos de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)colección respectivamente. Ambos métodos toman el índice de fila o columna inicial y el número de filas o columnas que deben ocultarse como parámetros.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

 También es posible utilizar el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) clase'[**Mostrar filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) y[**Mostrar columnas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns)métodos para hacer visibles varias filas y columnas.

{{% /alert %}}
