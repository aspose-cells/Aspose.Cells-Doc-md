---
title: Преобразование Excel в формат OFD
linktitle: Преобразование Excel в формат OFD
description: Aspose.Cells — библиотека C++ для работы с файлами электронных таблиц, которая поддерживает преобразование рабочих книг Excel в формат OFD (Open Fixed-layout Document). В этой статье демонстрируется, как создать содержимое Excel и экспортировать его в OFD, а также как преобразовать существующие файлы Excel в OFD с помощью Aspose.Cells.
keywords: Aspose.Cells, библиотека C++, электронные таблицы, Excel в OFD, преобразование в OFD, SaveFormat.Ofd, документ с фиксированной разметкой, экспорт рабочей книги
type: docs
weight: 195
url: /ru/cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает прямое преобразование рабочих книг Excel в формат OFD (Open Fixed-layout Document) с помощью значения перечисления `SaveFormat.Ofd`. В результирующем документе OFD сохраняются видимая разметка, содержимое, объединенные ячейки, ширина столбцов, высота строк, шрифты, цвета, границы и числовые форматы рабочей книги. Благодаря этому Aspose.Cells подходит для задач архивирования, печати, представления отчетности регулирующим органам и подачи документов в государственные органы, где требуется результат с фиксированной разметкой.
{{% /alert %}}

## **Введение**
OFD (Open Fixed-layout Document) — китайский национальный стандарт (GB/T 33190-2016) для представления цифровых документов с фиксированной постраничной разметкой. Он используется аналогично PDF в случаях, когда визуальное оформление исходного документа необходимо воспроизвести точно в том виде, в каком оно было создано. OFD широко применяется для подачи документов в государственные органы, представления отчетности регулирующим органам, выставления электронных счетов и долгосрочного архивирования в Китайской Народной Республике.
Преобразование рабочих книг Excel в OFD часто требуется в случаях, когда содержимое электронной таблицы необходимо передавать как артефакт, доступный только для чтения и имеющий фиксированную разметку, а не как редактируемую электронную таблицу. Примеры включают отправку окончательно оформленного счета клиенту, архивирование ежеквартального финансового отчета или представление бюджетной электронной таблицы регулирующему органу. Для этого в Aspose.Cells предусмотрено значение перечисления `SaveFormat.Ofd`, с помощью которого рабочую книгу можно сохранить непосредственно в OFD без промежуточного этапа преобразования. В выходном документе OFD сохраняются значения ячеек, объединенные диапазоны, шрифты, цвета, границы и числовые форматы, а также параметры страницы, заданные в рабочей книге.

{{% alert color="primary" %}}
Документ OFD, создаваемый с помощью Aspose.Cells, сохраняет видимую разметку исходной рабочей книги, включая содержимое ячеек, объединенные ячейки, ширину столбцов и высоту строк. Форматирование ячеек, например шрифты, цвета, границы, выравнивание и числовые форматы, также сохраняется в выходном документе с фиксированной разметкой. Параметры страницы, заданные на рабочем листе, например размер бумаги, ориентация и область печати, влияют на разметку результирующего документа OFD.
{{% /alert %}}

## **Создание рабочей книги Excel и сохранение в формате OFD**
Aspose.Cells позволяет программно создать рабочую книгу, заполнить ее данными и сохранить непосредственно в формате OFD с помощью перечисления `SaveFormat.Ofd`. В следующем примере счет создается с нуля. В него добавляются логотип компании, сведения в заголовке, раздел с реквизитами получателя счета, позиции счета и рассчитанные итоговые суммы, после чего рабочая книга экспортируется в документ OFD.

### **Создание счета с логотипом**
В примере создается рабочий лист для счета: в левую верхнюю область вставляется изображение логотипа, затем заполняются название компании и контактные данные, в объединенном диапазоне размещается заголовок «INVOICE», указываются номер и дата счета, вводятся данные клиента, которому выставляется счет, и создается таблица позиций со столбцами описания, количества, цены за единицу и общей стоимости. Промежуточная сумма, налог и общая сумма рассчитываются с помощью формул в ячейках. Форматирование — полужирные заголовки, денежный формат цен, границы и ширина столбцов — применяется с помощью объектов `Style` и `Font`. Наконец, рабочая книга сохраняется в файл с расширением `.ofd` с использованием `SaveFormat.Ofd`.

