---
title: Управление формулами файлов Excel
linktitle: Формулы
type: docs
weight: 122
url: /ru/python-net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells для Python via .NET может просто получать, устанавливать и вычислять формулы в файлах Excel.
description: Узнайте, как управлять формулами в файлах Excel через API Aspose.Cells для Python via .NET для NET.
keywords: Как вычислять формулы в Python, формулы и функции с помощью Python, управление встроенными функциями Python, использование надстроек функций с Python, использование массивных формул через Python, использование формул R1C1 в Python.
---

## **Введение**

Одной из впечатляющих функций Microsoft Excel является его способность обрабатывать данные с помощью формул и функций. Microsoft Excel предоставляет набор встроенных функций и формул, которые помогают пользователям быстро выполнять сложные расчеты. Aspose.Cells для Python via .NET также предоставляет большой набор встроенных функций и формул, которые помогают разработчикам легко вычислять значения. Aspose.Cells для Python via .NET также поддерживает надстройки функций. Более того, Aspose.Cells для Python via .NET поддерживает массивные и формулы R1C1.

## **Как использовать формулы и функции**

Aspose.Cells для Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), которая обеспечивает доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) обеспечивает коллекцию [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Каждый элемент в коллекции Cells представляет объект класса [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Можно применять формулы к ячейкам, используя свойства и методы, предлагаемые классом [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell), подробно обсуждаемым ниже.

- Использование встроенных функций.
- Использование функций дополнений.
- Работа с массивными формулами.
- Создание формулы R1C1.

## **Как использовать встроенные функции**

Встроенные функции или формулы предоставляются в виде готовых функций, чтобы снизить усилия и время разработчиков. См. [список встроенных функций](/cells/ru/python-net/supported-formula-functions/), поддерживаемых Aspose.Cells для Python via .NET. Функции перечислены в алфавитном порядке. В будущем будет поддерживаться больше функций.

Aspose.Cells для Python via .NET поддерживает большинство формул или функций, предлагаемых Microsoft Excel. Разработчики могут использовать эти формулы через API или [конструктор таблиц](/cells/ru/net/what-is-a-designer-spreadsheet/). Aspose.Cells для Python via .NET поддерживает большой набор математических, строковых, логических, дат/времени, статистических, баз данных, поиска и ссылочных формул.

Используйте свойство [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula) класса [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) для добавления формулы в ячейку. **Сложные формулы**, например

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, также поддерживаются в Aspose.Cells для Python via .NET. При применении формулы к ячейке всегда начинайте строку с знака равенства (=), как при создании формулы в Microsoft Excel, и используйте запятую (,) для разделения параметров функции.

В следующем примере к первой ячейке коллекции [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) рабочего листа применяется сложная формула. Формула использует встроенную функцию **IF**, предоставляемую Aspose.Cells для Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingBuiltinfunction-1.py" >}}

## **Как использовать функции дополнений**

Может быть необходимо включить в excel пользовательские формулы, которые мы хотим включить в виде добавления. При установке функции cell.Formula встроенные функции работают хорошо, однако требуется установить пользовательские функции или формулы, используя функции дополнений.

Aspose.Cells для Python via .NET предоставляет функции для регистрации надстроек функций с помощью [**worksheets.register_add_in_function()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/register_add_in_function). После этого, когда мы устанавливаем cell.Formula = anyFunctionFromAddIn, итоговый файл Excel содержит вычисленное значение из функции надстройки.

Для регистрации функции добавления в приведенном ниже образце кода следует загрузить файл XLAM. Аналогично, файл вывода "test_udf.xlsx" можно загрузить для проверки вывода.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-RegisterAndCallFuncFromAddIn-1.py" >}}

## **Как использовать массивную формулу**

Массивные формулы – это формулы, которые принимают массивы в качестве аргументов для функций, составляющих формулу. Когда массивная формула отображается, она окружена фигурными скобками ({}).

Некоторые функции Microsoft Excel возвращают массивы значений. Для вычисления нескольких результатов с помощью массивной формулы введите массив в диапазон ячеек с тем же количеством строк и столбцов, что и аргументы массива.

Возможно применить массивную формулу к ячейке, вызвав метод класса [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) [**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula). Метод [**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula) принимает следующие параметры:

- **Массивная Формула**, массивная формула.
- **Количество строк**, количество строк для заполнения результата массивной формулы.
- **Количество столбцов**, количество столбцов для заполнения результата массивной формулы.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingArrayFunction-1.py" >}}

## **Как использовать формулу R1C1**

Добавить формулу со ссылкой стиля **R1C1** в ячейку с помощью свойства [**r1c1_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/r1c1_formula) класса [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingR1C1-1.py" >}}

## **Продвинутые темы**
- [Предшественники и зависимые](/cells/ru/python-net/precedents-and-dependents/)
- [Установка внешних ссылок в формулах](/cells/ru/python-net/set-external-links-in-formulas/)
- [Распространить формулу в таблице или объекте списка автоматически при вводе данных в новые строки](/cells/ru/python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Установка формулы для именованного диапазона](/cells/ru/python-net/setting-formula-for-named-range/)
- [Установка формул - уведомление для пользователей не на английском языке](/cells/ru/python-net/setting-formulas-notice-for-non-english-users/)
- [Установка общей формулы](/cells/ru/python-net/setting-shared-formula/)
- [Укажите максимальное количество строк общей формулы](/cells/ru/python-net/specify-maximum-rows-of-shared-formula/)
- [Поддерживаемые функции Excel](/cells/ru/python-net/supported-formula-functions/)


{{< app/cells/assistant language="python-net" >}}
