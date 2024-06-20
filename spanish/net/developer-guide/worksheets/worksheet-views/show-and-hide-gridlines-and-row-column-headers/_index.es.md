---
title: Mostrar y ocultar las cuadrículas y encabezados de filas y columnas
type: docs
weight: 30
url: /es/net/show-and-hide-gridlines-and-row-column-headers/
description: Este artículo proporciona código de ejemplo para usar la API de C# o la Biblioteca .NET para ocultar o mostrar programáticamente las cuadrículas, encabezados de filas y columnas de una hoja de cálculo de Excel.
---

{{% alert color="primary" %}}

Aspose.Cells admite ocultar y mostrar las cuadrículas de la hoja de cálculo que son visibles de forma predeterminada. También proporciona el control de la visibilidad de los encabezados de filas y columnas de la hoja de cálculo.

{{% /alert %}}

## **Mostrar y ocultar las cuadrículas**

Todas las hojas de cálculo de Excel tienen cuadrículas de forma predeterminada. Ayudan a delimitar las celdas para que sea fácil ingresar datos en celdas particulares. Las cuadrículas nos permiten ver una hoja de cálculo como una colección de celdas, donde cada celda es fácilmente identificable.

### **Controlar la visibilidad de las cuadrículas**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite a los desarrolladores acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar una hoja de cálculo. Para controlar la visibilidad de las cuadrículas, utilice la propiedad [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) de la clase [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible). [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) es una propiedad booleana, lo que significa que solo puede almacenar un valor **true** o **false**.

#### **Hacer visible las líneas de cuadrícula**

Hacer visibles las cuadrículas estableciendo la propiedad [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) a **true**.

#### **Ocultar líneas de cuadrícula**

Ocultar las cuadrículas estableciendo la propiedad [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) a **false**.

A continuación se presenta un ejemplo completo que demuestra el uso de la propiedad [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) al abrir un archivo de Excel (book1.xls), ocultar las cuadrículas en la primera hoja de cálculo y guardar el archivo modificado como output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **Mostrar y ocultar los encabezados de filas y columnas**

Todas las hojas de cálculo en un archivo de Excel están compuestas por celdas que están dispuestas en filas y columnas. Todas las filas y columnas tienen valores únicos que se utilizan para identificarlas e identificar celdas individuales. Por ejemplo, las filas están numeradas - 1, 2, 3, 4, etc. - y las columnas están ordenadas alfabéticamente - A, B, C, D, etc. Los valores de filas y columnas se muestran en los encabezados. Con Aspose.Cells, los desarrolladores pueden controlar la visibilidad de estos encabezados de filas y columnas.

### **Controlar la visibilidad de las hojas de cálculo**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite a los desarrolladores acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar una hoja de cálculo. Para controlar la visibilidad de los encabezados de filas y columnas, utilice la propiedad [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) de la clase [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible). [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) es una propiedad booleana, lo que significa que solo puede almacenar un valor **true** o **false**.

#### **Hacer visibles los encabezados de fila/columna**

Hacer visibles los encabezados de filas y columnas estableciendo la propiedad [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) a **true**.

#### **Ocultar encabezados de filas/columnas**

Ocultar encabezados de fila y columna estableciendo la propiedad [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) de la clase [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) en **falso**.

Se muestra a continuación un ejemplo completo que muestra cómo usar la propiedad [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) abriendo un archivo de Excel (book1.xls), ocultando los encabezados de fila y columna en la primera hoja de trabajo y guardando el archivo modificado como output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

También es posible usar los métodos [**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) y [**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) de la clase [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) para hacer varias filas y columnas visibles.

{{% /alert %}}
