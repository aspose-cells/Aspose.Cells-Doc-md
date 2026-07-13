---
title: Преобразование Excel в формат OFD
linktitle: Преобразование Excel в формат OFD
description: Aspose.Cells — это библиотека .NET для работы с файлами электронных таблиц, которая поддерживает преобразование рабочих книг Excel в формат OFD (Open Fixed-layout Document). В этой статье показано, как создать содержимое Excel и экспортировать его в формат OFD, а также как преобразовать существующие файлы Excel в OFD с помощью Aspose.Cells.
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

// Создаём новую рабочую книгу
Workbook workbook = new Workbook();

// Получаем первый рабочий лист
Worksheet worksheet = workbook.Worksheets[0];

// Устанавливаем ширину столбцов
worksheet.Cells.SetColumnWidth(0, 5);
worksheet.Cells.SetColumnWidth(1, 35);
worksheet.Cells.SetColumnWidth(2, 12);
worksheet.Cells.SetColumnWidth(3, 15);
worksheet.Cells.SetColumnWidth(4, 15);
worksheet.Cells.SetColumnWidth(5, 5);

// Вставляем логотип компании
worksheet.Pictures.Add(1, 1, dataDir + "logo.png");

// Название компании и контактные данные
worksheet.Cells["B3"].PutValue("Acme Corporation");
worksheet.Cells["B4"].PutValue("123 Business Street");
worksheet.Cells["B5"].PutValue("City, State 12345");
worksheet.Cells["B6"].PutValue("Phone: (555) 123-4567");

// Заголовок INVOICE - объединяем ячейки
worksheet.Cells.Merge(7, 1, 2, 4);
Cell titleCell = worksheet.Cells["B8"];
titleCell.PutValue("INVOICE");

Style titleStyle = workbook.CreateStyle();
titleStyle.Font.IsBold = true;
titleStyle.Font.Size = 20;
titleStyle.HorizontalAlignment = TextAlignmentType.Center;
titleCell.SetStyle(titleStyle);

// Номер счёта и дата
worksheet.Cells["B11"].PutValue("Invoice Number:");
worksheet.Cells["C11"].PutValue("INV-2024-001");
worksheet.Cells["B12"].PutValue("Date:");
worksheet.Cells["C12"].PutValue(DateTime.Now.ToString("yyyy-MM-dd"));

// Раздел "Кому" (плательщик)
worksheet.Cells["B14"].PutValue("Bill To:");
worksheet.Cells["B15"].PutValue("Client Name");
worksheet.Cells["B16"].PutValue("Client Address");
worksheet.Cells["B17"].PutValue("Client City, State");

// Заголовок строк позиций
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
headerStyle.BackgroundColor = Color.Navy;
headerStyle.HorizontalAlignment = TextAlignmentType.Center;
headerStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

headerDesc.SetStyle(headerStyle);
headerQty.SetStyle(headerStyle);
headerPrice.SetStyle(headerStyle);
headerTotal.SetStyle(headerStyle);

// Стиль валюты с границами
Style currencyStyle = workbook.CreateStyle();
currencyStyle.Custom = "\"$\"#,##0.00";
currencyStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

// Обычный стиль границ для ячеек описания/количества
Style borderStyle = workbook.CreateStyle();
borderStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

// Строки позиций
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
    totalCell.Formula = "C" + row + "*D" + row;

    descCell.SetStyle(borderStyle);
    qtyCell.SetStyle(borderStyle);
    priceCell.SetStyle(currencyStyle);
    totalCell.SetStyle(currencyStyle);
}

// Промежуточная сумма, налог, итоговая сумма
worksheet.Cells["B24"].PutValue("Subtotal:");
Cell subtotalCell = worksheet.Cells["E24"];
subtotalCell.Formula = "SUM(E20:E22)";

worksheet.Cells["B25"].PutValue("Tax (10%):");
Cell taxCell = worksheet.Cells["E25"];
taxCell.Formula = "E24*0.1";

