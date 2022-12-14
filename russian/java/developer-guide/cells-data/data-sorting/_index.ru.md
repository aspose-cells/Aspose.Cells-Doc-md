---
title: Сортировка данных
type: docs
weight: 90
url: /ru/java/sort-data-of-excel/
---
{{% alert color="primary" %}}

Сортировка данных — одна из многих полезных функций Excel. Это позволяет пользователям упорядочивать данные, чтобы их было легче сканировать.

Aspose.Cells позволяет сортировать данные рабочего листа в алфавитном или числовом порядке. Он работает так же, как Microsoft Excel для сортировки данных.

{{% /alert %}}

## **Сортировка данных в Microsoft Excel**

Чтобы отсортировать данные в Microsoft Excel:

1.  Выбирать**Данные** от**Сортировать** меню.
 Появится диалоговое окно Сортировка.
1. Выберите вариант сортировки.

Как правило, сортировка выполняется в списке, определяемом как непрерывная группа данных, где данные отображаются в столбцах.

**Диалоговое окно «Сортировка» в Microsoft Excel**

![дело:изображение_альтернативный_текст](data-sorting_1.png)

## **Сортировка данных с Aspose.Cells**

 Aspose.Cells обеспечивает[**сортировщик данных**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) класс, используемый для сортировки данных в порядке возрастания или убывания. В классе есть несколько важных членов, например такие методы, как[**setKey1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1) ... [**setKey2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2) а также[**setOrder1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1) ... [**setOrder2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2)Эти элементы используются для определения отсортированных ключей и порядка сортировки ключей.

 Вы должны определить ключи и установить порядок сортировки перед реализацией сортировки данных. Класс предоставляет[**Сортировать**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()) метод, используемый для сортировки данных на основе данных ячеек на листе.

[**Сортировать**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()) принимает следующие параметры:

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), ячейки рабочего листа.
- [**CellArea**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea), диапазон ячеек. Определите область ячейки перед применением сортировки данных.

В этом примере показано, как сортировать данные с помощью Aspose.Cells API. В примере используется файл шаблона «Book1.xls» и данные сортируются по диапазону данных (A1:B14) на первом листе:

В этом примере используется файл шаблона «Book1.xls», созданный в Microsoft Excel.

**Шаблон файла Excel с данными**

![дело:изображение_альтернативный_текст](data-sorting_2.png)

После выполнения приведенного ниже кода данные сортируются соответствующим образом, как видно из выходного файла Excel.

**Выходной файл Excel после сортировки данных**

![дело:изображение_альтернативный_текст](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

 Сортировать*Слева направо* , использовать[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight) атрибут.

{{% /alert %}}

## **Сортировка данных по цвету фона**

 Excel предоставляет функцию сортировки данных по цвету фона. Та же функция предоставляется с использованием Aspose.Cells с использованием[**сортировщик данных**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) куда[**Сортировка по типу.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL_COLOR) можно использовать в[**добавить ключ()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int) ) для сортировки данных по цвету фона. Все ячейки, содержащие указанный цвет в[**добавить ключ()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int)), функция размещается сверху или снизу в соответствии с настройкой SortOrder, а порядок остальных ячеек вообще не меняется.

Ниже приведены примеры файлов, которые можно загрузить для тестирования этой функции:

[образецBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[outputsampleBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **Предварительные темы**
- [Сортировка данных в столбце с пользовательским списком сортировки](/cells/ru/java/sort-data-in-column-with-custom-sort-list/)
- [Указание предупреждения о сортировке при сортировке данных](/cells/ru/java/specifying-sort-warning-while-sorting-data/)

