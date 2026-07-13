---
title: Преобразование Excel в формат OFD
linktitle: Преобразование Excel в формат OFD
description: Aspose.Cells for Python via Java — это библиотека для работы с файлами электронных таблиц, которая поддерживает преобразование рабочих книг Excel в формат OFD (Open Fixed-layout Document). В этой статье показано, как создать содержимое Excel и экспортировать его в формат OFD, а также как преобразовать существующие файлы Excel в OFD с помощью Aspose.Cells for Python via Java.
keywords: Aspose.Cells, библиотека Python via Java, электронная таблица, Excel в OFD, преобразование в OFD, SaveFormat.Ofd, документ с фиксированной компоновкой, экспорт рабочей книги
type: docs
weight: 195
url: /ru/python-java/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via Java поддерживает преобразование рабочих книг Excel непосредственно в формат OFD (Open Fixed-layout Document) с помощью значения перечисления `SaveFormat.Ofd`. Полученный документ OFD сохраняет видимую компоновку рабочей книги, содержимое, объединённые ячейки, ширину столбцов, высоту строк, шрифты, цвета, границы и числовые форматы. Это делает Aspose.Cells for Python via Java подходящим решением для архивирования, печати, подачи в регуляторные органы и государственные учреждения, где требуется вывод с фиксированной компоновкой.

{{% /alert %}}
## **Введение**
OFD (Open Fixed-layout Document) — это китайский национальный стандарт (GB/T 33190-2016) для представления цифровых документов в фиксированной постраничной компоновке. Он выполняет роль, аналогичную PDF, для сценариев, в которых внешний вид исходного документа должен быть сохранён в точности так, как он был создан. OFD широко применяется для государственных представлений, подачи отчётности в регуляторные органы, электронных счетов-фактур и долгосрочного архивирования в Китайской Народной Республике.

Преобразование рабочих книг Excel в OFD является распространённым требованием в сценариях, где содержимое электронной таблицы должно распространяться как артефакт только для чтения с заблокированной компоновкой, а не как редактируемая электронная таблица. Примеры включают отправку окончательного счёта клиенту, архивирование квартального финансового отчёта или представление бюджетной таблицы в регуляторный орган. Aspose.Cells for Python via Java решает эту задачу с помощью значения перечисления `SaveFormat.Ofd`, которое записывает рабочую книгу непосредственно в OFD без необходимости промежуточного этапа преобразования. Выходной документ OFD сохраняет значения ячеек, объединённые диапазоны, шрифты, цвета, границы, числовые форматы и параметры настройки страницы, заданные в рабочей книге.

{{% alert color="primary" %}}

Выходной документ OFD, созданный Aspose.Cells for Python via Java, сохраняет видимую компоновку исходной рабочей книги, включая содержимое ячеек, объединённые ячейки, ширину столбцов и высоту строк. Форматирование ячеек, такое как шрифты, цвета, границы, выравнивание и числовые форматы, также отображается в выводе с фиксированной компоновкой. Параметры настройки страницы, заданные на листе, такие как размер бумаги, ориентация и область печати, влияют на компоновку результирующего документа OFD.

{{% /alert %}}
## **Создание рабочей книги Excel и сохранение в формате OFD**
Aspose.Cells for Python via Java позволяет программно создать рабочую книгу, заполнить её данными, а затем сохранить её непосредственно в формат OFD с помощью перечисления `SaveFormat.Ofd`. В следующем примере счёт-фактура создаётся с нуля. Добавляется логотип компании, заголовочная информация, раздел плательщика, позиции и вычисляемые итоги, после чего рабочая книга экспортируется в документ OFD.
### **Создание счёта-фактуры с логотипом**
В этом примере создаётся лист счёта-фактуры путём вставки изображения логотипа в верхнюю левую область, заполнения названия компании и контактных данных, добавления заголовка «INVOICE» через объединённые ячейки, записи номера и даты счёта, указания клиента-плательщика, формирования таблицы позиций с столбцами описания, количества, цены за единицу и итога, а также вычисления промежуточного итога, налога и общей суммы с использованием формул ячеек. Форматирование, такое как жирные заголовки, денежный формат для цен, границы и ширина столбцов, применяется с помощью объектов `Style` и `Font`. Наконец, рабочая книга сохраняется с расширением `.ofd` с использованием `SaveFormat.Ofd`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style, Cell, TextAlignmentType, BorderType, CellBorderType, Color

