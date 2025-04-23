---
title: Cambios en la API pública en Aspose.Cells 8.5.0
type: docs
weight: 170
url: /es/java/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.4.2 hasta la 8.5.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, [clases agregadas, etc.](/cells/es/java/public-api-changes-in-aspose-cells-8-5-0/), sino también una descripción de cualquier cambio en el comportamiento entre bastidores en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Cambiados los parámetros de ICustomFunction.CalculateCustomFunction**
Si un parámetro para la función personalizada es una referencia de celda, en versiones anteriores las API de Aspose.Cells solían convertir la referencia de celda en un valor de celda único o en una matriz de objetos de todos los valores de celda en el área referida. Sin embargo, para muchas funciones y usuarios, la matriz de valores de celda para todas las celdas en el área referida no es necesaria, solo necesitan una celda única correspondiente a la posición de la fórmula, o simplemente necesitan la referencia en sí misma en lugar del valor de la celda o una matriz de valores. Para algunas situaciones, obtener todos los valores de celda incluso aumentaba el riesgo de error de referencia circular.

Para soportar este tipo de requerimiento, Aspose.Cells for Java versión 8.5.0 ha cambiado el valor del parámetro a "paramsList" para el área referida. Desde la versión 8.5.0, la API simplemente coloca el objeto ReferredArea en la "paramsList" cuando el parámetro correspondiente es una referencia o su resultado calculado es una referencia. Si necesita la referencia en sí misma, entonces puede usar directamente ReferredArea. Si necesita obtener un único valor de celda de la referencia correspondiente con la posición de la fórmula, puede utilizar el método ReferredArea.getValue(rowOffset, int colOffset). Si necesita una matriz de valores de celda para toda el área, entonces puede utilizar el método ReferredArea.getValues.

