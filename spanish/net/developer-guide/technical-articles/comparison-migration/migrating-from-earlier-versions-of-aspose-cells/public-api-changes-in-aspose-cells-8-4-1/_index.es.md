---
title: Cambios en la API pública en Aspose.Cells 8.4.1
type: docs
weight: 140
url: /es/net/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.4.0 hasta la 8.4.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos métodos y clases actualizadas, [clases agregadas, etc.](/cells/es/net/public-api-changes-in-aspose-cells-8-4-1/) y [clases eliminadas, etc.](/cells/es/net/public-api-changes-in-aspose-cells-8-4-1/), sino también una descripción de cualquier cambio en el comportamiento en secreto en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Mecanismo para Modificar la Conexión a la Base de Datos**
La clase Aspose.Cells.ExternalConnections.ExternalConnection ya contenía el método y las propiedades que podrían usarse para inspeccionar los detalles de la conexión a la base de datos almacenados en una hoja de cálculo. La mayoría de las propiedades asociadas con la clase Aspose.Cells.ExternalConnections.ExternalConnection eran de solo lectura hasta el lanzamiento de Aspose.Cells for .NET 8.4.1. Con este lanzamiento, la API ha proporcionado soporte para manipular la configuración de la conexión a la base de datos.

El siguiente fragmento de código muestra cómo modificar dinámicamente la configuración de la conexión a la base de datos.

**C#**

{{< highlight csharp >}}

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



Aquí hay algunas propiedades más importantes expuestas por la clase {Aspose.Cells.ExternalConnections.ExternalConnection}.

|**Nombre de la Propiedad**|**Descripción**|
| :- | :- |
|ActualizarFondo|Indica si la conexión puede ser actualizada en segundo plano (asincrónicamente). <br>verdadero si el uso preferido de la conexión es actualizar asincrónicamente en segundo plano; <br>falso si el uso preferido de la conexión es actualizar sincrónicamente en primer plano.|
|DescripciónDeConexión|Especifica la descripción de usuario para esta conexión|
|IdDeConexión|Especifica el identificador único de esta conexión.|
|Credenciales|Especifica el método de autenticación a utilizar al establecer (o restablecer) la conexión.|
|HaSidoBorrado|Indica si la conexión del libro asociado ha sido eliminada. verdadero si la <br>conexión ha sido eliminada; de lo contrario, falso.|
|EsNuevo|Verdadero si la conexión no ha sido actualizada por primera vez; de lo contrario, falso. Este <br>estado puede ocurrir cuando el usuario guarda el archivo antes de que una consulta haya terminado de devolver resultados.|
|MantenerVivo|Verdadero cuando la aplicación de hojas de cálculo debe hacer esfuerzos para mantener la conexión <br>abierta. Cuando es falso, la aplicación debe cerrar la conexión después de recuperar la <br>información.|
|Nombre|Especifica el nombre de la conexión. Cada conexión debe tener un nombre único.|
|ArchivoOdc|Especifica la ruta completa al archivo de conexión externo desde el cual se creó esta conexión <br>Si una conexión falla durante un intento de actualizar datos y reconnectionMethod=1, <br>entonces la aplicación de hojas de cálculo intentará nuevamente usando información del archivo de conexión externo <br>en lugar del objeto de conexión incrustado en el libro de trabajo.|
|SoloUsarArchivoDeConexión|Indica si la aplicación de hojas de cálculo siempre y solo debe usar el <br>información de conexión en el archivo de conexión externo indicado por el atributo odcFile <br>cuando se actualice la conexión. Si es falso, entonces la aplicación de hojas de cálculo <br>debe seguir el procedimiento indicado por el atributo reconnectionMethod|
|Parámetros|Obtiene ConnectionParameterCollection para una consulta ODBC o web.|
|MétodoDeReconexión|Especificar el tipo de método de reconexión|
|RefreshInternal|Especifica el número de minutos entre las actualizaciones automáticas de la conexión.|
|ActualizarAlCargar|Verdadero si esta conexión debe ser actualizada al abrir el archivo; de lo contrario, falso.|
|GuardarDatos|Verdadero si los datos externos obtenidos a través de la conexión para poblar una tabla deben ser guardados<br>con el libro; de lo contrario, falso.|
|GuardarContraseña|Verdadero si la contraseña debe ser guardada como parte de la cadena de conexión; de lo contrario, Falso.|
|ArchivoFuente|Utilizado cuando la fuente de datos externa es basada en archivo. Cuando una conexión a tal fuente de datos <br>falla, la aplicación de hojas de cálculo intenta conectarse directamente a este archivo. Puede estar <br>expresado en URI o notación de ruta de archivo específica del sistema.|
|SSOId|Identificador para Inicio de Sesión Único (SSO) utilizado para autenticación entre un servidor intermedio de hojas de cálculoML y la fuente de datos externa.|
|Tipo|Especifica el tipo de fuente de datos.|

