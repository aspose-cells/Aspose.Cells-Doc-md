---
title: Поиск данных с использованием исходных значений
type: docs
weight: 380
url: /ru/net/search-data-using-original-values/
description: Узнайте, как искать данные, используя исходные значения, с помощью Aspose.Cells for .NET API.
keywords: Search Data using Original Values, Find Data using Original Values, Search Data by Original Values, Find Data by Original Values
---
{{% alert color="primary" %}}

 Иногда значение данных скрыто, поскольку они каким-либо образом отформатированы. Например, предположим, что ячейка D4 имеет формулу = Сумма (A1: A2) и ее значение равно 20, но оно отформатировано как ---, тогда значение 20 скрыто и его невозможно найти с помощью параметров поиска Excel Microsoft. Однако вы можете найти его по номеру Aspose.Cells, используя[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

 Следующий пример кода иллюстрирует вышеизложенное. Он находит ячейку D4, которую невозможно найти с помощью параметров поиска Excel Microsoft, но Aspose.Cells можно найти с помощью[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype). Пожалуйста, прочитайте комментарии внутри кода для получения дополнительной информации.

##  C# код для поиска данных с использованием исходных значений

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## Вывод консоли, созданный примером кода

Вот консольный вывод приведенного выше примера кода.

{{< highlight "java" >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
