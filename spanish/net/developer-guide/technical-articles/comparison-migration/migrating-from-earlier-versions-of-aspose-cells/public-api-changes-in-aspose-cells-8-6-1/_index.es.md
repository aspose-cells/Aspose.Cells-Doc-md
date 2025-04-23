---
title: Cambios en la API pública en Aspose.Cells 8.6.1
type: docs
weight: 200
url: /es/net/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.6.0 hasta la 8.6.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, clases agregadas, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Soporte para tipo de enlace HTML**
Esta versión de la API Aspose.Cells for .NET ha expuesto una enumeración llamada HtmlLinkTargetType junto con una nueva propiedad HtmlSaveOptions.LinkTargetType que juntas permiten [establecer el tipo de destino para los enlaces en la hoja de cálculo durante la conversión a formato HTML](/cells/es/net/change-the-html-link-target-type/). Los posibles valores de la enumeración HtmlLinkTargetType son los siguientes, donde el valor predeterminado es Self.

1. HtmlLinkTargetType.Blank: Abre el documento/enlace vinculado en una nueva ventana o pestaña.
1. HtmlLinkTargetType.Parent: Abre el documento/enlace vinculado en el marco padre.
1. HtmlLinkTargetType.Self: Abre el documento/enlace vinculado en el mismo marco donde se hizo clic en el enlace.
1. HtmlLinkTargetType.Top: Abre el documento/enlace vinculado en el cuerpo completo de la ventana.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.LinkTargetType = HtmlLinkTargetType.Blank;

//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.Save(outputFilePath, options);

{{< /highlight >}}


### **Agregado el Método VbaModuleCollection.Remove**
Aspose.Cells for .NET 8.6.1 ha expuesto otra sobrecarga del método VbaModuleCollection.Remove que ahora puede aceptar una instancia de Worksheet para eliminar todos los módulos VBA asociados con la hoja de cálculo especificada.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.VbaProject.Modules;

//Remove the VBA modules from specific Worksheet

modules.Remove(workbook.Worksheets[0]);

{{< /highlight >}}


### **Agregado el Método RangeCollection.Add**
Aspose.Cells for .NET 8.6.1 ha expuesto el método RangeCollection.Add que se puede usar para agregar objetos Range a la colección de rangos para una hoja de cálculo específica.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.Worksheets[0].Cells;

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.Ranges;

//Add another range to the collection

ranges.Add(cells.CreateRange("A1:B4"));

{{< /highlight >}}


### **Método Cell.SetCharacters Agregado**
El método Cell.SetCharacters se puede utilizar para [actualizar las partes del texto enriquecido](/cells/es/net/access-and-update-the-portions-of-rich-text-of-cell/) de un objeto Cell dado. El método Cell.GetCharacters se utiliza para acceder a las partes del texto y luego se pueden realizar modificaciones utilizando el método Cell.SetCharacters, mientras que el método **Get** devuelve una matriz de objetos FontSetting que se pueden manipular para establecer varias propiedades como el nombre de la fuente, color de la fuente, negrita, etc. y el método **Set** se puede usar para aplicar los cambios.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.Worksheets[0];

//Access the cells containing the Rich Text

Cell cell = worksheet.Cells["A1"];

//Retrieve the array of FontSetting from the cell

FontSetting[] settings = cell.GetCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].Font.Name = "Arial";

//Set the updated FontSetting

cell.SetCharacters(settings);

{{< /highlight >}}


### **Propiedad VbaProject.IsSigned Agregada**
Aspose.Cells for .NET 8.6.1 ha expuesto la propiedad VbaProject.IsSigned que se puede utilizar para [comprobar si un proyecto VbaProject en un libro de trabajo está firmado o no](/cells/es/net/check-if-vba-project-in-a-workbook-is-signed/). La propiedad de tipo Boolean devuelve verdadero si el proyecto está firmado.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

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
## **APIs Modificados**
### **Método Modificado Cell.GetFormatConditions**
Con el lanzamiento de v8.6.1, la API Aspose.Cells for .NET ha modificado el tipo de retorno del método Cell.GetFormatConditions que ahora devuelve una matriz de tipo FormatConditionCollection.
## **APIs obsoletas**
### **Método Workbook.CheckWriteProtectedPassword Obsoleto**
Con el lanzamiento de v8.6.1, el método Workbook.CheckWriteProtectedPassword ha sido marcado como obsoleto. Se recomienda utilizar el método WorkbookSettings.WriteProtection.ValidatePassword que puede aceptar un valor de cadena como parámetro y devuelve un Boolean si la contraseña coincide con la contraseña preestablecida de la hoja de cálculo.
{{< app/cells/assistant language="csharp" >}}
