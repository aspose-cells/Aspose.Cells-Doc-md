---
title: Público API Cambios en Aspose.Cells 8.6.0
type: docs
weight: 190
url: /es/net/public-api-changes-in-aspose-cells-8-6-0/
---
{{% alert color="primary" %}} 

 Este documento describe los cambios al Aspose.Cells API de la versión 8.5.2 a la 8.6.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados,[Clases añadidas, etc.](/cells/es/net/public-api-changes-in-aspose-cells-8-6-0/), pero también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Compatibilidad con la manipulación de metadatos sin crear un objeto de libro de trabajo**
Esta versión de Aspose.Cells for .NET API ha expuesto dos nuevas clases, a saber, WorkbookMetadata y MetadataOptions junto con una nueva enumeración MetadataType que ahora permite manipular las propiedades del documento (metadatos) sin crear una instancia de Workbook. La clase WorkbookMetadata es liviana y proporciona un mecanismo eficiente y muy fácil de usar para[lea, escriba y actualice las propiedades del documento sin afectar el rendimiento general](/cells/es/net/using-workbookmetadata/).

El siguiente es el escenario de uso simple.

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


### **Propiedad HtmlSaveOptions.ExportFrameScriptsAndProperties agregada**
Aspose.Cells for .NET 8.6.0 ha expuesto la propiedad HtmlSaveOptions.ExportFrameScriptsAndProperties que se puede usar para influir en la creación de scripts adicionales al convertir las hojas de cálculo al formato HTML. Con la configuración predeterminada, las API Aspose.Cells exportan la hoja de cálculo en formato HTML como la aplicación Excel hace la exportación, es decir; el HTML resultante contiene los marcos y los comentarios condicionales, que detecta el tipo de navegador y ajusta el diseño en consecuencia. El valor predeterminado de la propiedad HtmlSaveOptions.ExportFrameScriptsAndProperties es verdadero, eso significa; la exportación se realiza según los estándares de Excel. Sin embargo, si la propiedad se establece en falso, el API no[generar los scripts relacionados con marcos y comentarios condicionales](/cells/es/net/disable-exporting-frame-scripts-and-document-properties/). En este caso, el HTML resultante se puede ver correctamente en cualquier navegador, sin embargo, no se puede volver a importar utilizando las API Aspose.Cells.

El siguiente es el escenario de uso simple.

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


### **Propiedad Shape.MarcoName agregado**
Aspose.Cells for .NET 8.6.0 ha expuesto la propiedad Shape.MarcoName que se puede usar para[asignar cualquier módulo VBA a un control de formulario](/cells/es/net/assign-macro-to-form-control/) tal Botón para proporcionar la interacción. La propiedad es de tipo cadena por lo que puede aceptar el nombre del módulo y asignarlo al control.

El siguiente es el escenario de uso simple.

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


### **Propiedad OoxmlSaveOptions.UpdateZoom agregado**
Con el lanzamiento de v8.6.0, Aspose.Cells for .NET API ha expuesto la propiedad OoxmlSaveOptions.UpdateZoom que se puede usar para actualizar PageSetup.Zoom si se han usado las propiedades PageSetup.FitToPagesWide y/o PageSetup.FitToPagesTall para controlar el escalado de la hoja de trabajo.
