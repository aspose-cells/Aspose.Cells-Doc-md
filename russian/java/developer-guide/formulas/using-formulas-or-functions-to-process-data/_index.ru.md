---
title: Использование формул или функций для обработки данных
type: docs
weight: 5
url: /ru/java/get-and-set-formula/
---
{{% alert color="primary" %}}

Одной из привлекательных особенностей Excel Microsoft является его способность обрабатывать данные с помощью формул и функций. Microsoft Excel предоставляет набор встроенных функций и формул, которые помогают пользователям быстро выполнять сложные вычисления. Aspose.Cells также предоставляет огромный набор встроенных функций и формул, которые помогают разработчикам легко вычислять значения. Aspose.Cells также поддерживает дополнительные функции. Кроме того, Aspose.Cells поддерживает массив и формулы R1C1 в Aspose.Cells.

{{% /alert %}}

## **Использование формул и функций**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) класс предоставляет[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) коллекция. Каждый элемент в[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) коллекция представляет собой объект[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)учебный класс.

 Можно применять формулы к ячейкам, используя свойства и методы, предлагаемые[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)класс, более подробно обсуждаемый ниже.

- [Использование встроенных функций](/cells/ru/java/using-formulas-or-functions-to-process-data/#using-built-in-functions).
- [Использование дополнительных функций](/cells/ru/java/using-formulas-or-functions-to-process-data/#using-add-in-functions).
- [Работа с формулами массива](/cells/ru/java/using-formulas-or-functions-to-process-data/#using-array-formula).
- [Создание формулы R1C1](/cells/ru/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula).

## **Использование встроенных функций**

 Встроенные функции или формулы предоставляются в виде готовых функций, чтобы сократить усилия и время разработчиков. Видеть[список встроенных функций](/cells/ru/java/supported-formula-functions/). Функции перечислены в алфавитном порядке. В будущем будет поддерживаться больше функций.

 Aspose.Cells поддерживает большинство формул или функций, предлагаемых Microsoft Excel. Разработчики могут использовать эти формулы через API или[дизайнерская таблица](/cells/ru/java/what-is-a-designer-spreadsheet/). Aspose.Cells поддерживает огромный набор математических, строковых, логических, дат/времени, статистических, баз данных, поисковых и справочных формул.

 Использовать[**Формула**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)собственность[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) класс, чтобы добавить формулу в ячейку.**Сложные формулы**, Например

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, также поддерживаются в Aspose.Cells. При применении формулы к ячейке всегда начинайте строку со знака равенства (=), как при создании формулы в Microsoft Excel, и используйте запятую (,) для разделения параметров функции.

 В приведенном ниже примере сложная формула применяется к первой ячейке рабочего листа.[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) коллекция. В формуле используется встроенный**ЕСЛИ** Функция предоставлена Aspose.Cells.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **Использование дополнительных функций**

 У нас могут быть некоторые пользовательские формулы, которые мы хотим включить в качестве надстройки Excel. При установке[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) Встроенные функции работают нормально, однако необходимо установить пользовательские функции или формулы с помощью дополнительных функций.

 Aspose.Cells предоставляет возможности для регистрации дополнительных функций с использованием[**Рабочие листы.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction(java.lang.String,%20java.lang.String,%20boolean)). После этого, когда мы установили[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) anyFunctionFromAddIn, выходной файл Excel содержит вычисленное значение из функции AddIn.

После этого необходимо загрузить файл XLAM для регистрации функции надстройки в приведенном ниже образце кода. Точно так же можно загрузить выходной файл «test_udf.xlsx» для проверки вывода.

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **Использование формулы массива**

Формулы массива — это формулы, которые работают с массивами, а не с отдельными числами, в качестве аргументов функций, составляющих формулу. Когда отображается формула массива, она заключена в фигурные скобки ({}), как показано ниже.

**Установка формулы массива в ячейке G2** 

![дело:изображение_альтернативный_текст](using-formulas-or-functions-to-process-data_1.png)

Некоторые функции Excel Microsoft возвращают массивы значений. Чтобы вычислить несколько результатов с помощью формулы массива, введите массив в диапазон ячеек с тем же количеством строк и столбцов, что и аргументы массива.

 Формулу массива можно применить к ячейке, вызвав метод[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) учебный класс'[**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int) ) метод.[**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int)) принимает следующие параметры:

- **Формула массива**формула массива.
- **Количество рядов**, количество строк для заполнения результата формулы массива.
- **Число столбцов**, количество столбцов для заполнения результата формулы массива.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **Использование формулы R1C1**

 Применить**R1C1** формула стиля ссылки на ячейку с[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) учебный класс'[**setR1C1Формула**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula)имущество.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

