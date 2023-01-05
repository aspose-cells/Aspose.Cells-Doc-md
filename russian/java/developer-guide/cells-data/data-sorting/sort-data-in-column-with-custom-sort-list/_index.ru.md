---
title: Сортировка данных в столбце с пользовательским списком сортировки
type: docs
weight: 210
url: /ru/java/sort-data-in-column-with-custom-sort-list/
---
## **Возможные сценарии использования**

Вы можете сортировать данные в столбце с помощью пользовательского списка. Это можно сделать с помощью[DataSorter.AddKey (ключ int, порядок SortOrder, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) метод. Однако этот метод работает только в том случае, если элементы в пользовательском списке не имеют внутри запятых. Если у них есть запятые, такие как «США, США», «Китай, Китай» и т. д., то вы должны использовать[DataSorter.AddKey (ключ int, порядок SortOrder, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) метод. Здесь последний параметр — это не строка, а массив строк.

## **Сортировка данных в столбце с пользовательским списком сортировки**

В следующем примере кода показано, как использовать метод DataSorter.AddKey(int key, SortOrder order, String[]customList) для сортировки данных с помощью пользовательского списка сортировки. Пожалуйста, смотрите[образец файла Excel](50528359.xlsx)используется в этом коде и[выходной файл Excel](50528358.xlsx)порожденный им. На следующем снимке экрана показано влияние кода на образец файла Excel при выполнении.

![дело:изображение_альтернативный_текст](sort-data-in-column-with-custom-sort-list_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
