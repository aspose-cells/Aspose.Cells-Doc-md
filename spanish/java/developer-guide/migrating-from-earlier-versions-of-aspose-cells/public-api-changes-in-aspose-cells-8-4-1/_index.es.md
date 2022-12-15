---
title: Público API Cambios en Aspose.Cells 8.4.1
type: docs
weight: 150
url: /es/java/public-api-changes-in-aspose-cells-8-4-1/
---
{{% alert color="primary" %}} 

 Este documento describe los cambios al Aspose.Cells API de la versión 8.4.0 a la 8.4.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados,[Clases añadidas, etc.](/cells/es/java/public-api-changes-in-aspose-cells-8-4-1/) y[clases eliminadas, etc.](/cells/es/java/public-api-changes-in-aspose-cells-8-4-1/), pero también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Mecanismo para modificar la conexión de la base de datos**
La clase com.aspose.cells.ExternalConnection ya contenía el método y las propiedades que podrían usarse para inspeccionar los detalles de conexión de la base de datos almacenados en una hoja de cálculo. La mayoría de las propiedades asociadas con la clase ExternalConnection eran de solo lectura hasta el lanzamiento de Aspose.Cells for Java 8.4.1. Con esta versión, el API también ha brindado soporte para manipular la configuración de conexión de la base de datos.

El siguiente fragmento de código muestra cómo modificar dinámicamente la configuración de conexión de la base de datos.

**Java**

{{< highlight "csharp" >}}

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

Estas son algunas de las propiedades más importantes expuestas por la clase {ExternalConnection}}.

|**Nombre de la propiedad** |**Descripción** |
|:- |:- |
| FondoActualizar|Indica si la conexión se puede actualizar en segundo plano (asincrónicamente).<br> true si el uso preferido de la conexión es actualizar de forma asíncrona en segundo plano;<br> falso si el uso preferido de la conexión es actualizar sincrónicamente en primer plano.|
| ConexiónDescripción| Especifica la descripción del usuario para esta conexión.|
| ID de conexión| Especifica el identificador único de esta conexión.|
| Cartas credenciales| Especifica el método de autenticación que se utilizará al establecer (o restablecer) la conexión.|
| Esta borrado|Indica si se ha eliminado la conexión del libro de trabajo asociado. cierto si el<br> la conexión ha sido eliminada; en caso contrario, falso.|
| Es nuevo| True si la conexión no se ha actualizado por primera vez; en caso contrario, falso. Este<br> El estado puede ocurrir cuando el usuario guarda el archivo antes de que una consulta haya terminado de regresar.|
| Mantener viva|Verdadero cuando la aplicación de hoja de cálculo debe esforzarse por mantener la conexión<br> abierto. Cuando es falso, la aplicación debe cerrar la conexión después de recuperar el<br> información.|
| Nombre| Especifica el nombre de la conexión. Cada conexión debe tener un nombre único.|
| OdcArchivo| Especifica la ruta completa al archivo de conexión externa desde el que se realizó esta conexión.<br> creado. Si una conexión falla durante un intento de actualizar los datos y reconnectionMethod=1,<br> luego, la aplicación de hoja de cálculo volverá a intentarlo utilizando la información del archivo de conexión externa<br> en lugar del objeto de conexión incrustado en el libro de trabajo.|
| OnlyUseConnectionFile| Indica si la aplicación de hoja de cálculo debe usar siempre y solo el<br> información de conexión en el archivo de conexión externo indicado por el atributo odcFile<br> cuando se actualiza la conexión. Si es falso, entonces la aplicación de hoja de cálculo<br>debe seguir el procedimiento indicado por el atributo reconnectionMethod|
| Parámetros| Obtiene ConnectionParameterCollection para una consulta web o ODBC.|
| Método de reconexión| Especifique el tipo de método de reconexión|
|RefreshInterno| Especifica la cantidad de minutos entre actualizaciones automáticas de la conexión.|
| RefreshOnLoad| True si esta conexión debe actualizarse al abrir el archivo; en caso contrario, falso.|
| Guardar datos|True si se van a guardar los datos externos obtenidos a través de la conexión para completar una tabla<br> con el libro de trabajo; en caso contrario, falso.|
| Guardar contraseña| True si la contraseña se guardará como parte de la cadena de conexión; de lo contrario, Falso.|
| Archivo fuente| Se utiliza cuando la fuente de datos externa está basada en archivos. Cuando una conexión a tales datos<br> fuente falla, la aplicación de hoja de cálculo intenta conectarse directamente a este archivo. Quizás<br> expresado en URI o notación de ruta de archivo específica del sistema.|
|ID de SSO|Identificador de inicio de sesión único (SSO) utilizado para la autenticación entre un intermediario<br> servidor spreadsheetML y la fuente de datos externa.|
| Escribe| Especifica el tipo de fuente de datos.|

