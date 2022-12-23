---
title: Uso de fórmulas o funciones para procesar datos
type: docs
weight: 5
url: /es/java/get-and-set-formula/
---
{{% alert color="primary" %}}

Una de las características atractivas de Microsoft Excel es su capacidad para procesar datos con fórmulas y funciones. Microsoft Excel proporciona un conjunto de funciones y fórmulas integradas que ayudan a los usuarios a realizar cálculos complejos rápidamente. Aspose.Cells también proporciona un gran conjunto de funciones y fórmulas integradas que ayudan a los desarrolladores a calcular valores fácilmente. Aspose.Cells también admite funciones complementarias. Además, Aspose.Cells admite matrices y fórmulas R1C1 en Aspose.Cells.

{{% /alert %}}

## **Uso de fórmulas y funciones**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , que representa un archivo de Excel Microsoft. Él[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) colección que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase. Él[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) recopilación. Cada artículo en el[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) colección representa un objeto de la[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)clase.

 Es posible aplicar fórmulas a las celdas usando propiedades y métodos que ofrece el[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)clase, discutido en más detalle a continuación.

- [Uso de funciones integradas](/cells/es/java/using-formulas-or-functions-to-process-data/#using-built-in-functions).
- [Uso de funciones complementarias](/cells/es/java/using-formulas-or-functions-to-process-data/#using-add-in-functions).
- [Trabajar con fórmulas de matriz](/cells/es/java/using-formulas-or-functions-to-process-data/#using-array-formula).
- [Crear una fórmula R1C1](/cells/es/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula).

## **Uso de funciones integradas**

 Las funciones o fórmulas integradas se proporcionan como funciones listas para usar para reducir los esfuerzos y el tiempo de los desarrolladores. Ver[una lista de funciones integradas](/cells/es/java/supported-formula-functions/). Las funciones se enumeran en orden alfabético. Se admitirán más funciones en el futuro.

 Aspose.Cells admite la mayoría de las fórmulas o funciones que ofrece Microsoft Excel. Los desarrolladores pueden utilizar estas fórmulas a través del API o[hoja de cálculo del diseñador](/cells/es/java/what-is-a-designer-spreadsheet/). Aspose.Cells admite un gran conjunto de fórmulas matemáticas, de cadena, booleanas, de fecha/hora, estadísticas, de base de datos, de búsqueda y de referencia.

 Utilizar el[**Fórmula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)propiedad de la[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) class para agregar una fórmula a una celda.**fórmulas complejas**, por ejemplo

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, también se admiten en Aspose.Cells. Al aplicar una fórmula a una celda, siempre comience la cadena con un signo igual (=) como lo hace al crear una fórmula en Microsoft Excel y use una coma (,) para delimitar los parámetros de la función.

 En el siguiente ejemplo, se aplica una fórmula compleja a la primera celda de una hoja de trabajo.[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) recopilación. La fórmula utiliza un**SI** función proporcionada por Aspose.Cells.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **Uso de funciones complementarias**

 Podemos tener algunas fórmulas definidas por el usuario que queremos incluir como un complemento de Excel. Al configurar el[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) Las funciones incorporadas funcionan bien, sin embargo, es necesario configurar las funciones o fórmulas personalizadas utilizando las funciones complementarias.

 Aspose.Cells proporciona características para registrar funciones adicionales usando[**Hojas de trabajo.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction(java.lang.String,%20java.lang.String,%20boolean)). Luego cuando nos ponemos[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) anyFunctionFromAddIn, el archivo de salida de Excel contiene el valor calculado de la función AddIn.

A continuación, se descargará el archivo XLAM para registrar la función adicional en el código de ejemplo siguiente. De manera similar, el archivo de salida "test_udf.xlsx" se puede descargar para verificar la salida.

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **Uso de la fórmula de matriz**

Las fórmulas de matriz son fórmulas que funcionan con matrices, en lugar de números individuales, como argumentos de las funciones que componen la fórmula. Cuando se muestra una fórmula de matriz, está rodeada por llaves ({}) como se muestra a continuación.

**Establecer una fórmula matricial en la celda G2** 

![todo:imagen_alternativa_texto](using-formulas-or-functions-to-process-data_1.png)

Algunas funciones de Excel Microsoft devuelven matrices de valores. Para calcular varios resultados con una fórmula de matriz, ingrese la matriz en un rango de celdas con el mismo número de filas y columnas que los argumentos de la matriz.

 Es posible aplicar una fórmula de matriz a una celda llamando al[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) clase'[**setArrayFórmula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int) ) método. Él[**setArrayFórmula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int)) método toma los siguientes parámetros:

- **Fórmula de matriz**la fórmula matricial.
- **Número de filas**, el número de filas para completar el resultado de la fórmula de matriz.
- **Número de columnas**, el número de columnas para completar el resultado de la fórmula de matriz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **Usando la fórmula R1C1**

 Aplicar un**R1C1** fórmula de estilo de referencia a una celda con el[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) clase'[**setR1C1Fórmula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula)propiedad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

