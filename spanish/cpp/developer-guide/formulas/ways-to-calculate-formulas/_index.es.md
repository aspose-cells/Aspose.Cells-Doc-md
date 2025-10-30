---
title: Formas de calcular fórmulas
type: docs
weight: 30
url: /es/cpp/ways-to-calculate-formulas/
---

## **Introducción**
Aspose.Cells tiene un motor de cálculo de fórmulas integrado. No solo puede volver a calcular fórmulas importadas de plantillas de diseño, sino que también admite el cálculo de los resultados de fórmulas agregadas en tiempo de ejecución.
## **Agregar fórmulas y calcular resultados**
Aspose.Cells admite la mayoría de las fórmulas o funciones que forman parte de Microsoft Excel. Se pueden usar a través de la API o mediante hojas de cálculo de diseño. Aspose.Cells admite un gran conjunto de fórmulas matemáticas, de cadena, booleanas, de fecha/hora, estadísticas, de búsqueda y referencia.

Utilice el método Cell.SetFormula para agregar una fórmula a una celda. Al aplicar una fórmula a una celda, siempre comience el texto con un signo igual (=) como lo hace al crear una fórmula en Microsoft Excel. Use una coma (,) para delimitar los parámetros de la función.

Para calcular los resultados de las fórmulas, llame al método Workbook.CalculateFormula() que procesa todas las fórmulas incrustadas en un archivo de Excel. Consulte el siguiente código de ejemplo que agrega la fórmula y calcula sus resultados. Consulte el [archivo de Excel de salida](38109185.xlsx) generado con este código.

**Código de Ejemplo**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults-new.cpp" >}}
< ---## **Cálculo directo de fórmulas
A veces, es necesario calcular directamente los resultados de las fórmulas sin agregarlas a una hoja de cálculo. Los valores de las celdas utilizados en la fórmula ya existen en una hoja de cálculo y todo lo que necesita es encontrar el resultado de esos valores en función de alguna fórmula de Microsoft Excel sin agregar la fórmula en una hoja de cálculo.

Puede usar el método Worksheet.CalculateFormula(String formula) para calcular los resultados de dichas fórmulas sin agregarlas a la hoja de cálculo.

El código a continuación produce la siguiente salida.

{{< highlight java >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**Código de Ejemplo**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}   --->
## **Calcular fórmulas solo una vez**
Cuando se llama a Workbook.CalculateFormula() para calcular los valores de las fórmulas en una plantilla de libro de trabajo, Aspose.Cells crea una cadena de cálculo. Aumenta el rendimiento cuando las fórmulas se calculan por segunda o tercera vez.

Sin embargo, si la plantilla contiene muchas fórmulas, el tiempo de cálculo de la fórmula la primera vez puede consumir mucho tiempo de procesamiento de CPU y memoria.

Aspose.Cells te permite desactivar la creación de una cadena de cálculo, lo cual es útil cuando quieres calcular las fórmulas solo una vez.

Por favor llama a Workbook.GetISettings().SetCreateCalcChain() con el parámetro false. Puedes usar el [archivo de Excel proporcionado](38109186.xlsx) para probar este código.

**Código de Ejemplo**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
