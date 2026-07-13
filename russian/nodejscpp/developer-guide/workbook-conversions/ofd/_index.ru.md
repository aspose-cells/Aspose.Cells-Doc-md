---
title: Преобразование Excel в формат OFD
linktitle: Преобразование Excel в формат OFD
description: Aspose.Cells — это библиотека для Node.js, предназначенная для работы с файлами электронных таблиц, которая поддерживает преобразование рабочих книг Excel в формат OFD (Open Fixed-layout Document). В этой статье показано, как создать содержимое Excel и экспортировать его в OFD, а также как преобразовать существующие файлы Excel в OFD с помощью Aspose.Cells.
keywords: Aspose.Cells, Node.js library, spreadsheet, Excel to OFD, OFD conversion, SaveFormat.Ofd, fixed-layout document, workbook export
type: docs
weight: 195
url: /ru/nodejs-cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает прямое преобразование рабочих книг Excel в формат OFD (Open Fixed-layout Document) с использованием значения перечисления `SaveFormat.Ofd`. Полученный документ OFD сохраняет видимое расположение рабочей книги, содержимое, объединённые ячейки, ширину столбцов, высоту строк, шрифты, цвета, границы и числовые форматы. Это делает Aspose.Cells подходящим решением для задач архивирования, печати, подачи в регуляторные органы и предоставления в государственные учреждения, где требуется вывод с фиксированным макетом.

{{% /alert %}}
## **Введение**
OFD (Open Fixed-layout Document) — это китайский национальный стандарт (GB/T 33190-2016) для представления цифровых документов в фиксированном постраничном макете. Он выполняет роль, аналогичную PDF, в тех сценариях использования, где визуальное оформление исходного документа должно быть сохранено в точности так, как было создано. OFD широко применяется для подачи документов в государственные органы, регуляторные отчёты, электронные счета-фактуры и долгосрочное архивирование в Китайской Народной Республике.

Преобразование рабочих книг Excel в OFD — распространённое требование в сценариях, где содержимое электронной таблицы необходимо распространять в виде артефакта только для чтения с заблокированным макетом, а не в виде редактируемой электронной таблицы. Примеры включают отправку окончательного счёта клиенту, архивирование квартального финансового отчёта или передачу бюджетной таблицы в регуляторный орган. Aspose.Cells решает эту задачу с помощью значения перечисления `SaveFormat.Ofd`, которое записывает рабочую книгу непосредственно в OFD без промежуточного этапа преобразования. Выходной документ OFD сохраняет значения ячеек, объединённые диапазоны, шрифты, цвета, границы, числовые форматы и параметры настройки страницы, заданные в рабочей книге.

{{% alert color="primary" %}}

Выходной документ OFD, созданный Aspose.Cells, сохраняет видимый макет исходной рабочей книги, включая содержимое ячеек, объединённые ячейки, ширину столбцов и высоту строк. Форматирование ячеек, такое как шрифты, цвета, границы, выравнивание и числовые форматы, также отображается в выводе с фиксированным макетом. Параметры настройки страницы, заданные на рабочем листе, такие как размер бумаги, ориентация и область печати, влияют на макет результирующего документа OFD.

{{% /alert %}}
## **Создание рабочей книги Excel и сохранение в формат OFD**
Aspose.Cells позволяет программно создать рабочую книгу, заполнить её данными, а затем сохранить непосредственно в формат OFD с использованием перечисления `SaveFormat.Ofd`. В следующем примере счёт создаётся с нуля. Добавляются логотип компании, информация в шапке, раздел плательщика, позиции и вычисляемые итоги, после чего рабочая книга экспортируется в документ OFD.
### **Создание счёта с логотипом**
В примере формируется рабочий лист счёта путём вставки изображения логотипа в верхнюю левую область, заполнения названия компании и контактных данных, добавления заголовка «INVOICE» через объединённые ячейки, указания номера и даты счёта, перечисления данных клиента-плательщика, построения таблицы позиций с колонками описания, количества, цены за единицу и итога, а также вычисления промежуточной суммы, налога и общей суммы с использованием формул ячеек. Форматирование, такое как жирные заголовки, денежный формат для цен, границы и ширина столбцов, применяется с помощью объектов `Style` и `Font`. Наконец, рабочая книга сохраняется с расширением `.ofd` с использованием `SaveFormat.Ofd`.

