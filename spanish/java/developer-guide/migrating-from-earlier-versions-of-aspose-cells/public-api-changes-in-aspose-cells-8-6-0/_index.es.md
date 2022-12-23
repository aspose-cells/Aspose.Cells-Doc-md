---
title: Público API Cambios en Aspose.Cells 8.6.0
type: docs
weight: 200
url: /es/java/public-api-changes-in-aspose-cells-8-6-0/
---
{{% alert color="primary" %}} 

 Este documento describe los cambios al Aspose.Cells API de la versión 8.5.2 a la 8.6.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados,[Clases añadidas, etc.](/cells/es/java/public-api-changes-in-aspose-cells-8-6-0/), pero también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Compatibilidad con la manipulación de metadatos sin crear un objeto de libro de trabajo**
Esta versión de Aspose.Cells for Java API ha expuesto dos nuevas clases, a saber, WorkbookMetadata y MetadataOptions junto con una nueva enumeración MetadataType que ahora permite manipular las propiedades del documento (metadatos) sin crear una instancia de Workbook. La clase WorkbookMetadata es liviana y proporciona un mecanismo eficiente y muy fácil de usar para[lea, escriba y actualice las propiedades del documento sin afectar el rendimiento general](/cells/es/java/using-workbookmetadata/). 

El siguiente es el escenario de uso simple.

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
### **Propiedad HtmlSaveOptions.ExportFrameScriptsAndProperties agregada**
Aspose.Cells for Java 8.6.0 ha expuesto la propiedad HtmlSaveOptions.ExportFrameScriptsAndProperties que se puede usar para influir en la creación de scripts adicionales al convertir las hojas de cálculo al formato HTML. Con la configuración predeterminada, las API Aspose.Cells exportan la hoja de cálculo en formato HTML como la aplicación Excel hace la exportación, es decir; el HTML resultante contiene los marcos y los comentarios condicionales, que detecta el tipo de navegador y ajusta el diseño en consecuencia. El valor predeterminado de la propiedad HtmlSaveOptions.ExportFrameScriptsAndProperties es verdadero, eso significa; la exportación se realiza según los estándares de Excel. Si la propiedad se establece en falso, el API no[generar los scripts relacionados con los marcos y comentarios condicionales](/cells/es/java/disable-exporting-frame-scripts-and-document-properties/). En este caso, el HTML resultante se puede ver correctamente en cualquier navegador, sin embargo, no se puede volver a importar utilizando las API Aspose.Cells.

El siguiente es el escenario de uso simple.

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
### **Propiedad Shape.MarcoName agregado**
Aspose.Cells for Java 8.6.0 ha expuesto la propiedad Shape.MarcoName que se puede usar para[asignar un módulo VBA a un control de formulario](/cells/es/java/assign-macro-code-to-form-control/) tal Botón para proporcionar la interacción. La propiedad es de tipo cadena por lo que puede aceptar el nombre del módulo y asignarlo al control.

El siguiente es el escenario de uso simple.

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
### **Propiedad OoxmlSaveOptions.UpdateZoom agregado**
Con el lanzamiento de v8.6.0, Aspose.Cells for Java API ha expuesto la propiedad OoxmlSaveOptions.UpdateZoom que se puede usar para actualizar PageSetup.Zoom si se han usado las propiedades PageSetup.FitToPagesWide y/o PageSetup.FitToPagesTall para controlar el escalado de la hoja de trabajo.
