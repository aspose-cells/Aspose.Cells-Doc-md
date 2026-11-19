---
title: Преобразование Excel в формат OFD
linktitle: Преобразование Excel в формат OFD
description: Aspose.Cells — это библиотека Node.js для работы с файлами электронных таблиц, которая поддерживает преобразование рабочих книг Excel в формат OFD (Open Fixed-layout Document). В этой статье показано, как создать содержимое Excel и экспортировать его в OFD, а также как преобразовать существующие файлы Excel в OFD с помощью Aspose.Cells.
keywords: Aspose.Cells, библиотека Node.js, электронная таблица, преобразование Excel в OFD, преобразование в OFD, SaveFormat.Ofd, документ с фиксированной разметкой, экспорт рабочей книги
type: docs
weight: 195
url: /ru/nodejs-cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает прямое преобразование рабочих книг Excel в формат OFD (Open Fixed-layout Document) с помощью значения перечисления `SaveFormat.Ofd`. В результирующем документе OFD сохраняются видимая разметка, содержимое, объединенные ячейки, ширина столбцов, высота строк, шрифты, цвета, границы и числовые форматы рабочей книги. Благодаря этому Aspose.Cells подходит для процессов архивирования, печати, подготовки отчетности для регулирующих органов и подачи документов в государственные органы, требующих результата с фиксированной разметкой.
{{% /alert %}}

## **Введение**
OFD (Open Fixed-layout Document) — китайский национальный стандарт (GB/T 33190-2016), предназначенный для представления цифровых документов в фиксированной постраничной разметке. Он выполняет роль, аналогичную PDF, в случаях, когда визуальное оформление исходного документа должно быть сохранено точно таким, каким оно было создано. OFD широко используется при подаче документов в государственные органы, представлении отчетности в регулирующие органы, оформлении электронных счетов и долгосрочном архивировании в Китайской Народной Республике.
Преобразование рабочих книг Excel в OFD часто требуется в сценариях, в которых содержимое электронной таблицы необходимо распространять не как редактируемую таблицу, а как доступный только для чтения артефакт с заблокированной разметкой. Примеры включают отправку окончательного счета клиенту, архивирование квартального финансового отчета или представление бюджетной таблицы регулирующему органу. Aspose.Cells обеспечивает это требование с помощью значения перечисления `SaveFormat.Ofd`, которое записывает рабочую книгу непосредственно в OFD без промежуточного этапа преобразования. В выходном документе OFD сохраняются значения ячеек, объединенные диапазоны, шрифты, цвета, границы, числовые форматы и параметры настройки страницы, заданные для рабочей книги.

{{% alert color="primary" %}}
В создаваемом Aspose.Cells выходном документе OFD сохраняется видимая разметка исходной рабочей книги, включая содержимое ячеек, объединенные ячейки, ширину столбцов и высоту строк. Форматирование ячеек, включая шрифты, цвета, границы, выравнивание и числовые форматы, также воспроизводится в выходных данных с фиксированной разметкой. Параметры настройки страницы, заданные для рабочего листа, например размер бумаги, ориентация и область печати, влияют на разметку результирующего документа OFD.
{{% /alert %}}

## **Создание книги Excel и сохранение в формате OFD**
Aspose.Cells позволяет программно создать рабочую книгу, заполнить ее данными, а затем сохранить непосредственно в формате OFD с помощью перечисления `SaveFormat.Ofd`. В следующем примере счет создается с нуля. В него добавляются логотип компании, информация заголовка, раздел получателя платежа, позиции счета и рассчитанные итоги, после чего рабочая книга экспортируется в документ OFD.

### **Создание счета с логотипом**
В примере создается рабочий лист счета, на котором в левую верхнюю область вставляется изображение логотипа, заполняются название компании и контактные данные, в объединенные ячейки добавляется заголовок "INVOICE", указываются номер и дата счета, вводится клиент, которому выставляется счет, создается таблица позиций со столбцами описания, количества, цены за единицу и итога, а с помощью формул ячеек рассчитываются промежуточная сумма, налог и общий итог. Форматирование, например полужирное начертание заголовков, валютный формат цен, границы и ширина столбцов, применяется с помощью объектов `Style` и `Font`. Наконец рабочая книга сохраняется с расширением `.ofd` с помощью `SaveFormat.Ofd`.

