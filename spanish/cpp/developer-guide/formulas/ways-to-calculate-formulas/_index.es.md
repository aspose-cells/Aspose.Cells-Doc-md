---
title: Formas de calcular fórmulas
type: docs
weight: 30
url: /es/cpp/ways-to-calculate-formulas/
---
## **Introducción**
Aspose.Cells tiene un motor de cálculo de fórmula integrado. No solo puede volver a calcular fórmulas importadas de plantillas de diseñador, sino que también admite el cálculo de los resultados de fórmulas agregadas en tiempo de ejecución.
## **Adición de fórmulas y cálculo de resultados**
Aspose.Cells admite la mayoría de las fórmulas o funciones que forman parte de Microsoft Excel. se pueden utilizar a través del API o utilizando hojas de cálculo de diseño. Aspose.Cells admite un gran conjunto de fórmulas matemáticas, de cadena, booleanas, de fecha/hora, estadísticas, de búsqueda y de referencia.

Use el método Cell.Formula para agregar una fórmula a una celda. Al aplicar una fórmula a una celda, siempre comience la cadena con un signo igual (=) como lo hace al crear una fórmula en Microsoft Excel. Use una coma (,) para delimitar los parámetros de la función.

Para calcular los resultados de las fórmulas, llame al método Workbook.CalculateFormula() que procesa todas las fórmulas incrustadas en un archivo de Excel. Consulte el siguiente código de ejemplo que agrega la fórmula y calcula sus resultados. Por favor, checa el[archivo de salida de Excel](38109185.xlsx) generado con este código.

**Código de muestra**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults.cpp" >}}
## **Cálculo directo de fórmula**
A veces, necesita calcular los resultados de la fórmula directamente sin agregarlos a una hoja de cálculo. Los valores de las celdas utilizadas en la fórmula ya existen en una hoja de cálculo y todo lo que necesita es encontrar el resultado de esos valores en función de alguna fórmula de Excel Microsoft sin agregar la fórmula en una hoja de cálculo.

Puede usar el método Worksheet.CalculateFormula(String formula) para calcular los resultados de dichas fórmulas sin agregarlas a la hoja de trabajo.

El siguiente código produce el siguiente resultado.

{{< highlight "java" >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**Código de muestra**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}
## **Cálculo de fórmulas una sola vez**
Cuando se llama a Workbook.CalculateFormula() para calcular los valores de fórmulas en una plantilla de libro de trabajo, Aspose.Cells crea una cadena de cálculo. Aumenta el rendimiento cuando las fórmulas se calculan por segunda o tercera vez.

Sin embargo, si la plantilla contiene muchas fórmulas, la primera vez que se calcula la fórmula puede consumir mucho tiempo de procesamiento de CPU y memoria.

Aspose.Cells le permite desactivar la creación de una cadena de cálculo que es útil cuando desea calcular fórmulas solo una vez.

 Llame a Workbook.GetISettings().SetCreateCalcChain() con un parámetro falso. Puedes usar el[archivo excel proporcionado](38109186.xlsx) para probar este código.

**Código de muestra**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly.cpp" >}}
