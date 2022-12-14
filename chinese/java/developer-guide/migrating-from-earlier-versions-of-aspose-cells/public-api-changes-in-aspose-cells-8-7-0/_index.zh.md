---
title: 公共 API Aspose.Cells 8.7.0 的变化
type: docs
weight: 240
url: /zh/java/public-api-changes-in-aspose-cells-8-7-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.6.3 到 8.7.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持 PDF 优化**
Aspose.Cells API 已经提供了将电子表格转换为 PDF 的功能。有了这个 API 版本，用户现在可以[优化生成的 PDF 大小](/cells/zh/java/save-excel-into-pdf-with-standard-or-minimum-size/)以及。 Aspose.Cells for Java 8.7.0 公开了 PdfSaveOptions.OptimizationType 属性以及 PdfOptimizationType 枚举，以方便用户在将电子表格导出为 PDF 格式时选择所需的优化算法。 PdfSaveOptions.OptimizationType 属性有 2 个可能的值，如下所述。

1. PdfOptimizationType.MINIMUM_SIZE：质量因生成的文件大小而受到影响。
1. PdfOptimizationType.STANDARD：质量不会受到影响，因此生成的文件会很大。

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of PdfSaveOptions

PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();

//Set the OptimizationType property to desired value

pdfSaveOptions.setOptimizationType(PdfOptimizationType.MINIMUM_SIZE);

//Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Save the spreadsheet in PDF format while passing the instance of PdfSaveOptions

book.save(outFilePath, pdfSaveOptions);

{{< /highlight >}}
### **检测数字签名的 VBA 项目**
新公开的 VbaProject.isSigned 属性可用于[检测工作簿中的 VBA 项目是否经过数字签名](/cells/zh/java/check-if-vba-code-is-signed/)VbaProject.isSigned 属性属于布尔类型，如果 VBA 项目经过数字签名，则返回 true，反之亦然。

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

VbaProject vbaProject = book.getVbaProject();

//Check if VbaProject is digitally signed

if (vbaProject.isSigned())

{

	System.out.println("VbaProject is digitally signed");

}

else

{

	System.out.println("VbaProject is not digitally signed");

}

{{< /highlight >}}
### **方法 Protection.verifyPassword 添加**
Aspose.Cells API 通过引入 verifyPassword 方法增强了保护类，该方法允许将密码指定为 String 的实例，并且[验证是否使用了相同的密码来保护工作表](/cells/zh/java/verify-password-used-to-protect-the-worksheet/).如果指定的密码与用于保护给定工作表的密码匹配，则 Protection.verifyPassword 方法返回 true，如果指定的密码不匹配，则返回 false。以下代码使用 Protection.verifyPassword 方法结合 Protection.isProtectedWithPassword 字段来检测密码保护，并验证密码。

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load a spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the protected Worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Check if Worksheet is password protected

if (sheet.getProtection().isProtectedWithPassword())

{

  //Verify the password used to protect the Worksheet

  if (sheet.getProtection().verifyPassword("password"))

  {

	  System.out.println("Specified password has matched");

  }

  else

  {

	  System.out.println("Specified password has not matched");

  }

}

{{< /highlight >}}
### **Property Protection.isProtectedWithPassword 添加**
此版本 Aspose.Cells for Java 还公开了 Protection.isProtectedWithPassword 字段，可用于[检测工作表是否受密码保护](/cells/zh/java/detect-if-worksheet-is-password-protected/).

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

Worksheet sheet = book.getWorksheets().get(0);

//Access Protection module of desired Worksheet

Protection protection = sheet.getProtection();

//Check if Worksheet is password protected

if (protection.isProtectedWithPassword())

{

	System.out.println("Worksheet is password protected");

}

else

{

	System.out.println("Worksheet is not password protected");

}

{{< /highlight >}}
### **属性 ColorScale.Is3ColorScale 添加**
Aspose.Cells for Java 8.7.0暴露了ColorScale.Is3ColorScale属性，可用于[创建 2-Color Scale 条件格式](/cells/zh/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/).所述属性为布尔类型，默认值为 true，这意味着条件格式默认为 3-Color Scale。但是，将 ColorScale.Is3ColorScale 属性切换为 false 将生成 2-Color Scale 条件格式。

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access the Worksheet to which conditional formatting rule has to be added

Worksheet sheet = book.getWorksheets().get(0);

//Add FormatConditions to the collection

int index = sheet.getConditionalFormattings().add();

//Access newly added formatConditionCollection via its index

FormatConditionCollection formatConditionCollection = sheet.getConditionalFormattings().get(index);

//Create a CellArea on which conditional formatting rule will be applied

CellArea cellArea = CellArea.createCellArea("A1", "A5");

//Add conditional formatted cell range

formatConditionCollection.addArea(cellArea);

//Add format condition of type ColorScale

index = formatConditionCollection.addCondition(FormatConditionType.COLOR_SCALE);

//Access newly added format condition via its index

FormatCondition formatCondition = formatConditionCollection.get(index);

//Set Is3ColorScale to false in order to generate a 2-Color Scale format

formatCondition.getColorScale().setIs3ColorScale(false);

//Set other necessary properties

{{< /highlight >}}
### **添加了属性 TxtLoadOptions.HasFormula**
 Aspose.Cells for Java 8.7.0 已经支持[在加载具有定界纯数据的 CSV/TXT 文件时识别和解析公式](/cells/zh/java/load-or-import-csv-file-with-formulas/).新公开的 TxtLoadOptions.HasFormula 属性在设置为 true 时指示 API 从输入分隔文件中解析公式并将它们设置到相关单元格，而无需任何额外处理。

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of TxtLoadOptions

TxtLoadOptions options = new TxtLoadOptions();

//Set HasFormula property to true

options.setHasFormula(true);

//Set the Separator property as desired

options.setSeparator(',');

//Load the CSV/TXT file using the instance of TxtLoadOptions

Workbook book = new Workbook(inFilePath, options);

//Calculate formulas in order to get the calculated values of formula in CSV

book.calculateFormula();

//Write result in any of the supported formats

book.save(outFilePath);

{{< /highlight >}}
### **已添加属性 DataLabels.ResizeShapeToFitText**
 Aspose.Cells for Java 8.7.0 公开的另一个有用的功能是 DataLabels.ResizeShapeToFitText 属性，它可以启用[调整形状以适合文本](/cells/zh/java/resize-chart-s-data-label-shape-to-fit-text/)图表数据标签的 Excel 应用程序功能。

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook containing the Chart

Workbook book = new Workbook(inFilePath);

//Access the Worksheet that contains the Chart

Worksheet sheet = book.getWorksheets().get(0);

//Access the desired Chart via its index or name

Chart chart = sheet.getCharts().get(0);

//Access the DataLabels of desired NSeries

DataLabels labels = chart.getNSeries().get(0).getDataLabels();

//Set ResizeShapeToFitText property to true

labels.setResizeShapeToFitText(true);

//Calculate Chart

chart.calculate();

{{< /highlight >}}
## **删除的 API**
### **属性 Workbook.SaveOptions 已删除**
Workbook.SaveOptions 属性在一段时间前被标记为已废弃。在此版本中，它已从公共 API 中完全删除，因此建议使用 Workbook.save(Stream, SaveOptions) 或 Workbook.save(string, SaveOptions) 方法作为替代方法。
