---
title: Cambios en la API pública en Aspose.Cells 8.5.0
type: docs
weight: 160
url: /es/net/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.4.2 hasta la 8.5.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, [clases añadidas, etc.](/cells/es/net/public-api-changes-in-aspose-cells-8-5-0/), sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Cambiados los parámetros de ICustomFunction.CalculateCustomFunction**
Si un parámetro para la función personalizada es una referencia de celda, en versiones anteriores las API de Aspose.Cells solían convertir la referencia de celda en un valor de celda único o en una matriz de objetos de todos los valores de celda en el área referida. Sin embargo, para muchas funciones y usuarios, la matriz de valores de celda para todas las celdas en el área referida no es necesaria, solo necesitan una celda única correspondiente a la posición de la fórmula, o simplemente necesitan la referencia en sí misma en lugar del valor de la celda o una matriz de valores. Para algunas situaciones, obtener todos los valores de celda incluso aumentaba el riesgo de error de referencia circular.

Para apoyar este tipo de requisito, Aspose.Cells for .NET 8.5.0 ha cambiado el valor del parámetro por la "paramsList" para el área referida. Desde la v8.5.0, la API simplemente coloca el objeto ReferredArea en la "paramsList" cuando el parámetro correspondiente es una referencia o su resultado calculado es una referencia. Si necesita la referencia en sí, entonces puede usar directamente ReferredArea. Si necesita obtener un único valor de celda de la referencia correspondiente a la posición de la fórmula, puede utilizar el método ReferredArea.GetValue(fila, columna). Si necesita el arreglo de valores de celda para toda el área, entonces puede usar el método ReferredArea.GetValues.

Ahora, ya que Aspose.Cells for .NET 8.5.0 proporciona ReferredArea en "paramsList", la ReferredAreaCollection en "contextObjects" ya no será necesaria (en las versiones antiguas, no siempre podía dar un mapeo uno a uno a los parámetros de la función personalizada), por lo que esta versión también la ha eliminado de "contextObjects" ahora.

Este cambio requiere cambios en el código de la implementación para ICustomFunction un poco cuando se necesita el valor/valores del parámetro de referencia.

**Implementación Antigua**

