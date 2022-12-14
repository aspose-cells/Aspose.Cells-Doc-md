---
title: Показать или скрыть линии сетки в Aspose.Cells
type: docs
weight: 50
url: /ru/net/display-or-hide-gridlines-in-aspose-cells/
---
{{% alert color="primary" %}}

Все рабочие листы Excel имеют линии сетки по умолчанию. Они помогают разграничить ячейки, чтобы было легко вводить данные в определенные ячейки. Линии сетки позволяют нам рассматривать рабочий лист как набор ячеек, где каждую ячейку легко идентифицировать.

{{% /alert %}}

## **Управление видимостью линий сетки**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Класс предоставляет широкий спектр свойств и методов для управления рабочим листом. Для управления видимостью линий сетки используйте[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс'[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) имущество.[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) является логическим свойством, что означает, что оно может хранить только**истинный** или же**ЛОЖЬ** ценность.

 Ниже приведен полный пример, демонстрирующий использование[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) собственность[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс, чтобы скрыть линии сетки первого рабочего листа файла Excel.

На снимке экрана ниже видно, что файл Book1.xls содержит три рабочих листа: Sheet1, Sheet2 и Sheet3. Все рабочие листы имеют линии сетки.

**Book1.xls: вид листа до изменения** 

![дело:изображение_альтернативный_текст](display-or-hide-gridlines-in-aspose-cells_1.png)

Файл Book1.xls открывается с помощью класса Workbook, а линии сетки на первом листе скрыты. Измененный файл сохраняется как output.xls.

**Output.xls: рабочий лист после модификации** 

![дело:изображение_альтернативный_текст](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the gridlines of the first worksheet of the Excel file

worksheet.IsGridlinesVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Скачать рабочий код**

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Gridlines)

## **Скачать пример кода**

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
