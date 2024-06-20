---
title: Отображение или скрытие сетки в Aspose.Cells
type: docs
weight: 50
url: /ru/net/display-or-hide-gridlines-in-aspose-cells/
---

{{% alert color="primary" %}}

По умолчанию все листы Excel имеют сетку. Она помогает выделять ячейки, что упрощает ввод данных в конкретные ячейки. Сетка позволяет нам смотреть на лист как на коллекцию ячеек, где каждая ячейка легко идентифицируема.

{{% /alert %}}

## **Управление видимостью сетки**

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет собой файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), позволяющую получить доступ к каждому листу в файле Excel.

Лист представляется классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления листом. Для управления видимостью сетки используйте свойство [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) класса [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) - булево свойство, что означает, что оно может хранить только значение **true** или **false**.

Ниже приведен полный пример, демонстрирующий использование свойства [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) класса [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) для скрытия сетки на первом листе файла Excel.

На скриншоте ниже вы можете видеть, что файл Book1.xls содержит три листа: Sheet1, Sheet2 и Sheet3. Все листы имеют сетку.

**Book1.xls: вид листа до изменений** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_1.png)

Файл Book1.xls открыт с использованием класса Workbook, и сетка на первом листе скрыта. Измененный файл сохранен как output.xls.

**output.xls: лист после внесения изменений** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

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

## **Скачать работающий код**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Gridlines)

## **Загрузить образец кода**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
