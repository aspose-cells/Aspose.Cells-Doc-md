---
title: Поиск данных с использованием исходных значений
type: docs
weight: 540
url: /ru/java/search-data-using-original-values/
---

{{% alert color="primary" %}} 

Иногда значение данных скрыто, потому что оно отформатировано определённым образом. Например, предположим, что ячейка D4 содержит формулу =Sum(A1:A2), её значение равно 20, но оно отформатировано как ---, тогда значение 20 скрыто и его нельзя найти с помощью поиска в Microsoft Excel. Однако его можно найти с помощью Aspose.Cells, используя [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL-VALUES)

{{% /alert %}} 
## **Поиск данных с использованием исходных значений**
Следующий пример кода иллюстрирует этот момент. Он ищет ячейку D4, которую невозможно найти средствами поиска Microsoft Excel, но Aspose.Cells может найти с помощью [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL-VALUES). Ознакомьтесь с комментариями внутри кода для получения дополнительной информации.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **Вывод в консоль**
Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
