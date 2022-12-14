---
title: Сортировка данных
type: docs
weight: 130
url: /ru/net/sort-data-of-excel/
---
{{% alert color="primary" %}}

Сортировка данных — одна из многих полезных функций Excel. Это позволяет пользователям упорядочивать данные, чтобы их было легче сканировать. Aspose.Cells позволяет разработчикам сортировать данные рабочего листа в алфавитном или числовом порядке, что работает так же, как Microsoft Excel для сортировки данных.

{{% /alert %}}

## **Сортировка данных в Microsoft Excel**

Чтобы отсортировать данные в Microsoft Excel:

1.  Выбирать**Данные** от**Сортировать** меню. Появится диалоговое окно Сортировка.
1. Выберите вариант сортировки.

Как правило, сортировка выполняется в списке, определяемом как непрерывная группа данных, где данные отображаются в столбцах.

## **Сортировка данных с Aspose.Cells**

 Aspose.Cells обеспечивает[**сортировщик данных**](https://reference.aspose.com/cells/net/aspose.cells/datasorter)класс, используемый для сортировки данных в порядке возрастания или убывания. У класса есть несколько важных членов, например такие свойства, как Key1 ... Key3 и Order1 ... Order3. Эти элементы используются для определения отсортированных ключей и порядка сортировки ключей.

 Вы должны определить ключи и установить порядок сортировки перед реализацией сортировки данных. Класс предоставляет[**Сортировать**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index)метод, используемый для выполнения сортировки данных на основе данных ячеек на листе.

[**Сортировать**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1)метод принимает следующие параметры:

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), ячейки для основного рабочего листа.
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea), диапазон ячеек. Определите область ячейки перед применением сортировки данных.

В этом примере используется файл шаблона «Book1.xls», созданный в Microsoft Excel. После выполнения приведенного ниже кода данные сортируются соответствующим образом.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

 Если вы хотите отсортировать*Слева направо* , использовать[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright) атрибут.

{{% /alert %}}

### **Сортировка данных по цвету фона**

 Excel предоставляет функции для сортировки данных по цвету фона. Та же функция предоставляется с использованием Aspose.Cells с использованием DataSorter, где[**Сортировка по типу**](https://reference.aspose.com/cells/net/aspose.cells/sortontype) .CellColor можно использовать в[**ДобавитьКлюч()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey) для сортировки данных по цвету фона. Все ячейки, содержащие указанный цвет в[**ДобавитьКлюч()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey), функция размещается сверху или снизу в соответствии с настройкой SortOrder, а порядок остальных ячеек вообще не меняется.

Ниже приведены примеры файлов, которые можно загрузить для тестирования этой функции:

[образецBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

## **Предварительные темы**
- [Сортировка данных в столбце с пользовательским списком сортировки](/cells/ru/net/sort-data-in-column-with-custom-sort-list/)
- [Указание предупреждения о сортировке при сортировке данных](/cells/ru/net/specifying-sort-warning-while-sorting-data/)
