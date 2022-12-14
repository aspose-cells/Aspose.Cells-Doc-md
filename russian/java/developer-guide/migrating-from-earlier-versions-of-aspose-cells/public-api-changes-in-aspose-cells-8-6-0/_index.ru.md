---
title: Общедоступный API Изменения в Aspose.Cells 8.6.0
type: docs
weight: 200
url: /ru/java/public-api-changes-in-aspose-cells-8-6-0/
---
{{% alert color="primary" %}} 

 В этом документе описаны изменения в Aspose.Cells API с версии 8.5.2 до 8.6.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные публичные методы,[добавлены классы и т.д.](/cells/ru/java/public-api-changes-in-aspose-cells-8-6-0/), но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Поддержка манипулирования метаданными без создания объекта рабочей книги**
В этом выпуске Aspose.Cells for Java API представлены два новых класса, а именно WorkbookMetadata и MetadataOptions, а также новое перечисление MetadataType, которое теперь позволяет управлять свойствами документа (метаданными) без создания экземпляра Workbook. Класс WorkbookMetadata имеет небольшой вес и предоставляет очень простой в использовании эффективный механизм для[читать, писать и обновлять свойства документа, не влияя на общую производительность](/cells/ru/java/using-workbookmetadata/). 

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Open Workbook metadata while specifying the appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DOCUMENT_PROPERTIES);

WorkbookMetadata metaWorkbook = new WorkbookMetadata("sample.xlsx", options);

//Set some properties

metaWorkbook.getCustomDocumentProperties().add("test", "test");

//Save the metadata information to the spreadsheet file

metaWorkbook.save(filePath);

{{< /highlight >}}
### **Добавлено свойство HtmlSaveOptions.ExportFrameScriptsAndProperties.**
Aspose.Cells for Java 8.6.0 предоставляет свойство HtmlSaveOptions.ExportFrameScriptsAndProperties, которое можно использовать для влияния на создание дополнительных сценариев при преобразовании электронных таблиц в формат HTML. С настройками по умолчанию API-интерфейсы Aspose.Cells экспортируют электронную таблицу в формате HTML, поскольку приложение Excel выполняет экспорт, то есть; результирующий HTML содержит фреймы и условные комментарии, которые определяют тип браузера и соответствующим образом настраивают макет. Значение по умолчанию свойства HtmlSaveOptions.ExportFrameScriptsAndProperties равно true, это означает; экспорт осуществляется в соответствии со стандартами Excel. Если свойство установлено в false, API не будет[генерировать скрипты, относящиеся к фреймам и условным комментариям](/cells/ru/java/disable-exporting-frame-scripts-and-document-properties/). В этом случае результирующий HTML-код можно корректно просматривать в любом браузере, однако его нельзя импортировать обратно с помощью API-интерфейсов Aspose.Cells.

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.setExportFrameScriptsAndProperties(false);

//Save spreadsheet as HTML

book.save("output.html", options)

{{< /highlight >}}
### **Добавлено свойство Shape.MarcoName**
 Aspose.Cells for Java 8.6.0 предоставило свойство Shape.MarcoName, которое можно использовать для[назначить модуль VBA элементу управления формой](/cells/ru/java/assign-macro-code-to-form-control/) такую кнопку, чтобы обеспечить взаимодействие. Свойство имеет строковый тип, поэтому оно может принимать имя модуля и присваивать его элементу управления.

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Create a new Workbook object

Workbook workbook = new Workbook();

//Get the instance of first default worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Add a new module to the first worksheet

int moduleIdx = workbook.getVbaProject().getModules().add(sheet);

//Get the instance of newly added module

VbaModule module = workbook.getVbaProject().getModules().get(moduleIdx);

//Add module code

module.setCodes("Sub ShowMessage()" + "\r\n" +

        "    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

        "End Sub");

//Create a new button to the worksheet and set its various properties

Button button = (Button) sheet.getShapes().addShape(MsoDrawingType.BUTTON, 2, 0, 2, 0, 28, 80);

button.setPlacement(PlacementType.FREE_FLOATING);

button.getFont().setName("Tahoma");

button.getFont().setBold(true);

button.getFont().setColor(Color.getBlue());

button.setText("Aspose");

//Assign the newly added module to the button

button.setMacroName(module.getName() + ".ShowMessage" );

//Save the spreadsheet in XLSM format

workbook.save("output.xlsm");

{{< /highlight >}}
### **Добавлено свойство OoxmlSaveOptions.UpdateZoom**
В версии 8.6.0 в Aspose.Cells for Java API появилось свойство OoxmlSaveOptions.UpdateZoom, которое можно использовать для обновления PageSetup.Zoom, если свойства PageSetup.FitToPagesWide и/или PageSetup.FitToPagesTall использовались для управления масштабированием рабочего листа.
