---
title: Как проверить замороженное состояние без Excel.
linktitle: Замороженное состояние
type: docs
weight: 190
url: /ru/net/how-to-check-frozen-state-of-excel-worksheet
description: В этой статье вы узнаете, как программно проверить замороженное состояние листа Excel с помощью библиотеки C# с номером .NET API.
---
{{% alert color="primary" %}}

В этой статье мы узнаем, как программно проверить замороженное состояние листа Excel.
Мы можем просто узнать, заморожен или разделен рабочий лист в MS Excel. Но есть ли способ узнать, заморожен ли он или разделен с помощью CSharp.
Мы можем просто сделать это с помощью Aspose.Cells для .Net.
{{% /alert %}}

##  **Замерзли ли оконные стекла**
С помощью Aspose.Cells для .Net мы можем проверить, заморожено ли окно и сколько строк и столбцов заблокировано.

 Пожалуйста, используйте[**Рабочий лист.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/) свойство для проверки состояния оконных стекол
 и получает заблокированные строки и столбцы с помощью[**Рабочий лист.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/)метод.
1. Создайте рабочую книгу, чтобы открыть файл.
2. Проверьте, не заморожен ли лист.
3. Получает заблокированную строку и столбцы.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}