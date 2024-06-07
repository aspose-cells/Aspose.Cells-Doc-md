---
title: Aspose.Cells 16.12.0中的公共API更改
type: docs
weight: 360
url: /zh/net/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本16.11.0到16.12.0的Aspose.Cells API的变化，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，添加和删除的类等，还描述了Aspose.Cells背后行为的任何更改。

{{% /alert %}} 
## **已添加API**
### **在加载时过滤对象**
Aspose.Cells 16.12.0已经公开了LoadFilter类以及LoadOptions.LoadFilter属性，可以一起控制在从模板文件初始化工作簿实例时要加载的数据类型。

以下是从模板文件中仅加载文档属性的简单使用场景。

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



以下片段从现有电子表格中加载所有内容，除了图表。

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



LoadFilter类还允许根据工作表的属性自定义加载过程。为了根据工作表自定义加载过程，需要重写LoadFilter.StartSheet方法如下所示。

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



以下片段利用上面定义的CustomFilter类。

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **添加了FileFormatType.OTS枚举。**
Aspose.Cells 16.12.0已向FileFormatType枚举中添加了OTS条目，用于检测OTS文件的格式。

以下片段利用了FileFormatType.OTS。

**C#**

{{< highlight csharp >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **添加了FontConfigs.PreferSystemFontSubstitutes属性。**
Aspose.Cells 16.12.0已为FontConfigs类公开了PreferSystemFontSubstitutes属性。FontConfigs.PreferSystemFontSubstitutes属性是Boolean类型，表示API是否应首先使用系统的字体替换机制，以防所需字体不存在且未为特定字体定义替代。FontConfigs.PreferSystemFontSubstitutes属性的默认值为false。
### **添加了BuiltInDocumentPropertyCollection.ScaleCrop属性。**
Aspose.Cells 16.12.0已向BuiltInDocumentPropertyCollection类添加了ScaleCrop属性。ScaleCrop指示文档缩略图的显示模式。将此元素设置为true可根据显示缩放文档缩略图，而将其设置为false会裁剪文档缩略图以显示适合显示的部分。
### **添加了BuiltInDocumentPropertyCollection.LinksUpToDate属性。**
Aspose.Cells 16.12.0还为BuiltInDocumentPropertyCollection类公开了LinksUpToDate属性。LinksUpToDate属性指示文档中的超链接是否是最新的。
### **添加了Workbook.ExportXml方法。**
Aspose.Cells 16.12.0已公开了Workbook.ExportXml方法，允许将XML映射数据存储到指定的文件路径。Workbook.ExportXml方法接受2个参数，第一个参数应为字符串类型，表示XML映射名称，第二个参数应为要存储XML数据的文件路径。
### **添加了WorksheetCollection.CreateRange方法。**
Aspose.Cells 16.12.0已添加了WorksheetCollection.CreateRange方法，允许根据地址（单元格区域引用）和工作表索引创建范围。

以下片段利用WorksheetCollection.CreateRange方法在第一个（默认）工作表中创建一个跨越A1到A2的单元格范围。

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

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
