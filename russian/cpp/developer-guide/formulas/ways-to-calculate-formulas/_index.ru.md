---
title: Способы расчета формул
type: docs
weight: 30
url: /ru/cpp/ways-to-calculate-formulas/
---
##  **Введение**
Aspose.Cells имеет встроенный механизм расчета формул. Он может не только пересчитывать формулы, импортированные из шаблонов дизайнера, но также поддерживает расчет результатов формул, добавленных во время выполнения.
##  **Добавление формул и расчет результатов**
Aspose.Cells поддерживает большинство формул и функций, входящих в состав Microsoft Excel. их можно использовать по номеру API или с помощью дизайнерских таблиц. Aspose.Cells поддерживает огромный набор математических, строковых, логических формул, формул даты/времени, статистических, поисковых и справочных формул.

Используйте метод Cell.SetFormula, чтобы добавить формулу в ячейку. Применяя формулу к ячейке, всегда начинайте строку со знака равенства (=), как и при создании формулы в Microsoft Excel. Используйте запятую (,) для разделения параметров функции.

Чтобы вычислить результаты формул, вызовите метод Workbook.CalculateFormula(), который обрабатывает все формулы, встроенные в файл Excel. См. следующий пример кода, который добавляет формулу и вычисляет ее результаты. Пожалуйста, проверьте[выходной файл Excel](38109185.xlsx) созданный с помощью этого кода.

**Образец кода**

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
##  **Вычисление формул только один раз**
Когда Workbook.CalculateFormula() вызывается для вычисления значений формул в шаблоне книги, Aspose.Cells создает цепочку вычислений. Это повышает производительность при расчете формул во второй или третий раз.

Однако если шаблон содержит множество формул, при первом вычислении формулы может потребоваться много процессорного времени и памяти.

Aspose.Cells позволяет отключить создание цепочки вычислений, что полезно, если вы хотите вычислить формулы только один раз.

 Пожалуйста, вызовите Workbook.GetISettings().SetCreateCalcChain() с параметром false. Вы можете использовать[предоставил файл Excel](38109186.xlsx) чтобы протестировать этот код.

**Образец кода**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly-new.cpp" >}}
