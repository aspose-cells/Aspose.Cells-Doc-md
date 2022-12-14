---
title: Público API Cambios en Aspose.Cells 8.6.1
type: docs
weight: 200
url: /es/net/public-api-changes-in-aspose-cells-8-6-1/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.6.0 a la 8.6.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Compatibilidad con el tipo de destino de enlace HTML**
Esta versión de Aspose.Cells for .NET API ha expuesto una enumeración llamada HtmlLinkTargetType junto con una nueva propiedad HtmlSaveOptions.LinkTargetType que juntos permiten[establezca el tipo de destino para los enlaces en la hoja de cálculo durante la conversión a formato HTML](/cells/es/net/change-the-html-link-target-type/). Los valores posibles de la enumeración HtmlLinkTargetType son los siguientes, donde el valor predeterminado es Self.

1. HtmlLinkTargetType.Blank: abre el documento o la página vinculados en una nueva ventana o pestaña.
1. HtmlLinkTargetType.Parent: abre el documento o la página vinculados en el marco principal.
1. HtmlLinkTargetType.Self: abre el documento o la página vinculados en el mismo marco donde se hizo clic en el vínculo.
1. HtmlLinkTargetType.Top: abre el documento o la página vinculados en el cuerpo completo de la ventana.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.LinkTargetType = HtmlLinkTargetType.Blank;

//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.Save(outputFilePath, options);

{{< /highlight >}}


### **Método VbaModuleCollection.Remove Agregado**
Aspose.Cells for .NET 8.6.1 ha expuesto otra sobrecarga del método VbaModuleCollection.Remove que ahora puede aceptar una instancia de Worksheet para eliminar todos los módulos VBA asociados con la hoja de trabajo especificada.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.VbaProject.Modules;

//Remove the VBA modules from specific Worksheet

modules.Remove(workbook.Worksheets[0]);

{{< /highlight >}}


### **Método RangeCollection.Add Agregado**
Aspose.Cells for .NET 8.6.1 ha expuesto el método RangeCollection.Add que se puede usar para agregar objetos Range a la colección de rangos para una hoja de trabajo en particular.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.Worksheets[0].Cells;

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.Ranges;

//Add another range to the collection

ranges.Add(cells.CreateRange("A1:B4"));

{{< /highlight >}}


### **Método Cell. Establecer caracteres añadidos**
 El método Cell.SetCharacters se puede utilizar para[actualizar las partes del texto enriquecido](/cells/es/net/access-and-update-the-portions-of-rich-text-of-cell/) de un objeto Cell dado. El método Cell.GetCharacters se debe usar para acceder a las partes del texto y luego se pueden hacer enmiendas usando el método Cell.SetCharacters mientras que el**Obtener** El método devuelve una matriz de objetos FontSetting que se pueden manipular para establecer varias propiedades: nombre de fuente, color de fuente, negrita, etc.**Establecer** El método se puede utilizar para aplicar los cambios.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.Worksheets[0];

//Access the cells containing the Rich Text

Cell cell = worksheet.Cells["A1"];

//Retrieve the array of FontSetting from the cell

FontSetting[]settings = cell.GetCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].Font.Name = "Arial";

//Set the updated FontSetting

cell.SetCharacters(settings);

{{< /highlight >}}


### **Propiedad VbaProject.IsSigned agregada**
 Aspose.Cells for .NET 8.6.1 ha expuesto la propiedad VbaProject.IsSigned que se puede utilizar para[probar si un VbaProject en un libro de trabajo está firmado o no](/cells/es/net/check-if-vba-project-in-a-workbook-is-signed/). La propiedad de tipo booleano devuelve verdadero si el proyecto está firmado.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VbaProject from the Workbook

VbaProject project = workbook.VbaProject;

//Test if VbaProject is signed

if (project.IsSigned)

{

    Console.WriteLine("VBA Project is Signed");

}

else

{

    Console.WriteLine("VBA Project is not Signed");

}

{{< /highlight >}}
## **API modificadas**
### **Método Cell.GetFormatConditions modificado**
Con el lanzamiento de v8.6.1, Aspose.Cells for .NET API ha modificado el tipo de devolución del método Cell.GetFormatConditions que ahora devuelve una matriz de tipo FormatConditionCollection.
## **API obsoletas**
### **Método Workbook.CheckWriteProtectedPassword obsoleto**
Con el lanzamiento de v8.6.1, el método Workbook.CheckWriteProtectedPassword se ha marcado como obsoleto. Se recomienda utilizar el método WorkbookSettings.WriteProtection.ValidatePassword que puede aceptar un valor de cadena como parámetro y devuelve un valor booleano si la contraseña coincide con la contraseña preestablecida de la hoja de cálculo.
