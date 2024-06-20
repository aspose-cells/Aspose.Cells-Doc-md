---
title: Declaración
type: docs
weight: 30
url: /es/net/declaration/
---

{{% alert color="primary" %}} 

Generalmente, todos los componentes .NET de Aspose requieren permisos de Full Trust. La razón es que los componentes de Aspose para .NET necesitan acceder a la configuración del registro, archivos del sistema que no sean directorios virtuales para ciertas operaciones como el análisis de fuentes, etc. Además, los componentes de Aspose para .NET (incluido Aspose.Cells for .NET) están basados en clases del sistema principal de .NET que también requieren permisos de Full Trust en muchos casos

{{% /alert %}} 
## **Desafío de confianza parcial/confianza media**
Los proveedores de servicios de Internet que alojan múltiples aplicaciones de diferentes empresas en su mayoría imponen un nivel de seguridad de Confianza Media. Además, a veces es necesario alojar múltiples aplicaciones en un servidor compartido, como en un ISP u otros escenarios, es necesario usar el nivel de confianza Media para restringir las aplicaciones. El nivel de confianza Media de ASP.NET proporciona un entorno de ejecución restringido que es adecuado para aislar múltiples aplicaciones alojadas en servidores de ISP. En el caso de .NET 2.0, este nivel de seguridad puede establecer las siguientes restricciones que podrían afectar la capacidad de Aspose.Cells for .NET para funcionar correctamente, por ejemplo:

- **PermissionRegistry no está disponible**. Esto significa que no se puede acceder al registro, que es necesario para enumerar las fuentes instaladas al renderizar hojas de cálculo u otros documentos
- **Se restringe el permiso de FileIOPermission**. Esto significa que solo se puede acceder a archivos en la jerarquía de directorios virtuales de su aplicación. Esto posiblemente significa que no se pueden leer fuentes durante la exportación
## **Usar Aspose.Cells for .NET en un conjunto de permisos de Confianza Media**
Puede seguir algunas recomendaciones para ejecutar Aspose.Cells for .NET en el nivel de confianza Media o en un entorno de servidor compartido:

- Para establecer un archivo de licencia en su código, es mejor que llame al método License.SetLicense(Stream) después de obtener el archivo de licencia en flujos
- Se debe establecer el directorio de fuentes (al cual se puede acceder con permiso). Si no hay forma de acceder al archivo en el servidor, agregue los archivos de fuentes necesarios a su aplicación
- En modo de confianza parcial, la conversión de Shape a EMF no es compatible, por lo que establezca el tipo de imagen exportada (para shapes) en otros formatos de imagen.

Vea el siguiente ejemplo que demuestra cómo usar/ejecutar Aspose.Cells for .NET en modo de confianza medio.

{{< highlight csharp >}}

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





