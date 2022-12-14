---
title: Сортировка данных в столбце с пользовательским списком сортировки
type: docs
weight: 290
url: /ru/net/sort-data-in-column-with-custom-sort-list/
---
## **Возможные сценарии использования**

 Вы можете сортировать данные в столбце с помощью пользовательского списка. Это можно сделать с помощью[**DataSorter.AddKey (ключ int, порядок SortOrder, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)метод. Однако этот метод работает только в том случае, если элементы в пользовательском списке не имеют внутри запятых. Если в них есть запятые, такие как «США, США», «Китай, Китай» и т. д., вы должны использовать [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference. aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3). Здесь последний параметр — это не строка, а массив строк.

## **Сортировка данных в столбце с пользовательским списком сортировки**

В следующем примере кода объясняется, как использовать [**метод DataSorter.AddKey (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey /methods/3) метод сортировки данных с помощью пользовательского списка сортировки. См. [пример файла Excel] (50528327.xlsx), используемый в этом коде, и [выходной файл Excel] (50528328.xlsx), созданный им. На следующем снимке экрана показано влияние кода на образец файла Excel при выполнении.

![дело:изображение_альтернативный_текст](sort-data-in-column-with-custom-sort-list_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
