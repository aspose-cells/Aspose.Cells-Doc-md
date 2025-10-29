---
title: Вычисление формул с помощью Golang через C++
linktitle: Расчет формул
description: В этой статье рассказывается о том, как использовать библиотеку Aspose.Cells для вычисления формул в Microsoft Excel с помощью Golang через C++. Загружая существующий Excel файл или создавая новый, мы можем использовать методы Aspose.Cells для вычисления формулы и получения результата. В завершение, мы сохраняем исправленный Excel файл на диск.
keywords: Aspose.Cells, Excel, формулы, вычисления, Прямой расчет формул, Повторный расчет формул, добавление формул.
type: docs
weight: 125
url: /ru/go-cpp/calculate-formulas/
---

## **Добавление формул и вычисление результатов**

У Aspose.Cells встроен движок вычисления формул. Он может не только пересчитывать импортированные из шаблонов Excel формулы, но и поддерживает вычисление результатов добавленных формул в режиме выполнения.

Aspose.Cells поддерживает большинство формул или функций, входящих в Microsoft Excel (читать [список поддерживаемых функций движка вычислений](/cells/ru/cpp/supported-formula-functions/)). Эти функции можно использовать через API или при создании диаграмм. Aspose.Cells поддерживает обширный набор математических, строковых, булевых, дат/времени, статистических, баз данных, поиска и ссылочных формул.

Используйте свойство [**GetFormula**](https://reference.aspose.com/cells/go-cpp/cell/getformula/) или методы [**SetFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setformula/) класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) для добавления формулы в ячейку. При применении формулы всегда начинайте строку с знака равенства (=), как при создании формулы в Microsoft Excel, и используйте запятую (,) для разделения параметров функции.

Для вычисления результатов формул пользователь может вызвать метод [**CalculateFormula**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) класса [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который обрабатывает все встроенные формулы в файле Excel. Или вызвать метод [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) класса [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/), который обрабатывает формулы на листе. Также можно вызвать метод [**Calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/calculate/) класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/), который обрабатывает формулу отдельной ячейки:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas.go" >}}
### **Важно знать о формулах**

{{% alert color="primary" %}}

Свойство **GetFormula** и методы **SetFormula(...)** класса [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) работают иначе, чем методы **Calculate** классов [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) и [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/). Свойство **GetFormula** и методы **SetFormula(...)** просто добавляют формулу в ячейку, но не вычисляют результат во время выполнения. Чтобы получить результат формул, вызовите методы **Calculate**.

{{% /alert %}}

## **Прямое вычисление формулы**

Aspose.Cells имеет встроенный механизм расчета формул. Кроме того, в Aspose.Cells можно вычислять результаты формул непосредственно, импортированных из файла дизайнера.

Иногда нужно вычислить результаты формул напрямую, не добавляя их в лист. Значения ячеек, используемых в формуле, уже существуют в листе, и все, что нужно — это найти результат этих значений на основе формулы Microsoft Excel без добавления самой формулы в лист.

Можно использовать API движка вычислений формул Aspose.Cells для [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) для получения результатов таких формул без добавления их в лист:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas-1.go" >}}
Приведенный выше код производит следующий вывод:
{{< highlight cpp >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Как повторно вычислять формулы**

Когда в рабочей книге много формул и пользователь должен вычислять их повторно с небольшими изменениями, может быть полезно для производительности включить цепочку вычислений формул: [**FormulaSettings.GetEnableCalculationChain()**](https://reference.aspose.com/cells/go-cpp/formulasettings/getenablecalculationchain/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas-2.go" >}}
### **Важно знать**

{{% alert color="primary" %}}

По умолчанию цепочка вычислений отключена. Создание цепочки также требует дополнительного времени, поэтому при первом вычислении формул ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)) может потребоваться больше процессорного времени и памяти по сравнению с вычислением формул без цепочки. Если пользователю не нужно повторно вычислять формулы, лучше оставить поведение по умолчанию (вычисление формулы напрямую без создания цепочки вычислений).

{{% /alert %}}

## **Дополнительные темы**
- [Добавление ячеек в окно наблюдения формул Microsoft Excel](/cells/ru/cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Вычисление функции IFNA с помощью Aspose.Cells](/cells/ru/cpp/calculating-ifna-function-using-aspose-cells/)
- [Расчет массивной формулы таблиц данных](/cells/ru/cpp/calculation-of-array-formula-of-data-tables/)
- [Расчет функций MINIFS и MAXIFS Excel 2016](/cells/ru/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Уменьшение времени расчета метода Cell.Calculate](/cells/ru/cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Прямой расчет пользовательской функции без записи ее на лист](/cells/ru/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Реализация пользовательского расчетного механизма для расширения расчетного механизма по умолчанию Aspose.Cells](/cells/ru/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Возвращение диапазона значений с использованием абстрактного расчетного механизма](/cells/ru/cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Установка режима расчета формул книги](/cells/ru/cpp/setting-formula-calculation-mode-of-workbook/)
- [Использование функции FormulaText в Aspose.Cells](/cells/ru/cpp/using-formulatext-function-in-aspose-cells/)
