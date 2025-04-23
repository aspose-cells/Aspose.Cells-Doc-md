---
title: Изменение шрифта для конкретных юникодных символов при сохранении в PDF с помощью Python.NET
linktitle: Изменить шрифт для конкретных юникодных символов
type: docs
weight: 260
url: /ru/python-net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Узнайте, как изменять шрифты для определенных юникодных символов при преобразовании в PDF с помощью Aspose.Cells для Python via .NET. Обеспечьте точное отображение текста с помощью подстановки шрифтов на уровне символов.
---

{{% alert color="primary" %}}

Некоторые юникодные символы не отображаются выбранными пользователем шрифтами. Пример такого символа — **непрерывный дефис** (U+2011), его код Unicode 8209. Этот символ нельзя отобразить шрифтом **Times New Roman**, но он допустим для таких шрифтов как **Arial Unicode MS**.

Когда такие символы встречаются в тексте, отформатированном выбранным шрифтом (например, Times New Roman), Aspose.Cells по умолчанию изменяет весь слово или предложение шрифт на совместимый (например, Arial Unicode MS). Для тех пользователей, кто хочет менять только шрифт неподдерживаемого символа, предоставляется более гранулярный контроль через свойство **PdfSaveOptions.is_font_substitution_char_granularity**.

{{% /alert %}}

## **Сравнение примеров**

Ниже приведены скриншоты с разными настройками. Первый PDF показывает полную замену текста шрифта, второй — замену только конкретных символов.

|**Полная замена текста**|**Замена на уровне символов**|
| :- | :- |
|![Полная замена шрифта](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|![Выборочная замена шрифта](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

## **Этапы реализации**

Для включения подстановки шрифтов на уровне символов:

1. Создайте объект [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)
2. Получите доступ к ячейкам листа, используя свойство [**Worksheet.cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)
3. Установите значения ячеек, содержащих специальные символы Unicode
Настройте [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) с:
   - `is_font_substitution_char_granularity = True`
Сохраните рабочую книгу в формат PDF

```python
import os
from aspose.cells import Workbook, PdfSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Create workbook object
workbook = Workbook()

# Access the first worksheet
worksheet = workbook.worksheets[0]

# Access cells
cell1 = worksheet.cells.get("A1")
cell2 = worksheet.cells.get("B1")

# Set the styles of both cells to Times New Roman
style = cell1.get_style()
style.font.name = "Times New Roman"
cell1.set_style(style)
cell2.set_style(style)

# Put the values inside the cell
cell1.put_value("Hello without Non-Breaking Hyphen")
cell2.put_value("Hello" + chr(8209) + " with Non-Breaking Hyphen")

# Autofit the columns
worksheet.auto_fit_columns()

# Save to Pdf without setting PdfSaveOptions.is_font_substitution_char_granularity
workbook.save(os.path.join(data_dir, "SampleOutput_out.pdf"))

# Save to Pdf after setting PdfSaveOptions.is_font_substitution_char_granularity to true
opts = PdfSaveOptions()
opts.is_font_substitution_char_granularity = True
workbook.save(os.path.join(data_dir, "SampleOutput2_out.pdf"), opts)
```

## **Ключевая настройка**

Используйте эти основные компоненты API:

- класс [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) для настроек отображения PDF
- свойство **is_font_substitution_char_granularity** для замены шрифта на уровне символов
- метод [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/) для генерации вывода

{{% alert color="note" %}} 
**Примечание о различиях API**: В Python.NET свойства типа boolean используют стиль snake_case (`is_font_substitution_char_granularity`) вместо PascalCase, используемого в .NET.
{{% /alert %}}
