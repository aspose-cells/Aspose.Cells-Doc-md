---
title: Изменения в общедоступном API в Aspose.Cells 8.4.0
type: docs
weight: 130
url: /ru/net/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

Данный документ описывает изменения в API Aspose.Cells с версии 8.3.2 до 8.4.0, которые могут быть интересны разработчикам модуля/приложения. В нем содержатся не только новые и обновленные публичные методы, [добавленные классы и т.д.](/cells/ru/net/public-api-changes-in-aspose-cells-8-4-0/) и [удаленные классы и т.д.](/cells/ru/net/public-api-changes-in-aspose-cells-8-4-0/), но также описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Механизм изменения кода VBA/Macro в электронных таблицах**
Для предоставления функции [Манипуляция кодом VBA/Macro](/cells/ru/net/modifying-vba-or-macro-code-using-aspose-cells/), Aspose.Cells for .NET 8.4.0 предоставил ряд новых классов и свойств в пространстве имен Aspose.Cells.Vba. Несколько важных деталей этих новых классов следующие.

- Класс VbaProject может быть использован для извлечения проекта VBA из заданной электронной таблицы.
- Класс VbaModuleCollection представляет коллекцию VBA-модулей, которые являются частью заданного VbaProject.
- Класс VbaModule представляет один модуль из VbaModuleCollection.

Далее приведен фрагмент кода, показывающий, как динамически изменить сегменты кода VBA.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

foreach (VbaModule module in workbook.VbaProject.Modules)

{

    string code = module.Codes;

    //Replace the original message with the modified message

    if (code.Contains("This is test message."))

    {

        code = code.Replace("This is test message.", "This is Aspose.Cells message.");

        module.Codes = code;

    }

}

//Save the output Excel file

workbook.Save("output.xlsm");

{{< /highlight >}}


### **Возможность удалить сводную таблицу**
Aspose.Cells for .NET 8.4.0 предоставил два метода для коллекции PivotTable для предоставления функции удаления сводной таблицы из заданной электронной таблицы. Подробности указанных методов следующие.

- Метод PivotTableCollection.Remove принимает объект PivotTable и удаляет его из коллекции.
- Метод PivotTableCollection.RemoveAt принимает значение целочисленного типа на основе нулевого индекса и удаляет конкретную сводную таблицу из коллекции.

Далее показан фрагмент кода, показывающий, как удалить сводную таблицу с использованием обоих вышеупомянутых методов.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the first pivot table object

PivotTable pivotTable = worksheet.PivotTables[0];

//Remove pivot table using pivot table object

worksheet.PivotTables.Remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.PivotTables.RemoveAt(0);

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Поддержка различных макетов сводных таблиц**
Aspose.Cells for .NET 8.4.0 предоставляет поддержку различных предопределенных макетов для сводных таблиц. Для реализации этой функции API Aspose.Cells предоставляет три метода для класса PivotTable, подробности о которых приведены ниже.

- Метод PivotTable.ShowInCompactForm отображает сводную таблицу в компактном макете.
- Метод PivotTable.ShowInOutlineForm отображает сводную таблицу в макете контура.
- Метод PivotTable.ShowInTabularForm отображает сводную таблицу в табличном макете.

{{% alert color="primary" %}} 

Важно вызывать методы PivotTable.RefreshData и PivotTable.CalculateData после установки любого из вышеупомянутых макетов.

{{% /alert %}} 

В следующем примере кода устанавливаются различные компоновки для сводной таблицы и результат сохраняется на диск.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first pivot table

PivotTable pivotTable = worksheet.PivotTables[0];

//Render the pivot table in compact form

pivotTable.ShowInCompactForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("CompactForm.xlsx");

//Render the pivot table in outline form

pivotTable.ShowInOutlineForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("OutlineForm.xlsx");

//Render the pivot table in tabular form

pivotTable.ShowInTabularForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("TabularForm.xlsx");

{{< /highlight >}}


### **Добавлены класс TxtLoadStyleStrategy и свойство TxtLoadOptions.LoadStyleStrategy.**
Aspose.Cells for .NET 8.4.0 предоставил класс TxtLoadStyleStrategy и свойство TxtLoadOptions.LoadStyleStrategy для указания стратегии форматирования разобранных значений при преобразовании строкового значения в число или дату.
### **Добавлен метод DataBar.ToImage.**
С выпуском v8.4.0 API Aspose.Cells предоставил метод DataBar.ToImage для сохранения условно отформатированных DataBars в формате изображения. Метод DataBar.ToImage принимает два параметра, подробности которых приведены ниже.

- Первый параметр имеет тип Aspose.Cells.Cell, на который было применено условное форматирование.
- Второй параметр имеет тип Aspose.Cells.Rendering.ImageOrPrintOptions для установки различных параметров результирующего изображения.

Следующий пример кода демонстрирует использование метода DataBar.ToImage для отображения DataBar в формате изображения.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.Cells["C1"];

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.GetFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc[0].DataBar;

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.ImageFormat = ImageFormat.Png;

//Get the image bytes of the databar

byte[] imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **Добавлено свойство Border.ThemeColor.**
API Aspose.Cells позволяет извлекать данные форматирования, связанные с темами, из электронных таблиц. С выпуском Aspose.Cells for .NET 8.4.0 API предоставил свойство Border.ThemeColor, которое можно использовать для извлечения цветовых атрибутов темы границ ячеек.
### **Добавлено свойство DrawObject.ImageBytes.**
Aspose.Cells for .NET 8.4.0 предоставил свойство DrawObject.ImageBytes для получения данных изображения из графика или формы.
### **Добавлено свойство HtmlSaveOptions.ExportBogusRowData.**
Aspose.Cells for .NET 8.4.0 предоставил свойство {HtmlSaveOptions.ExportBogusRowData}}. Это логическое свойство определяет, вставит ли API ложные данные для нижней строки при экспорте электронной таблицы в формат HTML.

{{% alert color="primary" %}} 

Значение по умолчанию - true.

{{% /alert %}} 

В следующем примере кода иллюстрируется использование вышеупомянутого свойства.

**C#**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Добавлено свойство HtmlSaveOptions.CellCssPrefix.**
Новое свойство HtmlSaveOptions.CellCssPrefix позволяет установить префикс для CSS-файлов при экспорте таблиц в формат HTML.

{{% alert color="primary" %}} 

Значение по умолчанию - "" (пустая строка).

{{% /alert %}}
## **Устаревшие API**
### **Устарели методы Cells.GetCellByIndex и Row.GetCellByIndex**
Используйте метод GetEnumerator для перебора всех ячеек вместо них.
### **Свойство DrawObject.Image устарело**
Используйте свойство DrawObject.ImageBytes для получения данных изображения вместо этого.
