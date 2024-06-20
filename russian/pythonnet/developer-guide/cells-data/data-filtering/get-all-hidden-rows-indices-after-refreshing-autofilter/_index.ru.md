---
title: Получить все скрытые индексы строк после обновления автофильтра
type: docs
weight: 320
url: /ru/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Узнайте, как получить все скрытые индексы строк после обновления автофильтра с помощью Aspose.Cells для Python via .NET API.
keywords: Библиотека Python Excel, Получить все скрытые индексы строк после обновления автофильтра Python, Получить все скрытые индексы строк после обновления автофильтра с помощью Python, Получить все скрытые индексы строк после обновления автофильтра с помощью Python
---

## **Возможные сценарии использования**

Когда вы применяете автофильтр к ячейкам рабочего листа, некоторые строки автоматически скрываются. Но может возникнуть ситуация, когда некоторые строки уже были скрыты вручную конечным пользователем Excel, и они не скрыты автофильтром. Поэтому трудно узнать, какие строки скрыты автофильтром, а какие из них скрыты вручную конечным пользователем Excel. Aspose.Cells для Python via .NET решает эту проблему с помощью [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool) метода. Этот метод возвращает индексы строк всех строк, скрытых автофильтром и не вручную конечным пользователем Excel.

## **Получить все скрытые индексы строк после обновления автофильтра**

Пожалуйста, ознакомьтесь с примерным кодом, загружающим [образец Excel-файла](64716909.xlsx), который содержит некоторые из строк, скрытых вручную конечным пользователем Excel. Код применяет автофильтр и обновляет его с использованием метода [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool), который возвращает индексы скрытых строк автофильтром. Затем он выводит индексы скрытых строк на консоль вместе с именами и значениями ячеек.

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.py" >}}

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
