---
title: Показать или скрыть полосы прокрутки в Aspose.Cells
type: docs
weight: 70
url: /ru/net/display-or-hide-scroll-bars-in-aspose-cells/
---
{{% alert color="primary" %}}

Полосы прокрутки очень часто используются для навигации по содержимому любого файла. Обычно существует два вида полос прокрутки:

- Вертикальные полосы прокрутки
- Горизонтальные полосы прокрутки

Microsoft Excel также предоставляет горизонтальные и вертикальные полосы прокрутки, чтобы пользователи могли прокручивать содержимое рабочего листа. Используя Aspose.Cells, разработчики могут управлять видимостью обоих типов полос прокрутки в файлах Excel.

{{% /alert %}}

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет файл Excel.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Класс предоставляет широкий спектр свойств и методов для управления файлом Excel. Для управления видимостью полос прокрутки используйте[**WorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings) учебный класс'[**Исвскроллбарвидибле**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) а также[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) характеристики.[**Исвскроллбарвидибле**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) а также[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) являются логическими свойствами, что означает, что эти свойства могут хранить только**истинный** или же**ЛОЖЬ** ценности.

Ниже приведен полный код, который открывает файл Excel, book1.xls, скрывает обе полосы прокрутки, а затем сохраняет измененный файл как output.xls.

На снимке экрана ниже показан файл Book1.xls, содержащий обе полосы прокрутки. Измененный файл сохраняется как файл output.xls, также показанный ниже.

**Book1.xls: файл Excel до каких-либо изменений**

![дело:изображение_альтернативный_текст](display-or-hide-scroll-bars-in-aspose-cells_1.png)

**output.xls: файл Excel после модификации**

![дело:изображение_альтернативный_текст](display-or-hide-scroll-bars-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

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

## **Скачать рабочий код**

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Scroll%20Bars)

## **Скачать пример кода**

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
