---
title: Сортировка данных
type: docs
weight: 130
url: /ru/nodejs-cpp/sort-data-of-excel/
description: Узнайте, как сортировать данные, используя API Aspose.Cells for Node.js via C++.
keywords: Сортировка данных в порядке возрастания или убывания, сортировка данных на основе цвета фона
---

{{% alert color="primary" %}}

Сортировка данных — одна из многочисленных полезных функций Microsoft Excel. Она позволяет упорядочить данные, что облегчает их просмотр. Aspose.Cells for Node.js via C++ позволяет разработчикам сортировать данные листа по алфавиту или числовому порядку, так же как это делает Microsoft Excel.

{{% /alert %}}

## **Сортировка данных в Microsoft Excel**

Чтобы отсортировать данные в Microsoft Excel:

1. Выберите **Данные** в меню **Сортировка**. В диалоговом окне сортировки будет отображаться.
1. Выберите вариант сортировки.

Обычно сортировка выполняется в списке - это непрерывная группа данных, отображаемых в столбцах.

## **Сортировка данных с помощью Aspose.Cells**

Aspose.Cells for Node.js via C++ предоставляет класс [**DataSorter**](https://reference.aspose.com/cells/nodejs-cpp/datasorter), используемый для сортировки данных в порядке возрастания или убывания. Этот класс имеет важные члены, например, свойства Key1 ... Key3 и Order1 ... Order3. Эти члены используются для определения ключей сортировки и указания порядка сортировки ключей.

Перед реализацией сортировки данных необходимо определить ключи и установить порядок сортировки. В классе предоставляется метод [**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-), используемый для выполнения сортировки данных на основе данных ячейки на листе таблицы.

Метод [**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-) принимает следующие параметры:

- [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), ячейки для основного листа таблицы.
- [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea), диапазон ячеек. Определите область ячеек перед применением сортировки данных.

В этом примере используется шаблонный файл "Book1.xls", созданный в Microsoft Excel. После выполнения приведенного ниже кода данные сортируются правильно.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataSorting-1.js" >}}

{{% alert color="primary" %}}

Если вы хотите выполнить сортировку *СлеваНаправо*, используйте атрибут [**DataSorter.setSortLeftToRight**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#setSortLeftToRight-boolean-).

{{% /alert %}}

### **Сортировка данных с цветом фона**

Excel предоставляет функции сортировки данных по цвету фона. Та же функция реализована через Aspose.Cells for Node.js via C++ с помощью DataSorter, в котором [**SortOnType**](https://reference.aspose.com/cells/nodejs-cpp/sortontype/).CellColor можно использовать в [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) для сортировки данных по цвету фона. Все ячейки с указанным цветом в [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-), функция помещает сверху или снизу в соответствии с настройкой SortOrder, а порядок остальных ячеек при этом не меняется.

Ниже приведены образцовые файлы, которые можно загрузить для тестирования этой функции:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithBackgroundColor-1.js" >}}

## **Продвинутые темы**
- [Сортировка данных в столбце с пользовательским списком](/cells/ru/nodejs-cpp/sort-data-in-column-with-custom-sort-list/)
- [Указание предупреждения при сортировке данных](/cells/ru/nodejs-cpp/specifying-sort-warning-while-sorting-data/)

