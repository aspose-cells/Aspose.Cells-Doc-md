---
title: Разморозить строки или столбцы
linktitle: Разморозить панели
type: docs
weight: 190
url: /ru/net/unfreeze-rows-or-columns-of-excel-worksheet
description: В этой статье вы узнаете, как программно разморозить строки, столбцы или панели рабочих листов Excel с помощью библиотеки C# с .NET API.
keywords: Unfreeze panes, Unfreeze rows, Unfreeze columns, unFreeze window.
---
{{% alert color="primary" %}}

В этой статье мы узнаем, как разморозить строки, столбцы и панели.
Если рабочие листы в файлах Excel заморожены, иногда нам нужно разморозить их или настроить замороженные строки, столбцы или панели.

{{% /alert %}}

##  **В Excel**

1. Щелкните вкладку «Вид» > «Закрепить области» > «Отменить закрепление областей».

**![разморозить панели в Excel](Unfreeze-Panes.png)**




##  **Разморозить строки, столбцы или панели с помощью Aspose.Cells для .Net**
 Разморозить панели с помощью Aspose.Cells для .Net очень просто. Пожалуйста, используйте[**Рабочий лист.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes)способ разблокировать стекла.

1. Создайте рабочую книгу, чтобы открыть замороженный файл.
2. Разморозьте панели с помощью метода Worksheet.UnFreezePanes().
3. Сохраните файл.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

 Прикрепил[образец исходного файла Excel](Frozen.xlsx).
