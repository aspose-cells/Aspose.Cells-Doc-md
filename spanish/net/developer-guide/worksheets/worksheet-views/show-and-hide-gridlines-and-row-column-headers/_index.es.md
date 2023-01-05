---
title: Mostrar y ocultar líneas de cuadrícula y encabezados de columna de fila
type: docs
weight: 30
url: /es/net/show-and-hide-gridlines-and-row-column-headers/
description: Este artículo proporciona un código de muestra para usar la biblioteca C# API o .NET para ocultar o mostrar mediante programación líneas de cuadrícula, encabezados de fila y columna de una hoja de cálculo de Excel.
---
{{% alert color="primary" %}}

Aspose.Cells admite ocultar y mostrar líneas de cuadrícula de la hoja de trabajo que son visibles de forma predeterminada. También proporciona visibilidad de control de los encabezados de columna de fila de la hoja de trabajo.

{{% /alert %}}

## **Mostrar y ocultar líneas de cuadrícula**

Todas las hojas de cálculo de Excel tienen líneas de cuadrícula de forma predeterminada. Ayudan a delinear celdas para que sea fácil ingresar datos en celdas particulares. Las líneas de cuadrícula nos permiten ver una hoja de trabajo como una colección de celdas, donde cada celda es fácilmente identificable.

### **Controlar la visibilidad de las líneas de cuadrícula**

Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Excel Microsoft. Él[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)colección que permite a los desarrolladores acceder a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. Él[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La clase proporciona una amplia gama de propiedades y métodos para administrar una hoja de cálculo. Para controlar la visibilidad de las líneas de cuadrícula, utilice el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase[**EsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) propiedad.[**EsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) es una propiedad booleana, lo que significa que solo puede almacenar una**verdadero** o**falso** valor.

#### **Hacer visibles las líneas de cuadrícula**

 Haga que las líneas de la cuadrícula sean visibles configurando el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase[**EsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) propiedad a**verdadero**.

#### **Ocultar líneas de cuadrícula**

 Oculte las líneas de cuadrícula configurando el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase[**EsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) propiedad a**falso**.

 A continuación se muestra un ejemplo completo que demuestra el uso de la[**EsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)propiedad abriendo un archivo de Excel (book1.xls), ocultando las líneas de cuadrícula en la primera hoja de trabajo y guardando el archivo modificado como salida.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **Mostrar y ocultar encabezados de columna de fila**

Todas las hojas de trabajo en un archivo de Excel se componen de celdas que se organizan en filas y columnas. Todas las filas y columnas tienen valores únicos que se utilizan para identificarlas y para identificar celdas individuales. Por ejemplo, las filas están numeradas (1, 2, 3, 4, etc.) y las columnas están ordenadas alfabéticamente (A, B, C, D, etc.). Los valores de fila y columna se muestran en los encabezados. Usando Aspose.Cells, los desarrolladores pueden controlar la visibilidad de estos encabezados de fila y columna.

### **Control de la visibilidad de las hojas de trabajo**

Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Excel Microsoft. Él[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)colección que permite a los desarrolladores acceder a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)clase. Él[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La clase proporciona una amplia gama de propiedades y métodos para administrar una hoja de cálculo. Para controlar la visibilidad de los encabezados de fila y columna, use el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) propiedad.[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) es una propiedad booleana, lo que significa que solo puede almacenar una**verdadero** o**falso**valor.

#### **Hacer visibles los encabezados de fila/columna**

 Haga que los encabezados de fila y columna sean visibles configurando el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) propiedad a**verdadero**.

#### **Ocultar encabezados de fila/columna**

 Oculte los encabezados de fila y columna configurando el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) propiedad a**falso**.

A continuación se muestra un ejemplo completo que muestra cómo utilizar el[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)propiedad abriendo un archivo de Excel (book1.xls), ocultando los encabezados de fila y columna en la primera hoja de trabajo y guardando el archivo modificado como salida.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

 También es posible utilizar el[**Mostrar filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) y[**Mostrar columnas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) métodos de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) class para hacer visibles varias filas y columnas.

{{% /alert %}}