dataDir = "/tmp/"

# Создаем новую рабочую книгу
workbook = Workbook()

# Получаем первый рабочий лист
worksheet = workbook.getWorksheets().get(0)

# Устанавливаем ширину столбцов
worksheet.getCells().setColumnWidth(0, 5)
worksheet.getCells().setColumnWidth(1, 35)
worksheet.getCells().setColumnWidth(2, 12)
worksheet.getCells().setColumnWidth(3, 15)
worksheet.getCells().setColumnWidth(4, 15)
worksheet.getCells().setColumnWidth(5, 5)

# Вставляем логотип компании
worksheet.getPictures().add(1, 1, dataDir + "logo.png")

# Название компании и контактные данные
worksheet.getCells().get("B3").putValue("Acme Corporation")
worksheet.getCells().get("B4").putValue("123 Business Street")
worksheet.getCells().get("B5").putValue("City, State 12345")
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567")

# Заголовок INVOICE - объединяем ячейки
worksheet.getCells().merge(7, 1, 2, 4)
titleCell = worksheet.getCells().get("B8")
titleCell.putValue("INVOICE")

titleStyle = workbook.createStyle()
titleStyle.getFont().setBold(True)
titleStyle.getFont().setSize(20)
titleStyle.setHorizontalAlignment(TextAlignmentType.CENTER)
titleCell.setStyle(titleStyle)

# Номер счета и дата
worksheet.getCells().get("B11").putValue("Invoice Number:")
worksheet.getCells().get("C11").putValue("INV-2024-001")
worksheet.getCells().get("B12").putValue("Date:")
worksheet.getCells().get("C12").putValue(datetime.datetime.now().strftime("%Y-%m-%d"))

# Раздел "Кому"
worksheet.getCells().get("B14").putValue("Bill To:")
worksheet.getCells().get("B15").putValue("Client Name")
worksheet.getCells().get("B16").putValue("Client Address")
worksheet.getCells().get("B17").putValue("Client City, State")

# Заголовок таблицы позиций
headerDesc = worksheet.getCells().get("B19")
headerQty = worksheet.getCells().get("C19")
headerPrice = worksheet.getCells().get("D19")
headerTotal = worksheet.getCells().get("E19")

headerDesc.putValue("Description")
headerQty.putValue("Quantity")
headerPrice.putValue("Unit Price")
headerTotal.putValue("Total")

headerStyle = workbook.createStyle()
headerStyle.getFont().setBold(True)
headerStyle.getFont().setColor(Color.getWhite())
headerStyle.setBackgroundColor(Color.getNavy())
headerStyle.setHorizontalAlignment(TextAlignmentType.CENTER)
headerStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

headerDesc.setStyle(headerStyle)
headerQty.setStyle(headerStyle)
headerPrice.setStyle(headerStyle)
headerTotal.setStyle(headerStyle)

# Стиль валюты с границами
currencyStyle = workbook.createStyle()
currencyStyle.setCustom("\"$\"#,##0.00")
currencyStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

# Простой стиль границ для ячеек описания/количества
borderStyle = workbook.createStyle()
borderStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

# Строки позиций
lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]

for i in range(len(lineItems)):
    row = 20 + i
    descCell = worksheet.getCells().get(row, 1)
    qtyCell = worksheet.getCells().get(row, 2)
    priceCell = worksheet.getCells().get(row, 3)
    totalCell = worksheet.getCells().get(row, 4)

    descCell.putValue(lineItems[i][0])
    qtyCell.putValue(lineItems[i][1])
    priceCell.putValue(lineItems[i][2])
    totalCell.setFormula("C" + str(row) + "*D" + str(row))

    descCell.setStyle(borderStyle)
    qtyCell.setStyle(borderStyle)
    priceCell.setStyle(currencyStyle)
    totalCell.setStyle(currencyStyle)

# Промежуточный итог, налог, общий итог
worksheet.getCells().get("B24").putValue("Subtotal:")
subtotalCell = worksheet.getCells().get("E24")
subtotalCell.setFormula("SUM(E20:E22)")

worksheet.getCells().get("B25").putValue("Tax (10%):")
taxCell = worksheet.getCells().get("E25")
taxCell.setFormula("E24*0.1")

