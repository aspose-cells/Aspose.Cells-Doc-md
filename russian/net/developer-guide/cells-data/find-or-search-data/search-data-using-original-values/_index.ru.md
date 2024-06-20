---
title: Поиск данных с использованием исходных значений
type: docs
weight: 380
url: /ru/net/search-data-using-original-values/
description: Узнайте, как искать данные по исходным значениям через API Aspose.Cells for .NET.
keywords: Поиск данных по исходным значениям, Поиск данных по исходным значениям, Поиск данных по исходным значениям, Поиск данных по исходным значениям
---

{{% alert color="primary" %}}

Иногда значение данных скрыто, потому что оно отформатировано каким-то образом. Например, предположим, что ячейка D4 имеет формулу =Сумма(A1:A2) и ее значение равно 20, но оно отформатировано как ---, то значение 20 скрыто и не может быть найдено с помощью функции поиска в Microsoft Excel. Однако вы можете найти его с помощью Aspose.Cells, используя [**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

Приведенный ниже образец кода иллюстрирует вышеупомянутый момент. Он находит ячейку D4, которую нельзя найти с помощью опций поиска Microsoft Excel, но Aspose.Cells может найти ее с помощью [**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype). Пожалуйста, прочтите комментарии внутри кода для получения дополнительной информации.

## Код C# для поиска данных по исходным значениям

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## Консольный вывод, сгенерированный образцовым кодом

Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
