---
title: Autoajustar filas y columnas
type: docs
weight: 20
url: /es/net/autofit-rows-and-columns/
---
{{% alert color="primary" %}}

Microsoft Excel permite a los usuarios cambiar automáticamente el tamaño del ancho y el alto de las celdas según su contenido. Esta función también está disponible a través del Aspose.Cells para que los desarrolladores puedan cambiar automáticamente el tamaño de las dimensiones de una celda en tiempo de ejecución.

{{% /alert %}}

## **Ajuste automático**

Aspose.Cells proporciona un[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)clase que representa un archivo de Excel Microsoft. Él[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)colección que permite el acceso a cada hoja de trabajo en un archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. Él[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La clase proporciona una amplia gama de propiedades y métodos para administrar una hoja de cálculo. Este artículo analiza el uso de la[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)clase para autoajustar filas o columnas.

### **Autoajustar fila - Simple**

 El enfoque más sencillo para cambiar automáticamente el tamaño del ancho y el alto de una fila es llamar al[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase[**Autoajustar fila**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) método. Él[**Autoajustar fila**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)El método toma un índice de fila (de la fila a redimensionar) como parámetro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **Autoajustar fila en un rango de Cells**

 Una fila se compone de muchas columnas. Aspose.Cells permite a los desarrolladores ajustar automáticamente una fila según el contenido de un rango de celdas dentro de la fila llamando a una versión sobrecargada del[**Autoajustar fila**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)método. Toma los siguientes parámetros:

- **Índice de fila**, el índice de la fila que se va a ajustar automáticamente.
- **Índice de la primera columna**, el índice de la primera columna de la fila.
- **Índice de la última columna**, el índice de la última columna de la fila.

 Él[**Autoajustar fila**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)El método verifica el contenido de todas las columnas en la fila y luego ajusta automáticamente la fila.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **Autoajustar columna en un rango de Cells**

 Una columna se compone de muchas filas. Es posible ajustar automáticamente una columna en función del contenido de un rango de celdas de la columna llamando a una versión sobrecargada de[**Autoajustar columna**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)método que toma los siguientes parámetros:

- **índice de columna**el índice de la columna a punto de autoajustarse.
- **Índice de la primera fila**, el índice de la primera fila de la columna.
- **Índice de la última fila**, el índice de la última fila de la columna.

 Él[**Autoajustar columna**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)El método verifica el contenido de todas las filas en la columna y luego ajusta automáticamente la columna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **Autoajustar filas para combinar Cells**

 Con Aspose.Cells es posible autoajustar filas incluso para celdas que se han combinado usando el[**AutoFitterOpciones**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**AutoFitterOpciones**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)clase proporciona[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) propiedad que se puede usar para autoajustar filas para celdas combinadas.[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)acepta[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) enumerable que tiene los siguientes miembros.

- Ninguno: ignora las celdas combinadas.
- FirstLine: solo expande la altura de la primera fila.
- LastLine: solo expande la altura de la última fila.
- Cada línea: solo expande la altura de cada fila.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

 También puede intentar usar las versiones sobrecargadas de[**Autoajustar filas**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**Autoajustar columnas**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) métodos que aceptan un rango de filas/columnas y una instancia de[**AutoFitterOpciones**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) para ajustar automáticamente las filas/columnas seleccionadas con su deseado[**AutoFitterOpciones**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)respectivamente.

Las firmas de los métodos antes mencionados son las siguientes:

1.  AutoFitRows(int StartRow, int EndRow,[**AutoFitterOpciones**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)opciones)
1. AutoFitColumns (int primera columna, int última columna,[**AutoFitterOpciones**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)opciones)

{{% /alert %}}

## **Importante saber**

{{% alert color="primary" %}}

 Si se fusiona una celda, no se aplicarán los métodos AutoFit, que es el mismo comportamiento que en Microsoft Excel. Puede evitar esto usando el filtro automático API. Además, si el texto en una celda está ajustado, el[**Autoajustar columna**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) tampoco se aplicará el método. Otra cosa que debes saber es que el*Autoajustar*los métodos requieren mucho tiempo. Por lo tanto, debe llamar a estos métodos con la menor frecuencia posible para garantizar la eficiencia de su aplicación.

{{% /alert %}}

## **Temas avanzados**
- [Autoajustar filas para combinar Cells](/cells/es/net/autofit-rows-for-merged-cells/)