### **Capacidad para formatear una subcadena del texto de las etiquetas de datos**
Aspose.Cells for .NET 8.4.1 ha expuesto el método DataLabels.Characters para recuperar una instancia de la clase FontSetting que corresponde a la subcadena de un ChartPoints.DataLabels. A su vez, la instancia de la clase FontSetting se puede utilizar para formatear la subcadena de DataLabels con diferentes configuraciones de fuente y color.

El siguiente fragmento de código muestra cómo utilizar el método DataLabels.Characters.

**C#**

{{< highlight csharp >}}

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


### **Capacidad para establecer las dimensiones de imagen deseadas para la exportación de hojas de cálculo y gráficos**
Aspose.Cells for .NET 8.4.1 ha expuesto el método ImageOrPrintOptions.SetDesiredSize para establecer las dimensiones de la imagen resultante al exportar hojas de cálculo y gráficos a imágenes. El método ImageOrPrintOptions.SetDesiredSize acepta dos parámetros de tipo entero, donde el primero es el ancho deseado y el segundo es la altura deseada.

El siguiente fragmento de código muestra cómo establecer las dimensiones deseadas al exportar una hoja de cálculo a PNG.

**C#**

{{< highlight csharp >}}

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

La misma propiedad también se puede usar para convertir gráficos en imágenes.

{{% /alert %}} 


### **Renderización de comentarios a PDF**
Con el lanzamiento de la v8.4.1, la API de Aspose.Cells ha proporcionado la propiedad PageSetup.PrintComments y la enumeración PrintCommentsType para facilitar la renderización de comentarios al convertir hojas de cálculo al formato PDF. La enumeración PrintCommentsType tiene los siguientes constantes.

- PrintCommentsType.PrintNoComments: Los comentarios no deben ser renderizados.
- PrintCommentsType.PrintInPlace: Los comentarios deben ser renderizados donde estén ubicados.
- PrintCommentsType.PrintSheetEnd: Los comentarios deben ser renderizados al final de la hoja de cálculo.

El siguiente código de muestra demuestra el uso de la propiedad PageSetup.PrintComments para mostrar los comentarios utilizando todos los valores de enumeración PrintCommentsType.

**C#**

{{< highlight csharp >}}

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


### **Mover hojas de cálculo en Aspose.Cells.GridDesktop**
Aspose.Cells.GridDesktop proporciona el método WorksheetCollection.MoveTo, que se puede usar para mover una hoja de cálculo al índice especificado. El método anterior toma como parámetros los índices (basados en cero) de la hoja de cálculo de origen y la hoja de cálculo de destino.

El siguiente código de ejemplo demuestra el uso de la propiedad WorksheetCollection.MoveTo.

**C#**

{{< highlight csharp >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **Propiedad Workbook.IsLicensed añadida**
Aspose.Cells for .NET 8.4.1 ha expuesto el Workbook.IsLicensed que podría ser de gran ayuda para determinar si la licencia se ha cargado con éxito o no. Si accede a esta propiedad antes de establecer la licencia, devolverá falso y viceversa, sin embargo, la licencia debería ser válida.

El siguiente código de ejemplo demuestra el uso de la propiedad Workbook.IsLicensed.

**C#**

{{< highlight csharp >}}

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
Aspose.Cells for .NET 8.4.1 ha expuesto la propiedad SVGFitToViewPort para la clase ImageOrPrintOptions que se puede usar para activar el atributo viewBox para el formato de archivo SVG al exportar hojas de cálculo o gráficos al formato SVG. El valor predeterminado de esta propiedad es falso, por lo tanto, el XML base para el archivo SVG generado sin configurar la propiedad mencionada no incluirá el atributo viewBox.

El siguiente código de muestra demuestra el uso de la propiedad ImageOrPrintOptions.SVGFitToViewPort.

**C#**

{{< highlight csharp >}}

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
## **APIs obsoletas**
### **Método Workbook.ValidateFormula obsoleto**
Utilice el método Cell.Formula para validar la fórmula.
{{< app/cells/assistant language="csharp" >}}
