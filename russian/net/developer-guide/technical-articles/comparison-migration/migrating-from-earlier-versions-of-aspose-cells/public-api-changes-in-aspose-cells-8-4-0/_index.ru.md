---
title: Общедоступный API Изменения в Aspose.Cells 8.4.0
type: docs
weight: 130
url: /ru/net/public-api-changes-in-aspose-cells-8-4-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.3.2 до 8.4.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные публичные методы,[добавлены классы и т.д.](/cells/ru/net/public-api-changes-in-aspose-cells-8-4-0/) и[удалены классы и т.д.](/cells/ru/net/public-api-changes-in-aspose-cells-8-4-0/), но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Механизм изменения кода VBA/макро в электронных таблицах**
 Для обеспечения возможности[Манипуляции с кодом VBA/макро](/cells/ru/net/modifying-vba-or-macro-code-using-aspose-cells/), Aspose.Cells for .NET 8.4.0 представил ряд новых классов и свойств в пространстве имен Aspose.Cells.Vba. Вот несколько важных деталей этих новых классов.

- Класс VbaProject можно использовать для извлечения проекта VBA из данной электронной таблицы.
- Класс VbaModuleCollection представляет коллекцию модулей VBA, которые являются частью данного VbaProject.
- Класс VbaModule представляет один модуль из коллекции VbaModuleCollection.

В следующем фрагменте кода показано, как динамически изменять сегменты кода VBA.

**C#**

{{< highlight "csharp" >}}

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
Aspose.Cells for .NET 8.4.0 предоставляет два метода для PivotTableCollection, чтобы обеспечить функцию удаления сводной таблицы из данной электронной таблицы. Детали вышеупомянутых способов следующие.

- Метод PivotTableCollection.Remove принимает объект сводной таблицы и удаляет его из коллекции.
- Метод PivotTableCollection.RemoveAt принимает целочисленное значение на основе нулевого индекса и удаляет конкретную сводную таблицу из коллекции.

В следующем фрагменте кода показано, как удалить сводную таблицу, используя оба вышеупомянутых метода.

**C#**

{{< highlight "csharp" >}}

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
Aspose.Cells for .NET 8.4.0 обеспечивает поддержку различных предопределенных макетов для сводных таблиц. Чтобы обеспечить эту функцию, API-интерфейсы Aspose.Cells предоставили три метода для класса сводной таблицы, как подробно описано ниже.

- Метод PivotTable.ShowInCompactForm отображает сводную таблицу в компактном макете.
- Метод PivotTable.ShowInOutlineForm отображает сводную таблицу в макете Outline.
- Метод PivotTable.ShowInTabularForm отображает сводную таблицу в виде таблицы.

{{% alert color="primary" %}} 

Важно вызывать PivotTable.RefreshData и PivotTable.CalculateData после установки любого из вышеупомянутых макетов.

{{% /alert %}} 

Следующий пример кода задает различные макеты для сводной таблицы и сохраняет результат на диске.

**C#**

{{< highlight "csharp" >}}

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


### **Добавлен класс TxtLoadStyleStrategy и свойство TxtLoadOptions.LoadStyleStrategy.**
Aspose.Cells for .NET 8.4.0 предоставляет класс TxtLoadStyleStrategy и свойство TxtLoadOptions.LoadStyleStrategy для указания стратегии форматирования проанализированных значений при преобразовании строкового значения в число или дату и время.
### **Добавлен метод DataBar.ToImage**
С выпуском v8.4.0 Aspose.Cells API предоставил метод DataBar.ToImage для сохранения условно отформатированных панелей данных в формате изображения. Метод {DataBar.ToImage}} принимает два параметра, как описано ниже.

- Первый параметр имеет тип Aspose.Cells.Cell, к которому было применено условное форматирование.
- Второй параметр имеет тип Aspose.Cells.Rendering.ImageOrPrintOptions для установки различных параметров результирующего изображения.

В следующем примере кода показано использование метода DataBar.ToImage для отображения панели данных в формате изображения.

**C#**

{{< highlight "csharp" >}}

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

byte[]imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **Добавлено свойство Border.ThemeColor**
Aspose.Cells API позволяют извлекать данные форматирования, связанные с темой, из электронных таблиц. В выпуске Aspose.Cells for .NET 8.4.0 API предоставил свойство Border.ThemeColor, которое можно использовать для получения атрибутов цвета темы границ Cell.
### **Добавлено свойство DrawObject.ImageBytes**
Aspose.Cells for .NET 8.4.0 предоставляет свойство DrawObject.ImageBytes для получения данных изображения из диаграммы или формы.
### **Добавлено свойство HtmlSaveOptions.ExportBogusRowData.**
Aspose.Cells for .NET 8.4.0 предоставляет свойство {HtmlSaveOptions.ExportBogusRowData}}. Свойство логического типа определяет, будет ли API вводить фиктивные данные нижней строки при экспорте электронной таблицы в формат HTML.

{{% alert color="primary" %}} 

Значение по умолчанию верно.

{{% /alert %}} 

Следующий пример кода иллюстрирует использование вышеупомянутого свойства.

**C#**

{{< highlight "csharp" >}}

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
Недавно добавленное свойство HtmlSaveOptions.CellCssPrefix позволяет установить префикс для файлов CSS при экспорте электронных таблиц в формат HTML.

{{% alert color="primary" %}} 

Значение по умолчанию — "" (пустая строка).

{{% /alert %}}
## **Устаревшие API**
### **Методы Cells.GetCellByIndex и Row.GetCellByIndex устарели**
Вместо этого используйте метод GetEnumerator для перебора всех ячеек.
### **Свойство DrawObject.Image устарело**
Вместо этого используйте свойство DrawObject.ImageBytes для получения данных изображения.
