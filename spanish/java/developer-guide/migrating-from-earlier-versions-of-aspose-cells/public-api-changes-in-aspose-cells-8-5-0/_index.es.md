---
title: Público API Cambios en Aspose.Cells 8.5.0
type: docs
weight: 170
url: /es/java/public-api-changes-in-aspose-cells-8-5-0/
---
{{% alert color="primary" %}} 

 Este documento describe los cambios al Aspose.Cells API de la versión 8.4.2 a la 8.5.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados,[Clases añadidas, etc.](/cells/es/java/public-api-changes-in-aspose-cells-8-5-0/), pero también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Se cambiaron los parámetros de ICustomFunction.CalculateCustomFunction**
Si un parámetro para la función personalizada es la referencia de celda, en la versión anterior Aspose.Cells, las API se usaban para convertir la referencia de celda en un valor de celda o una matriz de objetos de todos los valores de celda en el área referida. Sin embargo, para muchas funciones y usuarios, no se requiere la matriz de valores de celda para todas las celdas en el área referida, solo necesitan una sola celda correspondiente a la posición de la fórmula, o solo necesitan la referencia en sí misma en lugar del valor de celda o la matriz de valores. . En algunas situaciones, obtener todos los valores de las celdas incluso aumentó el riesgo de error de referencia circular.

Para admitir este tipo de requisito, Aspose.Cells for Java 8.5.0 ha cambiado el valor del parámetro a "paramsList" para el área referida. Desde v8.5.0, API simplemente coloca el objeto ReferedArea en "paramsList" cuando el parámetro correspondiente es una referencia o su resultado calculado es una referencia. Si necesita la referencia en sí, puede usar ReferedArea directamente. Si necesita obtener un valor de una sola celda de la referencia correspondiente a la posición de la fórmula, puede usar el método ReferedArea.getValue(rowOffset, int colOffset). Si necesita una matriz de valores de celda para toda el área, puede usar el método ReferedArea.getValues.

Ahora, como Aspose.Cells for Java 8.5.0 proporciona ReferredArea en "paramsList", ReferredAreaCollection en "contextObjects" ya no será necesaria (en versiones anteriores, no siempre podía dar un mapa uno a uno a los parámetros de la función personalizada), por lo que esta versión también lo ha eliminado de "contextObjects" ahora.

Este cambio requiere cambios en el código de la implementación de ICustomFunction cuando necesite el valor o los valores del parámetro de referencia.

**Implementación antigua**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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
### **Se agregaron opciones de cálculo de clase**
 Aspose.Cells for Java 8.5.0 ha expuesto la clase CalculationOptions para agregar más flexibilidad y extensibilidad para el motor de cálculo de fórmulas. La clase recién agregada tiene las siguientes propiedades.

1. CalculationOptions.CalcStackSize: especificó el tamaño de pila para calcular celdas recursivamente. -1 especifica que el cálculo usará WorkbookSettings.CalcStackSize del libro de trabajo correspondiente.
1. CalculationOptions.CustomFunction: amplía el motor de cálculo de fórmulas con una fórmula personalizada.
1. CalculationOptions.IgnoreError: el valor de tipo booleano indica si los errores deben ocultarse al calcular las fórmulas, donde los errores podrían deberse a la función no compatible, enlace externo o más.
1. CalculationOptions.PrecisionStrategy: valor de tipo CalculationPrecisionStrategy que especifica la estrategia para procesar la precisión del cálculo.
### **Cálculo de enumeraciónEstrategia de precisión añadida**
Aspose.Cells for Java 8.5.0 ha expuesto la enumeración CalculationPrecisionStrategy para agregar más flexibilidad al motor de cálculo de fórmulas para obtener los resultados deseados. Esta enumeración planea el manejo de precisión de cálculo. Debido al problema de precisión de la aritmética de punto flotante IEEE 754, es posible que algunas fórmulas aparentemente simples no se calculen para dar los resultados esperados, por lo tanto, la última compilación API ha expuesto los siguientes campos para obtener los resultados deseados de acuerdo con la selección.

1. CalculationPrecisionStrategy.DECIMAL: utiliza decimal como operando siempre que sea posible y es más ineficaz por consideraciones de rendimiento.
1. CalculationPrecisionStrategy.ROUND: redondea los resultados del cálculo según el dígito significativo.
1. CalculationPrecisionStrategy.NONE: No se aplica ninguna estrategia, por lo tanto, durante el cálculo, el motor utiliza el valor doble original como operando y devuelve el resultado directamente. Esta opción es la más eficiente y es aplicable para la mayoría de los casos.
### **Métodos agregados para usar CalculationOptions**
Con el lanzamiento de v8.5.0, el Aspose.Cells API ha agregado versiones de sobrecarga del método de cálculo de fórmula como se indica a continuación.

- Workbook.calculateFormula(CalculationOptions)
- Worksheet.calculateFormula(opciones de CalculationOptions, booleano recursivo)
- Cell.calculate(Opciones de cálculo)
### **Campo de enumeración PasteType.ROW_HEIGHTS agregado**
Aspose.Cells Las API han proporcionado PasteType.ROW_HEIGHTS campo de enumeración con el propósito de copiar las alturas de las filas mientras se copian los rangos. Al establecer la propiedad PasteOptions.PasteType en ((PasteType.ROW_ALTURAS}} las alturas de todas las filas dentro del rango de origen se copiarán en el rango de destino.

**Java**

{{< highlight "csharp" >}}

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
### **Propiedad SheetRender.PageScale agregado**
Cuando configura Ajuste de escala de página usando**Ajustar a n página(s) de ancho por m de alto** opción, Microsoft Excel calcula el factor de escala de configuración de página. Se puede lograr lo mismo usando la propiedad SheetRender.PageScale expuesta por Aspose.Cells for Java 8.5.0. Esta propiedad devuelve un valor doble que se puede convertir en un valor porcentual. Por ejemplo, si devuelve 0,507968245, significa que el factor de escala es del 51 %.

**Java**

{{< highlight "csharp" >}}

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
### **Enumeración CellValueFormatStrategy Agregado**
 Aspose.Cells for Java 8.5.0 ha agregado una nueva enumeración CellValueFormatStrategy para manejar situaciones en las que los valores de celda deben extraerse con o sin formato aplicado. La enumeración CellValueFormatStrategy tiene los siguientes campos.

1. CellValueFormatStrategy.CELL_STYLE: Solo formateado con el formato original de la celda.
1. CellValueFormatStrategy.DISPLAY_STYLE: formateado con el estilo mostrado de la celda.
1. CellValueFormatStrategy.NONE: Sin formato.
### **Método Cell.getStringValue agregado**
Para usar la enumeración CellValueFormatStrategy, v8.5.0 ha expuesto el método Cell.getStringValue que podría aceptar un parámetro de tipo CellValueFormatStrategy y devuelve el valor que depende de la opción especificada.

El siguiente fragmento de código muestra cómo usar el método Cells.getStringValue recién expuesto.

**Java**

{{< highlight "csharp" >}}

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
