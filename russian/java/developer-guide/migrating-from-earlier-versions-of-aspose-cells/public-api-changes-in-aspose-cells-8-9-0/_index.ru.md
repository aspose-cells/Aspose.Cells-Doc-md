---
title: Изменения в общедоступном API в Aspose.Cells 8.9.0
type: docs
weight: 310
url: /ru/java/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.8.3 по 8.9.0, которые могут быть интересны для разработчиков модулей/приложений. Он включает не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Добавлено свойство HtmlSaveOptions.DefaultFontName**
Aspose.Cells for Java 8.9.0 добавил свойство DefaultFontName для класса HtmlSaveOptions, которое позволяет указать имя шрифта по умолчанию при рендеринге электронных таблиц в формат HTML. Шрифт по умолчанию будет использоваться только в том случае, если шрифт стиля не существует. Значение свойства HtmlSaveOptions.DefaultFontName по умолчанию равно null, что означает, что API Aspose.Cells for Java будет использовать универсальный шрифт с тем же семейством, что и оригинальный шрифт.

{{% alert color="primary" %}} 

Дополнительные сведения об этой функции можно найти в статье [Установка шрифта по умолчанию для рендеринга электронных таблиц в формате HTML](/cells/ru/java/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set default font name for Html rendering

options.setDefaultFontName("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.save(dir + "output.html", options);

{{< /highlight >}}
### **Добавлено свойство ImageOrPrintOptions.DefaultFont**
Aspose.Cells for Java 8.9.0 позволяет установить имя шрифта по умолчанию для класса ImageOrPrintOptions путем предоставления свойства DefaultFont. Указанное свойство может быть использовано, когда Юникод-символы в электронной таблице не установлены с правильным шрифтом в стиле ячейки, поэтому такие символы могут отображаться как блоки в результирующих изображениях. 

{{% alert color="primary" %}} 

Установите свойство DefaultFont в MingLiu или MS Gothic, чтобы отобразить Юникод-символы. Если указанное свойство не установлено, Aspose.Cells будет использовать шрифт по умолчанию системы для отображения Юникод-символов. 

{{% /alert %}} {{% alert color="primary" %}} 

Дополнительные сведения об этой функции можно найти в статье [Установка шрифта по умолчанию для рендеринга электронных таблиц в изображениях](/cells/ru/java/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //Create an instance of ImageOrPrintOptions

ImageOrPrintOptions options = new ImageOrPrintOptions();

//Set default font name for image rendering

options.setDefaultFont("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet to be rendered

Worksheet sheet = book.getWorksheets().get(0);

//Create an instance of SheetRender

SheetRender render = new SheetRender(sheet, options);

//Save spreadsheet to image

render.toImage(0, dir + "output.png");

{{< /highlight >}}
### **Добавлено свойство PivotTable.Excel2003Compatible**
Aspose.Cells for Java API добавил свойство типа Boolean Excel2003Compatible для класса PivotTable, которое позволяет указать, совместима ли сводная таблица Excel 2003 для целей обновления. Значение по умолчанию свойства Excel2003Compatible равно true, что означает, что строка должна быть меньше или равна 255 символам. Если строка превышает 255 символов, она будет усечена. Если установить значение false, указанное ограничение не будет применяться.

{{% alert color="primary" %}} 

Дополнительные сведения об этой функции можно найти в статье [Совместимость с Excel 2003 для обновления сводных таблиц](/cells/ru/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the desired Pivot Table from the spreadsheet

PivotTable pivot = book.getWorksheets().get(0).getPivotTables().get(0);

//Set Excel 2003 compatibility to false

pivot.setExcel2003Compatible(false);

//Refresh & recalculate Pivot Table

pivot.refreshData();

pivot.calculateData();

{{< /highlight >}}
