---
title: Получить все скрытые индексы строк после обновления автофильтра
type: docs
weight: 240
url: /ru/java/get-all-hidden-rows-indices-after-refreshing-autofilter/
---

## **Возможные сценарии использования**

Когда вы применяете автофильтр к ячейкам листа, то некоторые из строк автоматически скрываются. Но может оказаться так, что некоторые из строк уже скрыты вручную пользователем Excel и они не скрыты с помощью автофильтра. Поэтому сложно определить, какие из строк скрыты с помощью автофильтра, а какие из них скрыты вручную пользователем Excel. Aspose.Cells справляется с этой проблемой с помощью метода int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)). Этот метод возвращает индексы строк всех строк, которые скрыты с помощью автофильтра и не вручную пользователем Excel.

## **Получить все скрытые индексы строк после обновления автофильтра**

Пожалуйста, посмотрите следующий образец кода, который загружает [образец файла Excel](64716913.xlsx), который содержит некоторые из строк, скрытых вручную пользователем Excel. Код применяет автофильтр и обновляет его с помощью метода int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)), который возвращает индексы строк всех скрытых строк с помощью автофильтра. Затем он печатает индексы скрытых строк на консоли вместе с именами ячеек и значениями.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.java" >}}

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
