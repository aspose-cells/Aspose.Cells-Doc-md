---
title: Показ или Скрытие Полос Прокрутки в Aspose.Cells
type: docs
weight: 70
url: /ru/net/display-or-hide-scroll-bars-in-aspose-cells/
---

{{% alert color="primary" %}}

Полосы прокрутки широко используются для навигации по содержимому любого файла. Обычно существует два типа полос прокрутки:

- Вертикальные полосы прокрутки
- Горизонтальные полосы прокрутки

Microsoft Excel также предоставляет горизонтальные и вертикальные полосы прокрутки, чтобы пользователи могли пролистывать содержимое листа Excel. Используя Aspose.Cells, разработчики могут контролировать видимость обоих типов полос прокрутки в файлах Excel.

{{% /alert %}}

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет собой файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) предоставляет широкий спектр свойств и методов для управления файлом Excel. Чтобы контролировать видимость полос прокрутки, используйте свойства [**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) и [**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) класса [**WorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings). [**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) и [**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) являются логическими свойствами, что значит, что эти свойства могут хранить только **true** или **false** значения.

Ниже представлен полный код, который открывает файл Excel book1.xls, скрывает обе полосы прокрутки и затем сохраняет измененный файл как output.xls.

На скриншоте ниже показан файл Book1.xls, содержащий оба ползунка прокрутки. Измененный файл сохранен как файл output.xls, также показан ниже.

**Book1.xls: Файл Excel до любых изменений**

![todo:image_alt_text](display-or-hide-scroll-bars-in-aspose-cells_1.png)

**output.xls: Файл Excel после изменений**

![todo:image_alt_text](display-or-hide-scroll-bars-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Hiding the vertical scroll bar of the Excel file

workbook.Settings.IsVScrollBarVisible = false;

//Hiding the horizontal scroll bar of the Excel file

workbook.Settings.IsHScrollBarVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Скачать работающий код**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Scroll%20Bars)

## **Загрузить образец кода**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
