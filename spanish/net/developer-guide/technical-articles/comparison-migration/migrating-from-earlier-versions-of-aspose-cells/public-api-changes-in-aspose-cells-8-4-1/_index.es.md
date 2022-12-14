---
title: Público API Cambios en Aspose.Cells 8.4.1
type: docs
weight: 140
url: /es/net/public-api-changes-in-aspose-cells-8-4-1/
---
{{% alert color="primary" %}} 

 Este documento describe los cambios al Aspose.Cells API de la versión 8.4.0 a la 8.4.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados,[Clases añadidas, etc.](/cells/es/net/public-api-changes-in-aspose-cells-8-4-1/) y[clases eliminadas, etc.](/cells/es/net/public-api-changes-in-aspose-cells-8-4-1/), pero también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Mecanismo para modificar la conexión de la base de datos**
La clase Aspose.Cells.ExternalConnections.ExternalConnection ya contenía el método y las propiedades que podrían usarse para inspeccionar los detalles de conexión de la base de datos almacenados en una hoja de cálculo. La mayoría de las propiedades asociadas con la clase Aspose.Cells.ExternalConnections.ExternalConnection eran de solo lectura hasta el lanzamiento de Aspose.Cells for .NET 8.4.1. Con esta versión, el API también ha brindado soporte para manipular la configuración de conexión de la base de datos.

El siguiente fragmento de código muestra cómo modificar dinámicamente la configuración de conexión de la base de datos.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first data connection

Aspose.Cells.ExternalConnections.ExternalConnection conn = workbook.DataConnections[0];

//Change a few properties

conn.Name = "MyConnectionName";

conn.OdcFile = "MyDefaulConnection.odc";

conn.ConnectionDescription = "Test Connection";

conn.Credentials = Aspose.Cells.ExternalConnections.CredentialsMethodType.Prompt;

//Save the workbook

workbook.Save(output);

{{< /highlight >}}



Estas son algunas de las propiedades más importantes expuestas por la clase {Aspose.Cells.ExternalConnections.ExternalConnection}}.

|**Nombre de la propiedad**|**Descripción**|
|:- |:- |
|FondoActualizar|Indica si la conexión se puede actualizar en segundo plano (asincrónicamente).<br> true si el uso preferido de la conexión es actualizar de forma asíncrona en segundo plano;<br>falso si el uso preferido de la conexión es actualizar sincrónicamente en primer plano.|
|ConexiónDescripción|Especifica la descripción del usuario para esta conexión.|
|ID de conexión|Especifica el identificador único de esta conexión.|
|Cartas credenciales|Especifica el método de autenticación que se utilizará al establecer (o restablecer) la conexión.|
|Esta borrado|Indica si se ha eliminado la conexión del libro de trabajo asociado. cierto si el<br>la conexión ha sido eliminada; en caso contrario, falso.|
|Es nuevo| True si la conexión no se ha actualizado por primera vez; en caso contrario, falso. Este<br>El estado puede ocurrir cuando el usuario guarda el archivo antes de que una consulta haya terminado de regresar.|
|Mantener viva|Verdadero cuando la aplicación de hoja de cálculo debe esforzarse por mantener la conexión<br> abierto. Cuando es falso, la aplicación debe cerrar la conexión después de recuperar el<br>información.|
|Nombre|Especifica el nombre de la conexión. Cada conexión debe tener un nombre único.|
|OdcArchivo| Especifica la ruta completa al archivo de conexión externa desde el que se realizó esta conexión.<br> creado. Si una conexión falla durante un intento de actualizar los datos y reconnectionMethod=1,<br> luego, la aplicación de hoja de cálculo volverá a intentarlo utilizando la información del archivo de conexión externa<br>en lugar del objeto de conexión incrustado en el libro de trabajo.|
|OnlyUseConnectionFile| Indica si la aplicación de hoja de cálculo debe usar siempre y solo el<br> información de conexión en el archivo de conexión externo indicado por el atributo odcFile<br> cuando se actualiza la conexión. Si es falso, entonces la aplicación de hoja de cálculo<br>debe seguir el procedimiento indicado por el atributo reconnectionMethod|
|Parámetros|Obtiene ConnectionParameterCollection para una consulta web o ODBC.|
|Método de reconexión|Especifique el tipo de método de reconexión|
|RefreshInterno|Especifica la cantidad de minutos entre actualizaciones automáticas de la conexión.|
|RefreshOnLoad|True si esta conexión debe actualizarse al abrir el archivo; en caso contrario, falso.|
|Guardar datos|True si se van a guardar los datos externos obtenidos a través de la conexión para completar una tabla<br>con el libro de trabajo; en caso contrario, falso.|
|Guardar contraseña|True si la contraseña se guardará como parte de la cadena de conexión; de lo contrario, Falso.|
|Archivo fuente| Se utiliza cuando la fuente de datos externa está basada en archivos. Cuando una conexión a tales datos<br> fuente falla, la aplicación de hoja de cálculo intenta conectarse directamente a este archivo. Quizás<br>expresado en URI o notación de ruta de archivo específica del sistema.|
|ID de SSO|Identificador de inicio de sesión único (SSO) utilizado para la autenticación entre un intermediario<br>servidor spreadsheetML y la fuente de datos externa.|
|Escribe|Especifica el tipo de fuente de datos.|

### **Capacidad para formatear una subcadena de texto de DataLabels**
Aspose.Cells for .NET 8.4.1 ha expuesto el método DataLabels.Characters para recuperar una instancia de la clase FontSetting que corresponde a la subcadena de ChartPoints.DataLabels. A su vez, la instancia de la clase FontSetting se puede usar para formatear la subcadena de las etiquetas de datos con diferentes configuraciones y colores de fuente.

