---
title: Управление формулами файлов Excel
linktitle: Формулы
type: docs
weight: 122
url: /ru/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells может легко получать, устанавливать и вычислять формулы файлов Excel.
description: Узнайте, как управлять формулами файлов Excel через API Aspose.Cells for NET.
keywords: Как вычислить формулы в C#, Формулы и функции с использованием C#, Управление встроенными функциями C#, Как использовать дополнительные функции с помощью C#, Как использовать массивную формулу через C#, Как использовать формулу R1C1 в C#.
---

## **Введение**

Одним из убедительных функций Microsoft Excel является его возможность обработки данных с помощью формул и функций. Microsoft Excel предоставляет набор встроенных функций и формул, которые помогают пользователям быстро выполнять сложные вычисления. Aspose.Cells также предоставляет огромный набор встроенных функций и формул, которые помогают разработчикам легко вычислять значения. Aspose.Cells также поддерживает дополнительные функции. Более того, Aspose.Cells поддерживает массивные и R1C1 формулы в Aspose.Cells.

## **Как использовать формулы и функции**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), которая позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Каждый элемент в коллекции Cells представляет объект класса [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Можно применять формулы к ячейкам, используя свойства и методы, предлагаемые классом [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell), подробно обсуждаемым ниже.

- Использование встроенных функций.
- Использование функций дополнений.
- Работа с массивными формулами.
- Создание формулы R1C1.

## **Как использовать встроенные функции**

Встроенные функции или формулы предоставляются в виде готовых функций для уменьшения усилий и времени разработчиков. См. [список встроенных функций](/cells/ru/net/supported-formula-functions/), поддерживаемых Aspose.Cells. Функции перечислены в алфавитном порядке. В будущем будут добавлены новые функции.

Aspose.Cells поддерживает большинство формул или функций, предлагаемых Microsoft Excel. Разработчики могут использовать эти формулы через API или [электронные таблицы дизайнера](/cells/ru/net/what-is-a-designer-spreadsheet/). Aspose.Cells поддерживает обширный набор математических, строковых, логических, даты/времени, статистических, баз данных, лукап и ссылочных формул.

Используйте свойство [**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) класса [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) для добавления формулы в ячейку. **Сложные формулы**, например

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, также поддерживаются в Aspose.Cells. Применяя формулу к ячейке, всегда начинайте строку с знака равенства (=), как при создании формулы в Microsoft Excel, и используйте запятую (,) для разделения параметров функции.

В приведенном ниже примере к первой ячейке каталога [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) применяется сложная формула. Формула использует встроенную **Функцию IF**, предоставленную Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **Как использовать функции дополнений**

Может быть необходимо включить в excel пользовательские формулы, которые мы хотим включить в виде добавления. При установке функции cell.Formula встроенные функции работают хорошо, однако требуется установить пользовательские функции или формулы, используя функции дополнений.

Aspose.Cells предоставляет возможности для регистрации функций добавления с помощью [**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). После этого, когда мы устанавливаем cell.Formula = anyFunctionFromAddIn, итоговый файл Excel содержит вычисленное значение из функции AddIn.

Для регистрации функции добавления в приведенном ниже образце кода следует загрузить файл XLAM. Аналогично, файл вывода "test_udf.xlsx" можно загрузить для проверки вывода.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **Как использовать массивную формулу**

Массивные формулы – это формулы, которые принимают массивы в качестве аргументов для функций, составляющих формулу. Когда массивная формула отображается, она окружена фигурными скобками ({}).

Некоторые функции Microsoft Excel возвращают массивы значений. Для вычисления нескольких результатов с помощью массивной формулы введите массив в диапазон ячеек с тем же количеством строк и столбцов, что и аргументы массива.

Возможно применить массивную формулу к ячейке, вызвав метод класса [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) [**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula). Метод [**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) принимает следующие параметры:

- **Массивная Формула**, массивная формула.
- **Количество строк**, количество строк для заполнения результата массивной формулы.
- **Количество столбцов**, количество столбцов для заполнения результата массивной формулы.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **Как использовать формулу R1C1**

Добавить формулу со ссылкой стиля **R1C1** в ячейку с помощью свойства [**R1C1Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) класса [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **Продвинутые темы**
- [Предшественники и зависимые](/cells/ru/net/precedents-and-dependents/)
- [Установка внешних ссылок в формулах](/cells/ru/net/set-external-links-in-formulas/)
- [Распространить формулу в таблице или объекте списка автоматически при вводе данных в новые строки](/cells/ru/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Установка формулы для именованного диапазона](/cells/ru/net/setting-formula-for-named-range/)
- [Установка формул - уведомление для пользователей не на английском языке](/cells/ru/net/setting-formulas-notice-for-non-english-users/)
- [Установка общей формулы](/cells/ru/net/setting-shared-formula/)
- [Укажите максимальное количество строк общей формулы](/cells/ru/net/specify-maximum-rows-of-shared-formula/)
- [Поддерживаемые функции Excel](/cells/ru/net/supported-formula-functions/)

