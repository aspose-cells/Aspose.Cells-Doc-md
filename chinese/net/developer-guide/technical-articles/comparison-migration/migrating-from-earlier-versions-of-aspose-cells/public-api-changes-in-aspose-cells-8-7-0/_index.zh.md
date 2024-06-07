---
title: Aspose.Cells 8.7.0中的公共API更改
type: docs
weight: 230
url: /zh/net/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

本文档描述了从8.6.3版本到8.7.0版本的Aspose.Cells API的更改，可能会对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等内容，还描述了Aspose.Cells背景工作中的任何更改。

{{% /alert %}} 
## **已添加API**
### **支持VBA项目数字签名、检测和提取**
此版本的Aspose.Cells for .NET已经暴露了一些新属性和方法，以帮助用户完成任务，比如数字签名VBA项目、检测VBA项目是否签名有效等。此外，新API还允许从数字签名的VBA项目中提取证书作为原始数据。
###### **数字签名VBA项目**
Aspose.Cells for .NET 8.7.0已公开了VbaProject.Sign方法，可用于[使用证书为工作簿中的VBA项目打数字签名](/cells/zh/net/digitally-sign-a-vba-code-project-with-certificate/)。该方法接受Aspose.Cells.DigitalSignatures命名空间中的DigitalSignature类的实例。

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
新公开的VbaProject.IsSigned属性可用于[检测工作簿中的VBA项目是否已数字签名](/cells/zh/net/check-if-vba-code-is-signed/)。VbaProject.IsSigned属性是布尔类型，如果VBA项目已数字签名则返回true，否则返回false。

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


###### **从VBA项目中提取数字证书**
API的这个修订还公开了VbaProject.CertRawData属性，允许从VBA项目中提取数字证书的原始数据[/cells/zh/net/export-vba-certificate-to-file-or-stream/]。VbaProject.CertRawData属性是字节数组类型，如果VBA项目已数字签名，则会包含原始证书数据，否则该属性将为null。

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


###### **验证VBA项目的数字签名**
公开的另一个API增加是VbaProject.IsValidSigned属性，可用于[验证VBA项目的数字签名是否有效](/cells/zh/net/check-if-digital-signature-of-vba-code-is-valid/)。该属性在数字签名有效时返回true，在签名无效时返回false。

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


### **添加Protection.VerifyPassword方法**
Aspose.Cells for .NET 8.7.0已公开了Protection.VerifyPassword方法，可用于[验证用于保护工作表的密码](/cells/zh/net/verify-password-used-to-protect-the-worksheet/)。该方法接受一个字符串实例作为参数，如果指定的密码与用于保护工作表的密码匹配，则返回true。

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


### **添加Protection.IsProtectedWithPassword属性**
这个Aspose.Cells for .NET API版本还公开了Protection.IsProtectedWithPassword属性，可用于[检测工作表是否受密码保护](/cells/zh/net/detect-if-worksheet-is-password-protected/)。

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


### **已添加 ColorScale.Is3ColorScale 属性**
Aspose.Cells for .NET 8.7.0已公开了ColorScale.Is3ColorScale属性，可用于创建2色比例条件格式。默认情况下，该属性的值是true，这意味着条件格式默认情况下将是3色比例。

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


### **已添加 TxtLoadOptions.HasFormula 属性**
Aspose.Cells for .NET 8.7.0已提供支持，用于[在加载包含分隔明文数据的CSV/TXT文件时识别和解析公式](/cells/zh/net/load-or-import-csv-file-with-formulas/)。新公开的TxtLoadOptions.HasFormula属性设置为true时，指示API从输入的分隔文件中解析公式，并将其设置到相关单元格，而无需任何额外的处理。

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


### **添加DataLabels.IsResizeShapeToFitText属性**
Aspose.Cells for .NET 8.7.0暴露了一个有用的功能，即DataLabels.IsResizeShapeToFitText属性，可以启用Excel应用程序的图表的数据标签的调整形状以适应文本功能。

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


### **添加PdfSaveOptions.OptimizationType属性**
Aspose.Cells for .NET 8.7.0已暴露了PdfSaveOptions.OptimizationType属性以及PdfOptimizationType枚举，以便用户可以选择将电子表格导出为PDF格式时所需的优化算法。

1. PdfOptimizationType.MinimumSize：质量会因为文件大小而受到影响。
1. PdfOptimizationType.Standard：质量不受损，结果文件大小将很大。

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
## **已删除APIs**
### **已删除Property Workbook.SaveOptions**
Workbook.SaveOptions属性在一段时间前被标记为过时。随着此版本的发布，它已从公共API中完全删除，因此建议使用Workbook.Save(Stream，SaveOptions)或Workbook.Save(string，SaveOptions)方法作为替代方法。
