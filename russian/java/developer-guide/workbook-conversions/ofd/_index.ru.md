---
title: Преобразование Excel в формат OFD
description: Aspose.Cells — это Java-библиотека для работы с файлами электронных таблиц, которая поддерживает преобразование рабочих книг Excel в формат OFD (Open Fixed-layout Document). В этой статье показано, как создать содержимое Excel и экспортировать его в OFD, а также как преобразовать существующие файлы Excel в OFD с помощью Aspose.Cells.
linktitle: Преобразование Excel в формат OFD
keywords: Aspose.Cells, Java-библиотека, электронная таблица, Excel в OFD, преобразование OFD, SaveFormat.Ofd, документ с фиксированным макетом, экспорт рабочей книги
type: docs
weight: 195
url: /ru/java/converting-excel-to-ofd-format/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает прямое преобразование рабочих книг Excel в формат OFD (Open Fixed-layout Document) с помощью значения перечисления `SaveFormat.Ofd`. Полученный документ OFD сохраняет видимый макет рабочей книги, содержимое, объединённые ячейки, ширину столбцов, высоту строк, шрифты, цвета, границы и числовые форматы. Это делает Aspose.Cells подходящим решением для архивирования, печати, подачи в регуляторные органы и государственных рабочих процессов, где требуется вывод в формате с фиксированным макетом.
{{% /alert %}}

## **Введение**
OFD (Open Fixed-layout Document) — это китайский национальный стандарт (GB/T 33190-2016) для представления цифровых документов в фиксированном, постраничном макете. Он выполняет роль, аналогичную PDF, для сценариев, в которых визуальное оформление исходного документа должно быть сохранено точно в том виде, в котором оно было создано. OFD широко используется для государственных представлений, регуляторных отчётов, электронных счетов-фактур и долгосрочного архивирования в Китайской Народной Республике.
Преобразование рабочих книг Excel в OFD является распространённым требованием в сценариях, где содержимое электронной таблицы должно быть распространено в виде артефакта только для чтения с заблокированным макетом, а не в виде редактируемой электронной таблицы. Примеры включают отправку окончательного счёта клиенту, архивирование квартального финансового отчёта или представление бюджетной таблицы в регуляторный орган. Aspose.Cells решает эту задачу с помощью значения перечисления `SaveFormat.Ofd`, которое записывает рабочую книгу напрямую в OFD без необходимости промежуточного этапа преобразования. Выходной документ OFD сохраняет значения ячеек, объединённые диапазоны, шрифты, цвета, границы, числовые форматы и параметры настройки страницы, заданные в рабочей книге.

{{% alert color="primary" %}}
Выходной документ OFD, сгенерированный Aspose.Cells, сохраняет видимый макет исходной рабочей книги, включая содержимое ячеек, объединённые ячейки, ширину столбцов и высоту строк. Форматирование ячеек, такое как шрифты, цвета, границы, выравнивание и числовые форматы, также отображается в выводе с фиксированным макетом. Параметры настройки страницы, заданные на рабочем листе, такие как размер бумаги, ориентация и область печати, влияют на макет результирующего документа OFD.
{{% /alert %}}

## **Создание рабочей книги Excel и сохранение в формат OFD**
Aspose.Cells позволяет программно создать рабочую книгу, заполнить её данными, а затем сохранить её напрямую в формат OFD с помощью перечисления `SaveFormat.Ofd`. В следующем примере счёт-фактура создаётся с нуля. Добавляется логотип компании, заголовочная информация, раздел «кому выставлен счёт», позиции и вычисляемые итоги, после чего рабочая книга экспортируется в документ OFD.

### **Создание счёта-фактуры с логотипом**
В примере формируется рабочий лист счёта-фактуры путём вставки изображения логотипа в верхнюю левую область, заполнения названия компании и контактных данных, добавления заголовка «INVOICE» через объединённые ячейки, указания номера и даты счёта, внесения данных клиента, формирования таблицы позиций с колонками описания, количества, цены за единицу и итога, а также вычисления промежуточного итога, налога и общего итога с использованием формул ячеек. Форматирование, такое как жирные заголовки, денежный формат для цен, границы и ширина столбцов, применяется с помощью объектов `Style` и `Font`. Наконец, рабочая книга сохраняется с расширением `.ofd` с использованием `SaveFormat.Ofd`.

