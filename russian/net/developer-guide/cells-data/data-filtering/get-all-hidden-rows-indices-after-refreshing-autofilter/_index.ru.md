---
title: Получить все скрытые индексы строк после обновления автофильтра
type: docs
weight: 320
url: /ru/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Узнайте, как получить все скрытые индексы строк после обновления автофильтра с помощью API Aspose.Cells for .NET.
keywords: Получите все скрытые индексы строк после обновления автофильтра, получите все скрытые индексы строк после обновления автофильтра, получите все скрытые индексы строк после обновления автофильтра
---

## **Возможные сценарии использования**

Когда вы применяете автофильтр к ячейкам листа, то некоторые строки автоматически скрываются. Однако может возникнуть ситуация, когда некоторые строки уже были скрыты вручную пользователем Excel, и они не скрыты автофильтром. Поэтому сложно знать, какие из строк были скрыты автофильтром, а какие - вручную. Aspose.Cells решает эту проблему с помощью метода int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1). Этот метод возвращает индексы строк всех строк, скрытых автофильтром, и не вручную пользователем Excel.

## **Получить все скрытые индексы строк после обновления автофильтра**

Пожалуйста, посмотрите следующий образец кода, который загружает [образец Excel-файла](64716909.xlsx), содержащий некоторые из строк, скрытых вручную пользователем Excel. Код применяет автофильтр и обновляет его с помощью метода int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1), который возвращает индексы скрытых строк автофильтром. Затем он выводит индексы скрытых строк в консоль, а также имена ячеек и их значения.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

## **Вывод в консоль**

{{< highlight java >}}

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
{{< app/cells/assistant language="csharp" >}}
