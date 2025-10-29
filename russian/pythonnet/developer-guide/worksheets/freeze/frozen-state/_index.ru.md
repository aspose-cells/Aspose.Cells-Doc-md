---
title: Как проверить закрепленное состояние без Excel.
linktitle: Замороженное состояние
type: docs
weight: 190
url: /ru/python-net/how-to-check-frozen-state-of-excel-worksheet
description: В этой статье вы узнаете, как программно проверить закрепленное состояние листа Excel с помощью API Aspose.Cells для Python via .NET.
keywords: Библиотека Python для работы с Excel, Python как проверить закрепленное состояние без Excel, Проверка закрепленного состояния без Excel в Python.
---

## **Введение**

В этой статье мы научимся как проверить замороженное состояние листа Excel программно. Мы можем просто определить, заморожен ли лист или разделен в MS Excel. Но есть ли способ определить, заморожен ли он или разделен на C#? Мы можем сделать это с Aspose.Cells для Python via .NET.

## **Как проверить замороженное состояние**
С помощью Aspose.Cells для Python via .NET мы можем проверить, заблокировано ли окно и сколько строк и столбцов заблокировано.

Пожалуйста, используйте свойство [**Worksheet.pane_state**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/pane_state/), чтобы проверить состояние оконных рамок 
и получить заблокированные строки и столбцы с помощью метода [**Worksheet.get_freezed_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/get_freezed_panes/#any-any-any-any).
1. Создайте рабочую книгу для открытия файла.
2. Проверьте, заморожен ли лист.
3. Получите заблокированные строки и столбцы

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Is-Worksheet-Frozen.py" >}}
{{< app/cells/assistant language="python-net" >}}
