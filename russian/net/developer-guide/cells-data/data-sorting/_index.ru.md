---
title: Сортировка данных
type: docs
weight: 130
url: /ru/net/sort-data-of-excel/
description: Узнайте, как сортировать данные с помощью Aspose.Cells for .NET API.
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

Aspose.Cells предоставляет класс [**DataSorter**](https://reference.aspose.com/cells/net/aspose.cells/datasorter), используемый для сортировки данных в порядке возрастания или убывания. В классе есть некоторые важные члены, например, свойства, такие как Key1 … Key3 и Order1 … Order3. Эти члены используются для определения отсортированных ключей и указания порядка сортировки ключей.

Перед реализацией сортировки данных необходимо определить ключи и установить порядок сортировки. В классе предоставляется метод [**Sort**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index), используемый для выполнения сортировки данных на основе данных ячейки на листе таблицы.

Метод [**Sort**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1) принимает следующие параметры:

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), ячейки для основного листа таблицы.
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea), диапазон ячеек. Определите область ячеек перед применением сортировки данных.

В этом примере используется шаблонный файл "Book1.xls", созданный в Microsoft Excel. После выполнения приведенного ниже кода данные сортируются правильно.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

Если вы хотите выполнить сортировку *СлеваНаправо*, используйте атрибут [**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright).

{{% /alert %}}

### **Сортировка данных с цветом фона**

Excel предоставляет функции для сортировки данных на основе цвета фона. Та же функция предоставляется с использованием Aspose.Cells с помощью DataSorter, где [**SortOnType**](https://reference.aspose.com/cells/net/aspose.cells/sortontype).CellColor может быть использован в [**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey) для сортировки данных на основе цвета фона. Все ячейки, которые содержат указанный цвет в [**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey), функции размещаются в начале или в конце в зависимости от установок SortOrder, и порядок остальных ячеек вообще не изменяется.

Ниже приведены образцовые файлы, которые можно загрузить для тестирования этой функции:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

## **Продвинутые темы**
- [Сортировка данных в столбце с пользовательским списком](/cells/ru/net/sort-data-in-column-with-custom-sort-list/)
- [Указание предупреждения при сортировке данных](/cells/ru/net/specifying-sort-warning-while-sorting-data/)
{{< app/cells/assistant language="csharp" >}}
