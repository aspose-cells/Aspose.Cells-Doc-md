---
title: Разморозить строки или столбцы
linktitle: Разморозить панели
type: docs
weight: 190
url: /ru/net/unfreeze-rows-or-columns-of-excel-worksheet
description: В этой статье вы узнаете, как программно разморозить строки, столбцы или панели листов Excel с помощью библиотеки C# с номером .NET API.
keywords: Unfreeze panes, Unfreeze rows, Unfreeze columns, unFreeze window.
---
{{% alert color="primary" %}}

В этой статье мы узнаем, как разморозить строки, столбцы и панели.
Если листы в файлах Excel заморожены, иногда нам нужно разморозить лист или настроить замороженные строки, столбцы или панели.

{{% /alert %}}

##  **В Excel**

1. Щелкните вкладку «Вид» > «Закрепить панели» > «Разморозить панели».

**![разморозить панели в Excel](Unfreeze-Panes.png)**




##  **Разморозьте строки, столбцы или панели с помощью Aspose.Cells для .Net**
 Разморозить панели просто с помощью Aspose.Cells для .Net. Пожалуйста, используйте[**Рабочий лист.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes)способ разблокировать панели.

1. Создайте рабочую книгу, чтобы открыть замороженный файл.
2. Разморозьте панели с помощью метода Worksheet.UnFreezePanes().
3. Сохраните файл.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

 Прикрепил[пример исходного файла Excel](Frozen.xlsx).
