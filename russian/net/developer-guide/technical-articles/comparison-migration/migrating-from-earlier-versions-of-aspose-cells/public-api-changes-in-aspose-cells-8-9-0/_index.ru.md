---
title: Изменения в общедоступном API в Aspose.Cells 8.9.0
type: docs
weight: 300
url: /ru/net/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.8.3 по 8.9.0, которые могут быть интересны для разработчиков модулей/приложений. Он включает не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Добавлено свойство HtmlSaveOptions.DefaultFontName**
Aspose.Cells for .NET 8.9.0 представил свойство DefaultFontName для класса HtmlSaveOptions, которое позволяет указать имя шрифта по умолчанию при рендеринге электронных таблиц в формат HTML. Шрифт по умолчанию будет использоваться только в том случае, если шрифт стиля не существует. Значение по умолчанию свойства HtmlSaveOptions.DefaultFontName равно null, что означает, что API Aspose.Cells for .NET будет использовать универсальный шрифт, который имеет ту же семью, что и оригинальный шрифт.

{{% alert color="primary" %}} 

Для получения дополнительной информации об этой функции, пожалуйста, прочтите статью о [Установке шрифта по умолчанию для рендеринга электронных таблиц в формате HTML](/cells/ru/net/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 // Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set default font name for Html rendering

options.DefaultFontName = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Добавлено свойство ImageOrPrintOptions.DefaultFont**
Aspose.Cells for .NET 8.9.0 позволяет установить имя шрифта по умолчанию для класса ImageOrPrintOptions, предоставив свойство DefaultFont. Указанное свойство может быть использовано, если Юникод-символы в электронной таблице не заданы с правильным шрифтом в стиле ячейки, поэтому такие символы могут отображаться как блоки в результирующих изображениях.

{{% alert color="primary" %}} 

Установите свойство DefaultFont в MingLiu или MS Gothic, чтобы отобразить Юникод-символы. Если указанное свойство не установлено, Aspose.Cells будет использовать шрифт по умолчанию системы для отображения Юникод-символов.

{{% /alert %}} {{% alert color="primary" %}} 

Для получения дополнительной информации об этой функции, пожалуйста, ознакомьтесь со статьей о [Установке шрифта по умолчанию для рендеринга электронных таблиц в форматах изображений](/cells/ru/net/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

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


### **Добавлено свойство PivotTable.IsExcel2003Compatible**
Aspose.Cells for .NET API добавил свойство Boolean IsExcel2003Compatible для класса PivotTable, которое позволяет указать, совместима ли сводная таблица с Excel 2003 для целей обновления. Значение по умолчанию свойства IsExcel2003Compatible - true, что означает, что строка должна быть меньше или равна 255 символам. Если строка содержит более 255 символов, она будет обрезана. Если false, упомянутое ограничение не будет накладываться.

{{% alert color="primary" %}} 

Для получения более подробной информации об этой функции, пожалуйста, ознакомьтесь со статьей: [Compatibility for Excel 2003 for Refreshing Pivot Tables](https://docs.aspose.com/cells/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

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


### **Добавлен метод GridWeb.GetVersion**
Aspose.Cells.GridWeb для .NET 8.9.0 добавил метод GetVersion, который возвращает версию выпуска компонента GridWeb.
{{< app/cells/assistant language="csharp" >}}