```javascript
let dataDir = "C:\\Temp\\";

// Создание новой рабочей книги
let workbook = new AsposeCells.Workbook();

// Получение первого листа
let worksheet = workbook.getWorksheets().get(0);

// Установка ширины столбцов
worksheet.getCells().setColumnWidth(0, 5);
worksheet.getCells().setColumnWidth(1, 35);
worksheet.getCells().setColumnWidth(2, 12);
worksheet.getCells().setColumnWidth(3, 15);
worksheet.getCells().setColumnWidth(4, 15);
worksheet.getCells().setColumnWidth(5, 5);

// Вставка логотипа компании
worksheet.getPictures().add(1, 1, dataDir + "logo.png");

// Название компании и контактные данные
worksheet.getCells().get("B3").putValue("Acme Corporation");
worksheet.getCells().get("B4").putValue("123 Business Street");
worksheet.getCells().get("B5").putValue("City, State 12345");
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567");

// Заголовок СЧЁТА - объединение ячеек
worksheet.getCells().merge(7, 1, 2, 4);
let titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");

let titleStyle = workbook.createStyle();
titleStyle.getFont().setIsBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
titleCell.setStyle(titleStyle);

// Номер счёта и дата
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
let now = new Date();
let dateStr = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
worksheet.getCells().get("C12").putValue(dateStr);

// Раздел "Плательщик"
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");

// Заголовок строк позиций
let headerDesc = worksheet.getCells().get("B19");
let headerQty = worksheet.getCells().get("C19");
let headerPrice = worksheet.getCells().get("D19");
let headerTotal = worksheet.getCells().get("E19");

headerDesc.putValue("Description");
headerQty.putValue("Quantity");
headerPrice.putValue("Unit Price");
headerTotal.putValue("Total");

let headerStyle = workbook.createStyle();
headerStyle.getFont().setIsBold(true);
headerStyle.getFont().setColor(AsposeCells.Color.White);
headerStyle.setBackgroundColor(AsposeCells.Color.Navy);
headerStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// Стиль валюты с границами
let currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

// Стиль простых границ для ячеек описания/количества
let borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

// Строки позиций
let lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
];

for (let i = 0; i < lineItems.length; i++) {
    let row = 20 + i;
    let descCell = worksheet.getCells().get(row, 1);
    let qtyCell = worksheet.getCells().get(row, 2);
    let priceCell = worksheet.getCells().get(row, 3);
    let totalCell = worksheet.getCells().get(row, 4);

    descCell.putValue(lineItems[i][0]);
    qtyCell.putValue(lineItems[i][1]);
    priceCell.putValue(lineItems[i][2]);
    totalCell.setFormula("C" + row + "*D" + row);

    descCell.setStyle(borderStyle);
    qtyCell.setStyle(borderStyle);
    priceCell.setStyle(currencyStyle);
    totalCell.setStyle(currencyStyle);
}

// Промежуточный итог, налог, общий итог
worksheet.getCells().get("B24").putValue("Subtotal:");
let subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");

worksheet.getCells().get("B25").putValue("Tax (10%):");
let taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");

worksheet.getCells().get("B26").putValue("Grand Total:");
let grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");

// Жирный стиль + стиль валюты для итоговых значений
let totalStyle = workbook.createStyle();
totalStyle.getFont().setIsBold(true);
totalStyle.setCustom("\"$\"#,##0.00");

subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);

// Жирный стиль для меток итогов
let boldStyle = workbook.createStyle();
boldStyle.getFont().setIsBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// Сохранение рабочей книги как файла OFD
workbook.save(dataDir + "Invoice.ofd", AsposeCells.SaveFormat.Ofd);
```
## **Преобразование существующего файла Excel в OFD**
Aspose.Cells также может загружать существующую рабочую книгу Excel с диска и экспортировать её непосредственно в формат OFD. Это полезно для конвейеров пакетного преобразования, рабочих процессов архивирования и сценариев, в которых исходная рабочая книга была создана другим инструментом и требуется только повторно сохранить её как артефакт с фиксированным макетом. В следующем примере загружается существующая рабочая книга `.xlsx`, считываются данные из её ячеек, применяются дополнительные настройки страницы и результат сохраняется как документ OFD.

```javascript
let workbook = new AsposeCells.Workbook(dataDir + "SampleBook.xlsx");

// (1) Чтение и отображение значений из выбранных ячеек для подтверждения загрузки файла
let firstSheet = workbook.getWorksheets().get(0);
console.log("First sheet name: " + firstSheet.getName());
console.log("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
console.log("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
console.log("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) Перебор коллекции Worksheets для перечисления доступных листов
console.log("\nAvailable worksheets:");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    let ws = workbook.getWorksheets().get(i);
    console.log("  [" + i + "] " + ws.getName());
}

// (3) При необходимости обновить ячейку с меткой времени, чтобы отразить преобразование
firstSheet.getCells().get("A1").putValue("Converted on: " + formatDate(new Date()));

// Append a summary header row at the top of the data block
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
firstSheet.getCells().get("A2").putValue("Generated: " + formatDate(new Date()));

// (4) Настройка свойств PageSetup на листе
let pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(AsposeCells.PageOrientationType.Landscape);
pageSetup.setPaperSize(AsposeCells.PaperSizeType.PaperA4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) При необходимости задать область печати для вывода OFD
let lastRow = firstSheet.getCells().getMaxDataRow();
let lastCol = firstSheet.getCells().getMaxDataColumn();
let lastColLetter = AsposeCells.CellsHelper.columnIndexToName(lastCol);
let printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
console.log("\nPrint area set to: " + printArea);

// (6) Сохранить книгу как файл OFD
workbook.save(dataDir + "SampleBook.ofd", AsposeCells.SaveFormat.Ofd);
console.log("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **Связанные статьи**
- [Разделение файлов Excel на несколько файлов](/cells/ru/nodejs-cpp/splitting-excel-files-into-multiple-files/)
- [Вставка изображения в ячейку](/cells/ru/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Чтение и запись файлов DBF](/cells/ru/nodejs-cpp/dbf/)
- [Преобразование спарклайна в изображение и HTML в Aspose.Cells for Node.js via C++](/cells/ru/nodejs-cpp/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="javascript" >}}