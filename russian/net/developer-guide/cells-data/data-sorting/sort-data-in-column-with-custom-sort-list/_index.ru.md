---
title: Сортировка данных в столбце с помощью пользовательского списка сортировки
type: docs
weight: 290
url: /ru/net/sort-data-in-column-with-custom-sort-list/
description: Узнайте, как сортировать данные в столбце с помощью настраиваемого списка, используя код Aspose.Cells for .NET API.
keywords: Sort Data in Column with Custom Sort List, Sort data by custom list.
---
##  **Возможные сценарии использования**

 Вы можете сортировать данные в столбце, используя настраиваемый список. Это можно сделать с помощью[**DataSorter.AddKey(int key, порядок SortOrder, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)метод. Однако этот метод работает только в том случае, если элементы пользовательского списка не содержат запятых. Если в них есть запятые, например «USA,US», «China,CN» и т. д., вам необходимо использовать [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference. aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3). Здесь последний параметр — это не строка, а массив строк.

##  **Сортировка данных в столбце с помощью пользовательского списка сортировки**

В следующем примере кода объясняется, как использовать [**Метод DataSorter.AddKey (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey /methods/3) метод для сортировки данных с помощью специального списка сортировки. Пожалуйста, ознакомьтесь с[образец файла Excel](50528327.xlsx) используется в этом коде и[выходной файл Excel](50528328.xlsx) порожденный им. На следующем снимке экрана показано влияние кода на пример файла Excel при выполнении.

![задача: image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

##  **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
