---
title: Отображение или скрытие заголовков строк и столбцов в Aspose.Cells
type: docs
weight: 60
url: /ru/net/display-or-hide-row-column-headers-in-aspose-cells/
---

{{% alert color="primary" %}}

Все листы в файле Excel состоят из ячеек, которые располагаются в строках и столбцах. Все строки и столбцы имеют уникальные значения, которые используются для их идентификации и для идентификации отдельных ячеек. Например, строки пронумерованы – 1, 2, 3, 4 и т. д., а столбцы упорядочены по алфавиту – A, B, C, D и т. д. Значения строк и столбцов отображаются в заголовках. С помощью Aspose.Cells разработчики могут контролировать видимость этих заголовков строк и столбцов.

{{% /alert %}}

## **Управление видимостью листов**

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет собой файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), позволяющую получить доступ к каждому листу в файле Excel.

Лист представляется классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления листами. Для управления видимостью заголовков строк и столбцов используйте свойство [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) класса [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) - булево свойство, что означает, что оно может хранить только значение **true** или **false**.

Ниже приведен полный пример, показывающий, как использовать свойство [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) класса [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) для скрытия заголовков строк и столбцов на первом листе файла.

На скриншоте показан файл Book1.xls, входной файл. Он содержит три листа: Sheet1, Sheet2 и Sheet3. Каждый лист показывает заголовки строк и столбцов.

**Book1.xls: лист перед внесением изменений**

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_1.png)

Файл Book1.xls открыт с помощью вызова метода Open класса Workbook, и заголовки строк и столбцов на первом листе скрыты. Измененный файл сохраняется как output.xls.

**output.xls: лист после внесения изменений** 

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the headers of rows and columns

worksheet.IsRowColumnHeadersVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Скачать работающий код**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Row%20Column%20Headers)

## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
