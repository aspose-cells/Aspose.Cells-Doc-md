---
title: Указание предупреждения о сортировке при сортировке данных
type: docs
weight: 140
url: /ru/net/specifying-sort-warning-while-sorting-data/
---
## **Возможные сценарии использования**

Пожалуйста, обратите внимание на эти текстовые данные, т.е. {11, 111, 22}. Эти текстовые данные отсортированы, потому что с точки зрения текста 111 предшествует 22. Но если вы хотите отсортировать эти данные не как текст, а как числа, тогда они станут {11, 22, 111}, потому что числовое значение 111 идет после 22. Aspose.Cells обеспечивает[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)имущества для решения этой проблемы. Пожалуйста, установите это свойство**истинный**и ваши текстовые данные будут отсортированы как числовые данные. На следующем снимке экрана показано предупреждение о сортировке, отображаемое Microsoft Excel при сортировке текстовых данных, которые выглядят как числовые данные.

![дело:изображение_альтернативный_текст](specifying-sort-warning-while-sorting-data_1.png)

## **Образец кода**

 Следующий пример кода иллюстрирует использование[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)собственности, как было объяснено ранее. Пожалуйста, проверьте его[образец файла Excel](43352075.xlsx) и[выходной файл Excel](43352076.xlsx) для получения дополнительной помощи.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
