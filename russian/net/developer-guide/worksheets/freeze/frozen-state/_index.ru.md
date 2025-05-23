---
title: Как проверить замороженное состояние без Excel.
linktitle: Замороженное состояние
type: docs
weight: 190
url: /ru/net/how-to-check-frozen-state-of-excel-worksheet
description: В этой статье вы узнаете, как проверить замороженное состояние листа Excel программно, используя библиотеку C# с .NET API.

---

## **Введение**

В этой статье мы узнаем, как проверить замороженное состояние рабочего листа Excel программным образом. Мы можем просто узнать, является ли рабочий лист замороженным или разделенным в MS Excel. Но есть ли способ узнать, заморожен ли он или разделен с помощью C#? Мы можем сделать это с помощью Aspose.Cells для .Net.

## **Заморожены ли оконные рамы**
С помощью Aspose.Cells для .Net мы можем проверить, заморожено ли окно и сколько строк и столбцов заблокированы.

Пожалуйста, используйте свойство [**Worksheet.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/), чтобы проверить состояние оконных рамок 
и получить заблокированные строки и столбцы с помощью метода [**Worksheet.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/).
1. Создайте рабочую книгу для открытия файла.
2. Проверьте, заморожен ли лист.
3. Получите заблокированные строки и столбцы

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}
{{< app/cells/assistant language="csharp" >}}
