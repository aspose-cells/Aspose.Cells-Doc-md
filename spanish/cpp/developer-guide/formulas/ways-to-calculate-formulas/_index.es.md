---
title: Formas de calcular fórmulas
type: docs
weight: 30
url: /es/cpp/ways-to-calculate-formulas/
---
##  **Introducción**
Aspose.Cells tiene un motor de cálculo de fórmulas integrado. No solo puede volver a calcular fórmulas importadas de plantillas de diseñador, sino que también admite el cálculo de los resultados de las fórmulas agregadas en tiempo de ejecución.
##  **Agregar fórmulas y calcular resultados**
Aspose.Cells admite la mayoría de las fórmulas o funciones que forman parte de Microsoft Excel. se pueden utilizar a través del API o utilizando hojas de cálculo del diseñador. Aspose.Cells admite un enorme conjunto de fórmulas matemáticas, de cadenas, booleanas, de fecha/hora, estadísticas, de búsqueda y de referencia.

Utilice el método Cell.SetFormula para agregar una fórmula a una celda. Al aplicar una fórmula a una celda, siempre comience la cadena con un signo igual (=) como lo hace al crear una fórmula en Microsoft Excel. Utilice una coma (,) para delimitar los parámetros de la función.

Para calcular los resultados de las fórmulas, llame al método Workbook.CalculateFormula() que procesa todas las fórmulas incrustadas en un archivo de Excel. Consulte el siguiente código de muestra que agrega la fórmula y calcula sus resultados. Por favor, checa el[archivo de excel de salida](38109185.xlsx) generado con este código.

**Código de muestra**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults-new.cpp" >}}
<!---## **Direct Calculation of Formula**
Sometimes, you need to calculate formula results directly without adding them into a worksheet. The values of the cells used in the formula already exist in a worksheet and all you need is to find the result of those values based on some Microsoft Excel formula without adding the formula in a worksheet.

You can use Worksheet.CalculateFormula(String formula) method to calculate the results of such formulas without adding them to worksheet.

The code below produces the following output.

{{< highlight java >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**Sample Code**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}   --->
##  **Calcular fórmulas solo una vez**
Cuando se llama a Workbook.CalculateFormula() para calcular los valores de las fórmulas en una plantilla de libro de trabajo, Aspose.Cells crea una cadena de cálculo. Aumenta el rendimiento cuando las fórmulas se calculan por segunda o tercera vez.

Sin embargo, si la plantilla contiene muchas fórmulas, la primera vez que se calcula la fórmula puede consumir mucho tiempo de procesamiento de la CPU y memoria.

Aspose.Cells le permite desactivar la creación de una cadena de cálculo, lo cual es útil cuando desea calcular fórmulas solo una vez.

 Llame a Workbook.GetISettings().SetCreateCalcChain() con un parámetro falso. Puedes usar el[archivo excel proporcionado](38109186.xlsx) para probar este código.

**Código de muestra**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly-new.cpp" >}}
