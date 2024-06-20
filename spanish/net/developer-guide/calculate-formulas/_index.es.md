---
title: Calcular Fórmulas
description: Este artículo introduce cómo utilizar la biblioteca Aspose.Cells para calcular fórmulas en Microsoft Excel. Al cargar un archivo de Excel existente o crear un nuevo archivo de Excel, podemos utilizar los métodos proporcionados por Aspose.Cells para calcular la fórmula y obtener el resultado. Finalmente, guardamos el archivo de Excel modificado en el disco.
keywords: Aspose.Cells, Excel, fórmulas, cálculos, Cálculo Directo de Fórmula, Calcular Fórmulas repetidamente, agregar fórmulas.
type: docs
weight: 125
url: /es/net/calculate-formulas/
---

## **Agregar fórmulas y calcular resultados**

Aspose.Cells tiene un motor de cálculo de fórmulas incorporado. No solo puede volver a calcular fórmulas importadas desde plantillas de diseño, sino que también admite calcular los resultados de fórmulas agregadas en tiempo de ejecución.

Aspose.Cells admite la mayoría de las fórmulas o funciones que forman parte de Microsoft Excel(Leer [una lista de las funciones compatibles con el motor de cálculo](/cells/es/net/supported-formula-functions/)). Esas funciones se pueden utilizar a través de las APIs o las hojas de cálculo de diseñador. Aspose.Cells admite un amplio conjunto de fórmulas matemáticas, de cadena, booleanas, de fecha/hora, estadísticas, de base de datos, de búsqueda y de referencia.

Utilice la propiedad [**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) o los métodos [**SetFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2) de la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) para agregar una fórmula a una celda. Al aplicar una fórmula, siempre comience la cadena con un signo igual (=) como lo hace al crear una fórmula en Microsoft Excel y use una coma (,) para delimitar los parámetros de función.

Para calcular los resultados de las fórmulas, el usuario puede llamar al método [**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que procesa todas las fórmulas incrustadas en un archivo de Excel. O, el usuario puede llamar al método [**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula) de la clase [**Worsheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) que procesa todas las fórmulas incrustadas en una hoja. O, el usuario también puede llamar al método [**Calculate**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate) de la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) que procesa la fórmula de una celda:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

### **Importante saber para las Fórmulas**

{{% alert color="primary" %}}

La propiedad **Formula** y los métodos **SetFormula(...)** de la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) funcionan de manera diferente a los métodos **Calculate** de las clases [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) y [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). La propiedad **Formula** y los métodos **SetFormula(...)** simplemente agregan la fórmula a una celda pero no calculan el resultado en tiempo de ejecución. Para obtener el resultado de las fórmulas, por favor llame a los métodos **Calculate**.

{{% /alert %}}

## **Cálculo directo de fórmulas**

Aspose.Cells tiene un motor de cálculo de fórmulas incorporado. Además de calcular las fórmulas importadas de un archivo de diseñador, Aspose.Cells puede calcular directamente los resultados de las fórmulas.

A veces, es necesario calcular directamente los resultados de las fórmulas sin agregarlas a una hoja de cálculo. Los valores de las celdas utilizados en la fórmula ya existen en una hoja de cálculo y todo lo que necesita es encontrar el resultado de esos valores en función de alguna fórmula de Microsoft Excel sin agregar la fórmula en una hoja de cálculo.

Puede utilizar las APIs del motor de cálculo de fórmulas de Aspose.Cells para [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) hasta [**calculate**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) los resultados de dichas fórmulas sin agregarlas a la hoja de cálculo:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

El código anterior produce la siguiente salida:
{{< highlight net >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Cómo Calcular Fórmulas repetidamente**

Cuando hay muchas fórmulas en el libro de trabajo y el usuario necesita calcularlas repetidamente con modificando solo una pequeña parte de ellas, puede ser útil para el rendimiento habilitar la cadena de cálculo de fórmulas: [**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

### **Importante saber**

{{% alert color="primary" %}}

De forma predeterminada, la cadena de cálculo está deshabilitada. Debido a que crear la cadena también necesita tiempo adicional, la primera vez que se calculan fórmulas ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)) puede consumir más tiempo de procesamiento de CPU y memoria en comparación con el cálculo de fórmulas sin cadena. Si el usuario no necesita calcular fórmulas repetidamente, el comportamiento predeterminado (calcular la fórmula directamente sin crear una cadena de cálculo) debería ser la mejor manera.

{{% /alert %}}


## **Temas avanzados**
- [Agregar celdas a la ventana de seguimiento de fórmulas de Microsoft Excel](/cells/es/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Cálculo de la función IFNA utilizando Aspose.Cells](/cells/es/net/calculating-ifna-function-using-aspose-cells/)
- [Cálculo de fórmulas de matriz de tablas de datos](/cells/es/net/calculation-of-array-formula-of-data-tables/)
- [Cálculo de las funciones MINIFS y MAXIFS de Excel 2016](/cells/es/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Reducir el tiempo de cálculo del método Cell.Calculate](/cells/es/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [Detección de referencia circular](/cells/es/net/detecting-circular-reference/)
- [Cálculo directo de una función personalizada sin escribirla en una hoja de cálculo](/cells/es/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementar un motor de cálculo personalizado para extender el motor de cálculo predeterminado de Aspose.Cells](/cells/es/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Interrumpir o cancelar el cálculo de fórmulas de una hoja de cálculo](/cells/es/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Devolver un rango de valores utilizando AbstractCalculationEngine](/cells/es/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [Devolver un rango de valores utilizando ICustomFunction](/cells/es/net/returning-a-range-of-values-using-icustomfunction/)
- [Configurar el modo de cálculo de fórmulas de una hoja de cálculo](/cells/es/net/setting-formula-calculation-mode-of-workbook/)
- [Usando la función FormulaText en Aspose.Cells](/cells/es/net/using-formulatext-function-in-aspose-cells/)
- [Usar la función ICustomFunction](/cells/es/net/using-icustomfunction-feature/)
