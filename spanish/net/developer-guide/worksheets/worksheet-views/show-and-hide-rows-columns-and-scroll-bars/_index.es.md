---
title: Mostrar y ocultar filas, columnas y barras de desplazamiento
type: docs
weight: 20
url: /es/net/show-and-hide-rows-columns-and-scroll-bars/
---
{{% alert color="primary" %}}

Aspose.Cells proporciona formas de controlar la visibilidad de las filas, las columnas y las barras de desplazamiento de una hoja de trabajo.

{{% /alert %}}

## **Mostrar y ocultar filas y columnas**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite a los desarrolladores acceder a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección que representa todas las celdas de la hoja de cálculo. los[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)colección proporciona varios métodos para administrar filas o columnas en una hoja de cálculo. Algunos de estos se discuten a continuación.

### **Mostrar filas y columnas**

 Los desarrolladores pueden mostrar cualquier fila o columna oculta llamando al[**Mostrar Fila**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) y[**Mostrar columna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) métodos de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)colección respectivamente. Ambos métodos toman dos parámetros:

- **Índice de fila o columna** - el índice de una fila o columna que se utiliza para mostrar la fila o columna específica.
- **Alto de fila o ancho de columna** - la altura de fila o el ancho de columna asignado a la fila o columna después de mostrarse.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Al hacer visible una columna oculta, si necesita restaurarla al ancho previamente asignado o al ancho original, muestre la columna con un ancho negativo. Por ejemplo: hoja de trabajo.Cells.MostrarColumna(5, -1)

{{% /alert %}}

### **Ocultar filas y columnas**

 Los desarrolladores pueden ocultar una fila o columna llamando al[**Ocultarfila**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) y[**OcultarColumna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) métodos de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)colección respectivamente. Ambos métodos toman el índice de fila y columna como parámetro para ocultar la fila o columna específica.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

También es posible ocultar una fila o columna configurando la altura de la fila o el ancho de la columna en 0 respectivamente.

{{% /alert %}}

### **Ocultar varias filas y columnas**

 Los desarrolladores pueden ocultar varias filas o columnas a la vez llamando al[**Ocultar Filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) y[**Ocultar columnas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) métodos de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)colección respectivamente. Ambos métodos toman el índice de fila o columna inicial y el número de filas o columnas que deben ocultarse como parámetros.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **Mostrar y ocultar barras de desplazamiento**

Las barras de desplazamiento se utilizan para navegar por el contenido de cualquier archivo. Normalmente, hay dos tipos de barras de desplazamiento:

- Barras de desplazamiento verticales
- Barras de desplazamiento horizontales

Microsoft Excel también proporciona barras de desplazamiento horizontales y verticales para que los usuarios puedan desplazarse por el contenido de la hoja de trabajo. Usando Aspose.Cells, los desarrolladores pueden controlar la visibilidad de ambos tipos de barras de desplazamiento en archivos de Excel.

### **Control de la visibilidad de las barras de desplazamiento**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) La clase proporciona una amplia gama de propiedades y métodos para administrar un archivo de Excel. Para controlar la visibilidad de las barras de desplazamiento, utilice el[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) y[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)propiedades.[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) y[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) son propiedades booleanas, lo que significa que estas propiedades solo pueden almacenar**verdadero** o**falso** valores.

#### **Haciendo visibles las barras de desplazamiento**

 Haga que las barras de desplazamiento sean visibles configurando el[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) o[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) propiedad a**verdadero**.

#### **Ocultar barras de desplazamiento**

 Oculte las barras de desplazamiento configurando el[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) o[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) propiedad a**falso**.

**Código de muestra**

A continuación se muestra un código completo que abre un archivo de Excel, book1.xls, oculta ambas barras de desplazamiento y luego guarda el archivo modificado como salida.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
