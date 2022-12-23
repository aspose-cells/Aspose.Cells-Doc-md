---
title: 公共 API Aspose.Cells 8.9.1 的变化
type: docs
weight: 310
url: /zh/net/public-api-changes-in-aspose-cells-8-9-1/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.9.0 到 8.9.1 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **可配置的字体源**
Aspose.Cells for .NET 公开了一些类来提供对渲染电子表格的可配置字体源的支持。这是已添加 Aspose.Cells for .NET 8.9.1 的类列表。

1. FontConfigs 类指定字体设置。
1. FontSourceBase 类是允许用户指定各种字体源的类的抽象基类。
1. FileFontSource 类表示存储在文件系统中的单个 TrueType 字体文件。
1. FolderFontSource 类表示包含 TrueType 字体文件的文件夹。
1. MemoryFontSource 类表示存储在内存中的单个 TrueType 字体文件。
1. FontSourceType 枚举指定字体源的类型。

通过上述更改，Aspose.Cells for .NET 允许设置字体，详情如下。

1. 使用 FontConfigs.SetFontFolder 方法时设置一个自定义字体文件夹。
1. 使用 FontConfigs.SetFontFolders 方法时设置多个自定义字体文件夹。
1. 使用 FontConfigs.SetFontSources 方法时，从自定义字体文件夹、单个字体文件或字节数组中的字体数据设置字体源。

下面是上述方法的简单使用场景。

**C#**

{{< highlight "csharp" >}}

 // Defining string variables to store paths to font folders & font file

string fontFolder1 = "D:/Arial";

string fontFolder2 = "D:/Calibri";

string fontFile = "D:/Arial/arial.ttf";

// Setting first font folder with SetFontFolder method

// Second parameter directs the API to search the subfolders for font files

FontConfigs.SetFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method

// Second parameter prohibits the API to search the subfolders for font files

FontConfigs.SetFontFolders(new string[]{ fontFolder1, fontFolder2 }, false);

// Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

// Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

// Defining MemoryFontSource

MemoryFontSource sourceMemory = new MemoryFontSource(System.IO.File.ReadAllBytes(fontFile));

//Setting font sources

