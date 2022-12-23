---
title: 公共 API Aspose.Cells 8.7.0 的变化
type: docs
weight: 230
url: /zh/net/public-api-changes-in-aspose-cells-8-7-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.6.3 到 8.7.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持 VBA 项目数字签名、检测和提取**
此版本 Aspose.Cells for .NET 公开了一些新的属性和方法来帮助用户完成诸如对 VBA 项目进行数字签名、检测 VBA 项目是否已签名和有效等任务。此外，新的 API 允许从工作簿中的数字签名 VBA 项目中提取证书作为原始数据。
###### **对 VBA 项目进行数字签名**
Aspose.Cells for .NET 8.7.0公开了VbaProject.Sign方法，可用于[对工作簿中的 VBA 项目进行数字签名](/cells/zh/net/digitally-sign-a-vba-code-project-with-certificate/).所述方法接受驻留在 Aspose.Cells.DigitalSignatures 命名空间中的 DigitalSignature 类的实例。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Sign the VbaProject using the X509Certificate

vbaProject.Sign(new DigitalSignature(new System.Security.Cryptography.X509Certificates.X509Certificate2(cert), "Comments", DateTime.Now));

{{< /highlight >}}


###### **检测数字签名的 VBA 项目**
新公开的 VbaProject.IsSigned 属性可用于[检测工作簿中的 VBA 项目是否经过数字签名](/cells/zh/net/check-if-vba-code-is-signed/)VbaProject.IsSigned 属性属于布尔类型，如果 VBA 项目经过数字签名，则返回 true，反之亦然。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Check if VbaProject is digitally signed

if (vbaProject.IsSigned)

{

    Console.WriteLine("VbaProject is digitally signed");

}

else

{

    Console.WriteLine("VbaProject is not digitally signed");

}

{{< /highlight >}}


###### **从 VBA 项目中提取数字签名**
API 的此修订版还公开了 VbaProject.CertRawData 属性，该属性允许[从 VBA 项目中提取数字证书的原始数据](/cells/zh/net/export-vba-certificate-to-file-or-stream/)VbaProject.CertRawData 属性是字节数组类型，如果 VBA 项目经过数字签名，它将包含原始证书数据，否则该属性将为空。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **验证 VBA 项目的数字签名**
公共 API 的另一个补充是 VbaProject.IsValidSigned 属性，它可能对[验证 VBA 项目的数字签名](/cells/zh/net/check-if-digital-signature-of-vba-code-is-valid/).如果数字签名有效，则该属性返回 true，如果签名无效，则返回 false。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Check if VbaProject is digitally signed

if (vbaProject.IsSigned)

{

    //Check if signature is valid

    if (vbaProject.IsValidSigned)

    {

        Console.WriteLine("VbaProject is digitally signed & signature is valid");

    }

}

{{< /highlight >}}


### **方法 Protection.VerifyPassword 添加**
Aspose.Cells for .NET 8.7.0暴露了Protection.VerifyPassword方法，可以用来[验证用于保护工作表的密码](/cells/zh/net/verify-password-used-to-protect-the-worksheet/).此方法接受字符串实例作为参数，如果指定的密码与用于保护工作表的密码匹配，则返回 true。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

var sheet = book.Worksheets[0];

//Access Protection module of desired Worksheet

var protection = sheet.Protection;

//Verify the password for Worksheet

if (protection.VerifyPassword(password))

{

    Console.WriteLine("Password has matched");

}

else

{

    Console.WriteLine("Password did not match");

}

{{< /highlight >}}


### **属性保护.IsProtectedWithPassword 添加**
此版本 Aspose.Cells for .NET API 还公开了 Protection.IsProtectedWithPassword 属性，可用于[检测工作表是否受密码保护](/cells/zh/net/detect-if-worksheet-is-password-protected/).

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

var sheet = book.Worksheets[0];

//Access Protection module of desired Worksheet

var protection = sheet.Protection;

//Check if Worksheet is password protected

if (protection.IsProtectedWithPassword)

{

    Console.WriteLine("Worksheet is password protected");

}

else

{

    Console.WriteLine("Worksheet is not password protected");

}

{{< /highlight >}}


