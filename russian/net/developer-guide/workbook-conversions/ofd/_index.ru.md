---
title: Преобразование Excel в формат OFD
description: Aspose.Cells — это библиотека .NET для работы с файлами электронных таблиц, которая поддерживает преобразование рабочих книг Excel в формат OFD (Open Fixed-layout Document). В этой статье показано, как создать содержимое Excel и экспортировать его в формат OFD, а также как преобразовать существующие файлы Excel в OFD с помощью Aspose.Cells.
linktitle: Преобразование Excel в формат OFD
keywords: Aspose.Cells, библиотека .NET, электронные таблицы, Excel в OFD, преобразование в OFD, SaveFormat.Ofd, документ с фиксированным макетом, экспорт рабочей книги
type: docs
weight: 195
url: /ru/net/converting-excel-to-ofd-format/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает прямое преобразование рабочих книг Excel в формат OFD (Open Fixed-layout Document) с помощью значения перечисления `SaveFormat.Ofd`. Полученный документ OFD сохраняет видимый макет рабочей книги, содержимое, объединённые ячейки, ширину столбцов, высоту строк, шрифты, цвета, границы и числовые форматы. Это делает Aspose.Cells подходящим решением для архивирования, печати, подачи в регуляторные органы и государственные учреждения, где требуется вывод с фиксированным макетом.
{{% /alert %}}

## **Введение**
OFD (Open Fixed-layout Document) — это китайский национальный стандарт (GB/T 33190-2016) для представления цифровых документов в фиксированном страничном макете. Он выполняет роль, аналогичную PDF, в тех случаях, когда внешний вид исходного документа должен быть сохранён в точности так, как он был создан. OFD широко применяется для государственных отправлений, подачи в регуляторные органы, электронных счетов-фактур и долгосрочного архивирования в Китайской Народной Республике.
Преобразование рабочих книг Excel в формат OFD является распространённой задачей в сценариях, где содержимое электронной таблицы должно распространяться как артефакт только для чтения с заблокированным макетом, а не как редактируемая электронная таблица. Примеры включают отправку готового счёта клиенту, архивирование квартального финансового отчёта или подачу бюджетной таблицы в регуляторный орган. Aspose.Cells решает эту задачу с помощью значения перечисления `SaveFormat.Ofd`, которое записывает рабочую книгу напрямую в формат OFD без необходимости промежуточного этапа преобразования. Выходной документ OFD сохраняет значения ячеек, объединённые диапазоны, шрифты, цвета, границы, числовые форматы и параметры настройки страницы, заданные в рабочей книге.

{{% alert color="primary" %}}
Выходной документ OFD, сформированный Aspose.Cells, сохраняет видимый макет исходной рабочей книги, включая содержимое ячеек, объединённые ячейки, ширину столбцов и высоту строк. Форматирование ячеек, такое как шрифты, цвета, границы, выравнивание и числовые форматы, также отображается в выводе с фиксированным макетом. Параметры настройки страницы, заданные на рабочем листе, такие как размер бумаги, ориентация и область печати, влияют на макет результирующего документа OFD.
{{% /alert %}}

## **Создание рабочей книги Excel и сохранение в формате OFD**
Aspose.Cells позволяет программно создать рабочую книгу, заполнить её данными, а затем сохранить её непосредственно в формате OFD с помощью перечисления `SaveFormat.Ofd`. Следующий пример создаёт счёт-фактуру с нуля. В него добавляется логотип компании, заголовочная информация, раздел получателя, позиции и вычисляемые итоги, после чего рабочая книга экспортируется в документ OFD.

### **Формирование счёта-фактуры с логотипом**
Пример формирует лист счёта-фактуры путём вставки изображения логотипа в верхнюю левую область, заполнения названия компании и контактных данных, добавления заголовка «INVOICE» через объединённые ячейки, указания номера и даты счёта, перечисления клиента-получателя, построения таблицы позиций с колонками описания, количества, цены за единицу и итога, а также расчёта промежуточной суммы, налога и общей суммы с помощью формул ячеек. Форматирование, такое как жирные заголовки, денежный формат для цен, границы и ширина столбцов, применяется с помощью объектов `Style` и `Font`. Наконец, рабочая книга сохраняется с расширением `.ofd` с использованием `SaveFormat.Ofd`.