FontConfigs.SetFontSources(new FontSourceBase[]{ sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

FontConfigs.SetFontFolder 和 FontConfigs.SetFontFolders 方法都接受布尔类型的第二个参数。将 true 作为第二个参数传递将指示 Aspose.Cells API 在子文件夹中搜索字体文件。

{{% /alert %}} 

Aspose.Cells for .NET 还允许配置字体替换。当必须进行转换的机器上所需的字体不可用时，此机制很有用。用户可以提供一个字体名称列表来替代最初需要的字体。为了实现这一点，Aspose.Cells API 公开了接受 2 个参数的 FontConfigs.SetFontSubstitutes 方法。第一个参数是字符串类型，应该是需要替换的字体名称。第二个参数是一个字符串类型的数组。用户可以提供字体名称列表作为原始字体名称（在第一个参数中指定）的替代。

下面是 FontConfigs.SetFontSubstitutes 方法的简单使用场景。

**C#**

{{< highlight "csharp" >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}



Aspose.Cells for .NET 还提供了收集有关已设置的源和替换信息的方法。

1. FontConfigs.GetFontSources 方法返回一个 FontSourceBase 类型的数组，其中包含指定字体源的列表。如果没有设置源，FontConfigs.GetFontSources 方法将返回一个空数组。
1. FontConfigs.GetFontSubstitutes 方法接受字符串类型的参数，允许指定已设置替换的字体名称。如果没有为指定的字体名称设置替换，则 FontConfigs.GetFontSubstitutes 方法将返回 null。

{{% alert color="primary" %}} 

有关 FontConfigs 的更多详细信息，请查看有关的文章[配置呈现电子表格的字体](/cells/zh/net/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **添加了 IFilePathProvider 接口和 HtmlSaveOptions.FilePathProvider 属性**
Aspose.Cells for .NET 8.9.1 允许获取/设置 IFilePathProvider 以将工作表导出到单独的 HTML 文件。这些新的 API 在一个工作表中的超链接指向另一个工作表中的位置的情况下很有用，在这种情况下，应用程序要求将每个工作表呈现为单独的 HTML 文件。实施 IFilePathProvider 允许保持上述超链接完好无损，而不管它们指向单独的结果 HTML 文件中的位置这一事实。

以下是 HtmlSaveOptions.FilePathProvider 属性的简单使用场景。

**C#**

{{< highlight "csharp" >}}

 // 在 Workbook 的实例中加载电子表格

var book = new Workbook(dir + "sample.xlsx");

// 将每个工作表保存到单独的 HTML 文件

对于 (int i = 0; i< book.Worksheets.Count; i++)

{

    book.Worksheets.ActiveSheetIndex = i;

    // Create an instance of HtmlSaveOptions & set FilePathProvider property

    var options = new HtmlSaveOptions

    {

        ExportActiveWorksheetOnly = true,

        FilePathProvider = new FilePathProvider()

    };

    // Write HTML file to disc

    book.Save(dir + string.Format(@"sheet{0}.html", i), options);

}

{{< /highlight >}}



下面介绍如何实现 IFilePathProvider 接口。

**C#**

{{< highlight "csharp" >}}

 public class FilePathProvider : IFilePathProvider

{

    public FilePathProvider()

    {

    }

    /// <summary>

    /// Gets the full path of the file by Worksheet name when exporting Worksheet to html separately.

    /// So the references among the Worksheets can be exported correctly.

    /// </summary>

    /// <param name="sheetName">Worksheet name</param>

    /// <returns>the full path of the file</returns>

    public string GetFullName(string sheetName)

    {

        if ("Sheet2".Equals(sheetName))

        {

            return "sheet1.html";

        }

        else if ("Sheet3".Equals(sheetName))

        {

            return "sheet2.html";

        }

        return "";

    }

}

{{< /highlight >}}

{{% alert color="primary" %}} 

有关此增强功能的更多详细信息，请查看有关的文章[实现 IFilePathProvider 接口](/cells/zh/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **为 Cells.CopyRows 方法添加了 CopyOptions.ReferToDestinationSheet 属性和重载**
Aspose.Cells for .NET API 公开了布尔类型 CopyOptions.ReferToDestinationSheet 属性以及 Cells.CopyRows 方法的重载，以便在要复制的行还包含图表及其数据源时方便复制行操作。开发人员可以利用这些新的 API 将图表的数据源指向源或目标工作表。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet containing the chart & its data source

var source = book.Worksheets[0];

// Add a new worksheet to the collection

var destination = book.Worksheets[book.Worksheets.Add()];

// Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.ReferToDestinationSheet = true;

// Copy the rows

destination.Cells.CopyRows(source.Cells, 0, 0, source.Cells.MaxDisplayRange.RowCount, options);

// Save the result on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看有关的文章[复制行时控制图表的数据源](/cells/zh/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **添加了 CalculationOptions.Recursive 属性**
Aspose.Cells for .NET 8.9.1 暴露了 Boolean 类型的 CalculationOptions.Recursive 属性。将 CalculationOptions.Recursive 属性设置为 true 并将对象传递给 Workbook.CalculateFormula 方法会指示 Aspose.Cells API 在计算依赖于其他单元格的单元格时递归计算依赖单元格。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Initialize CalculationOptions & set Recursive property to true

var options = new CalculationOptions();

options.Recursive = true;

// Recalculate formulas

book.CalculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看有关的文章[优化计算时间](/cells/zh/net/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **过时的 API**
### **废弃的 CellsHelper.FontDir 属性**
建议改用文件夹递归为 false 的 FontConfigs.SetFontFolder(string, bool) 方法。
### **废弃的 CellsHelper.FontDirs 属性**
使用 FontConfigs.SetFontFolders(string[], bool) 方法，文件夹递归为 false。
### **废弃的 CellsHelper.FontFiles 属性**
请改用 FontConfigs.SetFontSources(FontSourceBase[]) 方法。