### **Capacidad para formatear una subcadena de texto de DataLabels**
Aspose.Cells for Java 8.4.1 ha expuesto el método DataLabels.characters para recuperar una instancia de la clase FontSetting que corresponde a la subcadena de ChartPoints.DataLabels. A su vez, la instancia de la clase FontSetting se puede usar para formatear la subcadena de las etiquetas de datos con diferentes configuraciones y colores de fuente.

El siguiente fragmento de código muestra cómo usar el método DataLabels.characters.

**Java**

{{< highlight "csharp" >}}

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

### **Capacidad para establecer las dimensiones de imagen deseadas para la hoja de cálculo y la exportación de gráficos**
Aspose.Cells for Java 8.4.1 ha expuesto el método ImageOrPrintOptions.setDesiredSize para establecer las dimensiones de la imagen resultante al exportar hojas de cálculo y gráficos a imágenes. El método ImageOrPrintOptions.setDesiredSize acepta dos parámetros de tipo entero, donde el primero es el ancho deseado y el segundo es la altura deseada.

El siguiente fragmento de código muestra cómo establecer las dimensiones deseadas al exportar la hoja de trabajo a PNG.

**Java**

{{< highlight "csharp" >}}

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
 Con el lanzamiento de v8.4.1, Aspose.Cells API ha proporcionado la propiedad PageSetup.PrintComments y la enumeración PrintCommentsType para facilitar la representación de comentarios al convertir hojas de cálculo a formato PDF. La enumeración PrintCommentsType tiene las siguientes constantes.

- ImprimirComentariosTipo.IMPRIMIR_NO_COMENTARIOS: Los comentarios no deben ser renderizados.
- ImprimirComentariosTipo.IMPRIMIR_EN_LUGAR: Los comentarios deben presentarse donde se colocan.
- ImprimirComentariosTipo.IMPRIMIR_SÁBANA_FIN: Los comentarios deben presentarse al final de la hoja de trabajo.

El siguiente código de ejemplo muestra el uso de la propiedad PageSetup.PrintComments para representar los comentarios con todos los valores de enumeración PrintCommentsType posibles.

**Java**

{{< highlight "csharp" >}}

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
Aspose.Cells for Java 8.4.1 ha expuesto Workbook.isLicensed, que podría ser de gran ayuda para determinar si la licencia se cargó correctamente o no. Si accede a esta propiedad antes de establecer la licencia, devolverá falso y viceversa, sin embargo, la licencia debería ser válida.

El siguiente código de ejemplo muestra el uso de la propiedad Workbook.isLicensed.

**Java**

{{< highlight "csharp" >}}

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
Aspose.Cells for Java 8.4.1 ha expuesto la propiedad SVGFitToViewPort para la clase ImageOrPrintOptions que se puede usar para activar el atributo viewBox para el formato de archivo SVG al exportar hojas de cálculo o gráficos al formato SVG. El valor predeterminado de esta propiedad es falso, por lo tanto, el XML base para el archivo SVG generado sin configurar la propiedad mencionada anteriormente no incluirá el atributo viewBox.

El siguiente código de ejemplo demuestra el uso de la propiedad ImageOrPrintOptions.SVGFitToViewPort.

**Java**

{{< highlight "csharp" >}}

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
## **API obsoletas**
### **Método Workbook.validateFormula Obsoleto**
Utilice la propiedad Cell.Formula para validar la fórmula.
