---
title: Поиск данных с использованием исходных значений
type: docs
weight: 380
url: /ru/net/search-data-using-original-values/
---
{{% alert color="primary" %}}

 Иногда значение данных скрыто из-за того, что они каким-то образом отформатированы. Например, предположим, что в ячейке D4 есть формула = Сумма (A1: A2), и ее значение равно 20, но оно отформатировано как ---, тогда значение 20 скрыто и не может быть найдено с помощью параметров поиска Microsoft Excel. Однако вы можете найти его, используя Aspose.Cells, используя[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

 Следующий пример кода иллюстрирует указанный выше пункт. Он находит ячейку D4, которую нельзя найти с помощью параметров поиска Excel Microsoft, но Aspose.Cells может найти ее с помощью[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype). Пожалуйста, прочитайте комментарии внутри кода для получения дополнительной информации.

## C# код для поиска данных с использованием исходных значений

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## Консольный вывод, сгенерированный примером кода

Вот вывод консоли приведенного выше примера кода.

{{< highlight "java" >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]{{< /highlight >}}
