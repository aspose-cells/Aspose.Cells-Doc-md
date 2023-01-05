---
title: 宣言
type: docs
weight: 30
url: /zh/net/declaration/
---
{{% alert color="primary" %}} 

通常，所有 Aspose .NET 组件都需要 Full Trust 权限集。原因是 Aspose for .NET 组件需要访问注册表设置，系统文件而不是虚拟目录以进行某些操作，如解析字体等。此外， Aspose for .NET 组件（包括 Aspose.Cells for .NET）基于核心 .NET 系统类，也需要 Full Trust 权限在许多情况下设置。

{{% /alert %}} 
## **部分信任/中度信任挑战**
托管来自不同公司的多个应用程序的 Internet 服务提供商大多强制实施中等信任安全级别。而且，有时你需要在一个共享服务器上托管多个应用程序，比如在 ISP 或其他场景中，你必须使用 Medium 信任级别来约束应用程序。 ASP.NET 中等信任级别提供了一个受限的执行环境，适用于隔离 ISP 服务器上托管的多个应用程序。在 .NET 2.0 的情况下，这样的安全级别可能会设置以下限制，这些限制可能会影响 Aspose.Cells for .NET 正常执行的能力，例如：

- **RegistryPermission 不可用**.这意味着您无法访问注册表，而注册表需要在呈现电子表格或其他文档时枚举已安装的字体。
- **文件 IO 权限受限**.这意味着您只能访问应用程序虚拟目录层次结构中的文件。这可能意味着在导出期间无法读取字体。
## **在中等信任权限集上使用 Aspose.Cells for .NET**
您可以按照一些建议在中等信任级别或共享服务器环境中运行 Aspose.Cells for .NET：

- 要在您的代码中设置许可文件，最好在将许可文件获取到流后调用 License.SetLicense(Stream) 方法。
- 必须设置字体的目录（可以在许可的情况下访问）。如果无法访问服务器上的文件，请将所需的字体文件添加到您的应用程序中。
- 在部分信任模式下，不支持 Shape-to-EMF 转换，因此将导出的图像类型（对于形状）设置为其他图像格式。

请参阅以下示例，该示例演示了如何在中等信任模式下使用/运行 Aspose.Cells for .NET。

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