```java
import com.aspose.cells.*;
import java.text.SimpleDateFormat;
import java.util.Date;
String dataDir = "C:\\Temp\\";
// Create a new Workbook
Workbook workbook = new Workbook();
// Obtain the first worksheet
Worksheet worksheet = workbook.getWorksheets().get(0);
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
Cell titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");
Style titleStyle = workbook.createStyle();
titleStyle.getFont().setBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(TextAlignmentType.CENTER);
titleCell.setStyle(titleStyle);
// Invoice number and date
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
worksheet.getCells().get("C12").putValue(new SimpleDateFormat("yyyy-MM-dd").format(new Date()));
// Bill-to section
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");
// Line items header
Cell headerDesc = worksheet.getCells().get("B19");
Cell headerQty = worksheet.getCells().get("C19");
Cell headerPrice = worksheet.getCells().get("D19");
Cell headerTotal = worksheet.getCells().get("E19");
headerDesc.putValue("Description");
headerQty.putValue("Quantity");
headerPrice.putValue("Unit Price");
headerTotal.putValue("Total");
Style headerStyle = workbook.createStyle();
headerStyle.getFont().setBold(true);
headerStyle.getFont().setColor(Color.getWhite());
headerStyle.setBackgroundColor(Color.getNavy());
headerStyle.setHorizontalAlignment(TextAlignmentType.CENTER);
headerStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);
headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);
// Currency style with borders
Style currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);
// Plain border style for description/quantity cells
Style borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);
// Line items rows
Object[][] lineItems = new Object[][] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};
for (int i = 0; i < lineItems.length; i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.getCells().get(row, 1);
    Cell qtyCell = worksheet.getCells().get(row, 2);
    Cell priceCell = worksheet.getCells().get(row, 3);
    Cell totalCell = worksheet.getCells().get(row, 4);
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
Cell subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");
worksheet.getCells().get("B25").putValue("Tax (10%):");
Cell taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");
worksheet.getCells().get("B26").putValue("Grand Total:");
Cell grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");
// Bold + currency style for total values
Style totalStyle = workbook.createStyle();
totalStyle.getFont().setBold(true);
totalStyle.setCustom("\"$\"#,##0.00");
subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);
// Bold style for total labels
Style boldStyle = workbook.createStyle();
boldStyle.getFont().setBold(true);
worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);
// Save the workbook as an OFD file
workbook.save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```

## **Преобразование существующего файла Excel в OFD**
Aspose.Cells также может загрузить существующую рабочую книгу Excel с диска и экспортировать её напрямую в формат OFD. Это полезно для конвейеров пакетного преобразования, архивных рабочих процессов и сценариев, в которых исходная рабочая книга была создана другим инструментом и должна быть только повторно выпущена в виде артефакта с фиксированным макетом. В следующем примере загружается существующая рабочая книга `.xlsx`, считываются данные из её ячеек, применяются необязательные настройки страницы, и результат сохраняется как документ OFD.

```java
import com.aspose.cells.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
String dataDir = "C:\\Examples\\";
// Open an existing Excel workbook from disk
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");
// (1) Read and display values from selected cells to confirm the file was loaded
Worksheet firstSheet = workbook.getWorksheets().get(0);
System.out.println("First sheet name: " + firstSheet.getName());
System.out.println("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
System.out.println("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
System.out.println("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());
// (2) Iterate over the Worksheets collection to enumerate available sheets
System.out.println("\nAvailable worksheets:");
for (int i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    Worksheet ws = workbook.getWorksheets().get(i);
    System.out.println("  [" + i + "] " + ws.getName());
}
// (3) Optionally update a timestamp cell to reflect the conversion
String timestamp1 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A1").putValue("Converted on: " + timestamp1);
// Append a summary header row at the top of the data block
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
String timestamp2 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A2").putValue("Generated: " + timestamp2);
// (4) Configure PageSetup properties on the worksheet
PageSetup pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(PageOrientationType.LANDSCAPE);
pageSetup.setPaperSize(PaperSizeType.PAPER_A_4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);
// (5) Optionally set the print area for the OFD output
int lastRow = firstSheet.getCells().getMaxDataRow();
int lastCol = firstSheet.getCells().getMaxDataColumn();
String lastColLetter = CellsHelper.columnIndexToName(lastCol);
String printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
System.out.println("\nPrint area set to: " + printArea);
// (6) Save the workbook as an OFD file
workbook.save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
System.out.println("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **Связанные статьи**
- [Разделение файлов Excel на несколько файлов](/cells/ru/java/splitting-excel-files-into-multiple-files/)
- [Вставка изображения в ячейку](/cells/ru/java/inserting-an-image-into-a-cell/)
- [Чтение и запись файлов DBF](/cells/ru/java/dbf/)
- [Преобразование спарклайна в изображение и HTML в Aspose.Cells for Java](/cells/ru/java/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="java" >}}