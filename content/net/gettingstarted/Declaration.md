+++
title = "Declaration" 
description = "" 
weight = 8005 
+++

Aspose.Cells for .NET : Declaration  

# Aspose.Cells for .NET : Declaration



Generally, all Aspose .NET components require Full Trust permissions set. The reason is that Aspose for .NET components need to access registry settings, system files other than virtual directory for certain operations like parsing fonts etc. Moreover, Aspose for .NET components (including Aspose.Cells for .NET) are based on core .NET system classes that also require Full Trust permissions set in many cases.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Partial Trust / Medium Trust Challenge](#Declaration-PartialTrust/MediumTrustChallenge)
*   2 [Use Aspose.Cells for .NET on Medium Trust Permissions Set](#Declaration-UseAspose.Cellsfor.NETonMediumTrustPermissionsSet)
{{< /panel >}}
 

 

## Partial Trust / Medium Trust Challenge

Internet Service Providers hosting multiple applications from different companies mostly enforce a Medium Trust security level. Moreover, sometimes you need to host multiple applications on a shared server, such as in an ISP or other scenarios, you have to use the Medium trust level to constrain the applications. The ASP.NET Medium trust level provides a constrained execution environment that is suitable for isolating multiple applications hosted on ISP servers. In case of .NET 2.0, such a security level may set the following constraints which could affect the ability of Aspose.Cells for .NET to perform properly, for example:

*   **RegistryPermission is not available**. This means you cannot access the registry, which is required to enumerate installed fonts when rendering spreadsheets or other documents.
*   **FileIOPermission is restricted**. This means you can only access files in your application's virtual directory hierarchy. This potentially means fonts cannot be read during export.

## Use Aspose.Cells for .NET on Medium Trust Permissions Set

You may follow some recommendations to run Aspose.Cells for .NET on Medium Trust level or shared server environment:

*   To set license file in your code, it's better you should call the `License.SetLicense(Stream)` method instead after obtaining the license file into streams.
*   The fonts' directory (which could be accessed with permission) must be set. If there is no way to access the file on the server, please add the needed font files to your application.
*   In partial trust mode, Shape-to-EMF conversion is not supported, so set the exported image type (for shapes) to another image formats.

See the following example that demonstrates on how to use/run Aspose.Cells for .NET in Medium Trust mode.

{{< code lang="cs" >}}
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
 
{{< /code >}}

  
  

