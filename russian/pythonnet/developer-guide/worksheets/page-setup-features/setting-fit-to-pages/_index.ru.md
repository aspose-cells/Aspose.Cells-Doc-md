---
title: Как распечатать Excel как страницу, подогнанную по ширине и высоте, с помощью Python.NET
linktitle: Как напечатать Excel так, чтобы страницы были шириной и высотой, подогнанными под страницу
type: docs
weight: 200
url: /ru/python-net/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Узнайте, как установить свойства fit_to_pages_wide и fit_to_pages_tall для печати Excel с помощью API Aspose.Cells for Python via .NET.
keywords: Печать Excel на Python, настройки подгонки страницы, FitToPagesWide, FitToPagesTall, печать листа одним страницм в Python, печать всех колонок на одной странице
---

## **Введение**

Параметры fit_to_pages_wide и fit_to_pages_tall управляют масштабированием таблицы при печати. Эти настройки обеспечивают, что распечатанный результат укладывается в заданные размеры страниц:

1. **fit_to_pages_wide**: указывает количество страниц по горизонтали при печати
1. **fit_to_pages_tall**: указывает количество страниц по вертикали при печати

## **Зачем использовать FitToPagesWide и FitToPagesTall**
Основные преимущества включают:
1. Точное управление макетом печати
1. Последовательное форматирование нескольких листов
1. Профессиональное оформление документов

## **Как распечатать файл по страницам по ширине и высоте в Excel**
Для настройки в Microsoft Excel:
1. Откройте рабочую книгу и выберите лист
1. Перейдите к диалоговому окну **Макет страницы** → **Настройка страницы**
1. Во вкладке **Страница** в разделе **Масштаб**:
   - Выберите "Поместить в"
   - Укажите количество страниц по ширине (горизонтально) и высоте (вертикально)

<br>
<img src="2.png" width=60% />

## **Как распечатать Excel как страницы по ширине и высоте, используя Aspose.Cells**
Для программной настройки:
1. Загрузите [пример файла](input.xlsx)
1. Получите доступ к объекту рабочей таблицы [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/)
1. Установите свойства [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall/) и [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide/)

```python
from aspose.cells import Workbook

# Instantiating a Workbook object
workbook = Workbook("input.xlsx")

# Accessing the first worksheet in the Excel file
worksheet = workbook.worksheets[0]

# Setting the number of pages to which the length of the worksheet will be spanned
worksheet.page_setup.fit_to_pages_tall = 1

# Setting the number of pages to which the width of the worksheet will be spanned
worksheet.page_setup.fit_to_pages_wide = 1

# Save the workbook
workbook.save("out_net.pdf")
```

Результат вывода:
<br>
<img src="1.png" width=60% />

## **Как распечатать лист как одну страницу**
Чтобы принудительно вывести на одну страницу:
1. Используйте [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)
1. Установите свойство [**one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/one_page_per_sheet/)

```python
from aspose.cells import Workbook, PdfSaveOptions

# Instantiating a Workbook object
workbook = Workbook("sample.xlsx")

options = PdfSaveOptions()

# Setting OnePagePerSheet option
options.one_page_per_sheet = True

# Save the workbook with options
workbook.save("OnePagePerSheet.pdf", options)
```

Результат вывода:
<br>
<img src="3.png" width=60% />

## **Как распечатать все столбцы на одной странице**
Для объединения столбцов по горизонтали:
1. Настройте [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)
1. Включите свойство [**all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/all_columns_in_one_page_per_sheet/)

```python
from aspose.cells import Workbook, PdfSaveOptions

# Instantiating a Workbook object
workbook = Workbook("sample.xlsx")

options = PdfSaveOptions()

# Setting all columns in one page per sheet
options.all_columns_in_one_page_per_sheet = True

# Save the workbook
workbook.save("AllColumnsInOnePagePerSheet.pdf", options)
```

Результат вывода:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="python-net" >}}
