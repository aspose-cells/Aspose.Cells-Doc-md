---
title: Calcular Fórmulas
type: docs
weight: 110
url: /es/java/calculate-formulas/
---

## **Agregar fórmulas y calcular resultados**

Aspose.Cells tiene un motor de cálculo de fórmulas incorporado. No solo puede volver a calcular fórmulas importadas desde plantillas de diseño, sino que también admite calcular los resultados de fórmulas agregadas en tiempo de ejecución.

Aspose.Cells admite la mayoría de las funciones o fórmulas que son parte de Microsoft Excel (Lee [una lista de las funciones admitidas por el motor de cálculo](/cells/es/java/supported-formula-functions/)). Estas funciones se pueden utilizar a través de las APIs o las hojas de cálculo del diseñador. Aspose.Cells soporta un amplio conjunto de fórmulas matemáticas, de cadena, booleanas, de fecha/hora, estadísticas, de base de datos, de búsqueda y referencia.

Utilice la propiedad [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) o los métodos [**SetFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setFormula-java.lang.String-com.aspose.cells.FormulaParseOptions-java.lang.Object-) de la clase [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) para agregar una fórmula a una celda. Al aplicar una fórmula, siempre comience la cadena con un signo igual (=) como lo hace al crear una fórmula en Microsoft Excel y use una coma (,) para delimitar los parámetros de función.

Para calcular los resultados de las fórmulas, el usuario puede llamar al [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions--) método de la clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) que procesa todas las fórmulas incrustadas en un archivo de Excel. O, el usuario también puede llamar al método [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula-com.aspose.cells.CalculationOptions-boolean-) de la clase [**Worsheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) que procesa todas las fórmulas en una hoja. También puede llamar al método [**Calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#calculate-com.aspose.cells.CalculationOptions-) de la clase [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) que procesa la fórmula de una Celda:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **Importante saber**

{{% alert color="primary" %}}

La propiedad **Formula** y los métodos **SetFormula(...)** de la clase [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) funcionan de manera diferente a los métodos **Calculate** de las clases [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) y [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell). La propiedad **Formula** y los métodos **SetFormula(...)** simplemente agregan la fórmula a una celda pero no calculan el resultado en tiempo de ejecución. Para obtener el resultado de las fórmulas, por favor llame a los métodos **Calculate**.

{{% /alert %}}

## **Cálculo directo de fórmulas**

Aspose.Cells tiene un motor de cálculo de fórmulas incorporado. Además de calcular las fórmulas importadas de un archivo de diseñador, Aspose.Cells puede calcular directamente los resultados de las fórmulas.

A veces, es necesario calcular directamente los resultados de las fórmulas sin agregarlas a una hoja de cálculo. Los valores de las celdas utilizados en la fórmula ya existen en una hoja de cálculo y todo lo que necesita es encontrar el resultado de esos valores en función de alguna fórmula de Microsoft Excel sin agregar la fórmula en una hoja de cálculo.

Puede utilizar las APIs del motor de cálculo de fórmulas de Aspose.Cells para [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) hasta [**calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula-java.lang.String-com.aspose.cells.CalculationOptions-) los resultados de dichas fórmulas sin agregarlas a la hoja de cálculo:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

El código anterior produce la siguiente salida:
{{< highlight java >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Calculando fórmulas repetidamente**

Cuando hay muchas fórmulas en el libro de trabajo y el usuario necesita calcularlas repetidamente con modificando solo una pequeña parte de ellas, puede ser útil para el rendimiento habilitar la cadena de cálculo de fórmulas: [**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#EnableCalculationChain).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}

### **Importante saber**

{{% alert color="primary" %}}

Por defecto, la cadena de cálculo está deshabilitada. Debido a que crear la cadena también requiere tiempo adicional, la primera vez que se calculan fórmulas ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions--) puede consumir más tiempo de CPU y memoria en comparación con calcular fórmulas sin cadena. Si el usuario no necesita calcular fórmulas repetidamente, el comportamiento predeterminado (calcular la fórmula directamente sin crear la cadena de cálculo) debería ser la mejor opción.

{{% /alert %}}

## **Temas avanzados**
- [Agregar celdas a la ventana de seguimiento de fórmulas de Microsoft Excel](/cells/es/java/add-cells-to-microsoft-excel-formula-watch-window/)
- [Motor de cálculo de fórmulas Aspose.Cells](/cells/es/java/aspose-cells-formula-calculation-engine/)
- [Cálculo de la función IFNA utilizando Aspose.Cells](/cells/es/java/calculating-ifna-function-using-aspose-cells/)
- [Cálculo de fórmulas de matriz de tablas de datos](/cells/es/java/calculation-of-array-formula-of-data-tables/)
- [Cálculo de las funciones MINIFS y MAXIFS de Excel 2016](/cells/es/java/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Reducir el tiempo de cálculo del método Cell.Calculate](/cells/es/java/decrease-the-calculation-time-of-cell-calculate-method/)
- [Detección de referencia circular](/cells/es/java/detecting-circular-reference/)
- [Cálculo directo de una función personalizada sin escribirla en una hoja de cálculo](/cells/es/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementar un motor de cálculo personalizado para extender el motor de cálculo predeterminado de Aspose.Cells](/cells/es/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Interrumpir o cancelar el cálculo de fórmulas de una hoja de cálculo](/cells/es/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Devolver un rango de valores utilizando AbstractCalculationEngine](/cells/es/java/returning-a-range-of-values-using-abstractcalculationengine/)
- [Devolver un rango de valores utilizando ICustomFunction](/cells/es/java/returning-a-range-of-values-using-icustomfunction/)
- [Usar la función ICustomFunction](/cells/es/java/using-icustomfunction-feature/)
{{< app/cells/assistant language="java" >}}