Ahora como Aspose.Cells for Java versión 8.5.0 proporciona ReferredArea en "paramsList", la ReferredAreaCollection en "contextObjects" ya no será necesaria (en las versiones antiguas no siempre podía dar un mapeo uno a uno con los parámetros de la función personalizada), por lo que esta versión también la ha eliminado de "contextObjects" ahora.

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

            o = ra.getValues();

        }

        else

        {

            o = ra.getValue(0, 0);

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
Aspose.Cells for Java versión 8.5.0 ha expuesto la clase CalculationOptions para agregar más flexibilidad y extensibilidad al motor de cálculo de fórmulas. La clase recién agregada tiene las siguientes propiedades. 

1. CalculationOptions.CalcStackSize: Especifica el tamaño de la pila para calcular celdas de forma recursiva. -1 especifica que el cálculo utilizará el CalcStackSize de WorkbookSettings del libro correspondiente.
1. CalculationOptions.CustomFunction: Extiende el motor de cálculo de fórmulas con fórmulas personalizadas.
1. CalculationOptions.IgnoreError: Valor de tipo booleano que indica si los errores deben ocultarse al calcular las fórmulas, donde los errores podrían deberse a la función no compatible, el enlace externo o más.
1. CalculationOptions.PrecisionStrategy: Valor de tipo CalculationPrecisionStrategy que especifica la estrategia para el procesamiento de la precisión del cálculo.
### **Se ha agregado la enumeración CalculationPrecisionStrategy**
Aspose.Cells for Java versión 8.5.0 ha expuesto la enumeración CalculationPrecisionStrategy para agregar más flexibilidad al motor de cálculo de fórmulas y obtener los resultados deseados. Esta enumeración estratifica el manejo de precisión del cálculo. Debido al problema de precisión de la Aritmética de Punto Flotante IEEE 754, algunas fórmulas aparentemente simples pueden no calcularse para dar los resultados esperados, por lo tanto, la última versión de la API ha expuesto los siguientes campos para obtener los resultados deseados según la selección.

1. CalculationPrecisionStrategy.DECIMAL: Utiliza decimales como operandos cuando sea posible, y es el más ineficiente desde el punto de vista del rendimiento.
1. CalculationPrecisionStrategy.ROUND: Redondea los resultados del cálculo según el dígito significativo.
1. CalculationPrecisionStrategy.NONE: No se aplica ninguna estrategia, por lo tanto, durante el cálculo el motor utiliza el valor doble original como operando y devuelve el resultado directamente. Esta opción es la más eficiente y es aplicable para la mayoría de los casos.
### **Métodos Agregados para usar CalculationOptions**
Con el lanzamiento de v8.5.0, la API Aspose.Cells ha agregado versiones sobrecargadas del método calculateFormula como se detalla a continuación.

- Workbook.calculateFormula(CalculationOptions)
- Worksheet.calculateFormula(CalculationOptions options, bool recursive)
- Cell.calculate(CalculationOptions)
### **Se añadió el campo de enumeración PasteType.ROW_HEIGHTS**
Las API de Aspose.Cells han proporcionado el campo de enumeración PasteType.ROW_HEIGHTS con el propósito de copiar las alturas de las filas mientras se copian los rangos. Al establecer la propiedad PasteOptions.PasteType como ((PasteType.ROW_HEIGHTS), las alturas de todas las filas dentro del rango de origen se copiarán al rango de destino.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Source worksheet

Worksheet srcSheet = workbook.getWorksheets().get(0);

//Add destination worksheet

Worksheet dstSheet = workbook.getWorksheets().add("Destination Sheet");

//Set the row height of the 4th row

//This row height will be copied to destination range

srcSheet.getCells().setRowHeight(3, 50);

//Create source range to be copied

Range srcRange = srcSheet.getCells().createRange("A1:D10");

//Create destination range in destination worksheet

Range dstRange = dstSheet.getCells().createRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range

PasteOptions opts = new PasteOptions();

opts.setPasteType(PasteType.ROW_HEIGHTS);

//Copy source range to destination range with paste options

dstRange.copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet

dstSheet.getCells().get("D4").putValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format

workbook.save("output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Se agregó la propiedad SheetRender.PageScale**
Cuando configura el escalado de la configuración de página usando la opción **Ajustar a n página(s) de ancho por m de alto**, Microsoft Excel calcula el factor de escala de la configuración de página. Lo mismo se puede lograr utilizando la propiedad SheetRender.PageScale expuesta por Aspose.Cells for Java 8.5.0. Esta propiedad devuelve un valor doble que se puede convertir a un valor porcentual. Por ejemplo, si devuelve 0.507968245, significa que el factor de escala es del 51%.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some data in these cells

worksheet.getCells().get("A4").putValue("Test");

worksheet.getCells().get("S4").putValue("Test");

//Set paper size

worksheet.getPageSetup().setPaperSize(PaperSizeType.PAPER_A_4);

//Set fit to pages wide as 1

worksheet.getPageSetup().setFitToPagesWide(1);

//Calculate page scale via sheet render

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Write the page scale value

System.out.println(sr.getPageScale());

{{< /highlight >}}
### **Se añadió la enumeración CellValueFormatStrategy**
Aspose.Cells for Java 8.5.0 ha agregado una nueva enumeración CellValueFormatStrategy para manejar situaciones en las que los valores de celda deben extraerse con o sin formato aplicado. La enumeración CellValueFormatStrategy tiene los siguientes campos. 

1. CellValueFormatStrategy.CELL_STYLE: Solo formateado con el formato original de la celda.
1. CellValueFormatStrategy.DISPLAY_STYLE: Formateado con el estilo mostrado de la celda.
1. CellValueFormatStrategy.NONE: Sin formato.
### **Se añadió el método Cell.getStringValue**
Para usar la enumeración CellValueFormatStrategy, v8.5.0 ha expuesto el método Cell.getStringValue que podría aceptar un parámetro de tipo CellValueFormatStrategy y devuelve el valor dependiendo de la opción especificada.

El siguiente fragmento de código muestra cómo usar el método Cells.getStringValue recién expuesto.

**Java**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cell A1

Cell cell = worksheet.getCells().get("A1");

//Put value inside the cell

cell.putValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.getStyle();

style.setNumber(2);

cell.setStyle(style);

//Get string value as Cell Style

String value = cell.getStringValue(CellValueFormatStrategy.CELL_STYLE);

System.out.println(value);

//Get string value without any formatting

value = cell.getStringValue(CellValueFormatStrategy.NONE);

System.out.println(value);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
