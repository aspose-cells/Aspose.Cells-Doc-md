---
title: Общедоступный API Изменения в Aspose.Cells 8.9.0
type: docs
weight: 310
url: /ru/java/public-api-changes-in-aspose-cells-8-9-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.8.3 до 8.9.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Добавлено свойство HtmlSaveOptions.DefaultFontName.**
Aspose.Cells for Java 8.9.0 предоставило свойство DefaultFontName для класса HtmlSaveOptions, которое позволяет указать имя шрифта по умолчанию при отображении электронных таблиц в формате HTML. Шрифт по умолчанию будет использоваться только в том случае, если шрифт стиля не существует. Значение по умолчанию для свойства HtmlSaveOptions.DefaultFontName равно null, что означает, что Aspose.Cells for Java API будет использовать универсальный шрифт, принадлежащий к тому же семейству, что и исходный шрифт.

{{% alert color="primary" %}} 

 Подробнее об этой функции читайте в статье[Установка шрифта по умолчанию для рендеринга электронных таблиц в формате HTML](/cells/ru/java/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set default font name for Html rendering

options.setDefaultFontName("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.save(dir + "output.html", options);

{{< /highlight >}}
### **Добавлено свойство ImageOrPrintOptions.DefaultFont.**
Aspose.Cells for Java 8.9.0 позволяет установить имя шрифта по умолчанию для класса ImageOrPrintOptions, предоставляя свойство DefaultFont. Указанное свойство можно использовать, когда символы Unicode в электронной таблице не установлены с правильным шрифтом в стиле ячейки, поэтому такие символы могут отображаться в виде блоков в результирующих изображениях.

{{% alert color="primary" %}} 

 Задайте для свойства DefaultFont значение MingLiu или MS Gothic, чтобы отображались символы Юникода. Если указанное свойство не установлено, Aspose.Cells будет использовать системный шрифт по умолчанию для отображения символов Unicode.

{{% /alert %}} {{% alert color="primary" %}} 

 Подробнее об этой функции читайте в статье[Установка шрифта по умолчанию для рендеринга электронных таблиц в форматах изображений](/cells/ru/java/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

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
### **Добавлено свойство PivotTable.Excel2003Compatible.**
Aspose.Cells for Java API предоставил свойство Excel2003Compatible логического типа для класса сводной таблицы, которое позволяет указать, совместима ли сводная таблица с Excel 2003 для целей обновления. Значение свойства Excel2003Compatible по умолчанию равно true, это означает, что длина строки должна быть меньше или равна 255 символам. Если строка превышает 255 символов, она будет усечена. Если false, вышеупомянутое ограничение не будет наложено.

{{% alert color="primary" %}} 

 Подробнее об этой функции читайте в статье[Совместимость с Excel 2003 для обновления сводных таблиц](/cells/ru/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

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