```cpp
// Aspose.Cells for C++ example
// Compile with Aspose.Cells 26.6.0 (or later) and a C++17 (or later) compiler
#include "Aspose.Cells.h"
#include <string>
#include <ctime>
using namespace Aspose::Cells;
int main()
{
    // Initialize Aspose.Cells
    Aspose::Cells::Startup();
    // Directory for resources and output
    const char16_t* dataDir = u"C:\\Temp\\";
    // Create a new workbook
    Workbook workbook;
    // Obtain the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // Set column widths
    cells.SetColumnWidth(0, 5.0);
    cells.SetColumnWidth(1, 35.0);
    cells.SetColumnWidth(2, 12.0);
    cells.SetColumnWidth(3, 15.0);
    cells.SetColumnWidth(4, 15.0);
    cells.SetColumnWidth(5, 5.0);
    // Insert company logo
    worksheet.GetPictures().Add(1, 1, U16String(dataDir) + u"logo.png");
    // Company name and contact details
    cells.Get(u"B3").PutValue(u"Acme Corporation");
    cells.Get(u"B4").PutValue(u"123 Business Street");
    cells.Get(u"B5").PutValue(u"City, State 12345");
    cells.Get(u"B6").PutValue(u"Phone: (555) 123-4567");
    // INVOICE title - merge cells
    cells.Merge(7, 1, 2, 4);
    Cell titleCell = cells.Get(u"B8");
    titleCell.PutValue(u"INVOICE");
    Style titleStyle = workbook.CreateStyle();
    titleStyle.GetFont().SetIsBold(true);
    titleStyle.GetFont().SetSize(20);
    titleStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    titleCell.SetStyle(titleStyle);
    // Invoice number and date
    cells.Get(u"B11").PutValue(u"Invoice Number:");
    cells.Get(u"C11").PutValue(u"INV-2024-001");
    cells.Get(u"B12").PutValue(u"Date:");
    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char dateBuffer[11];
    std::strftime(dateBuffer, sizeof(dateBuffer), "%Y-%m-%d", now);
    cells.Get(u"C12").PutValue(U16String(dateBuffer));
    // Bill-to section
    cells.Get(u"B14").PutValue(u"Bill To:");
    cells.Get(u"B15").PutValue(u"Client Name");
    cells.Get(u"B16").PutValue(u"Client Address");
    cells.Get(u"B17").PutValue(u"Client City, State");
    // Line items header
    Cell headerDesc = cells.Get(u"B19");
    Cell headerQty = cells.Get(u"C19");
    Cell headerPrice = cells.Get(u"D19");
    Cell headerTotal = cells.Get(u"E19");
    headerDesc.PutValue(u"Description");
    headerQty.PutValue(u"Quantity");
    headerPrice.PutValue(u"Unit Price");
    headerTotal.PutValue(u"Total");
    Style headerStyle = workbook.CreateStyle();
    headerStyle.GetFont().SetIsBold(true);
    headerStyle.GetFont().SetColor(Color::White());
    headerStyle.SetForegroundColor(Color{0xff, 0x00, 0x00, 0x80});
    headerStyle.SetPattern(BackgroundType::Solid);
    headerStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    headerStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    headerDesc.SetStyle(headerStyle);
    headerQty.SetStyle(headerStyle);
    headerPrice.SetStyle(headerStyle);
    headerTotal.SetStyle(headerStyle);
    // Currency style with borders
    Style currencyStyle = workbook.CreateStyle();
    currencyStyle.SetCustom(u"\"$\"#,##0.00");
    currencyStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    // Plain border style for description/quantity cells
    Style borderStyle = workbook.CreateStyle();
    borderStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    // Line items rows
    struct LineItem { const char16_t* desc; int qty; double price; };
    LineItem lineItems[] = {
        {u"Product A - Widget", 2, 50.00},
        {u"Product B - Gadget", 3, 75.00},
        {u"Product C - Service", 1, 100.00}
    };
    for (int i = 0; i < 3; i++)
    {
        int row = 20 + i;
        Cell descCell = cells.Get(row, 1);
        Cell qtyCell = cells.Get(row, 2);
        Cell priceCell = cells.Get(row, 3);
        Cell totalCell = cells.Get(row, 4);
        descCell.PutValue(lineItems[i].desc);
        qtyCell.PutValue(lineItems[i].qty);
        priceCell.PutValue(lineItems[i].price);
        std::string formula = "C" + std::to_string(row + 1) + "*D" + std::to_string(row + 1);
        totalCell.SetFormula(U16String(formula.c_str()));
        descCell.SetStyle(borderStyle);
        qtyCell.SetStyle(borderStyle);
        priceCell.SetStyle(currencyStyle);
        totalCell.SetStyle(currencyStyle);
    }
    // Subtotal, tax, grand total
    cells.Get(u"B24").PutValue(u"Subtotal:");
    Cell subtotalCell = cells.Get(u"E24");
    subtotalCell.SetFormula(u"SUM(E21:E23)");
    cells.Get(u"B25").PutValue(u"Tax (10%):");
    Cell taxCell = cells.Get(u"E25");
    taxCell.SetFormula(u"E24*0.1");
    cells.Get(u"B26").PutValue(u"Grand Total:");
    Cell grandTotalCell = cells.Get(u"E26");
    grandTotalCell.SetFormula(u"E24+E25");
    // Bold + currency style for total values
    Style totalStyle = workbook.CreateStyle();
    totalStyle.GetFont().SetIsBold(true);
    totalStyle.SetCustom(u"\"$\"#,##0.00");
    subtotalCell.SetStyle(totalStyle);
    taxCell.SetStyle(totalStyle);
    grandTotalCell.SetStyle(totalStyle);
    // Bold style for total labels
    Style boldStyle = workbook.CreateStyle();
    boldStyle.GetFont().SetIsBold(true);
    cells.Get(u"B24").SetStyle(boldStyle);
    cells.Get(u"B25").SetStyle(boldStyle);
    cells.Get(u"B26").SetStyle(boldStyle);
    // Save the workbook as an OFD file
    workbook.Save(U16String(dataDir) + u"Invoice.ofd", SaveFormat::Ofd);
    // Cleanup Aspose.Cells resources
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Преобразование существующего файла Excel в OFD**
Aspose.Cells также может загрузить существующую рабочую книгу Excel с диска и экспортировать ее непосредственно в формат OFD. Это полезно для конвейеров пакетного преобразования, архивных процессов и сценариев, в которых исходная рабочая книга создана сторонним инструментом и требуется лишь повторно сохранить ее в виде артефакта с фиксированной разметкой. В следующем примере загружается существующая рабочая книга `.xlsx`, считываются данные из ее ячеек, при необходимости корректируются параметры страницы, а результат сохраняется в формате OFD.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <iostream>
#include <ctime>
using namespace Aspose::Cells;
std::string GetCurrentTimestamp() {
    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char buffer[20];
    std::strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", now);
    return std::string(buffer);
}
int main() {
    Aspose::Cells::Startup();
    std::string dataDir = "C:\\Examples\\";
    // Open an existing Excel workbook from disk
    Workbook workbook(U16String((dataDir + "SampleBook.xlsx").c_str()));
    // (1) Read and display values from selected cells to confirm the file was loaded
    Worksheet firstSheet = workbook.GetWorksheets().Get(0);
    U16String sheetName = firstSheet.GetName();
    Cell a1 = firstSheet.GetCells().Get(u"A1");
    Cell b1 = firstSheet.GetCells().Get(u"B1");
    Cell c1 = firstSheet.GetCells().Get(u"C1");
    std::cout << "First sheet name: " << sheetName.ToUtf8() << std::endl;
    std::cout << "Cell A1: " << a1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell B1: " << b1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell C1: " << c1.GetStringValue().ToUtf8() << std::endl;
    // (2) Iterate over the Worksheets collection to enumerate available sheets
    std::cout << "\nAvailable worksheets:" << std::endl;
    WorksheetCollection sheets = workbook.GetWorksheets();
    int sheetCount = sheets.GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet ws = sheets.Get(i);
        U16String wsName = ws.GetName();
        std::cout << "  [" << i << "] " << wsName.ToUtf8() << std::endl;
    }
    // (3) Optionally update a timestamp cell to reflect the conversion
    std::string timestamp1 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A1").PutValue(U16String(("Converted on: " + timestamp1).c_str()));
    // Append a summary header row at the top of the data block
    firstSheet.GetCells().InsertRow(0);
    firstSheet.GetCells().Get(u"A1").PutValue(u"Conversion Summary");
    std::string timestamp2 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A2").PutValue(U16String(("Generated: " + timestamp2).c_str()));
    // (4) Configure PageSetup properties on the worksheet
    PageSetup pageSetup = firstSheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    pageSetup.SetFitToPagesTall(1);
    pageSetup.SetFitToPagesWide(1);
    // (5) Optionally set the print area for the OFD output
    int lastRow = firstSheet.GetCells().GetMaxDataRow();
    int lastCol = firstSheet.GetCells().GetMaxDataColumn();
    U16String lastColLetter = CellsHelper::ColumnIndexToName(lastCol);
    std::string printArea = "A1:" + lastColLetter.ToUtf8() + std::to_string(lastRow + 1);
    firstSheet.GetPageSetup().SetPrintArea(U16String(printArea.c_str()));
    std::cout << "\nPrint area set to: " << printArea << std::endl;
    // (6) Save the workbook as an OFD file
    workbook.Save(U16String((dataDir + "SampleBook.ofd").c_str()), SaveFormat::Ofd);
    std::cout << "\nFile successfully converted to OFD format: " << dataDir << "SampleBook.ofd" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Связанные статьи**
- [Разделение файлов Excel на несколько файлов](/cells/ru/cpp/splitting-excel-files-into-multiple-files/)
- [Вставка изображения в ячейку](/cells/ru/cpp/inserting-an-image-into-a-cell/)
- [Чтение и запись файлов DBF](/cells/ru/cpp/dbf/)

{{< app/cells/assistant language="cpp" >}}