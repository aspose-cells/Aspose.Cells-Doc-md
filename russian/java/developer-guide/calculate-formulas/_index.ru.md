---
title: Вычислить формулы
type: docs
weight: 110
url: /ru/java/calculate-formulas/
---
## **Добавление формул и расчет результатов**

Aspose.Cells имеет встроенный механизм расчета формул. Он не только может пересчитывать формулы, импортированные из шаблонов конструктора, но также поддерживает вычисление результатов формул, добавленных во время выполнения.

 Aspose.Cells поддерживает большинство формул и функций, входящих в состав Microsoft Excel(Читать[список функций, поддерживаемых расчетным движком](/cells/ru/java/supported-formula-functions/)). Эти функции можно использовать через API или электронные таблицы конструктора. Aspose.Cells поддерживает огромный набор математических, строковых, логических, дат/времени, статистических, баз данных, поисковых и справочных формул.

 Использовать[**Формула**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) собственность или[**УстановитьФормулу(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setFormula(java.lang.String,%20com.aspose.cells.FormulaParseOptions,%20java.lang.Object) ) методы[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)класс, чтобы добавить формулу в ячейку. При применении формулы всегда начинайте строку со знака равенства (=), как при создании формулы в Microsoft Excel, и используйте запятую (,) для разделения параметров функции.

 Чтобы вычислить результаты формул, пользователь может вызвать[**ВычислитьФормула**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) метод[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)класс, который обрабатывает все формулы, встроенные в файл Excel. Или пользователь может вызвать[**ВычислитьФормула**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(com.aspose.cells.CalculationOptions,%20boolean)) метод[**рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) класс, который обрабатывает все формулы, встроенные в лист. Или пользователь также может вызвать[**Рассчитать**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#calculate(com.aspose.cells.CalculationOptions)) метод[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)класс, который обрабатывает формулу одного Cell:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **Важно знать**

{{% alert color="primary" %}}

**Формула** имущество и**УстановитьФормулу(...)** методы[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)классная работа отличается от**Рассчитать** методы[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), [**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) а также[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) классы.**Формула** имущество и**УстановитьФормулу(...)** методы просто добавляют формулу в ячейку, но не вычисляют результат во время выполнения. Для получения результата формул позвоните по телефону**Рассчитать** методы.

{{% /alert %}}

## **Прямой расчет формулы**

Aspose.Cells имеет встроенный механизм расчета формул. Помимо вычисления формул, импортированных из файла конструктора, Aspose.Cells может напрямую вычислять результаты формул.

Иногда вам нужно вычислить результаты формулы напрямую, не добавляя их на лист. Значения ячеек, используемых в формуле, уже существуют на рабочем листе, и все, что вам нужно, это найти результат этих значений на основе какой-либо формулы Excel Microsoft без добавления формулы на рабочий лист.

 Вы можете использовать API-интерфейсы механизма расчета формул Aspose.Cells для[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) к[**рассчитать**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(java.lang.String,%20com.aspose.cells.CalculationOptions)) результаты таких формул без добавления их на лист:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

Вышеприведенный код выводит следующий результат:
{{< highlight "java" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Многократное вычисление формул**

 Когда в рабочей книге много формул и пользователю необходимо многократно их вычислять, изменяя только небольшую их часть, для повышения производительности может быть полезно включить цепочку вычисления формул:[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#EnableCalculationChain).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}

### **Важно знать**

{{% alert color="primary" %}}

По умолчанию цепочка вычислений отключена. Поскольку создание цепочки также требует дополнительного времени, первый раз вычисления формул ([**Книга.ВычислитьФормулу(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions))) может потреблять больше процессорного времени и памяти по сравнению с вычислением формул без цепочки. Если пользователю не нужно повторно вычислять формулы, поведение по умолчанию (вычисление формулы напрямую без создания цепочки вычислений) должно быть лучшим способом.

{{% /alert %}}

## **Предварительные темы**
- [Добавить Cells в Microsoft Окно просмотра формулы Excel](/cells/ru/java/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells Механизм вычисления формулы](/cells/ru/java/aspose-cells-formula-calculation-engine/)
- [Расчет функции IFNA с использованием Aspose.Cells](/cells/ru/java/calculating-ifna-function-using-aspose-cells/)
- [Вычисление формулы массива таблиц данных](/cells/ru/java/calculation-of-array-formula-of-data-tables/)
- [Вычисление функций Excel 2016 MINIFS и MAXIFS](/cells/ru/java/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Уменьшите время расчета Cell. Метод расчета](/cells/ru/java/decrease-the-calculation-time-of-cell-calculate-method/)
- [Обнаружение циклической ссылки](/cells/ru/java/detecting-circular-reference/)
- [Прямой расчет пользовательской функции без записи ее на листе](/cells/ru/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Реализовать пользовательский механизм расчета, чтобы расширить механизм расчета по умолчанию Aspose.Cells.](/cells/ru/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Прервать или отменить расчет формулы рабочей книги](/cells/ru/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Возврат диапазона значений с помощью AbstractCalculationEngine](/cells/ru/java/returning-a-range-of-values-using-abstractcalculationengine/)
- [Возврат диапазона значений с помощью ICustomFunction](/cells/ru/java/returning-a-range-of-values-using-icustomfunction/)
- [Использование функции ICustomFunction](/cells/ru/java/using-icustomfunction-feature/)