worksheet.Cells["B26"].PutValue("Grand Total:");
Cell grandTotalCell = worksheet.Cells["E26"];
grandTotalCell.Formula = "E24+E25";

// Жирный шрифт + стиль валюты для итоговых значений
Style totalStyle = workbook.CreateStyle();
totalStyle.Font.IsBold = true;
totalStyle.Custom = "\"$\"#,##0.00";

subtotalCell.SetStyle(totalStyle);
taxCell.SetStyle(totalStyle);
grandTotalCell.SetStyle(totalStyle);

// Жирный стиль для подписей итогов
Style boldStyle = workbook.CreateStyle();
boldStyle.Font.IsBold = true;

worksheet.Cells["B24"].SetStyle(boldStyle);
worksheet.Cells["B25"].SetStyle(boldStyle);
worksheet.Cells["B26"].SetStyle(boldStyle);

// Сохраняем рабочую книгу как файл OFD
workbook.Save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```
## **Преобразование существующего файла Excel в OFD**
Aspose.Cells также может загрузить существующую рабочую книгу Excel с диска и экспортировать её напрямую в формат OFD. Это полезно для конвейеров пакетного преобразования, архивных процессов и сценариев, в которых исходная рабочая книга была создана другим инструментом и требуется только повторно сформировать её как артефакт с фиксированным макетом. Следующий пример загружает существующую рабочую книгу `.xlsx`, считывает данные из её ячеек, при необходимости применяет настройки страницы и сохраняет результат как документ OFD.

```csharp
using System;
using Aspose.Cells;

string dataDir = "C:\\Examples\\";

// Открыть существующую книгу Excel с диска
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");

// (1) Прочитать и отобразить значения из выбранных ячеек для подтверждения загрузки файла
Worksheet firstSheet = workbook.Worksheets[0];
Console.WriteLine("First sheet name: " + firstSheet.Name);
Console.WriteLine("Cell A1: " + firstSheet.Cells["A1"].StringValue);
Console.WriteLine("Cell B1: " + firstSheet.Cells["B1"].StringValue);
Console.WriteLine("Cell C1: " + firstSheet.Cells["C1"].StringValue);

// (2) Перебрать коллекцию Worksheets для перечисления доступных листов
Console.WriteLine("\nAvailable worksheets:");
for (int i = 0; i < workbook.Worksheets.Count; i++)
{
    Worksheet ws = workbook.Worksheets[i];
    Console.WriteLine("  [" + i + "] " + ws.Name);
}

// (3) При необходимости обновить ячейку с меткой времени для отражения конвертации
firstSheet.Cells["A1"].PutValue("Converted on: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));

// Добавить строку заголовка сводки в начало блока данных
firstSheet.Cells.InsertRow(0);
firstSheet.Cells["A1"].PutValue("Conversion Summary");
firstSheet.Cells["A2"].PutValue("Generated: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));

// (4) Настроить свойства PageSetup на листе
PageSetup pageSetup = firstSheet.PageSetup;
pageSetup.Orientation = PageOrientationType.Landscape;
pageSetup.PaperSize = PaperSizeType.PaperA4;
pageSetup.FitToPagesTall = 1;
pageSetup.FitToPagesWide = 1;

// (5) При необходимости задать область печати для вывода OFD
int lastRow = firstSheet.Cells.MaxDataRow;
int lastCol = firstSheet.Cells.MaxDataColumn;
string lastColLetter = CellsHelper.ColumnIndexToName(lastCol);
string printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.PageSetup.PrintArea = printArea;
Console.WriteLine("\nPrint area set to: " + printArea);

// (6) Сохранить книгу как файл OFD
workbook.Save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
Console.WriteLine("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **Связанные статьи**
- [Разделение файлов Excel на несколько файлов](/cells/ru/net/splitting-excel-files-into-multiple-files/)
- [Вставка изображения в ячейку](/cells/ru/net/inserting-an-image-into-a-cell/)
- [Чтение и запись файлов DBF](/cells/ru/net/dbf/)
- [Преобразование спарклайна в изображение и HTML в Aspose.Cells for .NET](/cells/ru/net/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="csharp" >}}