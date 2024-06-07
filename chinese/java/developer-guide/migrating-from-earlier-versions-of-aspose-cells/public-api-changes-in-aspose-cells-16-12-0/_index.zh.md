---
title: Aspose.Cells 16.12.0中的公共API更改
type: docs
weight: 370
url: /zh/java/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本16.11.0到16.12.0的Aspose.Cells API的变化，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，添加和删除的类等，还描述了Aspose.Cells背后行为的任何更改。

{{% /alert %}} 
## **已添加API**
### **在加载时过滤对象**
Aspose.Cells 16.12.0已经公开了LoadFilter类以及LoadOptions.LoadFilter属性，可以一起控制在从模板文件初始化工作簿实例时要加载的数据类型。

以下是从模板文件中仅加载文档属性的简单使用场景。

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.DOCUMENT_PROPERTIES);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

以下片段从现有电子表格中加载所有内容，除了图表。

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.CHART);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

以下代码仅从现有电子表格中加载单元格数据（包括公式）和格式。

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.CELL_DATA);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}
### **添加了FileFormatType.OTS枚举。**
Aspose.Cells 16.12.0已向FileFormatType枚举中添加了OTS条目，用于检测OTS文件的格式。

以下片段利用了FileFormatType.OTS。

**Java**

{{< highlight csharp >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **添加了BuiltInDocumentPropertyCollection.ScaleCrop属性。**
Aspose.Cells 16.12.0已向BuiltInDocumentPropertyCollection类添加了ScaleCrop属性。ScaleCrop指示文档缩略图的显示模式。将此元素设置为true可根据显示缩放文档缩略图，而将其设置为false会裁剪文档缩略图以显示适合显示的部分。
### **添加了BuiltInDocumentPropertyCollection.LinksUpToDate属性。**
Aspose.Cells 16.12.0还为BuiltInDocumentPropertyCollection类公开了LinksUpToDate属性。LinksUpToDate属性指示文档中的超链接是否是最新的。 
### **添加了Workbook.exportXml方法**
Aspose.Cells 16.12.0已公开了Workbook.exportXml方法，允许将XML映射数据存储到指定文件路径。Workbook.exportXml方法接受2个参数，第一个参数应为string类型的XML映射名称，第二个参数应为文件路径位置，用于存储XML数据。
### **添加了WorksheetCollection.createRange方法**
Aspose.Cells 16.12.0添加了WorksheetCollection.createRange方法，允许基于地址（单元格区域参考）和工作表索引创建范围。

以下代码段利用WorksheetCollection.createRange方法在第一（默认）工作表中创建跨越A1至A2的单元格范围。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

{{< /highlight >}}
## **已废弃的API**
### **弃用的LoadOptions.LoadDataOptions属性**
请使用LoadOptions.LoadFilter属性作为替代。
### **弃用的LoadOptions.LoadDataFilterOptions属性**
请使用LoadOptions.LoadFilter属性作为替代。
### **弃用的LoadOptions.OnlyLoadDocumentProperties属性**
请使用LoadOptions.LoadFilter属性作为替代。
### **弃用的LoadOptions.LoadDataAndFormatting属性**
请使用LoadOptions.LoadFilter属性作为替代。

{{% alert color="primary" %}} 

上面已分享了所有弃用API的代码片段。

{{% /alert %}}
## **已删除的API**
### **已删除的DataLabels.Rotation属性**
请改用 DataLabels.RotationAngle 属性。
### **删除了 Title.Rotation 属性**
请使用 Title.RotationAngle 属性作为替代。
### **删除了 DataLabels.Background 属性**
建议使用 DataLabels.BackgroundMode 属性。
### **删除了 DisplayUnitLabel.Rotation 属性**
请考虑使用 DisplayUnitLabel.RotationAngle 属性来实现相同的目标。
### **删除了Title.getCharacters方法**
请改用Title.characters方法。
