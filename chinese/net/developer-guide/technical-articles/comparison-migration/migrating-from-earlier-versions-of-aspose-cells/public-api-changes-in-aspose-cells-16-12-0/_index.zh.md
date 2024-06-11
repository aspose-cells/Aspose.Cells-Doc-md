---
title: Aspose.Cells 16.12.0 中的公共 API 更改
type: docs
weight: 360
url: /zh/net/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

本文档描述了从 16.11.0 版本到 16.12.0 版本的 Aspose.Cells API 变化，这可能对模块/应用程序开发人员有兴趣。 其中包括新的和更新的公共方法，添加和删除的类等，同时还描述了 Aspose.Cells 后台行为的任何变化。

{{% /alert %}} 
## **添加的 API**
### **在加载时过滤对象**
Aspose.Cells 16.12.0 已公开了 LoadFilter 类及 LoadOptions.LoadFilter 属性，二者可一起控制在从模板文件初始化 Workbook 实例时加载的数据类型。

以下是仅加载模板文件中的文档属性的简单用法场景。

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



以下代码从现有电子表格中加载除图表之外的所有内容。

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



以下代码仅从现有电子表格中加载单元格数据（包括公式）和格式。

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



LoadFilter 类还允许根据 Worksheet 的属性自定义加载过程。为了根据工作表自定义加载过程，必须重写 LoadFilter.StartSheet 方法，如下所示。

**C#**

{{< highlight csharp >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}



以下代码片段使用了上述自定义的 CustomFilter 类。

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **已添加 FileFormatType.OTS 枚举**
Aspose.Cells 16.12.0 已向 FileFormatType 枚举中添加了 OTS 条目，用于检测 OTS 文件的格式。

以下代码片段使用了 FileFormatType.OTS。

**C#**

{{< highlight csharp >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **已添加 FontConfigs.PreferSystemFontSubstitutes 属性**
Aspose.Cells 16.12.0 已为 FontConfigs 类公开了 PreferSystemFontSubstitutes 属性。FontConfigs.PreferSystemFontSubstitutes 属性是布尔类型，指示 API 是否应首先使用系统的字体替代机制，以防所需字体不存在且未为特定字体定义替代。FontConfigs.PreferSystemFontSubstitutes 属性的默认值为 false。
### **已添加 BuiltInDocumentPropertyCollection.ScaleCrop 属性**
Aspose.Cells 16.12.0 已向 BuiltInDocumentPropertyCollection 类添加了 ScaleCrop 属性。ScaleCrop 属性指示文档缩略图的显示模式。将该元素设置为 true 可以根据显示缩放文档缩略图，而将其设置为 false 可以裁剪文档缩略图以显示适合显示的部分。
### **已添加 BuiltInDocumentPropertyCollection.LinksUpToDate 属性**
Aspose.Cells 16.12.0 还为 BuiltInDocumentPropertyCollection 类公开了 LinksUpToDate 属性。LinksUpToDate 属性指示文档中的超链接是否是最新的。
### **已添加 Workbook.ExportXml 方法**
Aspose.Cells 16.12.0公开了Workbook.ExportXml方法，允许将XML映射数据存储到指定的文件路径。Workbook.ExportXml方法接受2个参数，第一个参数为string类型，应为XML映射名称，第二个参数应为存储XML数据的文件路径位置。
### **添加了WorksheetCollection.CreateRange方法**
Aspose.Cells 16.12.0添加了WorksheetCollection.CreateRange方法，允许根据地址（单元区引用）和工作表索引创建范围。

以下示例使用了WorksheetCollection.CreateRange方法来创建跨越第一个（默认）工作表的A1到A2的单元格范围。

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

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
