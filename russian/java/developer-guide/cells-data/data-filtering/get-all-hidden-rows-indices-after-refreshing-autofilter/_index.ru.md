---
title: Получить все индексы скрытых строк после обновления автофильтра
type: docs
weight: 240
url: /ru/java/get-all-hidden-rows-indices-after-refreshing-autofilter/
---
## **Возможные сценарии использования**

Когда вы применяете автоматический фильтр к ячейкам рабочего листа, некоторые строки автоматически скрываются. Но может случиться так, что некоторые строки уже скрыты вручную конечным пользователем Excel, и они не скрыты автоматическим фильтром. Поэтому трудно узнать, какие строки скрыты автоматическим фильтром, а какие скрыты вручную конечным пользователем Excel. Aspose.Cells решает эту проблему, используя int[][**AutoFilter.refresh (bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)) метод. Этот метод возвращает индексы всех строк, скрытых автоматическим фильтром, а не вручную конечным пользователем Excel.

## **Получить все индексы скрытых строк после обновления автофильтра**

См. следующий пример кода, который загружает[образец файла Excel](64716913.xlsx)который содержит некоторые строки, скрытые вручную конечным пользователем Excel. Код применяет автоматический фильтр и обновляет его, используя int[][**AutoFilter.refresh (bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)), который возвращает индексы строк всех скрытых строк с помощью автоматического фильтра. Затем он выводит на консоль индексы скрытых строк вместе с именами и значениями ячеек.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.java" >}}

## **Консольный вывод**

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
