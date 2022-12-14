---
title: Público API Cambios en Aspose.Cells 8.6.1
type: docs
weight: 210
url: /es/java/public-api-changes-in-aspose-cells-8-6-1/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.6.0 a la 8.6.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Compatibilidad con el tipo de destino de enlace HTML**
Esta versión de Aspose.Cells for Java API ha expuesto una enumeración llamada HtmlLinkTargetType junto con una nueva propiedad HtmlSaveOptions.LinkTargetType que juntos permiten[establezca el tipo de destino para los enlaces en la hoja de cálculo durante la conversión a formato HTML](/cells/es/java/change-the-html-link-target-type/). Los valores posibles de la enumeración HtmlLinkTargetType son los siguientes, donde el valor predeterminado es SELF.

1. HtmlLinkTargetType.BLANK: abre el documento o la página vinculados en una nueva ventana o pestaña.
1. HtmlLinkTargetType.PARENT: abre el documento o la página vinculados en el marco principal.
1. HtmlLinkTargetType.SELF: abre el documento o la página vinculados en el mismo marco donde se hizo clic en el vínculo.
1. HtmlLinkTargetType.TOP: abre el documento o la página vinculados en el cuerpo completo de la ventana.

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.setLinkTargetType(HtmlLinkTargetType.BLANK);


//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.save(outputFilePath, options);

{{< /highlight >}}
### **Método VbaModuleCollection.remove Agregado**
Aspose.Cells for Java 8.6.1 ha expuesto otra sobrecarga del método VbaModuleCollection.remove que ahora puede aceptar una instancia de Worksheet para eliminar todos los módulos VBA asociados con la hoja de trabajo especificada.

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **Método RangeCollection.add Agregado**
Aspose.Cells for Java 8.6.1 ha expuesto el método RangeCollection.Add que se puede usar para agregar objetos Range a la colección de rangos para una hoja de trabajo en particular.

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.getWorksheets().get(0).getCells();

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.getRanges();

//Add another range to the collection

ranges.add(cells.createRange("A1:B4"));

{{< /highlight >}}
### **Método Cell.setCaracteres agregados**
 El método Cell.setCharacters se puede utilizar para[actualizar las partes del texto enriquecido](/cells/es/java/access-and-update-the-portions-of-rich-text-of-cell/) de un objeto Cell dado. El método Cell.getCharacters se debe usar para acceder a las partes del texto y luego se pueden hacer enmiendas usando el método Cell.setCharacters mientras que el**obtener** El método devuelve una matriz de objetos FontSetting que se pueden manipular para establecer varias propiedades: nombre de fuente, color de fuente, negrita, etc.**establecer** El método se puede utilizar para aplicar los cambios.

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cells containing the Rich Text

Cell cell = worksheet.getCells().get("A1");

//Retrieve the array of FontSetting from the cell

FontSetting[]settings = cell.getCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].getFont().setName("Arial");

//Set the updated FontSetting

cell.setCharacters(settings);

{{< /highlight >}}
### **Propiedad VbaProject.isSigned agregado**
 Aspose.Cells for Java 8.6.1 ha expuesto la propiedad VbaProject.isSigned que se puede utilizar para[probar si un VbaProject en un libro de trabajo está firmado o no](/cells/es/java/check-if-vba-project-in-a-workbook-is-signed/). La propiedad de tipo booleano devuelve verdadero si el proyecto está firmado.

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VbaProject from the Workbook

VbaProject project = workbook.getVbaProject();

//Test if VbaProject is signed

if (project.isSigned())

{

    System.out.println("VBA Project is Signed");

}

else

{

	System.out.println("VBA Project is not Signed");

}

{{< /highlight >}}
## **API modificadas**
### **Método Cell.getFormatConditions modificado**
Con el lanzamiento de v8.6.1, Aspose.Cells for Java API modificó el tipo de devolución del método Cell.getFormatConditions que ahora devuelve una matriz de tipo FormatConditionCollection.
## **API obsoletas**
### **Método Workbook.checkWriteProtectedPassword Obsoleto**
Con el lanzamiento de v8.6.1, el método Workbook.checkWriteProtectedPassword se ha marcado como obsoleto. Se recomienda utilizar el método WorkbookSettings.WriteProtection.validatePassword que puede aceptar un valor de cadena como parámetro y devuelve un valor booleano si la contraseña coincide con la contraseña preestablecida de la hoja de cálculo.
