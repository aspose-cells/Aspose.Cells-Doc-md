---
title: Блокировка ячеек для защиты с помощью Python.NET
linktitle: Блокировка ячеек для защиты их
type: docs
weight: 130
url: /ru/python-net/how-to-lock-cells-to-protect-them/
description: Узнайте, как заблокировать определённые ячейки и защитить листы в файлах Excel с использованием Aspose.Cells для Python via .NET.
keywords: Блокировка ячеек в Python, защита листов, защита ячеек в Excel с Python, учебник Aspose.Cells Python
---

## **Возможные сценарии использования**
Блокировка ячеек с целью защиты — распространённая практика в программах для работы с таблицами, таких как Microsoft Excel или Google Sheets, по нескольким важным причинам:

1. Предотвращение случайных изменений: блокировка ячеек может помешать пользователям случайно изменить важные данные или формулы.
2. Поддержание целостности данных: обеспечение сохранения критически важных данных в актуальном состоянии.
3. Управляемый доступ: управление разрешениями на редактирование в совместной работе.
4. Защита формул: сохранение важных расчетов от изменений.
5. Соблюдение бизнес-правил: соответствие требованиям защиты данных.
6. Руководство пользователями: предоставление ясных областей для редактирования в сложных таблицах.

## **Как заблокировать ячейки для защиты в Excel**
Вот как можно заблокировать ячейки в Microsoft Excel:

1. Выберите ячейки для блокировки: выберите ячейки или пропустите, чтобы заблокировать весь лист.
1. Откройте диалоговое окно «Формат ячеек»: Правый клик > «Формат ячеек» или Ctrl+1.
<br>
<img src="1.png" width=60% />
1. Заблокируйте ячейки: перейдите на вкладку «Защита» > установите флажок «Заблокировано» > нажмите «ОК».
1. Защитите лист: вкладка "Обзор" > "Защитить лист" > Установите пароль/разрешения > Нажмите "OK".
<br>
<img src="2.png" width=60% />

## **Как заблокировать ячейки для их защиты с помощью Python**

Aspose.Cells для Python via .NET позволяет программно защищать ячейки. Следуйте этим шагам:
1. Загрузите [пример файла](sample.xlsx)
2. Разблокируйте все ячейки (по умолчанию защита не применяется, пока не активирована защита)
3. Заблокировать определённые ячейки
4. Защитите лист для применения блокировки

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]

# Unlock all cells first
style = ac.Style()
style.is_locked = False
style_flag = ac.StyleFlag()
style_flag.locked = True
worksheet.cells.apply_style(style, style_flag)

# Lock specific cells
worksheet.cells["A1"].get_style().is_locked = True
worksheet.cells["B2"].get_style().is_locked = True

# Enable worksheet protection
worksheet.protect(ac.ProtectionType.ALL)

# Save protected workbook
workbook.save("output.xlsx")
```

## **Результат вывода**
Эта реализация блокирует указанные ячейки (A1 и B2), в то время как остальные остаются редактируемыми. Защита листа обеспечивает выполнение этих настроек.

<br>
<img src="3.png" width=60% />

```python
from aspose.cells import Workbook, ProtectionType, StyleFlag

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Unlock all cells first
unlock_style = workbook.create_style()
unlock_style.is_locked = False

style_flag = StyleFlag()
style_flag.locked = True
sheet.cells.apply_style(unlock_style, style_flag)

# Lock specific cells (A1 and B2)
lock_style = workbook.create_style()
lock_style.is_locked = True

sheet.cells.get("A1").set_style(lock_style)
sheet.cells.get("B2").set_style(lock_style)

# Protect the worksheet to enforce locking
sheet.protect(ProtectionType.ALL)

# Save the modified workbook
workbook.save("output_locked.xlsx")
```
