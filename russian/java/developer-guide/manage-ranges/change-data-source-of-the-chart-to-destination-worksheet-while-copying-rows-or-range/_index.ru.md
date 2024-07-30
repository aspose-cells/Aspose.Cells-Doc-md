---
title: Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона
type: docs
weight: 850
url: /ru/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Возможные сценарии использования**
Когда вы копируете строки или диапазон, содержащий диаграммы, на новый лист, исходный источник данных диаграммы не меняется. Например, если исходный источник данных диаграммы равен =Sheet1!$A$1:$B$4, то после копирования строк или диапазона на новый лист исходный источник данных останется таким же, т.е. =Sheet1!$A$1:$B$4. Он по-прежнему относится к старому листу, т.е. Sheet1. Это также поведение Microsoft Excel. Но если вы хотите, чтобы он относился к новому целевому листу, то, пожалуйста, используйте свойство CopyOptions.ReferToDestinationSheet и установите его в true при вызове метода Cells.CopyRows(). Теперь, если вашим целевым листом является DestSheet, то исходный источник данных вашей диаграммы изменится с =Sheet1!$A$1:$B$4 на =DestSheet!$A$1:$B$4.
## **Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона**
Следующий образец кода объясняет использование свойства CopyOptions.ReferToDestinationSheet при копировании строк или диапазона, содержащего диаграмму, на новый лист. Код использует [образец файла Excel](5472284.xlsx) и генерирует [выводной файл Excel](5472283.xlsx). На скриншоте показано, что исходный источник данных диаграммы в [выводном файле Excel](5472283.xlsx) теперь ссылается на DestSheet вместо Sheet1.

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeDataSource-ChangeDataSource.java" >}}






