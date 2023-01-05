---
title: Administrar fórmulas de archivos de Excel
linktitle: Fórmulas
type: docs
weight: 122
url: /es/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells puede simplemente obtener, configurar y calcular fórmulas de archivos de Excel.
---
## **Introducción**

Una de las atractivas características de Microsoft Excel es su capacidad para procesar datos con fórmulas y funciones. Microsoft Excel proporciona un conjunto de funciones y fórmulas integradas que ayudan a los usuarios a realizar cálculos complejos rápidamente. Aspose.Cells también proporciona un gran conjunto de funciones y fórmulas integradas que ayudan a los desarrolladores a calcular valores fácilmente. Aspose.Cells también admite funciones complementarias. Además, Aspose.Cells admite matrices y fórmulas R1C1 en Aspose.Cells.

## **Uso de fórmulas y funciones**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel Microsoft. Él[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. Él[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. Cada elemento de la colección Cells representa un objeto de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clase.

 Es posible aplicar fórmulas a las celdas usando propiedades y métodos que ofrece el[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clase, discutido en más detalle a continuación.

- Uso de funciones integradas.
- Uso de funciones complementarias.
- Trabajar con fórmulas matriciales.
- Creación de una fórmula R1C1.

## **Uso de funciones integradas**

 Las funciones o fórmulas integradas se proporcionan como funciones listas para usar para reducir los esfuerzos y el tiempo de los desarrolladores. Ver[una lista de funciones integradas](/cells/es/net/supported-formula-functions/) compatible con Aspose.Cells. Las funciones se enumeran en orden alfabético. Se admitirán más funciones en el futuro.

 Aspose.Cells admite la mayoría de las fórmulas o funciones que ofrece Microsoft Excel. Los desarrolladores pueden utilizar estas fórmulas a través del API o[hoja de cálculo del diseñador](/cells/es/net/what-is-a-designer-spreadsheet/). Aspose.Cells admite un gran conjunto de fórmulas matemáticas, de cadena, booleanas, de fecha/hora, estadísticas, de base de datos, de búsqueda y de referencia.

 Utilizar el[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clase'[**Fórmula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)propiedad para agregar una fórmula a una celda.**fórmulas complejas**, por ejemplo

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, también se admiten en Aspose.Cells. Al aplicar una fórmula a una celda, siempre comience la cadena con un signo igual (=) como lo hace al crear una fórmula en Microsoft Excel y use una coma (,) para delimitar los parámetros de la función.

 En el siguiente ejemplo, se aplica una fórmula compleja a la primera celda de una hoja de trabajo.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) recopilación. La fórmula utiliza un**SI** función proporcionada por Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **Uso de funciones complementarias**

Podemos tener algunas fórmulas definidas por el usuario que queremos incluir como un complemento de Excel. Al configurar la función cell.Formula, las funciones integradas funcionan bien; sin embargo, es necesario configurar las funciones o fórmulas personalizadas utilizando las funciones complementarias.

 Aspose.Cells proporciona características para registrar funciones adicionales usando[**Hojas de trabajo.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). Luego, cuando configuramos cell.Formula = anyFunctionFromAddIn, el archivo de salida de Excel contiene el valor calculado de la función AddIn.

Se descargará el siguiente archivo XLAM para registrar la función de complemento en el siguiente código de ejemplo. De manera similar, el archivo de salida "test_udf.xlsx" se puede descargar para verificar la salida.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **Uso de la fórmula de matriz**

Las fórmulas de matriz son fórmulas que toman matrices, en lugar de números individuales, como argumentos para las funciones que componen la fórmula. Cuando se muestra una fórmula de matriz, está rodeada por llaves ({}).

Algunas funciones de Excel Microsoft devuelven matrices de valores. Para calcular varios resultados con una fórmula de matriz, ingrese la matriz en un rango de celdas con el mismo número de filas y columnas que los argumentos de la matriz.

 Es posible aplicar una fórmula de matriz a una celda llamando al[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clase'[**EstablecerArrayFórmula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) método. Él[**EstablecerArrayFórmula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) método toma los siguientes parámetros:

- **Fórmula de matriz**la fórmula matricial.
- **Número de filas**, el número de filas para completar el resultado de la fórmula de matriz.
- **Número de columnas**el número de columnas para completar el resultado de la fórmula de matriz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **Usando la fórmula R1C1**

 Añadir un**R1C1** fórmula de estilo de referencia a una celda con el[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clase'[**R1C1Fórmula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **Temas avanzados**
- [Precedentes y dependientes](/cells/es/net/precedents-and-dependents/)
- [Establecer enlaces externos en fórmulas](/cells/es/net/set-external-links-in-formulas/)
- [Propague la fórmula en la tabla o el objeto de la lista automáticamente al ingresar datos en nuevas filas](/cells/es/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Configuración de la fórmula para el rango con nombre](/cells/es/net/setting-formula-for-named-range/)
- [Configuración de fórmulas - Aviso para usuarios que no hablan inglés](/cells/es/net/setting-formulas-notice-for-non-english-users/)
- [Configuración de fórmula compartida](/cells/es/net/setting-shared-formula/)
- [Especificar filas máximas de fórmula compartida](/cells/es/net/specify-maximum-rows-of-shared-formula/)
- [Funciones de Excel compatibles](/cells/es/net/supported-formula-functions/)

