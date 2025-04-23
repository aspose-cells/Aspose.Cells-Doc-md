---
title: Cambios en la API pública en Aspose.Cells 8.6.0
type: docs
weight: 190
url: /es/net/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.5.2 a la 8.6.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, [clases agregadas, etc.](/cells/es/net/public-api-changes-in-aspose-cells-8-6-0/), sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Soporte para Manipulación de Metadatos Sin Crear un Objeto de Libro de Trabajo**
Esta versión de la API Aspose.Cells for .NET ha expuesto dos nuevas clases, a saber, WorkbookMetadata y MetadataOptions junto con una nueva enumeración MetadataType que ahora permite manipular las propiedades del documento (metadatos) sin crear una instancia de Workbook. La clase WorkbookMetadata es liviana y proporciona un mecanismo muy fácil de usar y eficiente para [leer, escribir y actualizar las propiedades del documento sin afectar el rendimiento general](/cells/es/net/using-workbookmetadata/).

A continuación se muestra un escenario de uso simple.

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


### **Se agregó la propiedad HtmlSaveOptions.ExportFrameScriptsAndProperties**
Aspose.Cells for .NET 8.6.0 ha expuesto la propiedad HtmlSaveOptions.ExportFrameScriptsAndProperties que se puede utilizar para influir en la creación de scripts adicionales al convertir las hojas de cálculo a formato HTML. Con la configuración predeterminada, las API de Aspose.Cells exportan la hoja de cálculo en formato HTML como lo hace la aplicación Excel, es decir; el HTML resultante contiene los marcos y comentarios condicionales, que detectan el tipo de navegador y ajustan el diseño en consecuencia. El valor predeterminado de la propiedad HtmlSaveOptions.ExportFrameScriptsAndProperties es verdadero, lo que significa que la exportación se realiza según los estándares de Excel. Sin embargo, si la propiedad se establece en falso, la API no [generará los scripts relacionados con marcos y comentarios condicionales](/cells/es/net/disable-exporting-frame-scripts-and-document-properties/). En este caso, el HTML resultante se puede ver correctamente en cualquier navegador, sin embargo, no se puede importar de nuevo utilizando las API de Aspose.Cells.

A continuación se muestra un escenario de uso simple.

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


### **Se agregó la propiedad Shape.MarcoName**
Aspose.Cells for .NET 8.6.0 ha expuesto la propiedad Shape.MarcoName que se puede utilizar para [asignar cualquier módulo VBA a un control de formulario](/cells/es/net/assign-macro-to-form-control/) como un botón para proporcionar la interacción. La propiedad es de tipo cadena, por lo tanto, puede aceptar el nombre del módulo y asignarlo al control.

A continuación se muestra un escenario de uso simple.

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


### **Propiedad OoxmlSaveOptions.UpdateZoom agregada**
Con el lanzamiento de la v8.6.0, la API Aspose.Cells for .NET ha expuesto la propiedad OoxmlSaveOptions.UpdateZoom que se puede utilizar para actualizar el PageSetup.Zoom si se han utilizado las propiedades PageSetup.FitToPagesWide y/o PageSetup.FitToPagesTall para controlar el escalado de la hoja de cálculo.
{{< app/cells/assistant language="csharp" >}}