```csharp
using System;
using Aspose.Cells;
using System.Drawing;
string dataDir = "C:\\Temp\\";
// Create a new Workbook
Workbook workbook = new Workbook();
// Obtain the first worksheet
Worksheet worksheet = workbook.Worksheets[0];
// Set column widths
worksheet.Cells.SetColumnWidth(0, 5);
worksheet.Cells.SetColumnWidth(1, 35);
worksheet.Cells.SetColumnWidth(2, 12);
worksheet.Cells.SetColumnWidth(3, 15);
worksheet.Cells.SetColumnWidth(4, 15);
worksheet.Cells.SetColumnWidth(5, 5);
// Insert company logo
worksheet.Pictures.Add(1, 1, dataDir + "logo.png");
// Company name and contact details
worksheet.Cells["B3"].PutValue("Acme Corporation");
worksheet.Cells["B4"].PutValue("123 Business Street");
worksheet.Cells["B5"].PutValue("City, State 12345");
worksheet.Cells["B6"].PutValue("Phone: (555) 123-4567");
// INVOICE title - merge cells
worksheet.Cells.Merge(7, 1, 2, 4);
Cell titleCell = worksheet.Cells["B8"];
titleCell.PutValue("INVOICE");
Style titleStyle = workbook.CreateStyle();
titleStyle.Font.IsBold = true;
titleStyle.Font.Size = 20;
titleStyle.HorizontalAlignment = TextAlignmentType.Center;
titleCell.SetStyle(titleStyle);
// Invoice number and date
worksheet.Cells["B11"].PutValue("Invoice Number:");
worksheet.Cells["C11"].PutValue("INV-2024-001");
worksheet.Cells["B12"].PutValue("Date:");
worksheet.Cells["C12"].PutValue(DateTime.Now.ToString("yyyy-MM-dd"));
// Bill-to section
worksheet.Cells["B14"].PutValue("Bill To:");
worksheet.Cells["B15"].PutValue("Client Name");
worksheet.Cells["B16"].PutValue("Client Address");
worksheet.Cells["B17"].PutValue("Client City, State");
// Line items header
Cell headerDesc = worksheet.Cells["B19"];
Cell headerQty = worksheet.Cells["C19"];
Cell headerPrice = worksheet.Cells["D19"];
Cell headerTotal = worksheet.Cells["E19"];
headerDesc.PutValue("Description");
headerQty.PutValue("Quantity");
headerPrice.PutValue("Unit Price");
headerTotal.PutValue("Total");
Style headerStyle = workbook.CreateStyle();
headerStyle.Font.IsBold = true;
headerStyle.Font.Color = Color.White;
headerStyle.ForegroundColor = Color.Navy;
headerStyle.Pattern = BackgroundType.Solid;
headerStyle.HorizontalAlignment = TextAlignmentType.Center;
headerStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
headerDesc.SetStyle(headerStyle);
headerQty.SetStyle(headerStyle);
headerPrice.SetStyle(headerStyle);
headerTotal.SetStyle(headerStyle);
// Currency style with borders
Style currencyStyle = workbook.CreateStyle();
currencyStyle.Custom = "\"$\"#,##0.00";
currencyStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
// Plain border style for description/quantity cells
Style borderStyle = workbook.CreateStyle();
borderStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
// Line items rows
object[,] lineItems = new object[,] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};
for (int i = 0; i < lineItems.GetLength(0); i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.Cells[row, 1];
    Cell qtyCell = worksheet.Cells[row, 2];
    Cell priceCell = worksheet.Cells[row, 3];
    Cell totalCell = worksheet.Cells[row, 4];
    descCell.PutValue(lineItems[i, 0]);
    qtyCell.PutValue(lineItems[i, 1]);
    priceCell.PutValue(lineItems[i, 2]);
    totalCell.Formula = "C" + (row + 1) + "*D" + (row + 1);
    descCell.SetStyle(borderStyle);
    qtyCell.SetStyle(borderStyle);
    priceCell.SetStyle(currencyStyle);
    totalCell.SetStyle(currencyStyle);
}
// Subtotal, tax, grand total
worksheet.Cells["B24"].PutValue("Subtotal:");
Cell subtotalCell = worksheet.Cells["E24"];
subtotalCell.Formula = "SUM(E21:E23)";
worksheet.Cells["B25"].PutValue("Tax (10%):");
Cell taxCell = worksheet.Cells["E25"];
taxCell.Formula = "E24*0.1";
worksheet.Cells["B26"].PutValue("Grand Total:");
Cell grandTotalCell = worksheet.Cells["E26"];
grandTotalCell.Formula = "E24+E25";
// Bold + currency style for total values
Style totalStyle = workbook.CreateStyle();
totalStyle.Font.IsBold = true;
totalStyle.Custom = "\"$\"#,##0.00";
subtotalCell.SetStyle(totalStyle);
taxCell.SetStyle(totalStyle);
grandTotalCell.SetStyle(totalStyle);
// Bold style for total labels
Style boldStyle = workbook.CreateStyle();
boldStyle.Font.IsBold = true;
worksheet.Cells["B24"].SetStyle(boldStyle);
worksheet.Cells["B25"].SetStyle(boldStyle);
worksheet.Cells["B26"].SetStyle(boldStyle);
// Save the workbook as an OFD file
workbook.Save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```

