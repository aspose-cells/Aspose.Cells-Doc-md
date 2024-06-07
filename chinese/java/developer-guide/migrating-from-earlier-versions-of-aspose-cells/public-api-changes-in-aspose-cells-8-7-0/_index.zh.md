---
title: Aspose.Cells 8.7.0中的公共API更改
type: docs
weight: 240
url: /zh/java/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

本文档描述了从8.6.3版本到8.7.0版本的Aspose.Cells API的更改，可能会对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等内容，还描述了Aspose.Cells背景工作中的任何更改。

{{% /alert %}} 
## **已添加API**
### **支持PDF优化**
Aspose.Cells API已经提供了将电子表格转换为PDF的功能。通过此API的这个版本，用户现在还可以[优化结果PDF的大小](/cells/zh/java/save-excel-into-pdf-with-standard-or-minimum-size/)。Aspose.Cells for Java 8.7.0已经公开了PdfSaveOptions.OptimizationType属性以及PdfOptimizationType枚举，以便用户在将电子表格导出为PDF格式时选择所需的优化算法。PdfSaveOptions.OptimizationType属性有两个可能的值，如下所述。 

1. PdfOptimizationType.MINIMUM_SIZE: 为结果文件大小而牺牲质量。
1. PdfOptimizationType.STANDARD: 质量不牺牲，因此结果文件大小会很大。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

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
### **检测数字签名的VBA项目**
新公开的VbaProject.isSigned属性可用于[检测工作簿中的VBA项目是否已数字签名](/cells/zh/java/check-if-vba-code-is-signed/)。VbaProject.isSigned属性的类型为Boolean，如果VBA项目已数字签名，则返回true。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

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
### **已添加 Protection.verifyPassword 方法**
Aspose.Cells API通过引入verifyPassword方法增强了Protection类，允许指定一个String类型的密码，并[验证是否已使用相同的密码保护工作表](/cells/zh/java/verify-password-used-to-protect-the-worksheet/)。Protection.verifyPassword方法如果指定的密码与用于保护给定工作表的密码匹配，则返回true，否则返回false。以下代码片段使用Protection.verifyPassword方法结合Protection.isProtectedWithPassword字段来检测密码保护，并验证密码。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

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
### **已添加 Protection.isProtectedWithPassword 属性**
Aspose.Cells for Java这个版本还公开了Protection.isProtectedWithPassword字段，可用于[检测工作表是否已受密码保护](/cells/zh/java/detect-if-worksheet-is-password-protected/)。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

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
### **已添加 ColorScale.Is3ColorScale 属性**
Aspose.Cells for Java 8.7.0已经公开了ColorScale.Is3ColorScale属性，该属性可用于[创建2色标度条件格式](/cells/zh/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/)。所述属性为Boolean类型，其默认值为true，这意味着条件格式默认为3-Color Scale。但是，将ColorScale.Is3ColorScale属性更改为false将生成2-Color Scale条件格式。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

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
### **已添加 TxtLoadOptions.HasFormula 属性**
Aspose.Cells for Java 8.7.0已经提供了对[在加载包含分隔普通数据的CSV/TXT文件时识别和解析公式](/cells/zh/java/load-or-import-csv-file-with-formulas/)的支持。新添加的TxtLoadOptions.HasFormula属性，当设置为true时，指导API从输入的分隔文件中解析公式并将其设置到相关单元格中，无需进行任何额外的处理。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

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
### **已添加 DataLabels.ResizeShapeToFitText 属性**
Aspose.Cells for Java 8.7.0公开了DataLabels.ResizeShapeToFitText属性，该属性可启用Excel应用程序中图表数据标签的[调整形状以适应文本](/cells/zh/java/resize-chart-s-data-label-shape-to-fit-text/)功能。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

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
## **已删除APIs**
### **已移除 Workbook.SaveOptions 属性**
Workbook.SaveOptions属性已经被宣布废弃一段时间了。但本次发布中已经从公共API中完全移除，因此建议使用Workbook.save(Stream, SaveOptions)或Workbook.save(string, SaveOptions)方法作为替代。
