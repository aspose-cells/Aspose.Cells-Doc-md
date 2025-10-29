---
title: Снять замораживание строк или столбцов
linktitle: Снять замораживание панелей
type: docs
weight: 190
url: /ru/python-net/unfreeze-rows-or-columns-of-excel-worksheet
description: В этой статье вы узнаете, как программно разблокировать строки, столбцы или области листа Excel с помощью API Aspose.Cells для Python via .NET.
keywords: Библиотека Excel на Python, Разморозить области, как разблокировать строки, как разблокировать столбцы, как разблокировать окно.
---

## **Введение**

В этой статье мы узнаем, как убрать замораживание строк, столбцов и областей. Если рабочие листы в файлах Excel заморожены, иногда мы хотим разморозить рабочий лист или настроить замороженные строки, столбцы или области.


## **Как разблокировать строки или столбцы в Excel**

1. Нажмите вкладку Просмотр > Заморозить панели > Снять заморозку панелей.

**![снять замораживание панелей в Excel](Unfreeze-Panes.png)**




## **Как разблокировать строки, столбцы или области листа с помощью API Aspose.Cells для Python Excel**
Это просто разморозить области с помощью Aspose.Cells для Python via .NET. Пожалуйста, используйте метод [**Worksheet.un_freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/un_freeze_panes/) для размораживания областей.

1. Создать Рабочую книгу для открытия замороженного файла.
2. Снять замораживание панелей с помощью метода Worksheet.UnFreezePanes().
3. Сохранить файл.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Unfreeze-Pane.py" >}}

Прикреплен [образец исходного файла Excel](Frozen.xlsx).
{{< app/cells/assistant language="python-net" >}}
