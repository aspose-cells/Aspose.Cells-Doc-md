---
title: Преобразование Excel в формат OFD
linktitle: Преобразование Excel в формат OFD
description: Aspose.Cells — это библиотека C++ для работы с файлами электронных таблиц, которая поддерживает преобразование рабочих книг Excel в формат OFD (Open Fixed-layout Document). В этой статье показано, как создать содержимое Excel и экспортировать его в OFD, а также как преобразовать существующие файлы Excel в OFD с помощью Aspose.Cells.
keywords: Aspose.Cells, C++ library, spreadsheet, Excel to OFD, OFD conversion, SaveFormat.Ofd, fixed-layout document, workbook export
type: docs
weight: 195
url: /ru/cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает преобразование рабочих книг Excel непосредственно в формат OFD (Open Fixed-layout Document) с помощью значения перечисления `SaveFormat.Ofd`. Полученный документ OFD сохраняет видимое расположение рабочей книги, содержимое, объединённые ячейки, ширину столбцов, высоту строк, шрифты, цвета, границы и числовые форматы. Это делает Aspose.Cells подходящим для архивирования, печати, подачи в регуляторные органы и правительственные учреждения, где требуется вывод с фиксированным макетом.

{{% /alert %}}
## **Введение**
OFD (Open Fixed-layout Document) — это китайский национальный стандарт (GB/T 33190-2016) для представления цифровых документов в фиксированном постраничном макете. Он выполняет роль, аналогичную PDF, в сценариях, где внешний вид исходного документа должен быть сохранён в точности так, как он был создан. OFD широко используется для государственных представлений, регуляторных отчётов, электронных счетов и долгосрочного архивирования в Китайской Народной Республике.

Преобразование рабочих книг Excel в OFD — распространённое требование в сценариях, где содержимое электронной таблицы должно распространяться как артефакт только для чтения с заблокированным макетом, а не как редактируемая электронная таблица. Примеры включают отправку окончательного счёта клиенту, архивирование квартального финансового отчёта или представление бюджетной таблицы в регуляторный орган. Aspose.Cells решает эту задачу с помощью значения перечисления `SaveFormat.Ofd`, которое записывает рабочую книгу непосредственно в OFD без промежуточного шага преобразования. Выходной файл OFD сохраняет значения ячеек, объединённые диапазоны, шрифты, цвета, границы, числовые форматы и параметры настройки страницы, заданные в рабочей книге.

{{% alert color="primary" %}}

Выходной файл OFD, созданный Aspose.Cells, сохраняет видимый макет исходной рабочей книги, включая содержимое ячеек, объединённые ячейки, ширину столбцов и высоту строк. Форматирование ячеек, такое как шрифты, цвета, границы, выравнивание и числовые форматы, также отображается в выводе с фиксированным макетом. Параметры настройки страницы, заданные на рабочем листе, такие как размер бумаги, ориентация и область печати, влияют на макет результирующего документа OFD.

{{% /alert %}}
## **Создание рабочей книги Excel и сохранение в формате OFD**
Aspose.Cells позволяет программно создать рабочую книгу, заполнить её данными, а затем сохранить непосредственно в формат OFD с помощью перечисления `SaveFormat.Ofd`. Следующий пример создаёт счёт-фактуру с нуля. В него добавляется логотип компании, заголовочная информация, раздел плательщика, позиции и вычисляемые итоги, после чего рабочая книга экспортируется в документ OFD.
### **Создание счёта-фактуры с логотипом**
В примере формируется рабочий лист счёта-фактуры путём вставки изображения логотипа в верхнюю левую область, заполнения названия компании и контактных данных, добавления заголовка «INVOICE» в объединённых ячейках, записи номера и даты счёта, указания клиента-плательщика, построения таблицы позиций с столбцами описания, количества, цены за единицу и итога, а также вычисления промежуточного итога, налога и общего итога с использованием формул ячеек. Такое форматирование, как жирные заголовки, денежный формат для цен, границы и ширина столбцов, применяется с помощью объектов `Style` и `Font`. Наконец, рабочая книга сохраняется с расширением `.ofd` с использованием `SaveFormat.Ofd`.

