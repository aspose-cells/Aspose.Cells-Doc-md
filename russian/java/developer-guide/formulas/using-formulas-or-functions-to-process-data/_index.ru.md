---
title: Использование формул или функций для обработки данных
type: docs
weight: 5
url: /ru/java/get-and-set-formula/
---

{{% alert color="primary" %}}

Одной из убедительных особенностей Microsoft Excel является его способность обрабатывать данные с помощью формул и функций. Microsoft Excel предоставляет набор встроенных функций и формул, которые помогают пользователям быстро выполнять сложные вычисления. Aspose.Cells также предоставляет огромный набор встроенных функций и формул, которые помогают разработчикам легко вычислять значения. Кроме того, Aspose.Cells поддерживает функции дополнений. Кроме того, Aspose.Cells поддерживает массивные и R1C1 формулы в Aspose.Cells.

{{% /alert %}}

## **Использование формул и функций**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets), которая позволяет получить доступ к каждому листу книги Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). Каждый элемент в коллекции [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) представляет объект класса [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Можно применять формулы к ячейкам с использованием свойств и методов, предлагаемых классом [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell), о котором подробнее рассказано ниже.

- [Использование встроенных функций](/cells/ru/java/using-formulas-or-functions-to-process-data/#using-built-in-functions).
- [Использование функций дополнений](/cells/ru/java/using-formulas-or-functions-to-process-data/#using-add-in-functions).
- [Работа с массивными формулами](/cells/ru/java/using-formulas-or-functions-to-process-data/#using-array-formula)
- [Создание формулы R1C1](/cells/ru/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula).

## **Использование встроенных функций**

Встроенные функции или формулы предоставляются в виде готовых функций для уменьшения усилий и времени разработчиков. См. [список встроенных функций](/cells/ru/java/supported-formula-functions/). Функции перечислены в алфавитном порядке. Будут поддерживаться дополнительные функции в будущем.

Aspose.Cells поддерживает большинство формул или функций, предлагаемых Microsoft Excel. Разработчики могут использовать эти формулы через API или [электронную таблицу дизайнера](/cells/ru/java/what-is-a-designer-spreadsheet/). Aspose.Cells поддерживает огромный набор математических, строковых, логических, даты/времени, статистических, баз данных, поиска и ссылочных формул.

Используйте свойство [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) класса [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) для добавления формулы в ячейку. **Сложные формулы**, например

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, также поддерживаются в Aspose.Cells. Применяя формулу к ячейке, всегда начинайте строку с знака равенства (=), как при создании формулы в Microsoft Excel, и используйте запятую (,) для разделения параметров функции.

В приведенном ниже примере к первой ячейке коллекции [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) рабочего листа применяется сложная формула. Формула использует встроенную функцию **IF**, предоставленную Aspose.Cells.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **Использование Дополнительных Функций**

Мы можем иметь некоторые пользовательские формулы, которые мы хотим включить как дополнение Excel. При установке [**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) встроенные функции работают нормально, однако есть необходимость установить пользовательские функции или формулы с помощью дополнительных функций.

Aspose.Cells предоставляет возможность зарегистрировать дополнительные функции, используя [**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction-java.lang.String-java.lang.String-boolean-). После того как мы установим [**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) = anyFunctionFromAddIn, выходной файл Excel будет содержать вычисленное значение из функции AddIn.

Для регистрации функции дополнения в приведенном ниже образцовом коде следует загрузить файл XLAM. Аналогично, выходной файл "test_udf.xlsx" можно загрузить для проверки вывода.

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **Использование Массивной Формулы**

Массивные формулы - это формулы, которые работают с массивами, а не с отдельными числами, как аргументами для функций, составляющих формулу. Когда массивная формула отображается, она окружается фигурными скобками ({}) как показано ниже.

**Установка массивной формулы на ячейку G2** 

![todo:image_alt_text](using-formulas-or-functions-to-process-data_1.png)

Некоторые функции Microsoft Excel возвращают массивы значений. Для вычисления нескольких результатов с помощью массивной формулы введите массив в диапазон ячеек с тем же количеством строк и столбцов, что и аргументы массива.

Возможно применить массивную формулу к ячейке, вызвав метод класса [**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula-java.lang.String-int-int-). Метод [**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula-java.lang.String-int-int-) принимает следующие параметры:

- **Массивная Формула**, массивная формула.
- **Количество строк**, количество строк для заполнения результата массивной формулы.
 - **Количество столбцов**, количество столбцов для заполнения результата массивной формулы.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **Использование формулы R1C1**

Примените формулу стиля ссылки R1C1 к ячейке с [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) классом [**setR1C1Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula) свойства.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

{{< app/cells/assistant language="java" >}}
