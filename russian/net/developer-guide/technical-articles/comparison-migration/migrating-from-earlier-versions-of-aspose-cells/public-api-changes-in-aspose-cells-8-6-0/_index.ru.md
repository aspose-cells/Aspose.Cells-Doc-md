---
title: Общедоступный API Изменения в Aspose.Cells 8.6.0
type: docs
weight: 190
url: /ru/net/public-api-changes-in-aspose-cells-8-6-0/
---
{{% alert color="primary" %}} 

 В этом документе описаны изменения в Aspose.Cells API с версии 8.5.2 до 8.6.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные публичные методы,[добавлены классы и т.д.](/cells/ru/net/public-api-changes-in-aspose-cells-8-6-0/), но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Поддержка манипулирования метаданными без создания объекта рабочей книги**
В этом выпуске Aspose.Cells for .NET API представлены два новых класса, а именно WorkbookMetadata и MetadataOptions, а также новое перечисление MetadataType, которое теперь позволяет управлять свойствами документа (метаданными) без создания экземпляра Workbook. Класс WorkbookMetadata имеет небольшой вес и предоставляет очень простой в использовании эффективный механизм для[читать, писать и обновлять свойства документа, не влияя на общую производительность](/cells/ru/net/using-workbookmetadata/).

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet with WorkbookMetadata while specifying appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DocumentProperties);

WorkbookMetadata metadata = new WorkbookMetadata(filePath, options);

//Set some properties

metadata.CustomDocumentProperties.Add("test", "test");

//Save the metadata info to spreadsheet

metadata.Save(filePath);

{{< /highlight >}}


### **Добавлено свойство HtmlSaveOptions.ExportFrameScriptsAndProperties.**
Aspose.Cells for .NET 8.6.0 предоставляет свойство HtmlSaveOptions.ExportFrameScriptsAndProperties, которое можно использовать для влияния на создание дополнительных сценариев при преобразовании электронных таблиц в формат HTML. С настройками по умолчанию API-интерфейсы Aspose.Cells экспортируют электронную таблицу в формате HTML, поскольку приложение Excel выполняет экспорт, то есть; результирующий HTML содержит фреймы и условные комментарии, которые определяют тип браузера и соответствующим образом настраивают макет. Значение по умолчанию свойства HtmlSaveOptions.ExportFrameScriptsAndProperties равно true, это означает; экспорт осуществляется в соответствии со стандартами Excel. Однако, если свойство установлено в false, API не будет[генерировать скрипты, связанные с фреймами и условными комментариями](/cells/ru/net/disable-exporting-frame-scripts-and-document-properties/). В этом случае результирующий HTML можно корректно просмотреть в любом браузере, однако его нельзя импортировать обратно с помощью API Aspose.Cells.

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.ExportFrameScriptsAndProperties = false;

//Save spreadsheet as HTML

book.Save("output.html", options);

{{< /highlight >}}


### **Добавлено свойство Shape.MarcoName**
Aspose.Cells for .NET 8.6.0 предоставило свойство Shape.MarcoName, которое можно использовать для[назначить любой модуль VBA элементу управления формой](/cells/ru/net/assign-macro-to-form-control/) такую кнопку, чтобы обеспечить взаимодействие. Свойство имеет строковый тип, поэтому оно может принимать имя модуля и присваивать его элементу управления.

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

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
В версии 8.6.0 в Aspose.Cells for .NET API появилось свойство OoxmlSaveOptions.UpdateZoom, которое можно использовать для обновления PageSetup.Zoom, если свойства PageSetup.FitToPagesWide и/или PageSetup.FitToPagesTall использовались для управления масштабированием рабочего листа.
