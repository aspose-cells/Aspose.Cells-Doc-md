---
title: Конвертация Excel в формат OFD
linktitle: Конвертация Excel в формат OFD
description: Aspose.Cells for Python via .NET — это библиотека для обработки электронных таблиц, которая поддерживает преобразование книг Excel в формат OFD (Open Fixed-layout Document). В этой статье показано, как создать содержимое Excel и экспортировать его в OFD, а также как преобразовать существующие файлы Excel в OFD с помощью Aspose.Cells.
keywords: Aspose.Cells, библиотека Python via .NET, электронная таблица, Excel в OFD, преобразование в OFD, SaveFormat.Ofd, документ с фиксированным макетом, экспорт рабочей книги
type: docs
weight: 195
url: /ru/python-net/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает прямое преобразование книг Excel в формат OFD (Open Fixed-layout Document) с использованием значения перечисления `SaveFormat.Ofd`. Полученный документ OFD сохраняет видимый макет книги, содержимое, объединённые ячейки, ширину столбцов, высоту строк, шрифты, цвета, границы и числовые форматы. Это делает Aspose.Cells подходящим решением для архивирования, печати, подачи в регуляторные органы и представления в государственные органы, где требуется вывод с фиксированным макетом.

{{% /alert %}}
## **Введение**
OFD (Open Fixed-layout Document) — это китайский национальный стандарт (GB/T 33190-2016) для представления цифровых документов в фиксированном страничном макете. Он выполняет роль, аналогичную PDF, для сценариев использования, в которых визуальное представление исходного документа должно быть сохранено в точности так, как было создано. OFD широко применяется для государственных представлений, подачи в регуляторные органы, электронных счетов-фактур и долгосрочного архивирования в Китайской Народной Республике.

Преобразование книг Excel в OFD является распространённым требованием в сценариях, где содержимое электронной таблицы должно распространяться как артефакт только для чтения с заблокированным макетом, а не как редактируемая электронная таблица. Примеры включают отправку окончательного счёта клиенту, архивирование квартального финансового отчёта или передачу бюджетной таблицы в регуляторный орган. Aspose.Cells решает эту задачу с помощью значения перечисления `SaveFormat.Ofd`, которое записывает книгу напрямую в OFD без необходимости промежуточного этапа преобразования. Выходной формат OFD сохраняет значения ячеек, объединённые диапазоны, шрифты, цвета, границы, числовые форматы и параметры настройки страницы, заданные в книге.

{{% alert color="primary" %}}

Выходной формат OFD, создаваемый Aspose.Cells, сохраняет видимый макет исходной книги, включая содержимое ячеек, объединённые ячейки, ширину столбцов и высоту строк. Форматирование ячеек, такое как шрифты, цвета, границы, выравнивание и числовые форматы, также отображается в выводе с фиксированным макетом. Параметры настройки страницы, заданные на рабочем листе, такие как размер бумаги, ориентация и область печати, влияют на макет результирующего документа OFD.

{{% /alert %}}
## **Создание книги Excel и сохранение в формате OFD**
Aspose.Cells позволяет программно создать книгу, заполнить её данными, а затем сохранить её напрямую в формат OFD с помощью перечисления `SaveFormat.Ofd`. В следующем примере счёт-фактура создаётся с нуля. В него добавляются логотип компании, информация в заголовке, раздел «Кому», позиции и вычисляемые итоги, после чего книга экспортируется в документ OFD.
### **Создание счёта-фактуры с логотипом**
В примере формируется рабочий лист счёта-фактуры путём вставки изображения логотипа в верхнюю левую область, заполнения названия компании и контактных данных, добавления заголовка «INVOICE» через объединённые ячейки, записи номера и даты счёта, указания клиента в разделе «Кому», построения таблицы позиций с описанием, количеством, ценой за единицу и итоговыми столбцами, а также расчёта промежуточного итога, налога и общего итога с использованием формул в ячейках. Форматирование, такое как жирные заголовки, денежный формат для цен, границы и ширина столбцов, применяется с помощью объектов `Style` и `Font`. Наконец, книга сохраняется с расширением `.ofd` с использованием `SaveFormat.Ofd`.

