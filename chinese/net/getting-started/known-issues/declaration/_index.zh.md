---
title: Web服务器上的权限信任
type: docs
weight: 30
url: /zh/net/declaration/
---

{{% alert color="primary" %}} 

一般来说，所有Aspose .NET组件都需要设置完全信任权限。原因是Aspose for .NET组件需要访问注册表设置、系统文件等，而不仅仅是虚拟目录，用于某些操作，比如解析字体等。此外，Aspose for .NET组件（包括Aspose.Cells for .NET）基于核心.NET系统类，这在许多情况下也需要设置完全信任权限。
<br/>
中等信任已在.NET Core和.NET 5+中移除。中等信任是.NET Framework时代的安全机制。中等信任逐渐被更灵活的安全策略取代。建议用户优先升级到.NET 5+并采用容器化部署，而非依赖传统的信任级别。

{{% /alert %}} 
## **部分信任/中等信任挑战**
多家公司托管的互联网服务提供商通常会强制执行中等信任安全级别。此外，有时候您需要在共享服务器上托管多个应用程序，例如在ISP等方案中，您必须使用中等信任级别来限制应用程序。ASP.NET中等信任级别提供了适合隔离托管在ISP服务器上多个应用程序的受限执行环境。对于.NET 2.0情况下，此类安全级别可能设置以下约束，可能会影响Aspose.Cells for .NET正常执行的能力，例如：

- **RegistryPermission 不可用**。这意味着您无法访问注册表，这在渲染电子表格或其他文档时需要枚举已安装的字体。
- **FileIOPermission is restricted**. 这意味着您只能访问应用程序虚拟目录层次结构中的文件。这可能意味着在导出过程中无法读取字体。
## **在中等信任权限设置下使用Aspose.Cells for .NET**
您可以遵循一些建议在中等信任级别或共享服务器环境下运行Aspose.Cells for .NET：

- 在代码中设置许可文件时，最好在获取许可文件流后再调用License.SetLicense(Stream)方法。
- 必须设置可以访问的字体目录。如果无法在服务器上访问文件，请将所需的字体文件添加到应用程序中。
- 在部分信任模式下，不支持Shape-to-EMF转换，因此将导出的图像类型（用于形状）设置为其他图像格式。

请参阅以下示例，演示了如何在中等信任模式下使用/运行Aspose.Cells for .NET。

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





{{< app/cells/assistant language="csharp" >}}
