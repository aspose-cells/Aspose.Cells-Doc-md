---
title: 声明
type: docs
weight: 30
url: /zh/net/declaration/
---

{{% alert color="primary" %}} 

通常，所有Aspose .NET组件都需要设置完全信任权限。原因是Aspose for .NET组件需要访问注册表设置，系统文件以及虚拟目录之外的其他文件进行某些操作（例如解析字体等）。此外，Aspose for .NET组件（包括Aspose.Cells for .NET）基于核心的.NET系统类，在许多情况下也需要设置完全信任权限。

{{% /alert %}} 
## **部分信任/中等信任挑战**
大多数互联网服务提供商从不同公司托管的多个应用程序中施加中等信任安全级别。此外，有时您需要在共享服务器上托管多个应用程序，例如在ISP或其他场景中，您必须使用中等信任级别来约束应用程序。ASP.NET中的中等信任级别提供了适合于隔离托管在ISP服务器上的多个应用程序的受限制的执行环境。在.NET 2.0的情况下，这种安全级别可能设置以下约束，这可能会影响Aspose.Cells for .NET正常运行的能力，例如:

- **RegistryPermission不可用**。这意味着您无法访问注册表，这在呈现电子表格或其他文档时需要列举安装的字体。
- **FileIOPermission受限**。这意味着您只能访问应用程序的虚拟目录层次结构中的文件。这可能意味着在导出时无法读取字体。
## **在中等信任权限集上使用Aspose.Cells for .NET**
您可以遵循一些建议，在中等信任级别或共享服务器环境中运行Aspose.Cells for .NET:

- 在代码中设置许可文件时，最好在将许可文件获取到流后调用License.SetLicense(Stream)方法。
- 必须设置字体的目录（可以使用权限访问）。如果无法在服务器上访问文件，请将所需的字体文件添加到应用程序中。
- 在部分信任模式下，不支持形状转EMF转换，因此将导出的图像类型（用于形状）设置为其他图像格式。

查看以下示例，演示如何在中等信任模式下使用/运行Aspose.Cells for .NET。

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