```python
from datetime import datetime

data_dir = "C:\\Temp\\"

# Создать новую рабочую книгу
workbook = ac.Workbook()

# Получить первый рабочий лист
worksheet = workbook.worksheets[0]

# Установить ширину столбцов
worksheet.cells.set_column_width(0, 5)
worksheet.cells.set_column_width(1, 35)
worksheet.cells.set_column_width(2, 12)
worksheet.cells.set_column_width(3, 15)
worksheet.cells.set_column_width(4, 15)
worksheet.cells.set_column_width(5, 5)

# Вставить логотип компании
worksheet.pictures.add(1, 1, data_dir + "logo.png")

# Название компании и контактные данные
worksheet.cells["B3"].put_value("Acme Corporation")
worksheet.cells["B4"].put_value("123 Business Street")
worksheet.cells["B5"].put_value("City, State 12345")
worksheet.cells["B6"].put_value("Phone: (555) 123-4567")

# Заголовок ИНВОЙС - объединить ячейки
worksheet.cells.merge(7, 1, 2, 4)
title_cell = worksheet.cells["B8"]
title_cell.put_value("INVOICE")

title_style = workbook.create_style()
title_style.font.is_bold = True
title_style.font.size = 20
title_style.horizontal_alignment = ac.TextAlignmentType.CENTER
title_cell.set_style(title_style)

# Номер инвойса и дата
worksheet.cells["B11"].put_value("Invoice Number:")
worksheet.cells["C11"].put_value("INV-2024-001")
worksheet.cells["B12"].put_value("Date:")
worksheet.cells["C12"].put_value(datetime.now().strftime("%Y-%m-%d"))

# Секция "Плательщик"
worksheet.cells["B14"].put_value("Bill To:")
worksheet.cells["B15"].put_value("Client Name")
worksheet.cells["B16"].put_value("Client Address")
worksheet.cells["B17"].put_value("Client City, State")

# Заголовок строк позиций
header_desc = worksheet.cells["B19"]
header_qty = worksheet.cells["C19"]
header_price = worksheet.cells["D19"]
header_total = worksheet.cells["E19"]

header_desc.put_value("Description")
header_qty.put_value("Quantity")
header_price.put_value("Unit Price")
header_total.put_value("Total")

header_style = workbook.create_style()
header_style.font.is_bold = True
header_style.font.color = drawing.Color.white
header_style.background_color = drawing.Color.navy
header_style.horizontal_alignment = ac.TextAlignmentType.CENTER
header_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

header_desc.set_style(header_style)
header_qty.set_style(header_style)
header_price.set_style(header_style)
header_total.set_style(header_style)

# Стиль валюты с границами
currency_style = workbook.create_style()
currency_style.custom = "\"$\"#,##0.00"
currency_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

# Обычный стиль границ для ячеек описания/количества
border_style = workbook.create_style()
border_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

# Строки позиций
line_items = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]

for i in range(len(line_items)):
    row = 20 + i
    desc_cell = worksheet.cells[row, 1]
    qty_cell = worksheet.cells[row, 2]
    price_cell = worksheet.cells[row, 3]
    total_cell = worksheet.cells[row, 4]

    desc_cell.put_value(line_items[i][0])
    qty_cell.put_value(line_items[i][1])
    price_cell.put_value(line_items[i][2])
    total_cell.formula = "C" + str(row) + "*D" + str(row)

    desc_cell.set_style(border_style)
    qty_cell.set_style(border_style)
    price_cell.set_style(currency_style)
    total_cell.set_style(currency_style)

# Промежуточный итог, налог, общая сумма
worksheet.cells["B24"].put_value("Subtotal:")
subtotal_cell = worksheet.cells["E24"]
subtotal_cell.formula = "SUM(E20:E22)"

worksheet.cells["B25"].put_value("Tax (10%):")
tax_cell = worksheet.cells["E25"]
tax_cell.formula = "E24*0.1"

worksheet.cells["B26"].put_value("Grand Total:")
grand_total_cell = worksheet.cells["E26"]
grand_total_cell.formula = "E24+E25"

# Жирный стиль + стиль валюты для итоговых значений
total_style = workbook.create_style()
total_style.font.is_bold = True
total_style.custom = "\"$\"#,##0.00"

subtotal_cell.set_style(total_style)
tax_cell.set_style(total_style)
grand_total_cell.set_style(total_style)

# Жирный стиль для меток итогов
bold_style = workbook.create_style()
bold_style.font.is_bold = True

worksheet.cells["B24"].set_style(bold_style)
worksheet.cells["B25"].set_style(bold_style)
worksheet.cells["B26"].set_style(bold_style)

# Сохранить рабочую книгу как файл OFD
workbook.save(data_dir + "Invoice.ofd", ac.SaveFormat.Ofd)
```
## **Преобразование существующего файла Excel в OFD**
Aspose.Cells также может загрузить существующую книгу Excel с диска и экспортировать её напрямую в формат OFD. Это полезно для конвейеров пакетного преобразования, рабочих процессов архивирования и сценариев, в которых исходная книга была создана другим инструментом и её требуется только повторно выпустить как артефакт с фиксированным макетом. В следующем примере загружается существующая книга `.xlsx`, считываются данные из её ячеек, применяются необязательные настройки страницы, и результат сохраняется как документ OFD.

