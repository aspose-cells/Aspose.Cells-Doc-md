---
title: Изменения в общедоступном API в Aspose.Cells 8.6.0
type: docs
weight: 190
url: /ru/net/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в общедоступном API Aspose.Cells с версии 8.5.2 по 8.6.0, которые могут быть интересны разработчикам модулей/приложений. В нем представлены не только новые и обновленные общедоступные методы, [добавленные классы и т. д.](/cells/ru/net/public-api-changes-in-aspose-cells-8-6-0/), но также описание любых изменений в поведении позади сцены в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Поддержка манипулирования метаданными без создания объекта книги**
Эта версия Aspose.Cells for .NET API предоставила два новых класса, а именно WorkbookMetadata & MetadataOptions, а также новое перечисление MetadataType, которое теперь позволяет манипулировать свойствами документа (метаданными) без создания экземпляра Workbook. Класс WorkbookMetadata является легковесным и предоставляет очень простой и эффективный механизм [чтения, записи и обновления свойств документа без влияния на общую производительность](/cells/ru/net/using-workbookmetadata/).

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet with WorkbookMetadata while specifying appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DocumentProperties);

WorkbookMetadata metadata = new WorkbookMetadata(filePath, options);

//Set some properties

metadata.CustomDocumentProperties.Add("test", "test");

//Save the metadata info to spreadsheet

metadata.Save(filePath);

{{< /highlight >}}


### **Добавлено свойство HtmlSaveOptions.ExportFrameScriptsAndProperties**
Aspose.Cells for .NET 8.6.0 предоставил свойство HtmlSaveOptions.ExportFrameScriptsAndProperties, которое можно использовать для влияния на создание дополнительных скриптов при конвертации электронных таблиц в формат HTML. С настройками по умолчанию API Aspose.Cells экспортирует электронную таблицу в формат HTML так, как это делает приложение Excel, то есть результатирующий HTML содержит фреймы и условные комментарии, которые обнаруживают тип браузера и соответствующим образом настраивают макет. Значение свойства HtmlSaveOptions.ExportFrameScriptsAndProperties по умолчанию равно true, что означает, что экспорт выполняется в соответствии со стандартами Excel. Однако, если установить свойство в false, API не будет [генерировать скрипты, связанные с фреймами и условными комментариями](/cells/ru/net/disable-exporting-frame-scripts-and-document-properties/). В этом случае результатирующий HTML можно просматривать корректно в любом браузере, однако его нельзя будет импортировать обратно с использованием API Aspose.Cells.

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.ExportFrameScriptsAndProperties = false;

//Save spreadsheet as HTML

book.Save("output.html", options);

{{< /highlight >}}


### **Добавлено свойство Shape.MarcoName**
Aspose.Cells for .NET 8.6.0 предоставил свойство Shape.MarcoName, которое можно использовать для [назначения любого модуля VBA элементу управления формы](/cells/ru/net/assign-macro-to-form-control/), например, кнопке, чтобы обеспечить взаимодействие. Свойство имеет тип string, поэтому оно может принимать имя модуля и назначать его элементу управления.

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access first default worksheet

Worksheet sheet = workbook.Worksheets[0];

//Add a module to the worksheet

int moduleIdx = workbook.VbaProject.Modules.Add(sheet);

//Access newly added module from the collection

VbaModule module = workbook.VbaProject.Modules[moduleIdx];

//Add code to the module

module.Codes =

    "Sub ShowMessage()" + "\r\n" +

    "    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

    "End Sub";

//Add a Button on the worksheet and set its various properties

Aspose.Cells.Drawing.Button button = sheet.Shapes.AddButton(2, 0, 2, 0, 28, 80);

button.Placement = Aspose.Cells.Drawing.PlacementType.FreeFloating;

button.Font.Name = "Tahoma";

button.Font.IsBold = true;

button.Font.Color = System.Drawing.Color.Blue;

button.Text = "Aspose";

//Assign the VBA module to the button

button.MacroName = sheet.Name + ".ShowMessage";

//Save the result

workbook.Save("output.xlsm");

{{< /highlight >}}


### **Добавлено свойство OoxmlSaveOptions.UpdateZoom**
С выпуском v8.6.0, Aspose.Cells for .NET API предоставил свойство OoxmlSaveOptions.UpdateZoom, которое можно использовать для обновления свойства PageSetup.Zoom, если свойства PageSetup.FitToPagesWide и/или PageSetup.FitToPagesTall были использованы для управления масштабированием Листа.
{{< app/cells/assistant language="csharp" >}}
