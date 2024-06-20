---
title: Расчет формул
description: В этой статье рассматривается использование библиотеки Aspose.Cells для расчета формул в Microsoft Excel. Загружая существующий файл Excel или создавая новый файл Excel, мы можем использовать методы, предоставленные Aspose.Cells, для расчета формулы и получения результата. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, формулы, вычисления, Прямой расчет формул, Повторный расчет формул, добавление формул.
type: docs
weight: 125
url: /ru/net/calculate-formulas/
---

## **Добавление формул и вычисление результатов**

У Aspose.Cells есть встроенный механизм вычисления формул. Он не только может пересчитывать формулы, импортированные из шаблонов дизайнера, но также поддерживает вычисление результатов формул, добавленных во время выполнения.

Aspose.Cells поддерживает большинство формул или функций, которые являются частью Microsoft Excel (См. [список поддерживаемых функций вычислительного механизма](/cells/ru/net/supported-formula-functions/)). Эти функции могут использоваться через API или шаблоны дизайнера. Aspose.Cells поддерживает огромный набор математических, строковых, логических, дат/времени, статистических, баз данных, поиска и ссылочных формул.

Используйте свойство [**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) или методы [**SetFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2) класса для добавления формулы в ячейку. При применении формулы всегда начинайте строку с знака равенства (=), как это делается при создании формулы в Microsoft Excel, и используйте запятую (,) для разделения параметров функции.

Для расчета результатов формул пользователь может вызвать метод [**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) класса [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который обрабатывает все формулы, встроенные в файл Excel. Или пользователь может вызвать метод [**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula) класса [**Worsheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet), который обрабатывает все формулы, встроенные в листе. Или пользователь также может вызвать метод [**Calculate**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate) класса [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell), который обрабатывает формулу одной ячейки:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

### **Важно знать о формулах**

{{% alert color="primary" %}}

Свойство **Formula** и методы **SetFormula(...)** класса [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) работают по-разному от методов **Calculate** классов [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) и [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Свойство **Formula** и методы **SetFormula(...)** просто добавляют формулу в ячейку, но не вычисляют результат во время выполнения. Чтобы получить результат формул, пожалуйста, вызовите методы **Calculate**.

{{% /alert %}}

## **Прямое вычисление формулы**

Aspose.Cells имеет встроенный механизм расчета формул. Кроме того, в Aspose.Cells можно вычислять результаты формул непосредственно, импортированных из файла дизайнера.

Иногда вам нужно вычислить результаты формул напрямую, без добавления их в электронную таблицу. Значения ячеек, используемые в формуле, уже существуют в электронной таблице, и все, что вам нужно, - найти результат этих значений на основе некоторой формулы Microsoft Excel без добавления формулы в электронную таблицу.

Вы можете использовать API механизм расчета формул Aspose.Cells для [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) для [**calculate**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) результатов таких формул без их добавления в лист:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

Приведенный выше код производит следующий вывод:
{{< highlight net >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Как рассчитать формулы повторно**

Если в книге много формул, и пользователю необходимо повторно их вычислять, внося изменения только в небольшую часть из них, может быть полезным для производительности включить цепочку расчета формул: [**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

### **Важно знать**

{{% alert color="primary" %}}

По умолчанию цепочка расчета отключена. Поскольку создание цепочки требует дополнительного времени, при первом вычислении формул([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)) может потребляться больше процессорного времени и памяти по сравнению с вычислением формул без цепочки. Если пользователю не нужно повторно вычислять формулы, лучший способ - это использовать поведение по умолчанию (вычисление формул напрямую без создания цепочки расчета).

{{% /alert %}}


## **Продвинутые темы**
- [Добавление ячеек в окно наблюдения формул Microsoft Excel](/cells/ru/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Вычисление функции IFNA с помощью Aspose.Cells](/cells/ru/net/calculating-ifna-function-using-aspose-cells/)
- [Расчет массивной формулы таблиц данных](/cells/ru/net/calculation-of-array-formula-of-data-tables/)
- [Расчет функций MINIFS и MAXIFS Excel 2016](/cells/ru/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Уменьшение времени расчета метода Cell.Calculate](/cells/ru/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [Обнаружение циклических ссылок](/cells/ru/net/detecting-circular-reference/)
- [Прямой расчет пользовательской функции без записи ее на лист](/cells/ru/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Реализация пользовательского расчетного механизма для расширения расчетного механизма по умолчанию Aspose.Cells](/cells/ru/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Прерывание или отмена расчета формул книги](/cells/ru/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Возвращение диапазона значений с использованием абстрактного расчетного механизма](/cells/ru/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [Возврат диапазона значений с использованием ICustomFunction](/cells/ru/net/returning-a-range-of-values-using-icustomfunction/)
- [Установка режима расчета формул книги](/cells/ru/net/setting-formula-calculation-mode-of-workbook/)
- [Использование функции FormulaText в Aspose.Cells](/cells/ru/net/using-formulatext-function-in-aspose-cells/)
- [Использование функции ICustomFunction](/cells/ru/net/using-icustomfunction-feature/)
