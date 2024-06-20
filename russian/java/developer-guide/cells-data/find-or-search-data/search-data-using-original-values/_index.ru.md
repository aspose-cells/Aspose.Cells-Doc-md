---
title: Поиск данных с использованием исходных значений
type: docs
weight: 540
url: /ru/java/search-data-using-original-values/
---

{{% alert color="primary" %}} 

Иногда значение данных скрыто из-за того, что оно отформатировано определенным образом. Например, предположим, что ячейка D4 имеет формулу =Sum(A1:A2) и ее значение равно 20, но оно отформатировано как ---, тогда значение 20 скрыто и не может быть найдено с помощью параметров поиска в Microsoft Excel. Однако вы можете найти его с помощью Aspose.Cells, используя [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES)

{{% /alert %}} 
## **Поиск данных с использованием исходных значений**
Нижеприведенный образец кода иллюстрирует вышесказанное. Он находит ячейку D4, которая не может быть найдена с помощью параметров поиска в Microsoft Excel, но Aspose.Cells может найти ее, используя [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES). Пожалуйста, прочитайте комментарии внутри кода для получения дополнительной информации.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **Вывод в консоль**
Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
