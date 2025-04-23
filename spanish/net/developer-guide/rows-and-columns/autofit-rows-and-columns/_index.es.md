---
title: Ajustar automáticamente filas y columnas
type: docs
weight: 20
url: /es/net/autofit-rows-and-columns/
description: Este artículo muestra cómo ajustar automáticamente filas, columnas, filas de celdas fusionadas y filas en un rango de celdas utilizando la API Aspose.Cells for .NET.
keywords: Ajustar automáticamente filas, ajustar automáticamente columnas, ajustar automáticamente fila en un rango de celdas, ajustar automáticamente filas de celdas fusionadas
---

{{% alert color="primary" %}}

Microsoft Excel permite a los usuarios ajustar automáticamente el ancho y alto de las celdas según su contenido. Esta característica también está disponible a través de Aspose.Cells para que los desarrolladores puedan ajustar automáticamente las dimensiones de una celda en tiempo de ejecución.

{{% /alert %}}

## **Ajuste automático**

Aspose.Cells proporciona una clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) ofrece una amplia gama de propiedades y métodos para gestionar una hoja de cálculo. Este artículo examina el uso de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) para ajustar automáticamente filas o columnas.

### **Ajuste automático de fila - Simple**

El enfoque más directo para ajustar automáticamente el ancho y alto de una fila es llamar al método [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). El método [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) toma como parámetro el índice de la fila a redimensionar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **Cómo AutoAjustar una Fila en un Rango de Celdas**

Una fila está compuesta por muchas columnas. Aspose.Cells permite a los desarrolladores ajustar automáticamente una fila en función del contenido en un rango de celdas dentro de la fila llamando a una versión sobrecargada del método [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1). Toma los siguientes parámetros:

- **Índice de la fila**, el índice de la fila a ajustar automáticamente.
- **Índice de la primera columna**, el índice de la primera columna de la fila.
- **Índice de la última columna**, el índice de la última columna de la fila.

El método [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1) verifica el contenido de todas las columnas en la fila y luego ajusta automáticamente la fila.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **Cómo AutoAjustar una Columna en un Rango de Celdas**

Una columna está compuesta por muchas filas. Es posible ajustar automáticamente una columna en función del contenido en un rango de celdas en la columna llamando a una versión sobrecargada del método [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) que toma los siguientes parámetros:

- **Índice de columna**, el índice de la columna que se va a ajustar automáticamente.
- **Índice de la primera fila**, el índice de la primera fila de la columna.
- **Índice de la última fila**, el índice de la última fila de la columna.

El método [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) verifica el contenido de todas las filas en la columna y luego ajusta automáticamente la columna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **Cómo AutoAjustar Filas para Celdas Fusionadas**

Con Aspose.Cells es posible ajustar automáticamente filas incluso para celdas que han sido fusionadas utilizando la API [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions). La clase [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) proporciona la propiedad [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) que se puede utilizar para ajustar automáticamente filas para celdas fusionadas. [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) acepta el enumerador [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) que tiene los siguientes miembros.

- Ninguna: Ignorar celdas fusionadas.
- PrimeraLínea: Solo expande la altura de la primera fila.
- ÚltimaLínea: Solo expande la altura de la última fila.
- EachLine: solo expande la altura de cada fila.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

También puedes probar a usar las versiones sobrecargadas de los métodos [**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) y [**AutoFitColumns**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) que aceptan un rango de filas/columnas y una instancia de [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) para ajustar automáticamente las filas/columnas seleccionadas con tu [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) deseado correspondientemente.

Las firmas de los métodos antes mencionados son las siguientes:

1. AutoFitRows(int filaInicial, int filaFinal, opciones [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions))
1. AutoFitColumns(int primeraColumna, int últimaColumna, opciones [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions))

{{% /alert %}}

## **Importante saber**

{{% alert color="primary" %}}

Si una celda está fusionada, entonces los métodos AutoFit no se aplicarán, lo cual es el mismo comportamiento que en Microsoft Excel. Puedes evitar esto utilizando la API de filtro automático. Además, si el texto en una celda está envuelto, el método [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) tampoco se aplicará. Otro detalle que debes saber es que los métodos *AutoFit* consumen tiempo. Por lo tanto, debes llamar a estos métodos lo menos posible para garantizar la eficiencia de tu aplicación.

{{% /alert %}}

## **Temas avanzados**
- [Ajustar automáticamente filas para celdas fusionadas](/cells/es/net/autofit-rows-for-merged-cells/)
{{< app/cells/assistant language="csharp" >}}
