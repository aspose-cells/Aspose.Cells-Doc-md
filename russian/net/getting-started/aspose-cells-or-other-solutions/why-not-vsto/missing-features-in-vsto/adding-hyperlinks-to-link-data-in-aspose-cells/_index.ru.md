---
title: Добавление гиперссылок для связи данных в Aspose.Cells
type: docs
weight: 10
url: /ru/net/adding-hyperlinks-to-link-data-in-aspose-cells/
---

{{% alert color="primary" %}}

Гиперссылка используется для создания связи между двумя сущностями. Каждый знаком с использованием гиперссылок, особенно на веб-сайтах.

Используя Aspose.Cells, разработчики могут создавать различные виды гиперссылок в файлах Microsoft Excel. В этой теме обсуждается, какие типы гиперссылок поддерживает Aspose.Cells и как они могут быть использованы в наших файлах Excel.

{{% /alert %}}

## **Добавление гиперссылок**

С помощью Aspose.Cells можно добавлять три типа гиперссылок в ячейку:

- [Добавление ссылки на URL](#adding-link-to-a-url).
- [Добавление ссылки на другую ячейку в том же файле](#adding-a-link-to-a-cell-in-the-same-file).
- [Добавление ссылки на внешний файл](#adding-a-link-to-an-external-file).

Aspose.Cells позволяет разработчикам добавлять гиперссылки в файлы Excel с помощью API или [дизайнерских электронных таблиц](/cells/ru/net/what-is-a-designer-spreadsheet/) (таблиц, в которых гиперссылки создаются вручную, а Aspose.Cells используется для их импорта в другие таблицы).

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection), который позволяет получать доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет различные методы для добавления различных гиперссылок в файлы Excel.

### **Добавление ссылки на URL**

Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) содержит коллекцию [**Hyperlinks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks). Каждый элемент в коллекции Hyperlinks представляет собой гиперссылку. Добавьте гиперссылки на URL, вызвав метод Add коллекции Hyperlinks. Метод Add принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок
- URL-адрес, адрес URL.

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding a hyperlink to a URL at "A1" cell

worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **Добавление ссылки на ячейку в том же файле**

Возможно добавить гиперссылки в ячейки в том же файле Excel при вызове метода Add коллекции Hyperlink. Метод Add работает как для внутренних, так и для внешних гиперссылок. Одна из версий перегруженного метода принимает следующие параметры:

- Имя ячейки, имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес целевой ячейки.

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the first (default) worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("B3", 1, 1, "Sheet2!B9");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **Добавление ссылки на внешний файл**

Возможно добавить гиперссылку на внешний файл Excel, вызвав метод Add коллекции Hyperlinks. Метод Add принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес цели, внешний файл Excel.

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("A5", 1, 1, "C:\\book1.xls");

//Saving the Excel file

workbook.Save("C:\\book2.xls");

{{< /highlight >}}

## **Скачать работающий код**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Adding%20Hyperlinks%20to%20Link%20Data)

## **Загрузить образец кода**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
