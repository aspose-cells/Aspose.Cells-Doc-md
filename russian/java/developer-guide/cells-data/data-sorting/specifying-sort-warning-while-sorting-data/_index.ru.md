---
title: Указание предупреждения о сортировке при сортировке данных
type: docs
weight: 100
url: /ru/java/specifying-sort-warning-while-sorting-data/
---
## **Возможные сценарии использования**
 Пожалуйста, обратите внимание на эти текстовые данные, т.е. {11, 111, 22}. Эти текстовые данные отсортированы таким образом, потому что с точки зрения текста 111 предшествует 22. Но если вы хотите отсортировать эти данные не как текст, а как числа, тогда они станут {11, 22, 111}, потому что численно 111 идет после 22. Aspose.Cells предоставляет[DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) имущества для решения этой проблемы. Пожалуйста, установите это свойство**истинный**и ваши текстовые данные будут отсортированы как числовые данные. На следующем снимке экрана показано предупреждение о сортировке, отображаемое Microsoft Excel при сортировке текстовых данных, которые выглядят как числовые данные.

![дело:изображение_альтернативный_текст](specifying-sort-warning-while-sorting-data_1.png)
## **Образец кода**
 Следующий пример кода иллюстрирует использование[DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber)собственности, как было объяснено ранее. Пожалуйста, проверьте его[образец файла Excel](43352077.xlsx) а также[выходной файл Excel](43352078.xlsx) для получения дополнительной помощи.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SpecifyingSortWarningWhileSortingData.java" >}}