{{< highlight csharp >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}

**Nueva Implementación**

{{< highlight csharp >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.IsArea)

        {

            o = ra.GetValues();

        }

        else

        {

            o = ra.GetValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}


### **Clase CalculationOptions Agregada**
Aspose.Cells for .NET 8.5.0 ha expuesto la clase CalculationOptions para agregar más flexibilidad y extensibilidad al motor de cálculo de fórmulas. La clase recién añadida tiene las siguientes propiedades.

1. CalculationOptions.CalcStackSize: Especifica el tamaño de la pila para calcular celdas de forma recursiva. -1 especifica que el cálculo utilizará el CalcStackSize de WorkbookSettings del libro correspondiente.
1. CalculationOptions.CustomFunction: Extiende el motor de cálculo de fórmulas con fórmulas personalizadas.
1. CalculationOptions.IgnoreError: Valor de tipo booleano que indica si los errores deben ocultarse al calcular las fórmulas, donde los errores podrían deberse a la función no compatible, el enlace externo o más.
1. CalculationOptions.PrecisionStrategy: Valor de tipo CalculationPrecisionStrategy que especifica la estrategia para el procesamiento de la precisión del cálculo.
### **Se ha agregado la enumeración CalculationPrecisionStrategy**
Aspose.Cells for .NET 8.5.0 ha expuesto la enumeración CalculationPrecisionStrategy para agregar más flexibilidad al motor de cálculo de fórmulas para obtener los resultados deseados. Esta enumeración estrategias el manejo de precisión del cálculo. Debido al problema de precisión de la Aritmética de Punto Flotante IEEE 754, algunas fórmulas aparentemente simples pueden no calcularse para dar los resultados esperados, por lo tanto, la última versión de la API ha expuesto los siguientes campos para obtener los resultados deseados según la selección.

1. CalculationPrecisionStrategy.Decimal: Utiliza decimal como operando cuando es posible, y es la estrategia menos eficiente desde el punto de vista del rendimiento.
1. CalculationPrecisionStrategy.Round: Redondea los resultados de los cálculos de acuerdo con el dígito significativo.
1. CalculationPrecisionStrategy.None: No se aplica ninguna estrategia, por lo tanto, durante el cálculo, el motor utiliza el valor double original como operando y devuelve el resultado directamente. Esta opción es la más eficiente y es aplicable para la mayoría de los casos.
### **Métodos Agregados para usar CalculationOptions**
Con el lanzamiento de v8.5.0, la API de Aspose.Cells ha agregado versiones de sobrecarga del método CalculateFormula como se indica a continuación.

- Workbook.CalculateFormula(CalculationOptions)
- Worksheet.CalculateFormula(CalculationOptions options, bool recursive)
- Cell.Calculate(CalculationOptions)
### **Se agregó el campo de enumeración PasteType.RowHeights**
Las API de Aspose.Cells han proporcionado el campo de enumeración PasteType.RowHeights con el fin de copiar las alturas de las filas al copiar los rangos. Al establecer la propiedad PasteOptions.PasteType en PasteType.RowHeights, las alturas de todas las filas dentro del rango de origen se copiarán al rango de destino.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Source worksheet

Worksheet srcSheet = workbook.Worksheets[0];

//Add destination worksheet

Worksheet dstSheet = workbook.Worksheets.Add("Destination Sheet");

//Set the row height of the 4th row

//This row height will be copied to destination range

srcSheet.Cells.SetRowHeight(3, 50);

//Create source range to be copied

Range srcRange = srcSheet.Cells.CreateRange("A1:D10");

//Create destination range in destination worksheet

Range dstRange = dstSheet.Cells.CreateRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range

PasteOptions opts = new PasteOptions();

opts.PasteType = PasteType.RowHeights;

//Copy source range to destination range with paste options

dstRange.Copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet

dstSheet.Cells["D4"].PutValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format

workbook.Save("output.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}


### **Se agregó la propiedad SheetRender.PageScale**
Cuando se establece la escala de Configuración de página utilizando la opción 'Ajustar a n página(s) de ancho por m de alto', Microsoft Excel calcula el factor de escala de Configuración de página. Lo mismo se puede lograr utilizando la propiedad SheetRender.PageScale expuesta por Aspose.Cells for .NET 8.5.0. Esta propiedad devuelve un valor double que se puede convertir a un valor porcentual. Por ejemplo, si devuelve 0.507968245, significa que el factor de escala es del 51%.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put some data in these cells

worksheet.Cells["A4"].PutValue("Test");

worksheet.Cells["S4"].PutValue("Test");

//Set paper size

worksheet.PageSetup.PaperSize = PaperSizeType.PaperA4;

//Set fit to pages wide as 1

worksheet.PageSetup.FitToPagesWide = 1;

//Calculate page scale via sheet render

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Convert page scale double value to percentage

string strPageScale = sr.PageScale.ToString("0%");

//Write the page scale value

Console.WriteLine(strPageScale);

{{< /highlight >}}


### **Se añadió la enumeración CellValueFormatStrategy**
Aspose.Cells for .NET 8.5.0 ha añadido una nueva enumeración CellValueFormatStrategy para manejar situaciones en las que los valores de celda deben extraerse con o sin formato aplicado. La enumeración CellValueFormatStrategy tiene los siguientes campos.

1. CellValueFormatStrategy.CellStyle: Solo formateado con el formato original de la celda.
1. CellValueFormatStrategy.DisplayStyle: Formateado con el estilo mostrado de la celda.
1. CellValueFormatStrategy.None: Sin formato.
### **Se agregó el método Cell.GetStingValue**
Para utilizar la enumeración CellValueFormatStrategy, v8.5.0 ha expuesto el método Cell.GetStingValue que podría aceptar un parámetro de tipo CellValueFormatStrategy y devuelve el valor dependiendo de la opción especificada.

El siguiente fragmento de código muestra cómo utilizar el método Cells.GetStingValue recién expuesto.

**C#**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1

Cell cell = worksheet.Cells["A1"];

//Put value inside the cell

cell.PutValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.GetStyle();

style.Number = 2;

cell.SetStyle(style);

//Get string value as Cell Style

string value = cell.GetStingValue(CellValueFormatStrategy.CellStyle);

Console.WriteLine(value);

//Get string value without any formatting

value = cell.GetStingValue(CellValueFormatStrategy.None);

Console.WriteLine(value);

{{< /highlight >}}


### **Se añadió la propiedad ExportTableOptions.FormatStrategy**
Aspose.Cells for .NET 8.5.0 ha expuesto la propiedad ExportTableOptions.FormatStrategy para los usuarios que deseen exportar los datos a un DataTable con o sin formato. Esta propiedad utiliza la enumeración CellValueFormatStrategy y exporta los datos según la opción especificada.

El siguiente código explica el uso de la propiedad ExportTableOptions.FormatStrategy.

**C#**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1

Cell cell = worksheet.Cells["A1"];

//Put value inside the cell

cell.PutValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.GetStyle();

style.Number = 2;

cell.SetStyle(style);

//Print the cell values as it displays in excel

Console.WriteLine("Cell String Value: " + cell.StringValue);

//Print the cell value without any format

Console.WriteLine("Cell String Value without Format: " + cell.StringValueWithoutFormat);

//Export Data Table Options with FormatStrategy as CellStyle

ExportTableOptions opts = new ExportTableOptions();

opts.ExportAsString = true;

opts.FormatStrategy = CellValueFormatStrategy.CellStyle;

//Export Data Table

DataTable dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of very first cell

Console.WriteLine("Export Data Table with Format Strategy as Cell Style: " + dt.Rows[0][0].ToString());

//Export Data Table Options with FormatStrategy as None

opts.FormatStrategy = CellValueFormatStrategy.None;

dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of very first cell

Console.WriteLine("Export Data Table with Format Strategy as None: " + dt.Rows[0][0].ToString());

{{< /highlight >}}
