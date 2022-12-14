---
title: 公共 API Aspose.Cells 16.12.0 的变化
type: docs
weight: 370
url: /zh/java/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 16.11.0 到 16.12.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **在加载时过滤对象**
Aspose.Cells 16.12.0 公开了 LoadFilter 类和 LoadOptions.LoadFilter 属性，它们一起可以控制在从模板文件初始化工作簿实例时要加载的数据类型。

这是一个简单的使用场景，仅从模板文件加载文档属性。

**Java**

{{< highlight "csharp" >}}

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

以下代码段从现有电子表格加载除图表之外的所有内容。

**Java**

{{< highlight "csharp" >}}

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

以下代码仅加载现有电子表格中的单元格数据（以及公式）和格式。

**Java**

{{< highlight "csharp" >}}

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
### **添加了 FileFormatType.OTS 枚举**
Aspose.Cells 16.12.0 已将 OTS 条目添加到 FileFormatType 枚举中，以检测 OTS 文件的格式。

以下代码段使用了 FileFormatType.OTS。

**Java**

{{< highlight "csharp" >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **添加了 BuiltInDocumentPropertyCollection.ScaleCrop 属性**
Aspose.Cells 16.12.0 已将 ScaleCrop 属性添加到 BuiltInDocumentPropertyCollection 类。 ScaleCrop 表示文档缩略图的显示方式。将此元素设置为 true 可以根据显示缩放文档缩略图，而将其设置为 false 可以裁剪文档缩略图以显示适合显示的部分。
### **添加了 BuiltInDocumentPropertyCollection.LinksUpToDate 属性**
Aspose.Cells 16.12.0 还公开了 BuiltInDocumentPropertyCollection 类的 LinksUpToDate 属性。 LinksUpToDate 属性指示文档中的超链接是否是最新的。
### **添加了 Workbook.exportXml 方法**
Aspose.Cells 16.12.0 公开了允许将 XML 映射数据存储到指定文件路径的 Workbook.exportXml 方法。 Workbook.exportXml 方法接受 2 个参数，其中字符串类型的第一个参数应该是 XML 映射名称，第二个参数应该是存储 XML 数据的文件路径位置。
### **添加了 WorksheetCollection.createRange 方法**
Aspose.Cells 16.12.0 添加了 WorksheetCollection.createRange 方法，允许基于地址（单元格区域引用）和工作表索引创建范围。

以下代码段使用 WorksheetCollection.createRange 方法在第一个（默认）工作表中创建跨越 A1 到 A2 的一系列单元格。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

{{< /highlight >}}
## **过时的 API**
### **废弃的 LoadOptions.LoadDataOptions 属性**
请使用 LoadOptions.LoadFilter 属性作为替代。
### **废弃的 LoadOptions.LoadDataFilterOptions 属性**
请改用 LoadOptions.LoadFilter 属性。
### **废弃的 LoadOptions.OnlyLoadDocumentProperties 属性**
请使用 LoadOptions.LoadFilter 属性作为替代。
### **废弃的 LoadOptions.LoadDataAndFormatting 属性**
请改用 LoadOptions.LoadFilter 属性。

{{% alert color="primary" %}} 

所有已过时的 API 的代码片段已在上面共享。

{{% /alert %}}
## **已删除的 API**
### **删除的 DataLabels.Rotation 属性**
请改用 DataLabels.RotationAngle 属性。
### **删除 Title.Rotation 属性**
请使用 Title.RotationAngle 属性作为替代。
### **删除的 DataLabels.Background 属性**
建议改用 DataLabels.BackgroundMode 属性。
### **删除 DisplayUnitLabel.Rotation 属性**
请考虑使用 DisplayUnitLabel.RotationAngle 属性来实现相同的目标。
### **删除了 Title.getCharacters 方法**
请改用 Title.characters 方法。
