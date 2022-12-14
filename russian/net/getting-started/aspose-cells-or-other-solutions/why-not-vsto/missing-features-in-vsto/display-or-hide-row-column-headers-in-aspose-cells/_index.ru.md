---
title: Показать или скрыть заголовки столбцов строк в Aspose.Cells
type: docs
weight: 60
url: /ru/net/display-or-hide-row-column-headers-in-aspose-cells/
---
{{% alert color="primary" %}}

Все рабочие листы в файле Excel состоят из ячеек, расположенных в строках и столбцах. Все строки и столбцы имеют уникальные значения, которые используются для их идентификации и идентификации отдельных ячеек. Например, строки пронумерованы — 1, 2, 3, 4 и т. д. — а столбцы упорядочены в алфавитном порядке — A, B, C, D и т. д. Значения строк и столбцов отображаются в заголовках. Используя Aspose.Cells, разработчики могут контролировать видимость этих заголовков строк и столбцов.

{{% /alert %}}

## **Управление видимостью рабочих листов**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Класс предоставляет широкий спектр свойств и методов для управления рабочими листами. Чтобы управлять видимостью заголовков строк и столбцов, используйте[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс'[**Исровколумнхедерсвидибле**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) имущество.[**Исровколумнхедерсвидибле**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) является логическим свойством, что означает, что оно может хранить только**истинный** или же**ЛОЖЬ** ценность.

 Ниже приведен полный пример, который показывает, как использовать[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс'[**Исровколумнхедерсвидибле**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) свойство, чтобы скрыть заголовки строк и столбцов на первом рабочем листе в файле.

На снимке экрана показан входной файл Book1.xls. Он содержит три рабочих листа: Лист1, Лист2 и Лист3. Каждый рабочий лист показывает заголовки строк и столбцов.

**Book1.xls: рабочий лист до изменения**

![дело:изображение_альтернативный_текст](display-or-hide-row-column-headers-in-aspose-cells_1.png)

Book1.xls открывается путем вызова метода Open класса Workbook, а заголовки строк и столбцов на первом рабочем листе скрыты. Измененный файл сохраняется как output.xls.

**Output.xls: рабочий лист после модификации** 

![дело:изображение_альтернативный_текст](display-or-hide-row-column-headers-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

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

## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Row%20Column%20Headers)

## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