```python
from datetime import datetime

dataDir = "C:\\Examples\\"

# Открыть существующую книгу Excel с диска
workbook = ac.Workbook(dataDir + "SampleBook.xlsx")

# (1) Прочитать и отобразить значения из выбранных ячеек для подтверждения загрузки файла
firstSheet = workbook.worksheets[0]
print("First sheet name: " + firstSheet.name)
print("Cell A1: " + firstSheet.cells["A1"].string_value)
print("Cell B1: " + firstSheet.cells["B1"].string_value)
print("Cell C1: " + firstSheet.cells["C1"].string_value)

# (2) Перебрать коллекцию Worksheets для перечисления доступных листов
print("\nAvailable worksheets:")
for i in range(workbook.worksheets.count):
    ws = workbook.worksheets[i]
    print("  [" + str(i) + "] " + ws.name)

# (3) При необходимости обновить ячейку с временной меткой, чтобы отразить конвертацию
firstSheet.cells["A1"].put_value("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Добавить строку заголовка сводки в начало блока данных
firstSheet.cells.insert_row(0)
firstSheet.cells["A1"].put_value("Conversion Summary")
firstSheet.cells["A2"].put_value("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# (4) Настроить свойства PageSetup на листе
pageSetup = firstSheet.page_setup
pageSetup.orientation = ac.PageOrientationType.LANDSCAPE
pageSetup.paper_size = ac.PaperSizeType.PAPER_A4
pageSetup.fit_to_pages_tall = 1
pageSetup.fit_to_pages_wide = 1

# (5) При необходимости задать область печати для вывода OFD
lastRow = firstSheet.cells.max_data_row
lastCol = firstSheet.cells.max_data_column
lastColLetter = ac.CellsHelper.column_index_to_name(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.page_setup.print_area = printArea
print("\nPrint area set to: " + printArea)

# (6) Сохранить книгу как файл OFD
workbook.save(dataDir + "SampleBook.ofd", ac.SaveFormat.Ofd)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")
```

## **Связанные статьи**
- [Разделение файлов Excel на несколько файлов](/cells/ru/python-net/splitting-excel-files-into-multiple-files/)
- [Вставка изображения в ячейку](/cells/ru/python-net/inserting-an-image-into-a-cell/)
- [Чтение и запись файлов DBF](/cells/ru/python-net/dbf/)
- [Преобразование спарклайна в изображение и HTML в Aspose.Cells for Python via .NET](/cells/ru/python-net/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="python" >}}