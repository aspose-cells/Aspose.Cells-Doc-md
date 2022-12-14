---
title: Общедоступный API Изменения в Aspose.Cells 8.9.0
type: docs
weight: 300
url: /ru/net/public-api-changes-in-aspose-cells-8-9-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.8.3 до 8.9.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Добавлено свойство HtmlSaveOptions.DefaultFontName.**
Aspose.Cells for .NET 8.9.0 предоставило свойство DefaultFontName для класса HtmlSaveOptions, которое позволяет указать имя шрифта по умолчанию при отображении электронных таблиц в формате HTML. Шрифт по умолчанию будет использоваться только в том случае, если шрифт стиля не существует. Значение по умолчанию для свойства HtmlSaveOptions.DefaultFontName равно null, что означает, что Aspose.Cells for .NET API будет использовать универсальный шрифт, принадлежащий к тому же семейству, что и исходный шрифт.

{{% alert color="primary" %}} 

 Подробнее об этой функции читайте в статье[Установка шрифта по умолчанию для рендеринга электронных таблиц в формате HTML](/cells/ru/net/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set default font name for Html rendering

options.DefaultFontName = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Добавлено свойство ImageOrPrintOptions.DefaultFont.**
Aspose.Cells for .NET 8.9.0 позволяет установить имя шрифта по умолчанию для класса ImageOrPrintOptions, предоставляя свойство DefaultFont. Указанное свойство можно использовать, когда символы Unicode в электронной таблице не установлены с правильным шрифтом в стиле ячейки, поэтому такие символы могут отображаться в виде блоков в результирующих изображениях.

{{% alert color="primary" %}} 

Задайте для свойства DefaultFont значение MingLiu или MS Gothic, чтобы отображались символы Юникода. Если указанное свойство не установлено, Aspose.Cells будет использовать системный шрифт по умолчанию для отображения символов Unicode.

{{% /alert %}} {{% alert color="primary" %}} 

 Подробнее об этой функции читайте в статье[Установка шрифта по умолчанию для рендеринга электронных таблиц в форматах изображений](/cells/ru/net/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of ImageOrPrintOptions

var options = new ImageOrPrintOptions();

// Set default font name for image rendering

options.DefaultFont = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet to be rendered

var sheet = book.Worksheets[0];

// Create an instance of SheetRender

var render = new SheetRender(sheet, options);

// Save spreadsheet to image

render.ToImage(0, dir + "output.png");

{{< /highlight >}}


### **Добавлено свойство PivotTable.IsExcel2003Compatible.**
Aspose.Cells for .NET API предоставил свойство логического типа IsExcel2003Compatible для класса сводной таблицы, которое позволяет указать, совместима ли сводная таблица с Excel 2003 для целей обновления. Значение свойства IsExcel2003Compatible по умолчанию равно true, это означает, что длина строки должна быть меньше или равна 255 символам. Если строка превышает 255 символов, она будет усечена. Если false, вышеупомянутое ограничение не будет наложено.

{{% alert color="primary" %}} 

 Подробнее об этой функции читайте в статье[Совместимость с Excel 2003 для обновления сводных таблиц](https://docs.aspose.com/cells/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the desired Pivot Table from the spreadsheet

var pivot = book.Worksheets[0].PivotTables[0];

// Set Excel 2003 compatibility to false

pivot.IsExcel2003Compatible = false;

// Refresh & recalculate Pivot Table

pivot.RefreshData();

pivot.CalculateData();

{{< /highlight >}}


### **Добавлен метод GridWeb.GetVersion.**
Aspose.Cells.GridWeb for .NET 8.9.0 предоставил фабричный метод {GetVersion}}, который возвращает версию выпуска компонента GridWeb.
