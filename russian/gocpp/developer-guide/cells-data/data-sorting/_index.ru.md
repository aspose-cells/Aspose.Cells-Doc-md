---
title: Сортировка данных с Golang через C++
linktitle: Сортировка данных
type: docs
weight: 130
url: /ru/go-cpp/sort-data-of-excel/
description: Узнайте, как сортировать данные, используя API Aspose.Cells for C++.
keywords: Сортировка данных в порядке возрастания или убывания, сортировка данных на основе цвета фона
---

{{% alert color="primary" %}}

Сортировка данных - одна из многих полезных функций в Microsoft Excel. Она позволяет пользователям упорядочить данные для удобного просмотра. Aspose.Cells позволяет разработчикам сортировать данные на листе таблицы по алфавиту или числовому значению, что работает так же, как в Microsoft Excel.

{{% /alert %}}

## **Сортировка данных в Microsoft Excel**

Чтобы отсортировать данные в Microsoft Excel:

1. Выберите **Данные** в меню **Сортировка**. В диалоговом окне сортировки будет отображаться.
1. Выберите вариант сортировки.

Обычно сортировка выполняется в списке - это непрерывная группа данных, отображаемых в столбцах.

## **Сортировка данных с помощью Aspose.Cells**

Aspose.Cells предоставляет класс [**DataSorter**](https://reference.aspose.com/cells/go-cpp/datasorter/), используемый для сортировки данных в порядке возрастания или убывания. В классе есть некоторые важные члены, например, свойства, такие как Key1 … Key3 и Order1 … Order3. Эти члены используются для определения отсортированных ключей и указания порядка сортировки ключей.

Перед реализацией сортировки данных необходимо определить ключи и установить порядок сортировки. В классе предоставляется метод [**Sort**](https://reference.aspose.com/cells/go-cpp/datasorter/sort_cells_int_int_int_int/), используемый для выполнения сортировки данных на основе данных ячейки на листе таблицы.

Метод [**Sort**](https://reference.aspose.com/cells/go-cpp/datasorter/sort_cells_int_int_int_int/) принимает следующие параметры:

- [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/), ячейки для основного листа таблицы.
- [**CellArea**](https://reference.aspose.com/cells/go-cpp/cellarea/), диапазон ячеек. Определите область ячеек перед применением сортировки данных.

В этом примере используется шаблонный файл "Book1.xls", созданный в Microsoft Excel. После выполнения приведенного ниже кода данные сортируются правильно.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSorting.go" >}}
{{% alert color="primary" %}}

Если вы хотите выполнить сортировку *СлеваНаправо*, используйте атрибут [**DataSorter.GetSortLeftToRight()**](https://reference.aspose.com/cells/go-cpp/datasorter/getsortlefttoright/).

{{% /alert %}}

### **Сортировка данных с цветом фона**

Excel предоставляет функции для сортировки данных на основе цвета фона. Та же функция предоставляется с использованием Aspose.Cells с помощью DataSorter, где [**SortOnType**](https://reference.aspose.com/cells/go-cpp/sortontype/).CellColor может быть использован в [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) для сортировки данных на основе цвета фона. Все ячейки, которые содержат указанный цвет в [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/), функции размещаются в начале или в конце в зависимости от установок SortOrder, и порядок остальных ячеек вообще не изменяется.

Ниже приведены образцовые файлы, которые можно загрузить для тестирования этой функции:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSorting-1.go" >}}
## **Продвинутые темы**
- [Сортировка данных в столбце с пользовательским списком](/cells/ru/cpp/sort-data-in-column-with-custom-sort-list/)
- [Указание предупреждения при сортировке данных](/cells/ru/cpp/specifying-sort-warning-while-sorting-data/)
