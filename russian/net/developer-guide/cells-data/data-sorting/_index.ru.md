---
title: Сортировка данных
type: docs
weight: 130
url: /ru/net/sort-data-of-excel/
description: Узнайте, как сортировать данные, используя код Aspose.Cells for .NET API.
keywords: Sort data in ascending or descending order, Sort data based on the background color
---
{{% alert color="primary" %}}

Сортировка данных — одна из многих полезных функций Excel. Это позволяет пользователям упорядочивать данные, чтобы их было легче сканировать. Aspose.Cells позволяет разработчикам сортировать данные листа в алфавитном или числовом порядке, что работает так же, как Microsoft Excel для сортировки данных.

{{% /alert %}}

##  **Сортировка данных в Microsoft Excel**

Чтобы отсортировать данные в Excel Microsoft:

1.  Выбирать**Данные** из**Сортировать** меню. Откроется диалоговое окно Сортировка.
1. Выберите вариант сортировки.

Обычно сортировка выполняется по списку, определяемому как непрерывная группа данных, где данные отображаются в столбцах.

##  **Сортировка данных с помощью Aspose.Cells**

 Aspose.Cells обеспечивает[**Сортировщик данных**](https://reference.aspose.com/cells/net/aspose.cells/datasorter)класс, используемый для сортировки данных в порядке возрастания или убывания. Класс имеет несколько важных членов, например, такие свойства, как Key1... Key3 и Order1... Order3. Эти члены используются для определения отсортированных ключей и указания порядка сортировки ключей.

 Прежде чем реализовывать сортировку данных, вам необходимо определить ключи и установить порядок сортировки. Класс предоставляет[**Сортировать**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index)метод, используемый для сортировки данных на основе данных ячеек на листе.

[**Сортировать**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1)метод принимает следующие параметры:

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), ячейки базового листа.
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea), диапазон ячеек. Определите область ячейки перед применением сортировки данных.

В этом примере используется файл шаблона «Book1.xls», созданный в Excel Microsoft. После выполнения приведенного ниже кода данные сортируются соответствующим образом.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

 Если вы хотите отсортировать *LeftToRight*, используйте[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright) атрибут.

{{% /alert %}}

###  **Сортировка данных по цвету фона**

Excel предоставляет функции сортировки данных по цвету фона. Та же функция обеспечивается с помощью Aspose.Cells с использованием DataSorter, где[**Сортировать по типу**](https://reference.aspose.com/cells/net/aspose.cells/sortontype) .CellColor можно использовать в[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey) для сортировки данных по цвету фона. Все ячейки, содержащие указанный цвет в[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey), функции размещаются сверху или снизу в соответствии с настройкой SortOrder, а порядок остальных ячеек вообще не изменяется.

Ниже приведены примеры файлов, которые можно загрузить для тестирования этой функции:

[образецBackGroundFile.xlsx](81920906.xlsx)

[выходной образецBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

##  **Предварительные темы**
- [Сортировка данных в столбце с помощью пользовательского списка сортировки](/cells/ru/net/sort-data-in-column-with-custom-sort-list/)
- [Указание предупреждения о сортировке при сортировке данных](/cells/ru/net/specifying-sort-warning-while-sorting-data/)
