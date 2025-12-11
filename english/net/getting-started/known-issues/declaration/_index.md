---
title: Trust Permissions on Web Server
type: docs
weight: 30
url: /net/declaration/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Generally, all Aspose .NET components require Full Trust permissions set. The reason is that Aspose for .NET components need to access registry settings and system files other than the virtual directory for certain operations like parsing fonts, etc. Moreover, Aspose for .NET components (including Aspose.Cells for .NET) are based on core .NET system classes that also require Full Trust permissions set in many cases.  
<br/>
Medium Trust has been removed in .NET Core and .NET 5+. Medium Trust was the security mechanism in the era of .NET Framework. Medium Trust has gradually been replaced by more flexible security policies. We suggest that users prioritize upgrading to .NET 5+ and adopting containerized deployment instead of relying on traditional trust levels.

{{% /alert %}} 
## **Partial Trust / Medium Trust Challenge**
Internet Service Providers hosting multiple applications from different companies primarily enforce a Medium Trust security level. Moreover, sometimes you need to host multiple applications on a shared server, such as in an ISP or other scenarios, and you have to use the Medium Trust level to constrain the applications. The ASP.NET Medium Trust level provides a constrained execution environment that is suitable for isolating multiple applications hosted on ISP servers. In .NET 2.0, such a security level may impose the following constraints which could affect the ability of Aspose.Cells for .NET to perform properly, for example:

- **RegistryPermission is not available**. This means you cannot access the registry, which is required to enumerate installed fonts when rendering spreadsheets or other documents.
- **FileIOPermission is restricted**. This means you can only access files in your application's virtual directory hierarchy. This potentially means fonts cannot be read during export.

## **Use Aspose.Cells for .NET on Medium Trust Permissions Set**
You may follow some recommendations to run Aspose.Cells for .NET on a Medium Trust level or shared server environment:

- To set the license file in your code, it is better to call the `License.SetLicense(Stream)` method after obtaining the license file as a stream.  
- The fonts directory (which can be accessed with permission) must be set. If there is no way to access the file on the server, please add the needed font files to your application.  
- In partial trust mode, Shape‑to‑EMF conversion is not supported, so set the exported image type (for shapes) to another image format.

See the following example that demonstrates how to use/run Aspose.Cells for .NET in Medium Trust mode.

{{< highlight csharp >}}

 // Instantiate the License object
Aspose.Cells.License lic = new Aspose.Cells.License();

 // Get the license file into a stream
System.IO.Stream stream = System.IO.File.OpenRead(MapPath("~") + @"\Aspose.Cells.lic");

 // Set the License stream
lic.SetLicense(stream);

 // Close the stream
stream.Close();

 // Set the fonts directory
CellsHelper.FontDir = MapPath("~") + @"\Fonts";

 // Open the template file
Workbook workbook = new Workbook(MapPath("~") + @"\test.xlsx");

PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();

 // Set the image type to another format instead of the default EMF
pdfSaveOptions.ImageType = System.Drawing.Imaging.ImageFormat.Png;

 // Save the PDF file
workbook.Save(MapPath("~") + @"\dest.pdf", pdfSaveOptions);

 // Save the XLSX file
workbook.Save(MapPath("~") + @"\dest.xlsx");

{{< /highlight >}}

{{< app/cells/assistant language="csharp" >}}
