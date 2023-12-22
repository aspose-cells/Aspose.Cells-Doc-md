---
title: Calcular fórmulas
description: Este artículo presenta cómo utilizar la biblioteca Aspose.Cells para calcular fórmulas en Microsoft Excel. Al cargar un archivo de Excel existente o crear un nuevo archivo de Excel, podemos usar los métodos proporcionados por Aspose.Cells para calcular la fórmula y obtener el resultado. Finalmente, guardamos el archivo Excel modificado en el disco.
keywords: Aspose.Cells, Excel, formulas, calculations, Direct Calculation of Formula, Calculate Formulas repeatedly, add formulas.
type: docs
weight: 125
url: /es/net/calculate-formulas/
---
##  **Agregar fórmulas y calcular resultados**

Aspose.Cells tiene un motor de cálculo de fórmulas integrado. No solo puede volver a calcular fórmulas importadas desde plantillas de diseñador, sino que también permite calcular los resultados de las fórmulas agregadas en tiempo de ejecución.

 Aspose.Cells admite la mayoría de las fórmulas o funciones que forman parte de Microsoft Excel (Leer[una lista de las funciones soportadas por el motor de cálculo](/cells/es/net/supported-formula-functions/)). Esas funciones se pueden utilizar a través de las API o las hojas de cálculo del diseñador. Aspose.Cells admite un enorme conjunto de fórmulas matemáticas, de cadenas, booleanas, de fecha/hora, estadísticas, de bases de datos, de búsqueda y de referencia.

 Utilizar el[**Fórmula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) propiedad o[**Establecer fórmula (...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2) métodos de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)clase para agregar una fórmula a una celda. Al aplicar una fórmula, siempre comience la cadena con un signo igual (=) como lo hace al crear una fórmula en Microsoft Excel y use una coma (,) para delimitar los parámetros de la función.

 Para calcular los resultados de las fórmulas, el usuario puede llamar al[**CalcularFórmula**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) método de la[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase que procesa todas las fórmulas incrustadas en un archivo de Excel. O bien, el usuario puede llamar al[**CalcularFórmula**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula) método de la[**Hoja de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase que procesa todas las fórmulas incrustadas en una hoja. O bien, el usuario también puede llamar al[**Calcular**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate) método de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)clase que procesa la fórmula de uno Cell:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

###  **Importante saber sobre las fórmulas**

{{% alert color="primary" %}}

 El**Fórmula** propiedad y**Establecer fórmula (...)** métodos de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)trabajo de clase diferente al**Calcular** métodos de la[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) y[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clases. El**Fórmula** propiedad y**Establecer fórmula (...)** Los métodos simplemente agregan la fórmula a una celda pero no calculan el resultado en tiempo de ejecución. Para obtener el resultado de las fórmulas, llame**Calcular** métodos.

{{% /alert %}}

##  **Cálculo directo de fórmula**

Aspose.Cells tiene un motor de cálculo de fórmulas integrado. Además de calcular fórmulas importadas desde un archivo de diseñador, Aspose.Cells puede calcular los resultados de las fórmulas directamente.

A veces, es necesario calcular los resultados de la fórmula directamente sin agregarlos a una hoja de trabajo. Los valores de las celdas utilizadas en la fórmula ya existen en una hoja de cálculo y todo lo que necesita es encontrar el resultado de esos valores basándose en alguna Microsoft fórmula de Excel sin agregar la fórmula en una hoja de cálculo.

 Puede utilizar las API del motor de cálculo de fórmulas Aspose.Cells' para[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) a[**calcular**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) los resultados de tales fórmulas sin agregarlas a la hoja de trabajo:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

El código anterior produce el siguiente resultado:
{{< highlight "net" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

##  **Cómo calcular fórmulas repetidamente**

Cuando hay muchas fórmulas en el libro de trabajo y el usuario necesita calcularlas repetidamente modificando solo una pequeña parte de ellas, puede ser útil para el rendimiento habilitar la cadena de cálculo de fórmulas:[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

###  **Importante saber**

{{% alert color="primary" %}}

Por defecto la cadena de cálculo está deshabilitada. Debido a que crear la cadena también necesita tiempo extra, la primera vez que se calculan fórmulas ([**Libro de trabajo.CalcularFórmula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)) puede consumir más tiempo de procesamiento de CPU y memoria en comparación con fórmulas de cálculo sin cadena. Si el usuario no necesita calcular fórmulas repetidamente, el comportamiento predeterminado (calcular fórmulas directamente sin crear una cadena de cálculo) debería ser la mejor manera.

{{% /alert %}}


##  **Temas avanzados**
- [Agregue Cells a Microsoft Ventana de observación de fórmulas de Excel](/cells/es/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Calculando la función IFNA usando Aspose.Cells](/cells/es/net/calculating-ifna-function-using-aspose-cells/)
- [Cálculo de fórmula matricial de tablas de datos](/cells/es/net/calculation-of-array-formula-of-data-tables/)
- [Cálculo de funciones MINIFS y MAXIFS de Excel 2016](/cells/es/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Disminuya el tiempo de cálculo de Cell. Método de cálculo](/cells/es/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [Detección de referencia circular](/cells/es/net/detecting-circular-reference/)
- [Cálculo directo de una función personalizada sin escribirla en una hoja de trabajo](/cells/es/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementar un motor de cálculo personalizado para ampliar el motor de cálculo predeterminado de Aspose.Cells](/cells/es/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Interrumpir o cancelar el cálculo de la fórmula del libro de trabajo](/cells/es/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Devolver un rango de valores usando AbstractCalculationEngine](/cells/es/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [Devolver un rango de valores usando ICustomFunction](/cells/es/net/returning-a-range-of-values-using-icustomfunction/)
- [Configuración del modo de cálculo de fórmulas del libro de trabajo](/cells/es/net/setting-formula-calculation-mode-of-workbook/)
- [Usando la función FormulaText en Aspose.Cells](/cells/es/net/using-formulatext-function-in-aspose-cells/)
- [Uso de la función ICustomFunction](/cells/es/net/using-icustomfunction-feature/)
