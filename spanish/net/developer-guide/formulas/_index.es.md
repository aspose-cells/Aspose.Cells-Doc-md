---
title: Gestionar fórmulas de archivos de Excel
linktitle: Fórmulas
type: docs
weight: 122
url: /es/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells puede simplemente obtener, establecer y calcular fórmulas de archivos de Excel.
description: Aprenda cómo administrar fórmulas de archivos de Excel a través de las API de Aspose.Cells for NET.
keywords: Cómo calcular fórmulas en C#, Fórmulas y Funciones usando C#, C# Administrar Funciones Incorporadas, Cómo Usar Funciones de Complemento con C#, Cómo Usar Fórmula de Matriz a través de C#, Cómo Usar Fórmula R1C1 en C#.
---

## **Introducción**

Una de las características más atractivas de Microsoft Excel es su capacidad para procesar datos con fórmulas y funciones. Microsoft Excel proporciona un conjunto de funciones y fórmulas integradas que ayudan a los usuarios a realizar cálculos complejos rápidamente. Aspose.Cells también proporciona un gran conjunto de funciones y fórmulas integradas que ayudan a los desarrolladores a calcular valores fácilmente. Aspose.Cells también admite funciones de complemento. Además, Aspose.Cells admite fórmulas de matriz y R1C1 en Aspose.Cells.

## **Cómo Usar Fórmulas y Funciones**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite el acceso a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Cada elemento en la colección Cells representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Es posible aplicar fórmulas a celdas utilizando propiedades y métodos ofrecidos por la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell), discutidos con más detalle a continuación.

- Usar funciones incorporadas.
- Usar funciones de complemento.
- Trabajar con fórmulas de matriz.
- Crear una fórmula R1C1.

## **Cómo Usar Funciones Incorporadas**

Las funciones o fórmulas incorporadas se proporcionan como funciones listas para reducir los esfuerzos y el tiempo de los desarrolladores. Consulte [una lista de funciones incorporadas](/cells/es/net/supported-formula-functions/) admitidas por Aspose.Cells. Las funciones se enumeran en orden alfabético. Se admitirán más funciones en el futuro.

Aspose.Cells admite la mayoría de las fórmulas o funciones ofrecidas por Microsoft Excel. Los desarrolladores pueden utilizar estas fórmulas a través de la API o el [diseñador de hojas de cálculo](/cells/es/net/what-is-a-designer-spreadsheet/). Aspose.Cells admite un gran conjunto de fórmulas matemáticas, de cadena, booleanas, de fecha/hora, estadísticas, de base de datos, de búsqueda y referencia.

Utilice la propiedad [**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) de la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) para agregar una fórmula a una celda. **Las fórmulas complejas**, por ejemplo

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, también son compatibles en Aspose.Cells. Al aplicar una fórmula a una celda, siempre comience la cadena con un signo igual (=) como lo hace al crear una fórmula en Microsoft Excel y use una coma (,) para delimitar los parámetros de la función.

En el ejemplo a continuación, se aplica una fórmula compleja a la primera celda de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) de la hoja de cálculo. La fórmula utiliza una función integrada de **SI** proporcionada por Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **Cómo Usar Funciones de Complemento**

Podemos tener algunas fórmulas definidas por el usuario que queremos incluir como un complemento de Excel. Al configurar la función de celda.Formula, las funciones incorporadas funcionan bien, sin embargo, es necesario configurar las funciones o fórmulas personalizadas utilizando las funciones de complemento.

Aspose.Cells proporciona funciones para registrar funciones de complemento utilizando [**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). Posteriormente, cuando establecemos cell.Formula = anyFunctionFromAddIn, el archivo de Excel de salida contiene el valor calculado de la función de complemento.

A continuación, se deberá descargar el archivo XLAM para registrar la función del complemento en el código de muestra siguiente. De manera similar, el archivo de salida "test_udf.xlsx" se puede descargar para verificar el resultado.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **Cómo usar fórmulas de matriz**

Las fórmulas de matriz son fórmulas que toman matrices, en lugar de números individuales, como argumentos de las funciones que componen la fórmula. Cuando se muestra una fórmula de matriz, está rodeada por llaves ({}).

Algunas funciones de Microsoft Excel devuelven matrices de valores. Para calcular múltiples resultados con una fórmula de matriz, introduzca la matriz en un rango de celdas con el mismo número de filas y columnas que los argumentos de la matriz.

Es posible aplicar una fórmula de matriz a una celda llamando al método [**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) de la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). El método [**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) toma los siguientes parámetros:

- **Fórmula de matriz**, la fórmula de matriz.
- **Número de filas**, el número de filas para poblar el resultado de la fórmula de matriz.
- **Número de columnas**, el número de columnas para poblar el resultado de la fórmula de matriz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **Cómo usar la fórmula de R1C1**

Agregue una fórmula de estilo de referencia **R1C1** a una celda con la propiedad [**R1C1Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) de la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **Temas avanzados**
- [Precedentes y Dependientes](/cells/es/net/precedents-and-dependents/)
- [Establecer vínculos externos en fórmulas](/cells/es/net/set-external-links-in-formulas/)
- [Propagar fórmula en tabla u objeto de lista automáticamente al ingresar datos en nuevas filas](/cells/es/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Estableciendo fórmula para rango con nombre](/cells/es/net/setting-formula-for-named-range/)
- [Establecer fórmulas - Aviso para usuarios no angloparlantes](/cells/es/net/setting-formulas-notice-for-non-english-users/)
- [Establecer fórmula compartida](/cells/es/net/setting-shared-formula/)
- [Especificar el número máximo de filas de la fórmula compartida](/cells/es/net/specify-maximum-rows-of-shared-formula/)
- [Funciones de Excel soportadas](/cells/es/net/supported-formula-functions/)