### **属性 ColorScale.Is3ColorScale 添加**
Aspose.Cells for .NET 8.7.0 公开了可用于创建 2 色阶条件格式的 ColorScale.Is3ColorScale 属性。所述属性为布尔类型，默认值为 true，这意味着条件格式默认为 3-Color Scale。但是，将 ColorScale.Is3ColorScale 属性切换为 false 将[生成 2-Color Scale 条件格式](/cells/zh/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/).

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the Worksheet to which conditional formatting rule has to be added

var sheet = book.Worksheets[0];

//Add FormatConditions to the collection

int index = sheet.ConditionalFormattings.Add();

//Access newly added formatConditionCollection via its index

var formatConditionCollection = sheet.ConditionalFormattings[index];

//Create a CellArea on which conditional formatting rule will be applied

var cellArea = CellArea.CreateCellArea("A1", "A5");

//Add conditional formatted cell range

formatConditionCollection.AddArea(cellArea);

//Add format condition of type ColorScale

index = formatConditionCollection.AddCondition(FormatConditionType.ColorScale);

//Access newly added format condition via its index

var formatCondition = formatConditionCollection[index];

//Set Is3ColorScale to false in order to generate a 2-Color Scale format

formatCondition.ColorScale.Is3ColorScale = false;

//Set other necessary properties

{{< /highlight >}}


### **添加了属性 TxtLoadOptions.HasFormula**
 Aspose.Cells for .NET 8.7.0 已经支持[在加载具有分隔纯数据的 CSV/TXT 文件时识别和解析公式](/cells/zh/net/load-or-import-csv-file-with-formulas/).新公开的 TxtLoadOptions.HasFormula 属性在设置为 true 时指示 API 从输入分隔文件中解析公式并将它们设置到相关单元格，而无需任何额外处理。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of TxtLoadOptions

var options = new TxtLoadOptions();

//Set HasFormula property to true

options.HasFormula = true;

//Set the Separator property as desired

options.Separator = ',';

//Load the CSV/TXT file using the instance of TxtLoadOptions

var book = new Workbook(inFilePath, options);

//Calculate formulas in order to get the calculated values of formula in CSV

book.CalculateFormula();

//Write result in any of the supported formats

book.Save(outFilePath);

{{< /highlight >}}


### **已添加属性 DataLabels.IsResizeShapeToFitText**
 Aspose.Cells for .NET 8.7.0 公开的另一个有用的功能是 DataLabels.IsResizeShapeToFitText 属性，它可以启用[调整形状以适合文本](/cells/zh/net/resize-chart-s-data-label-shape-to-fit-text/)图表数据标签的 Excel 应用程序功能。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook containing the Chart

var book = new Workbook(inFilePath);

//Access the Worksheet that contains the Chart

var sheet = book.Worksheets[0];

//Access the desired Chart via its index or name

var chart = sheet.Charts[0];

//Access the DataLabels of desired NSeries

var labels = chart.NSeries[0].DataLabels;

//Set ResizeShapeToFitText property to true

labels.IsResizeShapeToFitText = true;

//Calculate Chart

chart.Calculate();

{{< /highlight >}}


### **已添加属性 PdfSaveOptions.OptimizationType**
Aspose.Cells for .NET 8.7.0 公开了 PdfSaveOptions.OptimizationType 属性以及 PdfOptimizationType 枚举，以方便用户[在将电子表格导出为 PDF 格式时选择所需的优化算法](/cells/zh/net/save-excel-into-pdf-with-standard-or-minimum-size/)PdfSaveOptions.OptimizationType 属性有 2 个可能的值，如下所述。

1. PdfOptimizationType.MinimumSize：质量因生成的文件大小而受到影响。
1. PdfOptimizationType.Standard：质量不会受到影响，因此生成的文件会很大。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of PdfSaveOptions

var pdfSaveOptions = new PdfSaveOptions();

//Set the OptimizationType property to desired value

pdfSaveOptions.OptimizationType = PdfOptimizationType.MinimumSize;

//Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook(inFilePath);

//Save the spreadsheet in PDF format while passing the instance of PdfSaveOptions

book.Save(outFilePath, pdfSaveOptions);

{{< /highlight >}}
## **删除的 API**
### **属性 Workbook.SaveOptions 已删除**
Workbook.SaveOptions 属性在一段时间前被标记为已废弃。在此版本中，它已从公共 API 中完全删除，因此建议使用 Workbook.Save(Stream, SaveOptions) 或 Workbook.Save(string, SaveOptions) 方法作为替代方法。
