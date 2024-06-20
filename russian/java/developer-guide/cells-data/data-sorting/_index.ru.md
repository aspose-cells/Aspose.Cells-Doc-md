---
title: Сортировка данных
type: docs
weight: 90
url: /ru/java/sort-data-of-excel/
---

{{% alert color="primary" %}}

Сортировка данных - одна из многих полезных функций Microsoft Excel. Она позволяет пользователям упорядочивать данные для удобного сканирования.

Aspose.Cells позволяет сортировать данные листа таблицы по алфавиту или числовому значению. Он работает так же, как и Microsoft Excel, чтобы упорядочить данные.

{{% /alert %}}

## **Сортировка данных в Microsoft Excel**

Чтобы отсортировать данные в Microsoft Excel:

1. Выберите **Данные** из меню **Сортировка**.
   Отобразится диалоговое окно сортировки.
1. Выберите вариант сортировки.

Обычно сортировка выполняется в списке - это непрерывная группа данных, отображаемых в столбцах.

**Диалоговое окно сортировки в Microsoft Excel**

![todo:image_alt_text](data-sorting_1.png)

## **Сортировка данных с помощью Aspose.Cells**

Aspose.Cells предоставляет класс [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter), используемый для сортировки данных по возрастанию или убыванию. У класса есть некоторые важные члены, например методы, такие как [**setKey1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1) ... [**setKey2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2) и [**setOrder1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1) ... [**setOrder2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2). Эти члены используются для определения отсортированных ключей и указания порядка сортировки ключей.

Перед реализацией сортировки данных необходимо определить ключи и установить порядок сортировки. В классе предоставляется метод [**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--), используемый для выполнения сортировки данных на основе данных ячейки на листе таблицы.

Метод [**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--) принимает следующие параметры:

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), ячейки листа.
- [**CellArea**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea), диапазон ячеек. Определите область ячеек перед применением сортировки данных.

В этом примере показано, как сортировать данные с помощью Aspose.Cells API. В примере используется файл-шаблон "Book1.xls", и данные для диапазона данных (A1:B14) сортируются на первом листе:

В этом примере используется файл шаблона "Book1.xls", созданный в Microsoft Excel.

**Файл Excel-шаблон с данными**

![todo:image_alt_text](data-sorting_2.png)

После выполнения приведенного ниже кода данные сортируются должным образом, как видно из выходного файла Excel.

**Выходной файл Excel после сортировки данных**

![todo:image_alt_text](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

Для сортировки *слева направо*, используйте атрибут [**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight).

{{% /alert %}}

## **Сортировка данных с цветом фона**

Excel предоставляет возможность сортировки данных на основе цвета фона. Ту же функциональность можно использовать с помощью Aspose.Cells, используя [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter), где [**SortOnType.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL_COLOR) может быть использован в [**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int)) для сортировки данных на основе цвета фона. Все ячейки, которые содержат указанный цвет в [**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int)) функции, размещаются вверху или внизу в соответствии с установкой SortOrder, и порядок остальных ячеек совершенно не изменяется.

Ниже приведены образцовые файлы, которые можно загрузить для тестирования этой функции:

[sampleBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[outputsampleBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **Продвинутые темы**
- [Сортировка данных в столбце с пользовательским списком](/cells/ru/java/sort-data-in-column-with-custom-sort-list/)
- [Указание предупреждения при сортировке данных](/cells/ru/java/specifying-sort-warning-while-sorting-data/)

