---
title: Снять замораживание строк или столбцов
linktitle: Снять замораживание панелей
type: docs
weight: 190
url: /ru/python-net/unfreeze-rows-or-columns-of-excel-worksheet
description: В этой статье вы узнаете, как программно размораживать строки, столбцы или панели рабочего листа Excel с помощью Aspose.Cells для Python via .NET API.
keywords: Библиотека Excel для Python, разморозка панелей в Python, как разморозить строки в Python, как разморозить столбцы в Python, как разморозить окно в Python.
---

## **Введение**

В этой статье мы узнаем, как убрать замораживание строк, столбцов и областей. Если рабочие листы в файлах Excel заморожены, иногда мы хотим разморозить рабочий лист или настроить замороженные строки, столбцы или области.


## **Как разморозить строки или столбцы в Excel**

1. Нажмите вкладку Просмотр > Заморозить панели > Снять заморозку панелей.

**![снять замораживание панелей в Excel](Unfreeze-Panes.png)**




## **Как разморозить строки, столбцы или панели с помощью библиотеки Aspose.Cells для Python Excel**
Просто разморозить панели с помощью Aspose.Cells для Python via .NET. Пожалуйста, используйте метод [**Worksheet.un_freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/un_freeze_panes/) для размораживания панелей.

1. Создать Рабочую книгу для открытия замороженного файла.
2. Снять замораживание панелей с помощью метода Worksheet.UnFreezePanes().
3. Сохранить файл.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Unfreeze-Pane.py" >}}

Прикреплен [образец исходного файла Excel](Frozen.xlsx).
