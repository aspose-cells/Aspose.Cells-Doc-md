---
title: Вычислить формулы
type: docs
weight: 125
url: /ru/net/calculate-formulas/
---
## **Добавление формул и расчет результатов**

Aspose.Cells имеет встроенный механизм расчета формул. Он не только может пересчитывать формулы, импортированные из шаблонов конструктора, но также поддерживает вычисление результатов формул, добавленных во время выполнения.

 Aspose.Cells поддерживает большинство формул и функций, входящих в состав Microsoft Excel(Читать[список функций, поддерживаемых расчетным движком](/cells/ru/net/supported-formula-functions/)). Эти функции можно использовать через API или электронные таблицы конструктора. Aspose.Cells поддерживает огромный набор математических, строковых, логических, дат/времени, статистических, баз данных, поисковых и справочных формул.

 Использовать[**Формула**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) собственность или[**УстановитьФормулу(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2) методы[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)класс, чтобы добавить формулу в ячейку. При применении формулы всегда начинайте строку со знака равенства (=), как при создании формулы в Microsoft Excel, и используйте запятую (,) для разделения параметров функции.

 Чтобы вычислить результаты формул, пользователь может вызвать[**ВычислитьФормула**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) метод[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)класс, который обрабатывает все формулы, встроенные в файл Excel. Или пользователь может вызвать[**ВычислитьФормула**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula) метод[**рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс, который обрабатывает все формулы, встроенные в лист. Или пользователь также может вызвать[**Рассчитать**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate) метод[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)класс, который обрабатывает формулу одного Cell:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

### **Важно знать**

{{% alert color="primary" %}}

**Формула** имущество и**УстановитьФормулу(...)** методы[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)классная работа отличается от**Рассчитать** методы[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) и[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) классы.**Формула** имущество и**УстановитьФормулу(...)** методы просто добавляют формулу в ячейку, но не вычисляют результат во время выполнения. Для получения результата формул позвоните по телефону**Рассчитать** методы.

{{% /alert %}}

## **Прямой расчет формулы**

Aspose.Cells имеет встроенный механизм расчета формул. Помимо вычисления формул, импортированных из файла конструктора, Aspose.Cells может напрямую вычислять результаты формул.

Иногда вам нужно вычислить результаты формулы напрямую, не добавляя их на лист. Значения ячеек, используемых в формуле, уже существуют на рабочем листе, и все, что вам нужно, это найти результат этих значений на основе какой-либо формулы Excel Microsoft без добавления формулы на рабочий лист.

 Вы можете использовать API-интерфейсы механизма расчета формул Aspose.Cells для[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) к[**рассчитать**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) результаты таких формул без добавления их на лист:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

Вышеприведенный код выводит следующий результат:
{{< highlight "net" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Многократное вычисление формул**

 Когда в рабочей книге много формул и пользователю необходимо многократно их вычислять, изменяя только небольшую их часть, для повышения производительности может быть полезно включить цепочку вычисления формул:[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

### **Важно знать**

{{% alert color="primary" %}}

По умолчанию цепочка вычислений отключена. Поскольку создание цепочки также требует дополнительного времени, первый раз вычисления формул ([**Книга.ВычислитьФормулу(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)) может потреблять больше процессорного времени и памяти по сравнению с вычислением формул без цепочки. Если пользователю не нужно повторно вычислять формулы, поведение по умолчанию (вычисление формулы напрямую без создания цепочки вычислений) должно быть лучшим способом.

{{% /alert %}}


## **Предварительные темы**
- [Добавить Cells в Microsoft Окно просмотра формулы Excel](/cells/ru/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Расчет функции IFNA с использованием Aspose.Cells](/cells/ru/net/calculating-ifna-function-using-aspose-cells/)
- [Вычисление формулы массива таблиц данных](/cells/ru/net/calculation-of-array-formula-of-data-tables/)
- [Вычисление функций Excel 2016 MINIFS и MAXIFS](/cells/ru/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Уменьшите время расчета Cell. Метод расчета](/cells/ru/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [Обнаружение циклической ссылки](/cells/ru/net/detecting-circular-reference/)
- [Прямой расчет пользовательской функции без записи ее на листе](/cells/ru/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Реализовать пользовательский механизм расчета, чтобы расширить механизм расчета по умолчанию Aspose.Cells.](/cells/ru/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Прервать или отменить расчет формулы рабочей книги](/cells/ru/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Возврат диапазона значений с помощью AbstractCalculationEngine](/cells/ru/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [Возврат диапазона значений с помощью ICustomFunction](/cells/ru/net/returning-a-range-of-values-using-icustomfunction/)
- [Настройка режима вычисления формулы в книге](/cells/ru/net/setting-formula-calculation-mode-of-workbook/)
- [Использование функции FormulaText в Aspose.Cells](/cells/ru/net/using-formulatext-function-in-aspose-cells/)
- [Использование функции ICustomFunction](/cells/ru/net/using-icustomfunction-feature/)
