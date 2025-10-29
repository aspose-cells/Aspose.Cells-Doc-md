---
title: Поиск данных с использованием исходных значений
type: docs
weight: 380
url: /ru/python-net/search-data-using-original-values/
description: Узнайте, как искать данные с использованием исходных значений через Aspose.Cells для API Python via .NET.
keywords: Библиотека Python Excel, Поиск данных с использованием исходных значений, Поиск данных с использованием исходных значений в Python, Найти данные с использованием исходных значений в Python, Поиск данных по исходным значениям в Python, Найти данные по исходным значениям
---

{{% alert color="primary" %}}

Иногда значение данных скрыто, потому что оно отформатировано каким-то образом. Например, предположим, что в ячейке D4 формула =Sum(A1:A2), и ее значение 20, но она отформатирована как ---, тогда значение 20 скрыто и не может быть найдено с помощью опций поиска в Microsoft Excel. Однако вы можете найти его с помощью Aspose.Cells для Python via .NET, используя [**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype).

{{% /alert %}}

Приведенный ниже образец кода иллюстрирует вышеупомянутый момент. Он находит ячейку D4, которую нельзя найти с помощью опций поиска Microsoft Excel, но Aspose.Cells может найти ее с помощью [**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype). Пожалуйста, прочтите комментарии внутри кода для получения дополнительной информации.

## Код Python для поиска данных с использованием исходных значений

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SearchDataUsingOriginalValues.py" >}}

## Консольный вывод, сгенерированный образцовым кодом

Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
