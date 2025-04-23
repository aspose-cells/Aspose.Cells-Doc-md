---
title: Изменения в общедоступном API в Aspose.Cells 8.6.0
type: docs
weight: 200
url: /ru/java/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.5.2 по 8.6.0, которые могут быть интересны разработчикам модуля/приложения. Он включает в себя не только новые и обновленные общедоступные методы, [добавленные классы и т. д.](/cells/ru/java/public-api-changes-in-aspose-cells-8-6-0/), но также описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Поддержка манипулирования метаданными без создания объекта книги**
В этой версии Aspose.Cells for Java API были выставлены два новых класса WorkbookMetadata и MetadataOptions, а также новое перечисление MetadataType, которое теперь позволяет манипулировать свойствами документа (метаданными) без создания экземпляра Workbook. Класс WorkbookMetadata является легким и предоставляет очень простой в использовании, эффективный механизм для [чтения, записи и обновления свойств документа без влияния на общую производительность](/cells/ru/java/using-workbookmetadata/). 

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //Open Workbook metadata while specifying the appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DOCUMENT_PROPERTIES);

WorkbookMetadata metaWorkbook = new WorkbookMetadata("sample.xlsx", options);

//Set some properties

metaWorkbook.getCustomDocumentProperties().add("test", "test");

//Save the metadata information to the spreadsheet file

metaWorkbook.save(filePath);

{{< /highlight >}}
### **Добавлено свойство HtmlSaveOptions.ExportFrameScriptsAndProperties**
Aspose.Cells for Java 8.6.0 выставил свойство HtmlSaveOptions.ExportFrameScriptsAndProperties, которое можно использовать для влияния на создание дополнительных скриптов при преобразовании таблиц в HTML формат. С настройками по умолчанию, Aspose.Cells APIs экспортируют таблицу в формате HTML так, как это делает приложение Excel; результат HTML содержит фреймы и условные комментарии, которые определяют тип браузера и подстраивают макет соответственно. Значение по умолчанию свойства HtmlSaveOptions.ExportFrameScriptsAndProperties равно true, что означает, что экспорт выполняется в соответствии с стандартами Excel. Если свойство установлено в false, API не будет [генерировать связанные со скриптами фреймов и условных комментариев](/cells/ru/java/disable-exporting-frame-scripts-and-document-properties/). В этом случае результат HTML можно корректно просмотреть в любом браузере, однако он не сможет быть импортирован обратно с использованием Aspose.Cells API.

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.setExportFrameScriptsAndProperties(false);

//Save spreadsheet as HTML

book.save("output.html", options)

{{< /highlight >}}
### **Добавлено свойство Shape.MarcoName**
Aspose.Cells for Java 8.6.0 выставил свойство Shape.MarcoName, которое можно использовать для [назначения модуля VBA элементу управления формы](/cells/ru/java/assign-macro-code-to-form-control/), такому как кнопка, чтобы обеспечить взаимодействие. Свойство имеет тип string, поэтому оно может принимать имя модуля и назначать его элементу управления.

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

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
С выходом v8.6.0, Aspose.Cells for Java API выставил свойство OoxmlSaveOptions.UpdateZoom, которое можно использовать для обновления масштабирования страницы, если использовались свойства PageSetup.FitToPagesWide и/или PageSetup.FitToPagesTall для управления масштабированием Листа.
{{< app/cells/assistant language="java" >}}
