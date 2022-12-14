---
title: Добавление гиперссылок к данным связи в Aspose.Cells
type: docs
weight: 10
url: /ru/net/adding-hyperlinks-to-link-data-in-aspose-cells/
---
{{% alert color="primary" %}}

Гиперссылка используется для создания связи между двумя объектами. Все знакомы с использованием гиперссылок, особенно на веб-сайтах.

Используя Aspose.Cells, разработчики могут создавать различные типы гиперссылок в Microsoft файлах Excel. В этом разделе обсуждается, какие типы гиперссылок поддерживаются Aspose.Cells и как их можно использовать в наших файлах Excel.

{{% /alert %}}

## **Добавление гиперссылок**

С помощью Aspose.Cells в ячейку можно добавить три типа гиперссылок:

- [Добавление ссылки к URL](#adding-link-to-a-url).
- [Добавление ссылки на другую ячейку в том же файле](#adding-a-link-to-a-cell-in-the-same-file).
- [Добавление ссылки на внешний файл](#adding-a-link-to-an-external-file).

 Aspose.Cells позволяет разработчикам добавлять гиперссылки в файлы Excel либо с помощью API, либо[дизайнерские таблицы](/cells/ru/net/what-is-a-designer-spreadsheet/)(электронные таблицы, в которых гиперссылки создаются вручную, а Aspose.Cells используется для их импорта в другие электронные таблицы).

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет собой файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочий листКоллекция**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) который позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Класс предоставляет различные методы для добавления различных гиперссылок в файлы Excel.

### **Добавление ссылки к URL-адресу**

[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс содержит[**Гиперссылки**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) коллекция. Каждый элемент в коллекции Hyperlinks представляет гиперссылку. Добавьте гиперссылки к URL-адресам, вызвав метод Add коллекции Hyperlinks. Метод Add принимает следующие параметры:

- Cell имя, имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок
- URL-адрес, URL-адрес.

**C#**

{{< highlight "csharp" >}}

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

### **Добавление ссылки на Cell в тот же файл**

Можно добавить гиперссылки в ячейки в том же файле Excel, вызвав метод Add коллекции Hyperlink. Метод Add работает как для внутренних, так и для внешних гиперссылок. Одна версия перегруженного метода принимает следующие параметры:

- Cell имя, имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес целевой ячейки.

**C#**

{{< highlight "csharp" >}}

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

Можно добавить гиперссылки во внешние файлы Excel, вызвав метод Add коллекции Hyperlinks. Метод Add принимает следующие параметры:

- Cell имя, имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес цели, внешний файл Excel.

**C#**

{{< highlight "csharp" >}}

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

## **Скачать рабочий код**

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Adding%20Hyperlinks%20to%20Link%20Data)

## **Скачать пример кода**

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
