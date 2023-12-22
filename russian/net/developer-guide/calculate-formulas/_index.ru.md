---
title: Рассчитать формулы
description: В этой статье рассказывается, как использовать библиотеку Aspose.Cells для расчета формул в Excel Microsoft. Загрузив существующий файл Excel или создав новый файл Excel, мы можем использовать методы, предоставленные Aspose.Cells, для расчета формулы и получения результата. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, formulas, calculations, Direct Calculation of Formula, Calculate Formulas repeatedly, add formulas.
type: docs
weight: 125
url: /ru/net/calculate-formulas/
---
##  **Добавление формул и расчет результатов**

Aspose.Cells имеет встроенный механизм расчета формул. Он не только может пересчитывать формулы, импортированные из шаблонов дизайнера, но также поддерживает расчет результатов формул, добавленных во время выполнения.

 Aspose.Cells поддерживает большинство формул и функций, входящих в Microsoft Excel (Читать[список функций, поддерживаемых вычислительным механизмом](/cells/ru/net/supported-formula-functions/)). Эти функции можно использовать через API или таблицы дизайнера. Aspose.Cells поддерживает огромный набор математических, строковых, логических формул, формул даты и времени, статистических, баз данных, формул поиска и справочных формул.

 Использовать[**Формула**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) имущество или[**УстановитьФормулу(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2) методы[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)класс для добавления формулы в ячейку. При применении формулы всегда начинайте строку со знака равенства (=), как при создании формулы в Excel Microsoft, и используйте запятую (,) для разделения параметров функции.

 Для расчета результатов формул пользователь может вызвать[**РассчитатьФормула**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) метод[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс, который обрабатывает все формулы, встроенные в файл Excel. Или пользователь может позвонить в[**РассчитатьФормула**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula) метод[**Ворлист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс, который обрабатывает все формулы, встроенные в лист. Или пользователь также может позвонить в[**Рассчитать**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate) метод[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)класс, который обрабатывает формулу одного Cell:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

###  **Важно знать формулы**

{{% alert color="primary" %}}

**Формула** собственность и**УстановитьФормулу(...)** методы[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)класс работает иначе, чем**Рассчитать** методы[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) и[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) занятия.**Формула** собственность и**УстановитьФормулу(...)** методы просто добавляют формулу в ячейку, но не вычисляют результат во время выполнения. Чтобы получить результат формул, позвоните по телефону**Рассчитать** методы.

{{% /alert %}}

##  **Прямой расчет формулы**

Aspose.Cells имеет встроенный механизм расчета формул. Помимо вычисления формул, импортированных из файла дизайнера, Aspose.Cells может напрямую рассчитывать результаты формулы.

Иногда вам необходимо вычислить результаты формулы напрямую, не добавляя их на лист. Значения ячеек, используемых в формуле, уже существуют на листе, и все, что вам нужно, это найти результат этих значений на основе некоторой формулы Excel Microsoft без добавления формулы на лист.

 Вы можете использовать API-интерфейсы механизма расчета формул Aspose.Cells для[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) к[**вычислить**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) результаты таких формул без добавления их на лист:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

Приведенный выше код выдает следующий результат:
{{< highlight "net" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

##  **Как вычислять формулы повторно**

Если в книге много формул и пользователю необходимо многократно вычислять их, изменяя лишь небольшую их часть, для повышения производительности может быть полезно включить цепочку вычислений формул:[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

###  **Важно знать**

{{% alert color="primary" %}}

По умолчанию цепочка вычислений отключена. Потому что создание цепочки тоже требует дополнительного времени, первый раз расчета формул([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)) может потреблять больше времени и памяти процессора по сравнению с вычислением формул без цепочки. Если пользователю не нужно повторно вычислять формулы, лучше использовать поведение по умолчанию (вычисление формулы напрямую без создания цепочки вычислений).

{{% /alert %}}


##  **Предварительные темы**
- [Добавьте от Cells до Microsoft Окно просмотра формул Excel](/cells/ru/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Вычисление функции IFNA с использованием Aspose.Cells](/cells/ru/net/calculating-ifna-function-using-aspose-cells/)
- [Расчет формулы массива таблиц данных](/cells/ru/net/calculation-of-array-formula-of-data-tables/)
- [Расчет функций Excel 2016 MINIFS и MAXIFS](/cells/ru/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Уменьшите время расчета Cell. Метод расчета.](/cells/ru/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [Обнаружение циклической ссылки](/cells/ru/net/detecting-circular-reference/)
- [Прямой расчет пользовательской функции без записи ее на листе](/cells/ru/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Внедрите пользовательский механизм вычислений, чтобы расширить механизм вычислений по умолчанию Aspose.Cells.](/cells/ru/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Прервите или отмените расчет формулы в рабочей книге](/cells/ru/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Возврат диапазона значений с помощью AbstractCalculationEngine](/cells/ru/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [Возврат диапазона значений с помощью ICustomFunction](/cells/ru/net/returning-a-range-of-values-using-icustomfunction/)
- [Настройка режима расчета формулы в рабочей книге](/cells/ru/net/setting-formula-calculation-mode-of-workbook/)
- [Использование функции FormulaText в Aspose.Cells](/cells/ru/net/using-formulatext-function-in-aspose-cells/)
- [Использование функции ICustomFunction](/cells/ru/net/using-icustomfunction-feature/)
