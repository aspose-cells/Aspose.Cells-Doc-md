---
title: Управление формулами файлов Excel
linktitle: Формулы
type: docs
weight: 122
url: /ru/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells может просто получать, устанавливать и вычислять формулы файлов Excel.
description: Узнайте, как управлять формулами файлов Excel с помощью API-интерфейсов Aspose.Cells для NET.
keywords: How to calculate formulas in C#, Formulas and Functions using C#, C# Manage Built-in Functions, How to Use Add-in Functions with C#, How to Use Array Formula via C#, How to Use R1C1 Formula in C#.
---
##  **Введение**

Одной из Microsoft привлекательных особенностей Excel является его способность обрабатывать данные с помощью формул и функций. Microsoft Excel предоставляет набор встроенных функций и формул, которые помогают пользователям быстро выполнять сложные вычисления. Aspose.Cells также предоставляет огромный набор встроенных функций и формул, которые помогают разработчикам легко вычислять значения. Aspose.Cells также поддерживает дополнительные функции. Кроме того, Aspose.Cells поддерживает массив и формулы R1C1 в Aspose.Cells.

##  **Как использовать формулы и функции**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , который представляет файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс обеспечивает[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция. Каждый элемент коллекции Cells представляет собой объект[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) сорт.

 К ячейкам можно применять формулы, используя свойства и методы, предлагаемые[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) класс, более подробно обсуждаемый ниже.

- Использование встроенных функций.
- Использование дополнительных функций.
- Работа с формулами массива.
- Создание формулы R1C1.

##  **Как использовать встроенные функции**

Встроенные функции или формулы предоставляются в виде готовых функций, что позволяет сократить усилия и время разработчиков. Видеть[список встроенных функций](/cells/ru/net/supported-formula-functions/) поддерживается по номеру Aspose.Cells. Функции перечислены в алфавитном порядке. В будущем будет поддерживаться больше функций.

 Aspose.Cells поддерживает большинство формул и функций, предлагаемых Microsoft Excel. Разработчики могут использовать эти формулы по телефону API или[дизайнерская таблица](/cells/ru/net/what-is-a-designer-spreadsheet/). Aspose.Cells поддерживает огромный набор математических, строковых, логических формул, формул даты/времени, статистических, баз данных, формул поиска и справочных формул.

 Использовать[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) сорт'[**Формула**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) свойство для добавления формулы в ячейку. *Сложные формулы**, например

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, также поддерживаются в Aspose.Cells. При применении формулы к ячейке всегда начинайте строку со знака равенства (=), как при создании формулы в Excel Microsoft, и используйте запятую (,) для разделения параметров функции.

 В примере ниже сложная формула применяется к первой ячейке рабочего листа.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)коллекция. В формуле используется встроенный**IF** функция предоставлена номером Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

##  **Как использовать функции надстройки**

У нас могут быть определенные пользователем формулы, которые мы хотим включить в качестве надстройки Excel. При настройке функции cell.Formula встроенные функции работают нормально, однако необходимо установить пользовательские функции или формулы с помощью функций надстройки.

 Aspose.Cells предоставляет возможности для регистрации дополнительных функций с помощью[**Рабочие листы.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). После этого, когда мы устанавливаем cell.Formula = AnyFunctionFromAddIn, выходной файл Excel содержит вычисленное значение из функции AddIn.

Следующий файл XLAM должен быть загружен для регистрации функции добавления в приведенном ниже примере кода. Аналогичным образом можно загрузить выходной файл «test_udf.xlsx», чтобы проверить выходные данные.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

##  **Как использовать формулу массива**

Формулы массива — это формулы, которые принимают массивы вместо отдельных чисел в качестве аргументов функций, составляющих формулу. Когда отображается формула массива, она заключена в фигурные скобки ({}).

Некоторые Microsoft функции Excel возвращают массивы значений. Чтобы вычислить несколько результатов с помощью формулы массива, введите массив в диапазон ячеек с тем же количеством строк и столбцов, что и аргументы массива.

 К ячейке можно применить формулу массива, вызвав метод[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) сорт'[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) метод.[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) метод принимает следующие параметры:

- *Формула массива**, формула массива.
- *Количество строк** — количество строк для заполнения результата формулы массива.
- *Количество столбцов** — количество столбцов, в которые будет заполнен результат формулы массива.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

##  **Как использовать формулу R1C1**

 Добавить**R1C1** формула стиля ссылки на ячейку с[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) сорт'[**R1C1Формула**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) свойство.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

##  **Предварительные темы**
- [Прецеденты и зависимые люди](/cells/ru/net/precedents-and-dependents/)
- [Установка внешних ссылок в формулах](/cells/ru/net/set-external-links-in-formulas/)
- [Автоматическое распространение формулы в объекте таблицы или списка при вводе данных в новые строки](/cells/ru/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Установка формулы для именованного диапазона](/cells/ru/net/setting-formula-for-named-range/)
- [Настройка формул — уведомление для пользователей, не владеющих английским языком](/cells/ru/net/setting-formulas-notice-for-non-english-users/)
- [Настройка общей формулы](/cells/ru/net/setting-shared-formula/)
- [Укажите максимальное количество строк общей формулы](/cells/ru/net/specify-maximum-rows-of-shared-formula/)
- [Поддерживаемые функции Excel](/cells/ru/net/supported-formula-functions/)

