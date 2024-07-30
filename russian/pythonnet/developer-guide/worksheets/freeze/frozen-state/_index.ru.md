---
title: Как проверить состояние заморозки без Excel.
linktitle: Замороженное состояние
type: docs
weight: 190
url: /ru/python-net/how-to-check-frozen-state-of-excel-worksheet
description: В этой статье вы узнаете, как программно проверить состояние заморозки рабочей книги Excel, используя Aspose.Cells для Python via .NET API.
keywords: Библиотека Excel для Python, Как проверить состояние заморозки без Excel на Python, Проверить состояние заморозки без Excel на Python.
---

## **Введение**

В этой статье мы узнаем, как программно проверить состояние заморозки рабочей книги Excel. Мы можем легко узнать, находится ли рабочая книга в предварительно замороженном или разделённом состоянии в MS Excel. Но есть ли способ узнать, находится ли она в замороженном или разделённом состоянии с помощью C#. Мы можем легко это сделать с помощью Aspose.Cells для Python via .NET.

## **Как проверить состояние заморозки**
С помощью Aspose.Cells для Python via .NET мы можем проверить, заморожено ли окно, и сколько строк и столбцов заблокировано.

Пожалуйста, используйте свойство [**Worksheet.pane_state**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/pane_state/), чтобы проверить состояние оконных рамок 
и получить заблокированные строки и столбцы с помощью метода [**Worksheet.get_freezed_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/get_freezed_panes/#any-any-any-any).
1. Создайте рабочую книгу для открытия файла.
2. Проверьте, заморожен ли лист.
3. Получите заблокированные строки и столбцы

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Is-Worksheet-Frozen.py" >}}