```javascript
const AsposeCells = require("aspose.cells.node");
let dataDir = "C:\\Temp\\";
// Create a new Workbook
let workbook = new AsposeCells.Workbook();
// Obtain the first worksheet
let worksheet = workbook.getWorksheets().get(0);
// Set column widths
worksheet.getCells().setColumnWidth(0, 5);
worksheet.getCells().setColumnWidth(1, 35);
worksheet.getCells().setColumnWidth(2, 12);
worksheet.getCells().setColumnWidth(3, 15);
worksheet.getCells().setColumnWidth(4, 15);
worksheet.getCells().setColumnWidth(5, 5);
// Insert company logo
worksheet.getPictures().add(1, 1, dataDir + "logo.png");
// Company name and contact details
worksheet.getCells().get("B3").putValue("Acme Corporation");
worksheet.getCells().get("B4").putValue("123 Business Street");
worksheet.getCells().get("B5").putValue("City, State 12345");
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567");
// INVOICE title - merge cells
worksheet.getCells().merge(7, 1, 2, 4);
let titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");
let titleStyle = workbook.createStyle();
titleStyle.getFont().setIsBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
titleCell.setStyle(titleStyle);
// Invoice number and date
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
let now = new Date();
let dateStr = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
worksheet.getCells().get("C12").putValue(dateStr);
// Bill-to section
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");
// Line items header
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
// Currency style with borders
let currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
// Plain border style for description/quantity cells
let borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
// Line items rows
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
// Subtotal, tax, grand total
worksheet.getCells().get("B24").putValue("Subtotal:");
let subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");
worksheet.getCells().get("B25").putValue("Tax (10%):");
let taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");
worksheet.getCells().get("B26").putValue("Grand Total:");
let grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");
// Bold + currency style for total values
let totalStyle = workbook.createStyle();
totalStyle.getFont().setIsBold(true);
totalStyle.setCustom("\"$\"#,##0.00");
subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);
// Bold style for total labels
let boldStyle = workbook.createStyle();
boldStyle.getFont().setIsBold(true);
worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);
// Save the workbook as an OFD file
workbook.save(dataDir + "Invoice.ofd", AsposeCells.SaveFormat.Ofd);
```

## **Преобразование существующего файла Excel в OFD**
Aspose.Cells также может загрузить существующую рабочую книгу Excel с диска и экспортировать ее непосредственно в формат OFD. Это полезно в конвейерах пакетного преобразования, рабочих процессах архивирования, а также в сценариях, где исходная рабочая книга была создана другим инструментом и ее необходимо только повторно сформировать как артефакт с фиксированной разметкой. В следующем примере загружается существующая рабочая книга `.xlsx`, данные считываются из ее ячеек, применяются необязательные изменения параметров настройки страницы, а результат сохраняется как документ OFD.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook(dataDir + "SampleBook.xlsx");
// (1) Read and display values from selected cells to confirm the file was loaded
let firstSheet = workbook.getWorksheets().get(0);
console.log("First sheet name: " + firstSheet.getName());
console.log("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
console.log("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
console.log("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());
// (2) Iterate over the Worksheets collection to enumerate available sheets
console.log("\nAvailable worksheets:");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    let ws = workbook.getWorksheets().get(i);
    console.log("  [" + i + "] " + ws.getName());
}
// (3) Optionally update a timestamp cell to reflect the conversion
firstSheet.getCells().get("A1").putValue("Converted on: " + formatDate(new Date()));
// Append a summary header row at the top of the data block
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
firstSheet.getCells().get("A2").putValue("Generated: " + formatDate(new Date()));
// (4) Configure PageSetup properties on the worksheet
let pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(AsposeCells.PageOrientationType.Landscape);
pageSetup.setPaperSize(AsposeCells.PaperSizeType.PaperA4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);
// (5) Optionally set the print area for the OFD output
let lastRow = firstSheet.getCells().getMaxDataRow();
let lastCol = firstSheet.getCells().getMaxDataColumn();
let lastColLetter = AsposeCells.CellsHelper.columnIndexToName(lastCol);
let printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
console.log("\nPrint area set to: " + printArea);
// (6) Save the workbook as an OFD file
workbook.save(dataDir + "SampleBook.ofd", AsposeCells.SaveFormat.Ofd);
console.log("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **Связанные статьи**
- [Разделение файлов Excel на несколько файлов](/cells/ru/nodejs-cpp/splitting-excel-files-into-multiple-files/)
- [Вставка изображения в ячейку](/cells/ru/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Чтение и запись файлов DBF](/cells/ru/nodejs-cpp/dbf/)

{{< app/cells/assistant language="nodejs-cpp" >}}