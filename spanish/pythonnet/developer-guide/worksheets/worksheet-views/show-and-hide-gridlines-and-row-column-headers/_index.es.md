---
title: Mostrar y ocultar las cuadrículas y encabezados de filas y columnas
type: docs
weight: 30
url: /es/python-net/show-and-hide-gridlines-and-row-column-headers/
description: Este artículo proporciona código de ejemplo para usar la API Aspose.Cells para Python via .NET para ocultar o mostrar programáticamente las líneas de cuadrícula, encabezados de filas y columnas de una hoja de cálculo de Excel.
keywords: Biblioteca de Excel en Python, Mostrar y Ocultar líneas de cuadrícula en Python, Cómo Mostrar y Ocultar encabezados de fila y columna en Python, Cómo Mostrar y Ocultar líneas de cuadrícula y encabezados de fila y columna en Python.
---

{{% alert color="primary" %}}

Aspose.Cells para Python via .NET soporta ocultar y mostrar líneas de cuadrícula de la hoja de cálculo que son visibles por defecto. También proporciona control de la visibilidad de los encabezados de fila y columna de la hoja.

{{% /alert %}}

## **Mostrar y ocultar las cuadrículas**

Todas las hojas de cálculo de Excel tienen cuadrículas de forma predeterminada. Ayudan a delimitar las celdas para que sea fácil ingresar datos en celdas particulares. Las cuadrículas nos permiten ver una hoja de cálculo como una colección de celdas, donde cada celda es fácilmente identificable.

### **Controlar la visibilidad de las cuadrículas**

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) que permite a los desarrolladores acceder a cada hoja en el archivo de Excel. Una hoja se representa mediante la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) ofrece una amplia gama de propiedades y métodos para gestionar una hoja de cálculo. Para controlar la visibilidad de las líneas de cuadrícula, usa la propiedad [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) de la clase [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/). [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) es una propiedad booleana, lo que significa que solo puede almacenar un valor **verdadero** o **falso**.

#### **Hacer visible las líneas de cuadrícula**

Hacer visibles las cuadrículas estableciendo la propiedad [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) de la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) a **true**.

#### **Ocultar líneas de cuadrícula**

Ocultar las cuadrículas estableciendo la propiedad [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) de la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) a **false**.

A continuación se presenta un ejemplo completo que demuestra el uso de la propiedad [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) al abrir un archivo de Excel (book1.xls), ocultar las cuadrículas en la primera hoja de cálculo y guardar el archivo modificado como output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideGridlines-1.py" >}}

## **Mostrar y ocultar los encabezados de filas y columnas**

Todas las hojas de cálculo en un archivo de Excel están compuestas por celdas que están organizadas en filas y columnas. Todas las filas y columnas tienen valores únicos que se usan para identificarlas y para identificar celdas individuales. Por ejemplo, las filas están numeradas – 1, 2, 3, 4, etc. – y las columnas están ordenadas alfabéticamente – A, B, C, D, etc. Los valores de fila y columna se muestran en los encabezados. Usando Aspose.Cells para Python via .NET, los desarrolladores pueden controlar la visibilidad de estos encabezados de fila y columna.

### **Controlar la visibilidad de las hojas de cálculo**

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) que permite a los desarrolladores acceder a cada hoja en el archivo de Excel. Una hoja se representa mediante la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) ofrece una amplia gama de propiedades y métodos para gestionar una hoja de cálculo. Para controlar la visibilidad de los encabezados de fila y columna, usa la propiedad [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) de la clase [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/). [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) es una propiedad booleana, lo que significa que solo puede almacenar un valor **verdadero** o **falso**.

#### **Hacer visibles los encabezados de fila/columna**

Hacer visibles los encabezados de filas y columnas estableciendo la propiedad [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) de la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) a **true**.

#### **Ocultar encabezados de filas/columnas**

Ocultar encabezados de fila y columna estableciendo la propiedad [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) de la clase [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) en **falso**.

Se muestra a continuación un ejemplo completo que muestra cómo usar la propiedad [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) abriendo un archivo de Excel (book1.xls), ocultando los encabezados de fila y columna en la primera hoja de trabajo y guardando el archivo modificado como output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideRowColumnHeaders-1.py" >}}

{{% alert color="primary" %}}

También es posible usar los métodos [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows) y [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns) de la clase [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) para hacer varias filas y columnas visibles.

{{% /alert %}}