El siguiente fragmento de código muestra cómo usar el método DataLabels.Characters.

**C#**

{{< highlight "csharp" >}}

 //Create a workbook from source Excel file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Access the first chart inside the sheet

Aspose.Cells.Charts.Chart chart = worksheet.Charts[0];

//Access the data label of first series first point

Aspose.Cells.Charts.DataLabels labels = chart.NSeries[0].Points[0].DataLabels;

//Set data label text

labels.Text = "Rich Text Label";

//Set the font setting of the first 10 characters

Aspose.Cells.FontSetting settings = labels.Characters(0, 10);

settings.Font.Color = System.Drawing.Color.Red;

settings.Font.IsBold = true;

//Save the workbook

workbook.Save(output);

{{< /highlight >}}


### **Capacidad para establecer las dimensiones de imagen deseadas para la hoja de cálculo y la exportación de gráficos**
Aspose.Cells for .NET 8.4.1 ha expuesto el método ImageOrPrintOptions.SetDesiredSize para establecer las dimensiones de la imagen resultante al exportar hojas de cálculo y gráficos a imágenes. El método ImageOrPrintOptions.SetDesiredSize acepta dos parámetros de tipo entero, donde el primero es el ancho deseado y el segundo es la altura deseada.

El siguiente fragmento de código muestra cómo establecer las dimensiones deseadas al exportar la hoja de trabajo a PNG.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Create an instance of ImageOrPrintOptions

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

//Set resultant image format

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Png;

//Set desired dimensions as 400x400

options.SetDesiredSize(400, 400);

//Render sheet to image

Aspose.Cells.Rendering.SheetRender renderer = new Aspose.Cells.Rendering.SheetRender(worksheet, options);

renderer.ToImage(0, "output.png"); 

{{< /highlight >}}

{{% alert color="primary" %}} 

La misma propiedad también se puede utilizar para convertir gráficos en imágenes.

{{% /alert %}} 


### **Renderización de comentarios a PDF**
Con el lanzamiento de v8.4.1, Aspose.Cells API ha proporcionado la propiedad PageSetup.PrintComments y la enumeración PrintCommentsType para facilitar la representación de comentarios al convertir hojas de cálculo a formato PDF. La enumeración PrintCommentsType tiene las siguientes constantes.

- PrintCommentsType.PrintNoComments: los comentarios no deben procesarse.
- PrintCommentsType.PrintInPlace: los comentarios deben representarse donde se colocaron.
- PrintCommentsType.PrintSheetEnd: los comentarios deben presentarse al final de la hoja de trabajo.

El siguiente código de ejemplo muestra el uso de la propiedad PageSetup.PrintComments para representar los comentarios con todos los valores de enumeración PrintCommentsType posibles.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of workbook

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Print no comments

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintNoComments;

//Save workbook in PDF format without comments

workbook.Save("nocomments.pdf");

//Print the comments as displayed on sheet

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintInPlace;

//Save workbook in PDF format while rendering comments in place

workbook.Save("printinplace.pdf");

//Print the comments at the end of sheet

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintSheetEnd;

//Save workbook in PDF format while rendering comments at the end of worksheet

workbook.Save("printsheetend.pdf");

{{< /highlight >}}


### **Mover hojas de trabajo en Aspose.Cells.GridDesktop**
Aspose.Cells.GridDesktop proporciona el método WorksheetCollection.MoveTo, que se puede usar para mover una hoja de trabajo al índice especificado. El método mencionado anteriormente toma los índices (basados en cero) de la hoja de trabajo de origen y la hoja de trabajo de destino como parámetros.

El siguiente código de ejemplo demuestra el uso de la propiedad WorksheetCollection.MoveTo.

**C#**

{{< highlight "csharp" >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **Se agregó la propiedad Workbook.IsLicensed**
Aspose.Cells for .NET 8.4.1 ha expuesto Workbook.IsLicensed, que podría ser de gran ayuda para determinar si la licencia se cargó correctamente o no. Si accede a esta propiedad antes de establecer la licencia, devolverá falso y viceversa, sin embargo, la licencia debería ser válida.

El siguiente código de ejemplo demuestra el uso de la propiedad Workbook.IsLicensed.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object before setting a license

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook();

//Check if the license is loaded or not

if (!workbook.IsLicensed)

{

    //Set license

    Aspose.Cells.License license = new Aspose.Cells.License();

    lic.SetLicense(licPath);

}

else

{

    //do process

}

{{< /highlight >}}


### **Se agregó la propiedad ImageOrPrintOptions.SVGFitToViewPort**
Aspose.Cells for .NET 8.4.1 ha expuesto la propiedad SVGFitToViewPort para la clase ImageOrPrintOptions que se puede usar para activar el atributo viewBox para el formato de archivo SVG al exportar hojas de cálculo o gráficos al formato SVG. El valor predeterminado de esta propiedad es falso, por lo tanto, el XML base para el archivo SVG generado sin configurar la propiedad mencionada anteriormente no incluirá el atributo viewBox.

El siguiente código de ejemplo demuestra el uso de la propiedad ImageOrPrintOptions.SVGFitToViewPort.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Create an instance of ImageOrPrintOptions

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

//Set image format to SVG

options.SaveFormat = Aspose.Cells.SaveFormat.SVG;

//Set the SVGFitToViewPort to true

options.SVGFitToViewPort = true;

//Create an instance of SheetRender and initialize it with worksheet instance as well as object of ImageOrPrintOptions

Aspose.Cells.Rendering.SheetRender renderer = new Aspose.Cells.Rendering.SheetRender(worksheet, options);

renderer.ToImage(0, "output.svg");

{{< /highlight >}}
## **API obsoletas**
### **Método Workbook.ValidateFormula Obsoleto**
Utilice el método Cell.Formula para validar la fórmula.
