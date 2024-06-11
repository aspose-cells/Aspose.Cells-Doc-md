---
title: Aspose.Cells 16.12.0 中的公共 API 更改
type: docs
weight: 370
url: /zh/java/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

本文档描述了从 16.11.0 版本到 16.12.0 版本的 Aspose.Cells API 变化，这可能对模块/应用程序开发人员有兴趣。 其中包括新的和更新的公共方法，添加和删除的类等，同时还描述了 Aspose.Cells 后台行为的任何变化。

{{% /alert %}} 
## **添加的 API**
### **在加载时过滤对象**
Aspose.Cells 16.12.0 已公开了 LoadFilter 类及 LoadOptions.LoadFilter 属性，二者可一起控制在从模板文件初始化 Workbook 实例时加载的数据类型。

以下是仅加载模板文件中的文档属性的简单用法场景。

Java

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

以下代码从现有电子表格中加载除图表之外的所有内容。

Java

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

Java

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
### **已添加 FileFormatType.OTS 枚举**
Aspose.Cells 16.12.0 已向 FileFormatType 枚举中添加了 OTS 条目，用于检测 OTS 文件的格式。

以下代码片段使用了 FileFormatType.OTS。

Java

{{< highlight csharp >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **已添加 BuiltInDocumentPropertyCollection.ScaleCrop 属性**
Aspose.Cells 16.12.0 已向 BuiltInDocumentPropertyCollection 类添加了 ScaleCrop 属性。ScaleCrop 属性指示文档缩略图的显示模式。将该元素设置为 true 可以根据显示缩放文档缩略图，而将其设置为 false 可以裁剪文档缩略图以显示适合显示的部分。
### **已添加 BuiltInDocumentPropertyCollection.LinksUpToDate 属性**
Aspose.Cells 16.12.0 还为 BuiltInDocumentPropertyCollection 类公开了 LinksUpToDate 属性。LinksUpToDate 属性指示文档中的超链接是否是最新的。 
### **添加了Workbook.exportXml方法**
Aspose.Cells 16.12.0已公开了Workbook.exportXml方法，允许将XML映射数据存储到指定的文件路径。 Workbook.exportXml方法接受2个参数，第一个参数是字符串类型，应该是XML映射名称，第二个参数应该是存储XML数据的文件路径。
### **添加了WorksheetCollection.createRange方法**
Aspose.Cells 16.12.0已添加了WorksheetCollection.createRange方法，允许根据地址（单元格区域引用）和工作表索引创建范围。

以下代码片段使用WorksheetCollection.createRange方法在第一个（默认）工作表上创建一个跨越A1到A2的单元格范围。

Java

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

{{< /highlight >}}
## **已弃用的API**
### **已弃用LoadOptions.LoadDataOptions属性**
请使用LoadOptions.LoadFilter属性作为替代。
### **已弃用LoadOptions.LoadDataFilterOptions属性**
请使用LoadOptions.LoadFilter属性来代替。
### **已弃用LoadOptions.OnlyLoadDocumentProperties属性**
请使用LoadOptions.LoadFilter属性作为替代。
### **已弃用的LoadOptions.LoadDataAndFormatting属性**
请使用LoadOptions.LoadFilter属性来代替。

{{% alert color="primary" %}} 

所有弃用API的代码段已经分享如上。

{{% /alert %}}
## **删除的API**
### **已删除DataLabels.Rotation属性**
请使用DataLabels.RotationAngle属性来替代。
### **已删除Title.Rotation属性**
请使用Title.RotationAngle属性作为替代。
### **已删除DataLabels.Background属性**
建议使用DataLabels.BackgroundMode属性来替代。
### **已删除DisplayUnitLabel.Rotation属性**
考虑使用DisplayUnitLabel.RotationAngle属性来实现同样的效果。
### **已删除Title.getCharacters方法**
请使用Title.characters方法来替代。