worksheet.getCells().get("B26").putValue("Grand Total:")
grandTotalCell = worksheet.getCells().get("E26")
grandTotalCell.setFormula("E24+E25")

# Жирный шрифт + стиль валюты для итоговых значений
totalStyle = workbook.createStyle()
totalStyle.getFont().setBold(True)
totalStyle.setCustom("\"$\"#,##0.00")

subtotalCell.setStyle(totalStyle)
taxCell.setStyle(totalStyle)
grandTotalCell.setStyle(totalStyle)

# Жирный стиль для меток итогов
boldStyle = workbook.createStyle()
boldStyle.getFont().setBold(True)

worksheet.getCells().get("B24").setStyle(boldStyle)
worksheet.getCells().get("B25").setStyle(boldStyle)
worksheet.getCells().get("B26").setStyle(boldStyle)

# Сохраняем рабочую книгу как файл OFD
workbook.save(dataDir + "Invoice.ofd", SaveFormat.Ofd)

jpype.shutdownJVM()
```
## **Преобразование существующего файла Excel в OFD**
Aspose.Cells for Python via Java также может загрузить существующую рабочую книгу Excel с диска и экспортировать её непосредственно в формат OFD. Это полезно для конвейеров пакетного преобразования, рабочих процессов архивирования и сценариев, в которых исходная рабочая книга была создана другим инструментом и её требуется только повторно выпустить как артефакт с фиксированной компоновкой. В следующем примере загружается существующая рабочая книга `.xlsx`, считываются данные из её ячеек, применяются дополнительные настройки страницы, и результат сохраняется как документ OFD.

```python
from datetime import datetime
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PageOrientationType, PaperSizeType, CellsHelper

dataDir = "C:\\Examples\\"

# Открыть существующую книгу Excel с диска
workbook = Workbook(dataDir + "SampleBook.xlsx")

# (1) Прочитать и отобразить значения выбранных ячеек для подтверждения загрузки файла
firstSheet = workbook.getWorksheets().get(0)
print("First sheet name: " + firstSheet.getName())
print("Cell A1: " + firstSheet.getCells().get("A1").getStringValue())
print("Cell B1: " + firstSheet.getCells().get("B1").getStringValue())
print("Cell C1: " + firstSheet.getCells().get("C1").getStringValue())

# (2) Перебор коллекции Worksheets для перечисления доступных листов
print("\nAvailable worksheets:")
for i in range(workbook.getWorksheets().getCount()):
    ws = workbook.getWorksheets().get(i)
    print("  [" + str(i) + "] " + ws.getName())

# (3) При необходимости обновить ячейку с меткой времени, чтобы отразить конвертацию
firstSheet.getCells().get("A1").putValue("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Добавить строку заголовка сводки в начало блока данных
firstSheet.getCells().insertRow(0)
firstSheet.getCells().get("A1").putValue("Conversion Summary")
firstSheet.getCells().get("A2").putValue("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# (4) Настроить свойства PageSetup на листе
pageSetup = firstSheet.getPageSetup()
pageSetup.setOrientation(PageOrientationType.LANDSCAPE)
pageSetup.setPaperSize(PaperSizeType.PAPER_A_4)
pageSetup.setFitToPagesTall(1)
pageSetup.setFitToPagesWide(1)

# (5) При необходимости задать область печати для вывода OFD
lastRow = firstSheet.getCells().getMaxDataRow()
lastCol = firstSheet.getCells().getMaxDataColumn()
lastColLetter = CellsHelper.columnIndexToName(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.getPageSetup().setPrintArea(printArea)
print("\nPrint area set to: " + printArea)

# (6) Сохранить книгу как файл OFD
workbook.save(dataDir + "SampleBook.ofd", SaveFormat.Ofd)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")

jpype.shutdownJVM()
```

## **Связанные статьи**
- [Разделение файлов Excel на несколько файлов](/cells/ru/python-java/splitting-excel-files-into-multiple-files/)
- [Вставка изображения в ячейку](/cells/ru/python-java/inserting-an-image-into-a-cell/)
- [Чтение и запись файлов DBF](/cells/ru/python-java/dbf/)
- [Преобразование спарклайна в изображение и HTML в Aspose.Cells for Python via Java](/cells/ru/python-java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="python" >}}