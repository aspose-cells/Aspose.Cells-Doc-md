---
title: Cambios en la API pública en Aspose.Cells 8.4.1
type: docs
weight: 150
url: /es/java/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.4.0 a la 8.4.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, [clases añadidas, etc.](/cells/es/java/cambios-en-la-api-pública-en-aspose-cells-8-4-1/) y [clases eliminadas, etc.](/cells/es/java/cambios-en-la-api-pública-en-aspose-cells-8-4-1/), sino también una descripción de cualquier cambio en el comportamiento tras bastidores en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Mecanismo para Modificar la Conexión a la Base de Datos**
La clase com.aspose.cells.ExternalConnection ya contenía el método y propiedades que podían ser utilizados para inspeccionar los detalles de la conexión a la base de datos almacenados en una hoja de cálculo. La mayoría de las propiedades asociadas con la clase ExternalConnection eran de solo lectura hasta el lanzamiento de Aspose.Cells for Java 8.4.1. Con este lanzamiento, la API ha proporcionado el soporte para manipular la configuración de la conexión a la base de datos.

El siguiente fragmento de código muestra cómo modificar dinámicamente la configuración de la conexión a la base de datos.

**Java**

{{< highlight csharp >}}

 //Create workbook object

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first data connection

com.aspose.cells.ExternalConnection conn = workbook.getDataConnections().get(0);

//Change a few properties

conn.setName("MyConnectionName");

conn.setOdcFile("MyDefaulConnection.odc");

conn.setConnectionDescription("Test Connection");

conn.setCredentials(com.aspose.cells.CredentialsMethodType.PROMPT);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

Aquí se muestran algunas propiedades más importantes expuestas por la clase {ExternalConnection}}.

|**Nombre de la propiedad** |**Descripción** |
| :- | :- |
|BackgroundRefresh |Indica si la conexión puede actualizarse en segundo plano (asíncronamente). <br>true si el uso preferido de la conexión es actualizar de forma asíncrona en segundo plano; <br>false si el uso preferido de la conexión es actualizar de forma sincrónica en primer plano. |
|ConnectionDescription |Especifica la descripción del usuario para esta conexión |
|ConnectionId |Especifica el identificador único de esta conexión. |
|Credentials |Especifica el método de autenticación a utilizar al establecer (o restablecer) la conexión. |
|IsDeleted |Indica si la conexión a la hoja de cálculo asociada ha sido eliminada. true si la<br>conexión ha sido eliminada; de lo contrario, false. |
|IsNew |True si la conexión no ha sido actualizada por primera vez; de lo contrario, false. Este <br>estado puede ocurrir cuando el usuario guarda el archivo antes de que una consulta haya terminado de devolver resultados. |
|KeepAlive |True cuando la aplicación de hoja de cálculo debe esforzarse por mantener la conexión <br>abierta. Cuando es false, la aplicación debe cerrar la conexión después de recuperar la <br>información. |
|Name |Especifica el nombre de la conexión. Cada conexión debe tener un nombre único. |
|OdcFile |Especifica la ruta completa al archivo de conexión externa desde el cual se creó esta conexión. Si una conexión falla durante un intento de actualizar datos, y reconnectionMethod=1, <br>entonces la aplicación de hoja de cálculo intentará nuevamente usando la información del archivo de conexión externa <br>en lugar del objeto de conexión incrustado dentro del libro de trabajo. |
|OnlyUseConnectionFile |Indica si la aplicación de hoja de cálculo debe siempre y solo utilizar la <br>información de conexión en el archivo de conexión externa indicado por el atributo odcFile <br>cuando se actualice la conexión. Si es false, entonces la aplicación de hoja de cálculo <br>debe seguir el procedimiento indicado por el atributo reconnectionMethod |
|Parameters |Obtiene ConnectionParameterCollection para un query de ODBC o web. |
|ReConnectionMethod |Especifica el tipo de reconnectionMethod |
|RefreshInternal|Especifica el número de minutos entre actualizaciones automáticas de la conexión. |
|RefreshOnLoad |Verdadero si esta conexión debe actualizarse al abrir el archivo; de lo contrario, falso. |
|SaveData |Verdadero si los datos externos recuperados a través de la conexión para poblar una tabla deben guardarse con el libro; de lo contrario, falso. |
|SavePassword |Verdadero si la contraseña debe guardarse como parte de la cadena de conexión; de lo contrario, falso. |
|SourceFile |Se utiliza cuando la fuente de datos externa es un archivo. Cuando falla una conexión a esa fuente de datos, la aplicación de hoja de cálculo intenta conectarse directamente a este archivo. Puede expresarse en URI o notación de ruta de archivo específica del sistema. |
|SSOId|Identificador para el inicio de sesión único (SSO) utilizado para la autenticación entre un servidor intermedio de spreadsheetML y la fuente de datos externa. |
|Type |Especifica el tipo de fuente de datos. |

### **Capacidad para formatear una subcadena del texto de las etiquetas de datos**
Aspose.Cells for JavaLa versión 8.4.1 ha expuesto el método DataLabels.characters para recuperar una instancia de la clase FontSetting que corresponde a la subcadena de DataLabels de ChartPoints. A su vez, la instancia de la clase FontSetting se puede utilizar para formatear la subcadena de los DataLabels con diferentes ajustes de fuente y color.

