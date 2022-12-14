---
title: Управление формулами файлов Excel
linktitle: Формулы
type: docs
weight: 122
url: /ru/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells может просто получить, установить и вычислить формулы файлов Excel.
---
## **Введение**

Одной из привлекательных особенностей Excel Microsoft является его способность обрабатывать данные с помощью формул и функций. Microsoft Excel предоставляет набор встроенных функций и формул, которые помогают пользователям быстро выполнять сложные вычисления. Aspose.Cells также предоставляет огромный набор встроенных функций и формул, которые помогают разработчикам легко вычислять значения. Aspose.Cells также поддерживает дополнительные функции. Кроме того, Aspose.Cells поддерживает массив и формулы R1C1 в Aspose.Cells.

## **Использование формул и функций**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс предоставляет[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция. Каждый элемент коллекции Cells представляет собой объект[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) учебный класс.

 Можно применять формулы к ячейкам, используя свойства и методы, предлагаемые[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) класс, более подробно обсуждаемый ниже.

- Использование встроенных функций.
- Использование дополнительных функций.
- Работа с формулами массива.
- Создание формулы R1C1.

## **Использование встроенных функций**

 Встроенные функции или формулы предоставляются в виде готовых функций, чтобы сократить усилия и время разработчиков. Видеть[список встроенных функций](/cells/ru/net/supported-formula-functions/) поддерживается по номеру Aspose.Cells. Функции перечислены в алфавитном порядке. В будущем будет поддерживаться больше функций.

 Aspose.Cells поддерживает большинство формул или функций, предлагаемых Microsoft Excel. Разработчики могут использовать эти формулы через API или[дизайнерская таблица](/cells/ru/net/what-is-a-designer-spreadsheet/). Aspose.Cells поддерживает огромный набор математических, строковых, логических, дат/времени, статистических, баз данных, поисковых и справочных формул.

 Использовать[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) учебный класс'[**Формула**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)свойство для добавления формулы в ячейку.**Сложные формулы**, Например

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, также поддерживаются в Aspose.Cells. При применении формулы к ячейке всегда начинайте строку со знака равенства (=), как при создании формулы в Microsoft Excel, и используйте запятую (,) для разделения параметров функции.

 В приведенном ниже примере сложная формула применяется к первой ячейке рабочего листа.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция. В формуле используется встроенный**ЕСЛИ** Функция предоставлена Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **Использование дополнительных функций**

У нас могут быть некоторые пользовательские формулы, которые мы хотим включить в качестве надстройки Excel. При настройке функции cell.Formula встроенные функции работают нормально, однако необходимо установить пользовательские функции или формулы с помощью дополнительных функций.

 Aspose.Cells предоставляет возможности для регистрации дополнительных функций с использованием[**Рабочие листы.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). Впоследствии, когда мы устанавливаем cell.Formula = anyFunctionFromAddIn, выходной файл Excel содержит вычисленное значение из функции AddIn.

Для регистрации функции надстройки в приведенном ниже примере кода необходимо загрузить следующий файл XLAM. Точно так же можно загрузить выходной файл «test_udf.xlsx» для проверки вывода.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **Использование формулы массива**

Формулы массива — это формулы, которые принимают массивы вместо отдельных чисел в качестве аргументов функций, составляющих формулу. Когда отображается формула массива, она заключена в фигурные скобки ({}).

Некоторые функции Excel Microsoft возвращают массивы значений. Чтобы вычислить несколько результатов с помощью формулы массива, введите массив в диапазон ячеек с тем же количеством строк и столбцов, что и аргументы массива.

 Формулу массива можно применить к ячейке, вызвав метод[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) учебный класс'[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) метод.[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) метод принимает следующие параметры:

- **Формула массива**, формула массива.
- **Количество рядов**количество строк для заполнения результата формулы массива.
- **Число столбцов**количество столбцов для заполнения результата формулы массива.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **Использование формулы R1C1**

 Добавить**R1C1** формула стиля ссылки на ячейку с[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) учебный класс'[**R1C1Формула**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) имущество.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **Предварительные темы**
- [Прецеденты и иждивенцы](/cells/ru/net/precedents-and-dependents/)
- [Установить внешние ссылки в формулах](/cells/ru/net/set-external-links-in-formulas/)
- [Автоматическое распространение формулы в таблице или объекте списка при вводе данных в новые строки](/cells/ru/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Формула настройки для именованного диапазона](/cells/ru/net/setting-formula-for-named-range/)
- [Настройка формул — уведомление для пользователей, не владеющих английским языком](/cells/ru/net/setting-formulas-notice-for-non-english-users/)
- [Настройка общей формулы](/cells/ru/net/setting-shared-formula/)
- [Укажите максимальное количество строк общей формулы](/cells/ru/net/specify-maximum-rows-of-shared-formula/)
- [Поддерживаемые функции Excel](/cells/ru/net/supported-formula-functions/)

