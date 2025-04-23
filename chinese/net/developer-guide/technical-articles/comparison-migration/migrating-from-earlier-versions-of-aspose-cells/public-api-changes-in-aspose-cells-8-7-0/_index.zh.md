---
title: Aspose.Cells 8.7.0中的公共API更改
type: docs
weight: 230
url: /zh/net/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.6.3到8.7.0的Aspose.Cells API的更改，这可能会对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，增加和删除的类等，还包括Aspose.Cells背后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持 VBA 项目数字签名、检测和提取**
该Aspose.Cells for .NET版本已公开了一些新属性和方法，在任务如数字签名VBA项目、检测VBA项目是否已签名和有效方面为用户提供了帮助。此外，新API允许从Workbook中的数字签名VBA项目中提取证书作为原始数据。
###### **数字签名 VBA 项目**
Aspose.Cells for .NET 8.7.0已公开了VbaProject.Sign方法，该方法可用于[数字签名Workbook中的VBA项目](/cells/zh/net/digitally-sign-a-vba-code-project-with-certificate/)。该方法接受在Aspose.Cells.DigitalSignatures命名空间中的DigitalSignature类的实例。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Sign the VbaProject using the X509Certificate

vbaProject.Sign(new DigitalSignature(new System.Security.Cryptography.X509Certificates.X509Certificate2(cert), "Comments", DateTime.Now));

{{< /highlight >}}


###### **检测数字签名的VBA项目**
新公开的 VbaProject.IsSigned 属性可用于[检查工作簿中的 VBA 项目是否已数字签名](/cells/zh/net/check-if-vba-code-is-signed/)。VbaProject.IsSigned 属性是布尔类型，如果 VBA 项目已数字签名，则返回 true，反之返回 false。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

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
此版本的 API 还公开了 VbaProject.CertRawData 属性，允许[从 VBA 项目中提取数字证书的原始数据](/cells/zh/net/export-vba-certificate-to-file-or-stream/)。VbaProject.CertRawData 属性是字节数组类型，如果 VBA 项目已数字签名，该属性将包含原始证书数据，否则该属性将为 null。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **验证 VBA 项目的数字签名**
公共 API 的另一个新增内容是 VbaProject.IsValidSigned 属性，可用于[验证 VBA 项目的数字签名是否有效](/cells/zh/net/check-if-digital-signature-of-vba-code-is-valid/)。该属性在数字签名有效时返回 true，在无效时返回 false。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

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


### **新增 Protection.VerifyPassword 方法**
Aspose.Cells for .NET 8.7.0已公开了Protection.VerifyPassword方法，该方法可用于[验证用于保护工作表的密码](/cells/zh/net/verify-password-used-to-protect-the-worksheet/)。此方法接受一个字符串实例用作参数，并且如果指定密码与用于保护工作表的密码匹配则返回true。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

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


### **新增 Protection.IsProtectedWithPassword 属性**
该Aspose.Cells for .NET版本还公开了Protection.IsProtectedWithPassword属性，有助于[检测工作表是否已受密码保护](/cells/zh/net/detect-if-worksheet-is-password-protected/)。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

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


### **添加了 ColorScale.Is3ColorScale 属性**
Aspose.Cells for .NET 8.7.0已公开了ColorScale.Is3ColorScale属性，可用于创建2-Color Scale条件格式。该属性是布尔值，默认值为true，这意味着默认情况下条件格式将是3-Color Scale。但是，将ColorScale.Is3ColorScale属性切换为false将[生成2-Color Scale条件格式](/cells/zh/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

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


### **添加了 TxtLoadOptions.HasFormula 属性**
Aspose.Cells for .NET 8.7.0已支持[识别及解析加载包含分隔纯数据的CSV/TXT文件中的公式](/cells/zh/net/load-or-import-csv-file-with-formulas/)。新公开的TxtLoadOptions.HasFormula属性，如果设置为true，则指导API从输入的分隔文件中解析公式并将其设置到相关的单元格，而无需任何额外的处理。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

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


### **新增 DataLabels.IsResizeShapeToFitText 属性**
Aspose.Cells for .NET 8.7.0还公开了DataLabels.IsResizeShapeToFitText属性，可启用Excel应用程序图表数据标签的[自动调整形状以适应文本](/cells/zh/net/resize-chart-s-data-label-shape-to-fit-text/)功能。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

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


### **新增 PdfSaveOptions.OptimizationType 属性**
Aspose.Cells for .NET 8.7.0已公开了PdfSaveOptions.OptimizationType属性以及PdfOptimizationType枚举，以便用户在将电子表格导出为PDF格式时[选择所需的优化算法](/cells/zh/net/save-excel-into-pdf-with-standard-or-minimum-size/)。PdfSaveOptions.OptimizationType属性有两个可能的值，如下所述。

1. PdfOptimizationType.MinimumSize：结果文件大小牺牲质量。
1. PdfOptimizationType.Standard：结果文件大小不会牺牲质量。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

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
## **删除了 API**
### **属性 Workbook.SaveOptions 已移除**
Workbook.SaveOptions 属性在一段时间前已被标记为过时。此次发布中，它已从公共 API 中完全移除，因此建议使用 Workbook.Save(Stream, SaveOptions) 或 Workbook.Save(string, SaveOptions) 方法作为替代。
{{< app/cells/assistant language="csharp" >}}
