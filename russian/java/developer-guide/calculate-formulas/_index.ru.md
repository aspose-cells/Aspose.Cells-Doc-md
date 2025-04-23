---
title: Расчет формул
type: docs
weight: 110
url: /ru/java/calculate-formulas/
---

## **Добавление формул и вычисление результатов**

У Aspose.Cells есть встроенный механизм вычисления формул. Он не только может пересчитывать формулы, импортированные из шаблонов дизайнера, но также поддерживает вычисление результатов формул, добавленных во время выполнения.

Aspose.Cells поддерживает большинство формул или функций, которые являются частью Microsoft Excel (см. [список функций, поддерживаемых движком вычислений](/cells/ru/java/supported-formula-functions/)). Эти функции могут использоваться через API или дизайнерские таблицы. Aspose.Cells поддерживает огромный набор математических, строковых, логических, дата/время, статистических, баз данных, поисковых и ссылочных формул.

Используйте свойство [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) или методы [**SetFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setFormula-java.lang.String-com.aspose.cells.FormulaParseOptions-java.lang.Object-) класса для добавления формулы в ячейку. При применении формулы всегда начинайте строку с знака равенства (=), как это делается при создании формулы в Microsoft Excel, и используйте запятую (,) для разделения параметров функции.

Для вычисления результатов формул пользователь может вызвать метод [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions--) класса [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), который обрабатывает все формулы, встроенные в файл Excel. Или пользователь может вызвать метод [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula-com.aspose.cells.CalculationOptions-boolean-) класса [**Worsheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet), который обрабатывает все формулы, встроенные в лист. Или пользователь также может вызвать метод [**Calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#calculate-com.aspose.cells.CalculationOptions-) класса [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell), который обрабатывает формулу одной ячейки:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **Важно знать**

{{% alert color="primary" %}}

Свойство **Formula** и методы **SetFormula(...)** класса [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) работают по-разному от методов **Calculate** классов [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) и [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell). Свойство **Formula** и методы **SetFormula(...)** просто добавляют формулу в ячейку, но не вычисляют результат во время выполнения. Чтобы получить результат формул, пожалуйста, вызовите методы **Calculate**.

{{% /alert %}}

## **Прямое вычисление формулы**

Aspose.Cells имеет встроенный механизм расчета формул. Кроме того, в Aspose.Cells можно вычислять результаты формул непосредственно, импортированных из файла дизайнера.

Иногда вам нужно вычислить результаты формул напрямую, без добавления их в электронную таблицу. Значения ячеек, используемые в формуле, уже существуют в электронной таблице, и все, что вам нужно, - найти результат этих значений на основе некоторой формулы Microsoft Excel без добавления формулы в электронную таблицу.

Вы можете использовать API механизм расчета формул Aspose.Cells для [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) для [**calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula-java.lang.String-com.aspose.cells.CalculationOptions-) результатов таких формул без их добавления в лист:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

Приведенный выше код производит следующий вывод:
{{< highlight java >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Повторное вычисление формул**

Если в книге много формул, и пользователю необходимо повторно их вычислять, внося изменения только в небольшую часть из них, может быть полезным для производительности включить цепочку расчета формул: [**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#EnableCalculationChain).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}

### **Важно знать**

{{% alert color="primary" %}}

По умолчанию цепочка вычислений отключена. Создание цепочки также требует дополнительного времени, поэтому при первом вычислении формул ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions--)) может потребоваться больше ресурсов ЦП и памяти по сравнению с вычислением формул без цепочки. Если пользователю не нужно вычислять формулы повторно, лучше соблюдать стандартное поведение (вычисление формулы напрямую без создания цепочки вычислений).

{{% /alert %}}

## **Продвинутые темы**
- [Добавление ячеек в окно наблюдения формул Microsoft Excel](/cells/ru/java/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells Расчетный механизм формул](/cells/ru/java/aspose-cells-formula-calculation-engine/)
- [Вычисление функции IFNA с помощью Aspose.Cells](/cells/ru/java/calculating-ifna-function-using-aspose-cells/)
- [Расчет массивной формулы таблиц данных](/cells/ru/java/calculation-of-array-formula-of-data-tables/)
- [Расчет функций MINIFS и MAXIFS Excel 2016](/cells/ru/java/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Уменьшение времени расчета метода Cell.Calculate](/cells/ru/java/decrease-the-calculation-time-of-cell-calculate-method/)
- [Обнаружение циклических ссылок](/cells/ru/java/detecting-circular-reference/)
- [Прямой расчет пользовательской функции без записи ее на лист](/cells/ru/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Реализация пользовательского расчетного механизма для расширения расчетного механизма по умолчанию Aspose.Cells](/cells/ru/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Прерывание или отмена расчета формул книги](/cells/ru/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Возвращение диапазона значений с использованием абстрактного расчетного механизма](/cells/ru/java/returning-a-range-of-values-using-abstractcalculationengine/)
- [Возврат диапазона значений с использованием ICustomFunction](/cells/ru/java/returning-a-range-of-values-using-icustomfunction/)
- [Использование функции ICustomFunction](/cells/ru/java/using-icustomfunction-feature/)
{{< app/cells/assistant language="java" >}}
