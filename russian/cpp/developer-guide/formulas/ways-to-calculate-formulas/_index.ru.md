﻿---
title: Способы вычисления формул
type: docs
weight: 30
url: /ru/cpp/ways-to-calculate-formulas/
---
## **Вступление**
Aspose.Cells имеет встроенный механизм расчета формул. Он может не только пересчитывать формулы, импортированные из шаблонов конструктора, но также поддерживает вычисление результатов формул, добавленных во время выполнения.
## **Добавление формул и расчет результатов**
Aspose.Cells поддерживает большинство формул и функций, входящих в состав Microsoft Excel. их можно использовать по телефону API или с помощью электронных таблиц дизайнера. Aspose.Cells поддерживает огромный набор математических, строковых, логических, дат/времени, статистических, поисковых и справочных формул.

Используйте метод Cell.Formula, чтобы добавить формулу в ячейку. При применении формулы к ячейке всегда начинайте строку со знака равенства (=), как при создании формулы в Microsoft Excel. Используйте запятую (,) для разделения параметров функции.

Чтобы вычислить результаты формул, вызовите метод Workbook.CalculateFormula(), который обрабатывает все формулы, встроенные в файл Excel. См. следующий пример кода, который добавляет формулу и вычисляет ее результаты. Пожалуйста, проверьте[выходной файл excel](38109185.xlsx) генерируется с помощью этого кода.

**Образец кода**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults.cpp" >}}
## **Прямой расчет формулы**
Иногда вам нужно вычислить результаты формулы напрямую, не добавляя их на лист. Значения ячеек, используемых в формуле, уже существуют на рабочем листе, и все, что вам нужно, это найти результат этих значений на основе какой-либо формулы Excel Microsoft без добавления формулы на рабочий лист.

Вы можете использовать метод Worksheet.CalculateFormula(String Formula) для вычисления результатов таких формул, не добавляя их на лист.

Код ниже производит следующий вывод.

{{< highlight "java" >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**Образец кода**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}
## **Расчет формул только один раз**
Когда Workbook.CalculateFormula() вызывается для вычисления значений формул в шаблоне книги, Aspose.Cells создает цепочку вычислений. Это увеличивает производительность, когда формулы вычисляются во второй или третий раз.

Однако, если шаблон содержит много формул, при первом вычислении формулы может потребоваться много процессорного времени и памяти.

Aspose.Cells позволяет отключить создание цепочки вычислений, что полезно, когда вы хотите вычислить формулы только один раз.

 Пожалуйста, вызовите Workbook.GetISettings().SetCreateCalcChain() с ложным параметром. Вы можете использовать[предоставил эксель файл](38109186.xlsx) для проверки этого кода.

**Образец кода**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly.cpp" >}}