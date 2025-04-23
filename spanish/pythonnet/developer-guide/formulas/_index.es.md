---
title: Gestionar fórmulas de archivos de Excel
linktitle: Fórmulas
type: docs
weight: 122
url: /es/python-net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells para Python via .NET puede simplemente obtener, establecer y calcular fórmulas de archivos de Excel.
description: Aprende cómo gestionar las fórmulas de archivos de Excel mediante las APIs Aspose.Cells para Python via .NET para NET.
keywords: Cómo calcular fórmulas en Python, Fórmulas y funciones usando Python, Gestionar funciones incorporadas con Python, Cómo usar funciones complementarias con Python, Cómo usar fórmulas de matriz con Python, Cómo usar fórmulas R1C1 en Python.
---

## **Introducción**

Una de las características más atractivas de Microsoft Excel es su capacidad de procesar datos con fórmulas y funciones. Microsoft Excel proporciona un conjunto de funciones y fórmulas incorporadas que ayudan a los usuarios a realizar cálculos complejos rápidamente. Aspose.Cells para Python via .NET también ofrece un conjunto extenso de funciones y fórmulas integradas que facilitan a los desarrolladores calcular valores. Aspose.Cells para Python via .NET también soporta funciones complementarias. Además, Aspose.Cells para Python via .NET soporta fórmulas de matriz y R1C1.

## **Cómo Usar Fórmulas y Funciones**

Aspose.Cells para Python via .NET provee una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) que permite acceder a cada hoja de cálculo del archivo Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Cada elemento en la colección Cells representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Es posible aplicar fórmulas a celdas utilizando propiedades y métodos ofrecidos por la clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell), discutidos con más detalle a continuación.

- Usar funciones incorporadas.
- Usar funciones de complemento.
- Trabajar con fórmulas de matriz.
- Crear una fórmula R1C1.

## **Cómo Usar Funciones Incorporadas**

Las funciones o fórmulas integradas se proporcionan como funciones listas para usar para reducir el esfuerzo y el tiempo de los desarrolladores. Consulte [una lista de funciones integradas](/cells/es/python-net/supported-formula-functions/) compatibles con Aspose.Cells para Python via .NET. Las funciones aparecen en orden alfabético. Se agregarán más funciones en el futuro.

Aspose.Cells para Python via .NET soporta la mayoría de las fórmulas o funciones ofrecidas por Microsoft Excel. Los desarrolladores pueden usar estas fórmulas a través de la API o [diseñador de hojas de cálculo](/cells/es/net/what-is-a-designer-spreadsheet/). Aspose.Cells para Python via .NET soporta un conjunto enorme de fórmulas matemáticas, de cadenas, Booleanas, de fecha/hora, estadísticas, bases de datos, consultas y referencias.

Utilice la propiedad [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula) de la clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) para agregar una fórmula a una celda. **Las fórmulas complejas**, por ejemplo

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, también son soportadas en Aspose.Cells para Python via .NET. Al aplicar una fórmula a una celda, siempre comience la cadena con un signo igual (=) como cuando crea una fórmula en Microsoft Excel y use una coma (,) para delimitar los parámetros de la función.

En el ejemplo a continuación, se aplica una fórmula compleja a la primera celda de la colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) de una hoja de cálculo. La fórmula usa una función **IF** integrada proporcionada por Aspose.Cells para Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingBuiltinfunction-1.py" >}}

## **Cómo Usar Funciones de Complemento**

Podemos tener algunas fórmulas definidas por el usuario que queremos incluir como un complemento de Excel. Al configurar la función de celda.Formula, las funciones incorporadas funcionan bien, sin embargo, es necesario configurar las funciones o fórmulas personalizadas utilizando las funciones de complemento.

Aspose.Cells para Python via .NET proporciona funciones para registrar add-ins usando [**worksheets.register_add_in_function()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/register_add_in_function). Luego, cuando establecemos cell.Formula = anyFunctionFromAddIn, el archivo de Excel generado contiene el valor calculado de la función AddIn.

A continuación, se deberá descargar el archivo XLAM para registrar la función del complemento en el código de muestra siguiente. De manera similar, el archivo de salida "test_udf.xlsx" se puede descargar para verificar el resultado.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-RegisterAndCallFuncFromAddIn-1.py" >}}

## **Cómo usar fórmulas de matriz**

Las fórmulas de matriz son fórmulas que toman matrices, en lugar de números individuales, como argumentos de las funciones que componen la fórmula. Cuando se muestra una fórmula de matriz, está rodeada por llaves ({}).

Algunas funciones de Microsoft Excel devuelven matrices de valores. Para calcular múltiples resultados con una fórmula de matriz, introduzca la matriz en un rango de celdas con el mismo número de filas y columnas que los argumentos de la matriz.

Es posible aplicar una fórmula de matriz a una celda llamando al método [**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula) de la clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). El método [**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula) toma los siguientes parámetros:

- **Fórmula de matriz**, la fórmula de matriz.
- **Número de filas**, el número de filas para poblar el resultado de la fórmula de matriz.
- **Número de columnas**, el número de columnas para poblar el resultado de la fórmula de matriz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingArrayFunction-1.py" >}}

## **Cómo usar la fórmula de R1C1**

Agregue una fórmula de estilo de referencia **R1C1** a una celda con la propiedad [**r1c1_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/r1c1_formula) de la clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingR1C1-1.py" >}}

## **Temas avanzados**
- [Precedentes y Dependientes](/cells/es/python-net/precedents-and-dependents/)
- [Establecer vínculos externos en fórmulas](/cells/es/python-net/set-external-links-in-formulas/)
- [Propagar fórmula en tabla u objeto de lista automáticamente al ingresar datos en nuevas filas](/cells/es/python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Estableciendo fórmula para rango con nombre](/cells/es/python-net/setting-formula-for-named-range/)
- [Establecer fórmulas - Aviso para usuarios no angloparlantes](/cells/es/python-net/setting-formulas-notice-for-non-english-users/)
- [Establecer fórmula compartida](/cells/es/python-net/setting-shared-formula/)
- [Especificar el número máximo de filas de la fórmula compartida](/cells/es/python-net/specify-maximum-rows-of-shared-formula/)
- [Funciones de Excel soportadas](/cells/es/python-net/supported-formula-functions/)