El siguiente fragmento de código muestra cómo utilizar el método DataLabels.characters.

**Java**

{{< highlight csharp >}}

 //Create a workbook from source Excel file

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first chart inside the sheet

com.aspose.cells.Chart chart = worksheet.getCharts().get(0);

//Access the data label of first series first point

com.aspose.cells.DataLabels labels = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

//Set data label text

labels.setText("Rich Text Label");

//Set the font setting of the first 10 characters

com.aspose.cells.FontSetting settings = labels.characters(0, 10);

settings.getFont().setColor(com.aspose.cells.Color.getRed());

settings.getFont().setBold(true);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **Capacidad para establecer las dimensiones de imagen deseadas para la exportación de hojas de cálculo y gráficos**
Aspose.Cells for JavaLa versión 8.4.1 ha expuesto el método ImageOrPrintOptions.setDesiredSize para establecer las dimensiones de la imagen resultante al exportar hojas de cálculo y gráficos a imágenes. El método ImageOrPrintOptions.setDesiredSize acepta dos parámetros de tipo entero, donde el primero es el ancho deseado y el segundo es el alto deseado.

El siguiente fragmento de código muestra cómo establecer las dimensiones deseadas al exportar una hoja de cálculo a PNG.

**Java**

{{< highlight csharp >}}

 com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions

com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();

//Set resultant image format

options.setImageFormat(com.aspose.cells.ImageFormat.getPng());

//Set desired dimensions as 400x400

options.setDesiredSize(400, 400);

//Render sheet to image

com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);

renderer.toImage(0, "output.png");

{{< /highlight >}}

{{% alert color="primary" %}} 

El mismo método también se puede utilizar para convertir gráficos en imágenes. 

{{% /alert %}} 

### **Renderización de comentarios a PDF**
Con el lanzamiento de la v8.4.1, la API de Aspose.Cells ha proporcionado la propiedad PageSetup.PrintComments y la enumeración PrintCommentsType para facilitar la renderización de comentarios al convertir hojas de cálculo al formato PDF. La enumeración PrintCommentsType tiene los siguientes constantes. 

- PrintCommentsType.PRINT_NO_COMMENTS: Los comentarios no se mostrarán.
- PrintCommentsType.PRINT_IN_PLACE: Los comentarios se mostrarán donde se encuentren.
- PrintCommentsType.PRINT_SHEET_END: Los comentarios se mostrarán al final de la hoja de cálculo.

El siguiente código de muestra demuestra el uso de la propiedad PageSetup.PrintComments para mostrar los comentarios utilizando todos los valores de enumeración PrintCommentsType.

**Java**

{{< highlight csharp >}}

 //Create an instance of workbook

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Print no comments

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_NO_COMMENTS);

//Save workbook in PDF format without comments

workbook.save("nocomments.pdf");

//Print the comments as displayed on sheet

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_IN_PLACE);

//Save workbook in PDF format while rendering comments in place

workbook.save("printinplace.pdf");

//Print the comments at the end of sheet

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_SHEET_END);

//Save workbook in PDF format while rendering comments at the end of worksheet

workbook.save("printsheetend.pdf");

{{< /highlight >}}

### **Se agregó la propiedad Workbook.isLicensed**
Aspose.Cells for Java 8.4.1 ha expuesto la propiedad Workbook.isLicensed que podría ser de gran ayuda para determinar si la licencia se ha cargado con éxito o no. Si accedes a esta propiedad antes de establecer la licencia, devolverá falso y viceversa, sin embargo, la licencia debería ser válida.

El siguiente código de muestra demuestra el uso de la propiedad Workbook.isLicensed.

**Java**

{{< highlight csharp >}}

 //Create workbook object before setting a license

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook();

//Check if the license is loaded or not

if (!workbook.isLicensed())

{

	//Set license

	com.aspose.cells.License license = new com.aspose.cells.License();

	lic.SetLicense(licPath);

}

else

{

  //do process

}

{{< /highlight >}}

### **Se agregó la propiedad ImageOrPrintOptions.SVGFitToViewPort**
Aspose.Cells for Java 8.4.1 ha expuesto la propiedad SVGFitToViewPort para la clase ImageOrPrintOptions que se puede utilizar para activar el atributo viewBox en el formato de archivo SVG al exportar hojas de cálculo o gráficos al formato SVG. El valor predeterminado de esta propiedad es falso por lo tanto el XML base para el archivo SVG generado sin configurar la propiedad mencionada anteriormente no incluirá el atributo viewBox.

El siguiente código de muestra demuestra el uso de la propiedad ImageOrPrintOptions.SVGFitToViewPort.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source file

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions

com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();

//Set image format to SVG

options.setSaveFormat(com.aspose.cells.SaveFormat.SVG);

//Set the SVGFitToViewPort to true

options.setSVGFitToViewPort(true);

//Create an instance of SheetRender and initialize it with worksheet instance as well as object of ImageOrPrintOptions

com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);

renderer.toImage(0, "output.svg");

{{< /highlight >}}
## **APIs obsoletas**
### **Método Workbook.validateFormula obsoleto**
Utilice la propiedad Cell.Formula para validar la fórmula.
{{< app/cells/assistant language="java" >}}
