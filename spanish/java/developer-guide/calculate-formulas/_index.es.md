---
title: Calcular fórmulas
type: docs
weight: 110
url: /es/java/calculate-formulas/
---
## **Adición de fórmulas y cálculo de resultados**

Aspose.Cells tiene un motor de cálculo de fórmula integrado. No solo puede volver a calcular fórmulas importadas de plantillas de diseñador, sino que también admite calcular los resultados de fórmulas agregadas en tiempo de ejecución.

 Aspose.Cells admite la mayoría de las fórmulas o funciones que forman parte de Microsoft Excel (Read[una lista de las funciones admitidas por el motor de cálculo](/cells/es/java/supported-formula-functions/)). Esas funciones se pueden usar a través de las API o las hojas de cálculo del diseñador. Aspose.Cells admite un gran conjunto de fórmulas matemáticas, de cadena, booleanas, de fecha/hora, estadísticas, de base de datos, de búsqueda y de referencia.

 Utilizar el[**Fórmula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) propiedad o[**EstablecerFórmula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setFormula(java.lang.String,%20com.aspose.cells.FormulaParseOptions,%20java.lang.Object) ) métodos de[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)class para agregar una fórmula a una celda. Al aplicar una fórmula, siempre comience la cadena con un signo igual (=) como lo hace al crear una fórmula en Microsoft Excel y use una coma (,) para delimitar los parámetros de la función.

 Para calcular los resultados de las fórmulas, el usuario puede llamar al[**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) método de la[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)clase que procesa todas las fórmulas incrustadas en un archivo de Excel. O bien, el usuario puede llamar al[**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(com.aspose.cells.CalculationOptions,%20boolean)) método de la[**hoja de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) clase que procesa todas las fórmulas incrustadas en una hoja. O bien, el usuario también puede llamar al[**Calcular**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#calculate(com.aspose.cells.CalculationOptions)) método de la[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)clase que procesa la fórmula de uno Cell:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **Importante saber**

{{% alert color="primary" %}}

 Él**Fórmula** propiedad y**EstablecerFórmula(...)** métodos de la[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)trabajo en clase de manera diferente a la**Calcular** métodos de la[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), [**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) y[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) clases Él**Fórmula** propiedad y**EstablecerFórmula(...)** los métodos simplemente agregan la fórmula a una celda pero no calculan el resultado en tiempo de ejecución. Para obtener el resultado de las fórmulas, llame al**Calcular** métodos.

{{% /alert %}}

## **Cálculo directo de fórmula**

Aspose.Cells tiene un motor de cálculo de fórmula integrado. Además de calcular fórmulas importadas de un archivo de diseñador, Aspose.Cells puede calcular resultados de fórmulas directamente.

A veces, necesita calcular los resultados de la fórmula directamente sin agregarlos a una hoja de cálculo. Los valores de las celdas utilizadas en la fórmula ya existen en una hoja de cálculo y todo lo que necesita es encontrar el resultado de esos valores en función de alguna fórmula de Excel Microsoft sin agregar la fórmula en una hoja de cálculo.

 Puede utilizar las API del motor de cálculo de fórmulas Aspose.Cells para[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) a[**calcular**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(java.lang.String,%20com.aspose.cells.CalculationOptions)) los resultados de dichas fórmulas sin agregarlas a la hoja de trabajo:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

El código anterior produce el siguiente resultado:
{{< highlight "java" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Cálculo de fórmulas repetidamente**

 Cuando hay muchas fórmulas en el libro de trabajo y el usuario necesita calcularlas repetidamente modificando solo una pequeña parte de ellas, puede ser útil para el rendimiento habilitar la cadena de cálculo de fórmulas:[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#EnableCalculationChain).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}

### **Importante saber**

{{% alert color="primary" %}}

Por defecto, la cadena de cálculo está deshabilitada. Porque la creación de la cadena también necesita tiempo extra, la primera vez que se calculan fórmulas ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions))) puede consumir más tiempo de procesamiento de CPU y memoria cuando se compara con el cálculo de fórmulas sin cadena. Si el usuario no necesita calcular fórmulas repetidamente, el comportamiento predeterminado (calcular la fórmula directamente sin crear una cadena de cálculo) debería ser la mejor manera.

{{% /alert %}}

## **Temas avanzados**
- [Agregar Cells a Microsoft Ventana de visualización de fórmulas de Excel](/cells/es/java/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells Motor de cálculo de fórmulas](/cells/es/java/aspose-cells-formula-calculation-engine/)
- [Cálculo de la función IFNA usando Aspose.Cells](/cells/es/java/calculating-ifna-function-using-aspose-cells/)
- [Cálculo de fórmula de matriz de tablas de datos](/cells/es/java/calculation-of-array-formula-of-data-tables/)
- [Cálculo de las funciones MINIFS y MAXIFS de Excel 2016](/cells/es/java/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Reduzca el tiempo de cálculo de Cell. Método de cálculo](/cells/es/java/decrease-the-calculation-time-of-cell-calculate-method/)
- [Detección de referencia circular](/cells/es/java/detecting-circular-reference/)
- [Cálculo directo de la función personalizada sin escribirla en una hoja de trabajo](/cells/es/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementar el motor de cálculo personalizado para ampliar el motor de cálculo predeterminado de Aspose.Cells](/cells/es/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Interrumpir o cancelar el cálculo de fórmulas del libro de trabajo](/cells/es/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Devolver un rango de valores usando AbstractCalculationEngine](/cells/es/java/returning-a-range-of-values-using-abstractcalculationengine/)
- [Devolver un rango de valores usando ICustomFunction](/cells/es/java/returning-a-range-of-values-using-icustomfunction/)
- [Uso de la función ICustomFunction](/cells/es/java/using-icustomfunction-feature/)