## **Преобразование существующего файла Excel в OFD**
Aspose.Cells также может загрузить существующую рабочую книгу Excel с диска и экспортировать её напрямую в формат OFD. Это полезно для конвейеров пакетного преобразования, архивных процессов и сценариев, в которых исходная рабочая книга была создана другим инструментом и требуется только повторно сформировать её как артефакт с фиксированным макетом. Следующий пример загружает существующую рабочую книгу `.xlsx`, считывает данные из её ячеек, при необходимости применяет настройки страницы и сохраняет результат как документ OFD.

```csharp
using System;
using Aspose.Cells;
string dataDir = "C:\\Examples\\";
// Open an existing Excel workbook from disk
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");
// (1) Read and display values from selected cells to confirm the file was loaded
Worksheet firstSheet = workbook.Worksheets[0];
Console.WriteLine("First sheet name: " + firstSheet.Name);
Console.WriteLine("Cell A1: " + firstSheet.Cells["A1"].StringValue);
Console.WriteLine("Cell B1: " + firstSheet.Cells["B1"].StringValue);
Console.WriteLine("Cell C1: " + firstSheet.Cells["C1"].StringValue);
// (2) Iterate over the Worksheets collection to enumerate available sheets
Console.WriteLine("\nAvailable worksheets:");
for (int i = 0; i < workbook.Worksheets.Count; i++)
{
    Worksheet ws = workbook.Worksheets[i];
    Console.WriteLine("  [" + i + "] " + ws.Name);
}
// (3) Optionally update a timestamp cell to reflect the conversion
firstSheet.Cells["A1"].PutValue("Converted on: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));
// Append a summary header row at the top of the data block
firstSheet.Cells.InsertRow(0);
firstSheet.Cells["A1"].PutValue("Conversion Summary");
firstSheet.Cells["A2"].PutValue("Generated: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));
// (4) Configure PageSetup properties on the worksheet
PageSetup pageSetup = firstSheet.PageSetup;
pageSetup.Orientation = PageOrientationType.Landscape;
pageSetup.PaperSize = PaperSizeType.PaperA4;
pageSetup.FitToPagesTall = 1;
pageSetup.FitToPagesWide = 1;
// (5) Optionally set the print area for the OFD output
int lastRow = firstSheet.Cells.MaxDataRow;
int lastCol = firstSheet.Cells.MaxDataColumn;
string lastColLetter = CellsHelper.ColumnIndexToName(lastCol);
string printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.PageSetup.PrintArea = printArea;
Console.WriteLine("\nPrint area set to: " + printArea);
// (6) Save the workbook as an OFD file
workbook.Save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
Console.WriteLine("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **Связанные статьи**
- [Разделение файлов Excel на несколько файлов](/cells/ru/net/splitting-excel-files-into-multiple-files/)
- [Вставка изображения в ячейку](/cells/ru/net/inserting-an-image-into-a-cell/)
- [Чтение и запись файлов DBF](/cells/ru/net/dbf/)
- [Преобразование спарклайна в изображение и HTML в Aspose.Cells for .NET](/cells/ru/net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="csharp" >}}