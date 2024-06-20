---
title: Указание предупреждения сортировки при сортировке данных
type: docs
weight: 100
url: /ru/java/specifying-sort-warning-while-sorting-data/
---

## **Возможные сценарии использования**
Рассмотрим следующие текстовые данные, т. е. {11, 111, 22}. Эти текстовые данные отсортированы так из-за того, что в терминах текста 111 идет перед 22. Но если вы хотите отсортировать эти данные не как текст, а как числа, то они станут {11, 22, 111}, потому что по числовым значениям 111 идет после 22. Aspose.Cells предоставляет свойство [DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) для решения этой проблемы. Пожалуйста, установите это свойство в **true**, и ваши текстовые данные будут отсортированы как числовые данные. Ниже показано предупреждение о сортировке, отображаемое Microsoft Excel при сортировке текстовых данных, которые выглядят как числовые.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)
## **Образец кода**
В следующем образце кода иллюстрируется использование свойства [DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber), как объяснено выше. Пожалуйста, ознакомьтесь с [образцом Excel-файла](43352077.xlsx) и [выходным Excel-файлом](43352078.xlsx) для получения дополнительной помощи.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SpecifyingSortWarningWhileSortingData.java" >}}
