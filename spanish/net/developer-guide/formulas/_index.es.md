---
title: Administrar fórmulas de archivos de Excel.
linktitle: Fórmulas
type: docs
weight: 122
url: /es/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells puede simplemente obtener, configurar y calcular fórmulas de archivos de Excel.
description: Aprenda a administrar fórmulas de archivos de Excel a través de las API Aspose.Cells para NET.
keywords: How to calculate formulas in C#, Formulas and Functions using C#, C# Manage Built-in Functions, How to Use Add-in Functions with C#, How to Use Array Formula via C#, How to Use R1C1 Formula in C#.
---
##  **Introducción**

Una de las características atractivas de Microsoft Excel es su capacidad para procesar datos con fórmulas y funciones. Microsoft Excel proporciona un conjunto de funciones y fórmulas integradas que ayudan a los usuarios a realizar cálculos complejos rápidamente. Aspose.Cells también proporciona un enorme conjunto de funciones y fórmulas integradas que ayudan a los desarrolladores a calcular valores fácilmente. Aspose.Cells también admite funciones complementarias. Además, Aspose.Cells admite fórmulas de matriz y R1C1 en Aspose.Cells.

##  **Cómo utilizar fórmulas y funciones**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo Excel Microsoft. El[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de cálculo del archivo Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. El[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. Cada artículo de la colección Cells representa un objeto de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clase.

 Es posible aplicar fórmulas a celdas usando propiedades y métodos ofrecidos por el[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clase, que se analiza con más detalle a continuación.

- Usando funciones integradas.
- Usando funciones complementarias.
- Trabajar con fórmulas matriciales.
- Creando una fórmula R1C1.

##  **Cómo utilizar las funciones integradas**

Las funciones o fórmulas integradas se proporcionan como funciones listas para usar para reducir el esfuerzo y el tiempo de los desarrolladores. Ver[una lista de funciones integradas](/cells/es/net/supported-formula-functions/) compatible con Aspose.Cells. Las funciones se enumeran en orden alfabético. En el futuro se admitirán más funciones.

 Aspose.Cells admite la mayoría de las fórmulas o funciones que ofrece Microsoft Excel. Los desarrolladores pueden utilizar estas fórmulas a través del API o[hoja de cálculo del diseñador](/cells/es/net/what-is-a-designer-spreadsheet/). Aspose.Cells admite un enorme conjunto de fórmulas matemáticas, de cadenas, booleanas, de fecha/hora, estadísticas, de bases de datos, de búsqueda y de referencia.

 Utilizar el[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clase'[**Fórmula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) propiedad para agregar una fórmula a una celda. *Fórmulas complejas**, por ejemplo

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, también son compatibles con Aspose.Cells. Al aplicar una fórmula a una celda, siempre comience la cadena con un signo igual (=) como lo hace al crear una fórmula en Microsoft Excel y use una coma (,) para delimitar los parámetros de la función.

 En el siguiente ejemplo, se aplica una fórmula compleja a la primera celda de una hoja de cálculo.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)recopilación. La fórmula utiliza un incorporado**IF** función proporcionada por Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

##  **Cómo utilizar funciones complementarias**

Podemos tener algunas fórmulas definidas por el usuario que queremos incluir como complemento de Excel. Al configurar la función cell.Formula, las funciones integradas funcionan bien, sin embargo, es necesario configurar las funciones o fórmulas personalizadas utilizando las funciones complementarias.

 Aspose.Cells proporciona funciones para registrar funciones adicionales utilizando[**Hojas de trabajo.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). Luego, cuando configuramos cell.Formula = anyFunctionFromAddIn, el archivo de Excel de salida contiene el valor calculado de la función AddIn.

Se descargará el siguiente archivo XLAM para registrar la función complementaria en el siguiente código de muestra. De manera similar, se puede descargar el archivo de salida "test_udf.xlsx" para verificar el resultado.

[PruebaUDF.xlam](81920908.xlam)

[prueba_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

##  **Cómo utilizar la fórmula matricial**

Las fórmulas matriciales son fórmulas que toman matrices, en lugar de números individuales, como argumentos para las funciones que componen la fórmula. Cuando se muestra una fórmula matricial, está rodeada de llaves ({}).

Algunas funciones de Excel Microsoft devuelven matrices de valores. Para calcular varios resultados con una fórmula matricial, ingrese la matriz en un rango de celdas con el mismo número de filas y columnas que los argumentos de la matriz.

 Es posible aplicar una fórmula matricial a una celda llamando al[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clase'[**Establecer matriz de fórmula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) método. El[**Establecer matriz de fórmula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) El método toma los siguientes parámetros:

- *Fórmula de matriz**, la fórmula de matriz.
- *Número de filas**, el número de filas para completar el resultado de la fórmula matricial.
- *Número de columnas**, el número de columnas para completar el resultado de la fórmula matricial.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

##  **Cómo utilizar la fórmula R1C1**

 Añadir un**R1C1** fórmula de estilo de referencia a una celda con el[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clase'[**Fórmula R1C1**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

##  **Temas avanzados**
- [Precedentes y dependientes](/cells/es/net/precedents-and-dependents/)
- [Establecer enlaces externos en fórmulas](/cells/es/net/set-external-links-in-formulas/)
- [Propague la fórmula en una tabla o un objeto de lista automáticamente mientras ingresa datos en nuevas filas](/cells/es/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Configuración de fórmula para rango con nombre](/cells/es/net/setting-formula-for-named-range/)
- [Configuración de fórmulas: aviso para usuarios que no hablan inglés](/cells/es/net/setting-formulas-notice-for-non-english-users/)
- [Configuración de fórmula compartida](/cells/es/net/setting-shared-formula/)
- [Especificar filas máximas de fórmula compartida](/cells/es/net/specify-maximum-rows-of-shared-formula/)
- [Funciones de Excel compatibles](/cells/es/net/supported-formula-functions/)

