---
title: Получить все индексы скрытых строк после обновления автофильтра
type: docs
weight: 320
url: /ru/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Узнайте, как получить индексы всех скрытых строк после обновления автофильтра с помощью Aspose.Cells for .NET API.
keywords: Get All Hidden Rows Indices after Refreshing AutoFilter, Obtain All Hidden Rows Indices after Refreshing AutoFilter, Retrieve All Hidden Rows Indices after Refreshing AutoFilter
---
##  **Возможные сценарии использования**

Когда вы применяете автоматический фильтр к ячейкам листа, некоторые строки автоматически скрываются. Но может случиться так, что некоторые строки уже скрыты вручную конечным пользователем Excel и не скрыты автоматическим фильтром. Поэтому сложно определить, какие строки скрыты автоматическим фильтром, а какие — вручную конечным пользователем Excel. Aspose.Cells решает эту проблему, используя int[][**AutoFilter.Refresh(boolideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)метод. Этот метод возвращает индексы всех строк, которые скрыты автоматическим фильтром, а не вручную конечным пользователем Excel.

##  **Получить все индексы скрытых строк после обновления автофильтра**

 См. следующий пример кода, который загружает[образец файла Excel](64716909.xlsx) который содержит некоторые строки, вручную скрытые конечным пользователем Excel. Код применяет автоматический фильтр и обновляет его, используя int[][**AutoFilter.Refresh(boolideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)метод, который возвращает индексы всех скрытых строк с помощью автоматического фильтра. Затем он печатает индексы скрытых строк на консоли вместе с именами и значениями ячеек.

##  **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

##  **Консольный вывод**

{{< highlight "java" >}}

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.

\--------------------------

1       A2      Apple

2       A3      Apple

3       A4      Apple

6       A7      Apple

7       A8      Apple

11      A12     Pear

12      A13     Pear

{{< /highlight >}}