```cpp
// Пример Aspose.Cells для C++
// Компилировать с Aspose.Cells 26.6.0 (или новее) и компилятором C++17 (или новее)

#include "Aspose.Cells.h"
#include <string>
#include <ctime>

using namespace Aspose::Cells;

int main()
{
    // Инициализация Aspose.Cells
    Aspose::Cells::Startup();

    // Каталог для ресурсов и выходных файлов
    const char16_t* dataDir = u"C:\\Temp\\";

    // Создание новой рабочей книги
    Workbook workbook;

    // Получение первого рабочего листа
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Установка ширины столбцов
    cells.SetColumnWidth(0, 5.0);
    cells.SetColumnWidth(1, 35.0);
    cells.SetColumnWidth(2, 12.0);
    cells.SetColumnWidth(3, 15.0);
    cells.SetColumnWidth(4, 15.0);
    cells.SetColumnWidth(5, 5.0);

    // Вставка логотипа компании
    worksheet.GetPictures().Add(1, 1, U16String(dataDir) + u"logo.png");

    // Название компании и контактные данные
    cells.Get(u"B3").PutValue(u"Acme Corporation");
    cells.Get(u"B4").PutValue(u"123 Business Street");
    cells.Get(u"B5").PutValue(u"City, State 12345");
    cells.Get(u"B6").PutValue(u"Phone: (555) 123-4567");

    // Заголовок INVOICE - объединение ячеек
    cells.Merge(7, 1, 2, 4);
    Cell titleCell = cells.Get(u"B8");
    titleCell.PutValue(u"INVOICE");

    Style titleStyle = workbook.CreateStyle();
    titleStyle.GetFont().SetIsBold(true);
    titleStyle.GetFont().SetSize(20);
    titleStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    titleCell.SetStyle(titleStyle);

    // Номер счёта и дата
    cells.Get(u"B11").PutValue(u"Invoice Number:");
    cells.Get(u"C11").PutValue(u"INV-2024-001");
    cells.Get(u"B12").PutValue(u"Date:");

    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char dateBuffer[11];
    std::strftime(dateBuffer, sizeof(dateBuffer), "%Y-%m-%d", now);
    cells.Get(u"C12").PutValue(U16String(dateBuffer));

    // Раздел "Плательщик"
    cells.Get(u"B14").PutValue(u"Bill To:");
    cells.Get(u"B15").PutValue(u"Client Name");
    cells.Get(u"B16").PutValue(u"Client Address");
    cells.Get(u"B17").PutValue(u"Client City, State");

    // Заголовок строк позиций
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
    headerStyle.SetForegroundColor(Color{0, 0, 128});
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

    // Стиль валюты с границами
    Style currencyStyle = workbook.CreateStyle();
    currencyStyle.SetCustom(u"\"$\"#,##0.00");
    currencyStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    // Обычный стиль с границами для ячеек описания/количества
    Style borderStyle = workbook.CreateStyle();
    borderStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    // Строки позиций
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

        std::string formula = "C" + std::to_string(row) + "*D" + std::to_string(row);
        totalCell.SetFormula(U16String(formula.c_str()));

        descCell.SetStyle(borderStyle);
        qtyCell.SetStyle(borderStyle);
        priceCell.SetStyle(currencyStyle);
        totalCell.SetStyle(currencyStyle);
    }

    // Промежуточный итог, налог, общий итог
    cells.Get(u"B24").PutValue(u"Subtotal:");
    Cell subtotalCell = cells.Get(u"E24");
    subtotalCell.SetFormula(u"SUM(E20:E22)");

    cells.Get(u"B25").PutValue(u"Tax (10%):");
    Cell taxCell = cells.Get(u"E25");
    taxCell.SetFormula(u"E24*0.1");

    cells.Get(u"B26").PutValue(u"Grand Total:");
    Cell grandTotalCell = cells.Get(u"E26");
    grandTotalCell.SetFormula(u"E24+E25");

    // Жирный стиль и стиль валюты для значений итогов
    Style totalStyle = workbook.CreateStyle();
    totalStyle.GetFont().SetIsBold(true);
    totalStyle.SetCustom(u"\"$\"#,##0.00");

    subtotalCell.SetStyle(totalStyle);
    taxCell.SetStyle(totalStyle);
    grandTotalCell.SetStyle(totalStyle);

    // Жирный стиль для меток итогов
    Style boldStyle = workbook.CreateStyle();
    boldStyle.GetFont().SetIsBold(true);

    cells.Get(u"B24").SetStyle(boldStyle);
    cells.Get(u"B25").SetStyle(boldStyle);
    cells.Get(u"B26").SetStyle(boldStyle);

    // Сохранение рабочей книги в формате OFD
    workbook.Save(U16String(dataDir) + u"Invoice.ofd", SaveFormat::Ofd);

    // Освобождение ресурсов Aspose.Cells
    Aspose::Cells::Cleanup();

    return 0;
}
```
## **Преобразование существующего файла Excel в OFD**
Aspose.Cells также может загрузить существующую рабочую книгу Excel с диска и экспортировать её непосредственно в формат OFD. Это полезно для конвейеров пакетного преобразования, рабочих процессов архивирования и сценариев, в которых исходная рабочая книга была создана другим инструментом и её нужно только повторно выпустить как артефакт с фиксированным макетом. Следующий пример загружает существующую рабочую книгу `.xlsx`, считывает данные из её ячеек, применяет необязательные корректировки настройки страницы и сохраняет результат как документ OFD.

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

    // Открыть существующую книгу Excel с диска
    Workbook workbook(U16String((dataDir + "SampleBook.xlsx").c_str()));

    // (1) Прочитать и отобразить значения из выбранных ячеек, чтобы подтвердить загрузку файла
    Worksheet firstSheet = workbook.GetWorksheets().Get(0);
    U16String sheetName = firstSheet.GetName();
    Cell a1 = firstSheet.GetCells().Get(u"A1");
    Cell b1 = firstSheet.GetCells().Get(u"B1");
    Cell c1 = firstSheet.GetCells().Get(u"C1");

    std::cout << "First sheet name: " << sheetName.ToUtf8() << std::endl;
    std::cout << "Cell A1: " << a1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell B1: " << b1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell C1: " << c1.GetStringValue().ToUtf8() << std::endl;

    // (2) Перебрать коллекцию Worksheets для перечисления доступных листов
    std::cout << "\nAvailable worksheets:" << std::endl;
    WorksheetCollection sheets = workbook.GetWorksheets();
    int sheetCount = sheets.GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet ws = sheets.Get(i);
        U16String wsName = ws.GetName();
        std::cout << "  [" << i << "] " << wsName.ToUtf8() << std::endl;
    }

    // (3) При необходимости обновить ячейку с меткой времени, чтобы отразить преобразование
    std::string timestamp1 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A1").PutValue(U16String(("Converted on: " + timestamp1).c_str()));

    // Добавить строку заголовка сводки в начало блока данных
    firstSheet.GetCells().InsertRow(0);
    firstSheet.GetCells().Get(u"A1").PutValue(u"Conversion Summary");

    std::string timestamp2 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A2").PutValue(U16String(("Generated: " + timestamp2).c_str()));

    // (4) Настроить свойства PageSetup на листе
    PageSetup pageSetup = firstSheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    pageSetup.SetFitToPagesTall(1);
    pageSetup.SetFitToPagesWide(1);

    // (5) При необходимости задать область печати для вывода OFD
    int lastRow = firstSheet.GetCells().GetMaxDataRow();
    int lastCol = firstSheet.GetCells().GetMaxDataColumn();
    U16String lastColLetter = CellsHelper::ColumnIndexToName(lastCol);
    std::string printArea = "A1:" + lastColLetter.ToUtf8() + std::to_string(lastRow + 1);
    firstSheet.GetPageSetup().SetPrintArea(U16String(printArea.c_str()));
    std::cout << "\nPrint area set to: " << printArea << std::endl;

    // (6) Сохранить книгу как файл OFD
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
- [Преобразование спарклайна в изображение и HTML в Aspose.Cells for C++](/cells/ru/cpp/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="cpp" >}}