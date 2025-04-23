---
title: Uso de fórmulas o funciones para procesar datos
type: docs
weight: 5
url: /es/java/get-and-set-formula/
---

{{% alert color="primary" %}}

Una de las características más atractivas de Microsoft Excel es su capacidad para procesar datos con fórmulas y funciones. Microsoft Excel proporciona un conjunto de funciones y fórmulas incorporadas que ayudan a los usuarios a realizar cálculos complejos rápidamente. Aspose.Cells también proporciona un gran conjunto de funciones y fórmulas incorporadas que ayudan a los desarrolladores a calcular valores fácilmente. Aspose.Cells también admite funciones de complemento. Además, Aspose.Cells admite fórmulas de matriz y R1C1 en Aspose.Cells.

{{% /alert %}}

## **Uso de fórmulas y funciones**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Es posible aplicar fórmulas a celdas utilizando propiedades y métodos ofrecidos por la clase [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell), discutidos con más detalle a continuación.

- [Uso de funciones incorporadas](/cells/es/java/using-formulas-or-functions-to-process-data/#using-built-in-functions).
- [Uso de funciones de complemento](/cells/es/java/using-formulas-or-functions-to-process-data/#using-add-in-functions).
- [Trabajar con fórmulas de matriz](/cells/es/java/using-formulas-or-functions-to-process-data/#using-array-formula).
- [Creación de una fórmula R1C1](/cells/es/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula).

## **Uso de funciones incorporadas**

Las funciones incorporadas o fórmulas se proporcionan como funciones predefinidas para reducir los esfuerzos y el tiempo de los desarrolladores. Consulte [una lista de funciones incorporadas](/cells/es/java/supported-formula-functions/). Las funciones están listadas en orden alfabético. Se admitirán más funciones en el futuro.

Aspose.Cells admite la mayoría de las fórmulas o funciones ofrecidas por Microsoft Excel. Los desarrolladores pueden usar estas fórmulas a través del API o [hoja de cálculo del diseñador](/cells/es/java/what-is-a-designer-spreadsheet/). Aspose.Cells admite un gran conjunto de fórmulas matemáticas, de cadena, booleanas, de fecha/hora, estadísticas, de base de datos, búsqueda y referencia.

Utilice la propiedad [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) de la clase [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) para agregar una fórmula a una celda. **También se admiten fórmulas complejas**, por ejemplo

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, también son compatibles en Aspose.Cells. Al aplicar una fórmula a una celda, siempre comience la cadena con un signo igual (=) como lo hace al crear una fórmula en Microsoft Excel y use una coma (,) para delimitar los parámetros de la función.

En el ejemplo a continuación, se aplica una fórmula compleja a la primera celda de la colección de la hoja de cálculo [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). La fórmula utiliza una función **SI** incorporada proporcionada por Aspose.Cells.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **Usando Funciones de Complemento**

Podemos tener algunas fórmulas definidas por el usuario que queremos incluir como un complemento de Excel. Cuando se establece la función [**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula), las funciones incorporadas funcionan bien, sin embargo, hay necesidad de establecer las funciones o fórmulas personalizadas utilizando las funciones del complemento.

Aspose.Cells proporciona características para registrar funciones de complemento usando [**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction-java.lang.String-java.lang.String-boolean-). Después, cuando configuramos [**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) = anyFunctionFromAddIn, el archivo de Excel de salida contiene el valor calculado de la función de complemento.

A continuación, se descargará el archivo XLAM para registrar la función de complemento en el siguiente código de ejemplo. De manera similar, el archivo de salida "test_udf.xlsx" se puede descargar para verificar el resultado.

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **Usando Fórmula de Matriz**

Las fórmulas de matriz son fórmulas que trabajan con arreglos, en lugar de números individuales, como argumentos de las funciones que componen la fórmula. Cuando se muestra una fórmula de matriz, está rodeada por llaves ({}) como se muestra a continuación.

**Estableciendo una fórmula de matriz en la celda G2** 

![todo:image_alt_text](using-formulas-or-functions-to-process-data_1.png)

Algunas funciones de Microsoft Excel devuelven matrices de valores. Para calcular múltiples resultados con una fórmula de matriz, introduzca la matriz en un rango de celdas con el mismo número de filas y columnas que los argumentos de la matriz.

Es posible aplicar una fórmula de matriz a una celda llamando al método [**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula-java.lang.String-int-int-) de la clase [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell). El método [**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula-java.lang.String-int-int-) recibe los siguientes parámetros:

- **Fórmula de matriz**, la fórmula de matriz.
- **Número de filas**, el número de filas para poblar el resultado de la fórmula de matriz.
- **Número de Columnas**, el número de columnas para poblar el resultado de la fórmula de matriz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **Usando Fórmula R1C1**

Aplicar una fórmula con estilo de referencia **R1C1** a una celda con la propiedad [**setR1C1Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula) de la clase [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

{{< app/cells/assistant language="java" >}}
