---
title: Сортировка данных
type: docs
weight: 130
url: /ru/python-net/sort-data-of-excel/
description: Узнайте, как сортировать данные с использованием API Aspose.Cells for for Python via .NET.
keywords: Python Excel библиотека, Сортировка данных в Python по возрастанию или убыванию, Сортировка данных в Python на основе цвета фона.
---

{{% alert color="primary" %}}

Сортировка данных - одна из множества полезных функций Microsoft Excel. Она позволяет пользователям упорядочивать данные для удобства сканирования. Aspose.Cells для Python via .NET позволяет разработчикам сортировать данные на листе таблицы алфавитно или числовым способом, что работает так же, как и в Microsoft Excel для сортировки данных.

{{% /alert %}}

## **Сортировка данных в Microsoft Excel**

Чтобы отсортировать данные в Microsoft Excel:

1. Выберите **Данные** в меню **Сортировка**. В диалоговом окне сортировки будет отображаться.
1. Выберите вариант сортировки.

Обычно сортировка выполняется в списке - это непрерывная группа данных, отображаемых в столбцах.

## **Сортировка данных с помощью Aspose.Cells для Python Excel библиотеки**

Aspose.Cells для Python via .NET предоставляет класс [**DataSorter**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter), используемый для сортировки данных по возрастанию или убыванию. В классе есть важные члены, например, свойства, такие как Key1 ... Key3 и Order1 ... Order3. Эти члены используются для определения ключевых значений сортировки и установки порядка сортировки ключей.

Перед реализацией сортировки данных необходимо определить ключи и установить порядок сортировки. В классе предоставляется метод [**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea), используемый для выполнения сортировки данных на основе данных ячейки на листе таблицы.

Метод [**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea) принимает следующие параметры:

- [**aspose.cells.Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), ячейки для основного листа таблицы.
- [**aspose.cells.CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea), диапазон ячеек. Определите область ячеек перед применением сортировки данных.

В этом примере используется шаблонный файл "Book1.xls", созданный в Microsoft Excel. После выполнения приведенного ниже кода данные сортируются правильно.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DataSorting-1.py" >}}

{{% alert color="primary" %}}

Если вы хотите выполнить сортировку *СлеваНаправо*, используйте атрибут [**DataSorter.sort_left_to_right**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_left_to_right/).

{{% /alert %}}

### **Сортировка данных с использованием цвета фона с помощью Aspose.Cells для Python Excel библиотеки**

Excel предоставляет функции сортировки данных на основе цвета фона. Ту же функцию можно использовать с помощью Aspose.Cells для Python via .NET с помощью DataSorter, где [**SortOnType**](https://reference.aspose.com/cells/python-net/aspose.cells/sortontype/). CellColor может быть использован в [**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any) для сортировки данных на основе цвета фона. Все ячейки, которые содержат указанный цвет в функции [**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any), располагаются вверху или внизу в соответствии с настройкой порядка сортировки, и порядок остальных ячеек не изменяется вовсе.

Ниже приведены образцовые файлы, которые можно загрузить для тестирования этой функции:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithBackgroundColor-1.py" >}}

## **Продвинутые темы**
- [Сортировка данных в столбце с пользовательским списком](/cells/ru/python-net/sort-data-in-column-with-custom-sort-list/)
- [Указание предупреждения при сортировке данных](/cells/ru/python-net/specifying-sort-warning-while-sorting-data/)
{{< app/cells/assistant language="python-net" >}}
