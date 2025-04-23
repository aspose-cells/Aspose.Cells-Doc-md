---
title: Cambios en la API pública en Aspose.Cells 8.6.1
type: docs
weight: 210
url: /es/java/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.6.0 hasta la 8.6.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, clases agregadas, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Soporte para tipo de enlace HTML**
Esta versión de la API Aspose.Cells for Java ha expuesto una enumeración llamada HtmlLinkTargetType junto con una nueva propiedad HtmlSaveOptions.LinkTargetType que juntas permiten [establecer el tipo de destino para los enlaces en la hoja de cálculo durante la conversión al formato HTML](/cells/es/java/change-the-html-link-target-type/). Los valores posibles de la enumeración HtmlLinkTargetType son: donde el valor predeterminado es SELF.

1. HtmlLinkTargetType.BLANK: Abre el documento/enlace vinculado en una nueva ventana o pestaña.
1. HtmlLinkTargetType.PARENT: Abre el documento/enlace vinculado en el marco principal.
1. HtmlLinkTargetType.SELF: Abre el documento/enlace vinculado en el mismo marco donde se hizo clic en el enlace.
1. HtmlLinkTargetType.TOP: Abre el documento/enlace vinculado en todo el cuerpo de la ventana.

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.setLinkTargetType(HtmlLinkTargetType.BLANK);


//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.save(outputFilePath, options);

{{< /highlight >}}
### **Método VbaModuleCollection.remove agregado**
Aspose.Cells for Java 8.6.1 ha expuesto otra sobrecarga del método VbaModuleCollection.remove que ahora puede aceptar una instancia de Worksheet para eliminar todos los módulos VBA asociados con la Hoja de cálculo especificada.

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **Método RangeCollection.add agregado**
Aspose.Cells for Java 8.6.1 ha expuesto el método RangeCollection.Add que se puede utilizar para agregar objetos Range a la colección de rangos para una Hoja de cálculo específica.

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.getWorksheets().get(0).getCells();

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.getRanges();

//Add another range to the collection

ranges.add(cells.createRange("A1:B4"));

{{< /highlight >}}
### **Agregado el Método Cell.setCharacters**
El método Cell.setCharacters puede utilizarse para [actualizar las porciones del texto enriquecido](/cells/es/java/acceder-y-actualizar-las-porciones-del-texto-enriquecido-de-una-celda/) de un objeto Cell dado. El método Cell.getCharacters se utiliza para acceder a las porciones del texto y luego se pueden realizar modificaciones usando el método Cell.setCharacters, mientras que el método **get** devuelve un array de objetos FontSetting que pueden ser manipulados para establecer diversas propiedades como el nombre de la fuente, color de la fuente, negrita, etc. El método **set** se puede utilizar para aplicar los cambios.

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cells containing the Rich Text

Cell cell = worksheet.getCells().get("A1");

//Retrieve the array of FontSetting from the cell

FontSetting[] settings = cell.getCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].getFont().setName("Arial");

//Set the updated FontSetting

cell.setCharacters(settings);

{{< /highlight >}}
### **Agregada la Propiedad VbaProject.isSigned**
La versión Aspose.Cells for Java 8.6.1 ha expuesto la propiedad VbaProject.isSigned que se puede usar para [comprobar si un VbaProject en un libro de Excel está firmado o no](/cells/es/java/comprobar-si-el-proyecto-vba-en-un-libro-de-excel-esta-firmado/). La propiedad de tipo booleano devuelve true si el proyecto está firmado.

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

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
## **APIs Modificados**
### **Método Cell.getFormatConditions Modificado**
Con el lanzamiento de v8.6.1, la API Aspose.Cells for Java ha modificado el tipo de retorno del método Cell.getFormatConditions, que ahora devuelve un array del tipo FormatConditionCollection.
## **APIs obsoletas**
### **Método Workbook.checkWriteProtectedPassword Obsoleto**
Con el lanzamiento de v8.6.1, el método Workbook.checkWriteProtectedPassword ha sido marcado como obsoleto. Se recomienda utilizar el método WorkbookSettings.WriteProtection.validatePassword que puede aceptar un valor de tipo String como parámetro y devuelve un valor Booleano si la contraseña coincide con la contraseña predefinida de la hoja de cálculo.
{{< app/cells/assistant language="java" >}}
