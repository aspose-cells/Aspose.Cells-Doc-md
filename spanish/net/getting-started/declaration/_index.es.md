---
title: Declaración
type: docs
weight: 30
url: /es/net/declaration/
---
{{% alert color="primary" %}} 

En general, todos los componentes Aspose .NET requieren el conjunto de permisos de plena confianza. La razón es que los componentes Aspose for .NET necesitan acceder a la configuración del registro, archivos del sistema que no sean directorios virtuales para ciertas operaciones como analizar fuentes, etc. Además, los componentes Aspose for .NET (incluidos Aspose.Cells for .NET) se basan en clases del sistema .NET centrales que también requieren permisos de plena confianza. fijado en muchos casos.

{{% /alert %}} 
## **Reto de confianza parcial/confianza media**
Los proveedores de servicios de Internet que alojan múltiples aplicaciones de diferentes compañías en su mayoría imponen un nivel de seguridad de confianza medio. Además, a veces necesita alojar varias aplicaciones en un servidor compartido, como en un ISP u otros escenarios, debe usar el nivel de confianza Medio para restringir las aplicaciones. El nivel de confianza medio ASP.NET proporciona un entorno de ejecución restringido que es adecuado para aislar varias aplicaciones alojadas en servidores ISP. En el caso de .NET 2.0, dicho nivel de seguridad puede establecer las siguientes restricciones que podrían afectar la capacidad de Aspose.Cells for .NET para funcionar correctamente, por ejemplo:

- **RegistryPermission no está disponible**. Esto significa que no puede acceder al registro, que es necesario para enumerar las fuentes instaladas al procesar hojas de cálculo u otros documentos.
- **FileIOPermission está restringido**Esto significa que solo puede acceder a archivos en la jerarquía de directorios virtuales de su aplicación. Esto significa potencialmente que las fuentes no se pueden leer durante la exportación.
## **Use Aspose.Cells for .NET en el conjunto de permisos de confianza media**
Puede seguir algunas recomendaciones para ejecutar Aspose.Cells for .NET en un nivel de confianza medio o en un entorno de servidor compartido:

- Para configurar el archivo de licencia en su código, es mejor llamar al método License.SetLicense(Stream) después de obtener el archivo de licencia en secuencias.
- Se debe configurar el directorio de fuentes (al que se puede acceder con permiso). Si no hay forma de acceder al archivo en el servidor, agregue los archivos de fuente necesarios a su aplicación.
- En el modo de confianza parcial, no se admite la conversión de forma a EMF, por lo tanto, establezca el tipo de imagen exportada (para formas) en otros formatos de imagen.

Consulte el siguiente ejemplo que demuestra cómo usar/ejecutar Aspose.Cells for .NET en el modo de confianza media.

{{< highlight "csharp" >}}

 // Instantiate the License object

Aspose.Cells.License lic = new Aspose.Cells.License();

// Get the license file into stream

System.IO.Stream stream = System.IO.File.OpenRead(MapPath("~") + @"\Aspose.Cells.lic");

// Set the License stream

lic.SetLicense(stream);

// Close the stream

stream.Close();

// Set the fonts directory

CellsHelper.FontDir = MapPath("~") + @"\Fonts";

//Open the template file

Workbook workbook = new Workbook(MapPath("~") + @"\test.xlsx");

PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();

// Set the image type to other format instead of using the default image type, that is, EMF

pdfSaveOptions.ImageType = System.Drawing.Imaging.ImageFormat.Png;

// Save the PDF file

workbook.Save(MapPath("~") + @"\dest.pdf", pdfSaveOptions);

// Save the XLSX file

workbook.Save(MapPath("~") + @"\dest.xlsx");



{{< /highlight >}}





