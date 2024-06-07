---
title: Aspose.Cells 8.9.1 中的公共 API 更改
type: docs
weight: 310
url: /zh/net/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

此文档描述了从版本 8.9.0 到 8.9.1 的 Aspose.Cells API 中的更改，可能对模块/应用程序开发人员感兴趣。除了新的和更新的公共方法，添加和删除的类等，还包括任何在 Aspose.Cells 底层行为中的更改的描述。

{{% /alert %}} 
## **已添加API**
### **可配置的字体源**
Aspose.Cells for .NET 已公开了许多类，以支持用于呈现电子表格的可配置字体源。以下是随 Aspose.Cells for .NET 8.9.1 添加的类列表。

1. FontConfigs 类指定字体设置。
1. FontSourceBase 类是用于允许用户指定各种字体源的类的抽象基类。
1. FileFontSource 类表示存储在文件系统中的单个 TrueType 字体文件。
1. FolderFontSource 类表示包含 TrueType 字体文件的文件夹。
1. MemoryFontSource 类表示存储在内存中的单个 TrueType 字体文件。
1. FontSourceType枚举指定字体源的类型。

在上述修改生效后，Aspose.Cells for .NET允许设置字体，详情如下。

1. 在使用FontConfigs.SetFontFolder方法时设置一个自定义字体文件夹。
1. 在使用FontConfigs.SetFontFolders方法时设置多个自定义字体文件夹。
1. 在使用FontConfigs.SetFontSources方法时，从自定义字体文件夹、单个字体文件或字体数据字节数组设置字体源。

以下是上述方法的简单使用场景。

**C#**

{{< highlight csharp >}}

 // Defining string variables to store paths to font folders & font file

string fontFolder1 = "D:/Arial";

string fontFolder2 = "D:/Calibri";

string fontFile = "D:/Arial/arial.ttf";

// Setting first font folder with SetFontFolder method

// Second parameter directs the API to search the subfolders for font files

FontConfigs.SetFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method

// Second parameter prohibits the API to search the subfolders for font files

FontConfigs.SetFontFolders(new string[] { fontFolder1, fontFolder2 }, false);

// Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

// Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

// Defining MemoryFontSource

MemoryFontSource sourceMemory = new MemoryFontSource(System.IO.File.ReadAllBytes(fontFile));

//Setting font sources

FontConfigs.SetFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

FontConfigs.SetFontFolder和FontConfigs.SetFontFolders方法都接受第二个参数为布尔类型。将true作为第二个参数传递将引导Aspose.Cells API搜索字体文件的子文件夹。

{{% /alert %}} 

Aspose.Cells for .NET还允许配置字体替代。当所需字体在转换所需发生的计算机上无法使用时，此机制很有帮助。用户可以提供作为原始所需字体的替代的字体名称列表。为了实现这一点，Aspose.Cells API提供了FontConfigs.SetFontSubstitutes方法，该方法接受2个参数。第一个参数是字符串类型，应该是需要替代的字体名称。第二个参数是字符串类型数组。用户可以提供字体名称列表作为原始字体名称（指定在第一个参数中）的替代。

以下是FontConfigs.SetFontSubstitutes方法的简单使用场景。

**C#**

{{< highlight csharp >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[] { "Times New Roman", "Calibri" });

{{< /highlight >}}



Aspose.Cells for .NET还提供了收集已设置的源和替代信息的手段。

1. FontConfigs.GetFontSources方法返回一个FontSourceBase类型的数组，其中包含指定的字体源列表。如果未设置任何源，则FontConfigs.GetFontSources方法将返回一个空数组。
1. FontConfigs.GetFontSubstitutes方法接受一个字符串类型参数，允许指定已设置替代的字体名称。如果未为指定的字体名称设置替代，则FontConfigs.GetFontSubstitutes方法将返回null。

{{% alert color="primary" %}} 

有关FontConfigs的更多详细信息，请查看[配置呈现电子表格的字体](/cells/zh/net/configuring-fonts-for-rendering-spreadsheets/)上的文章。

{{% /alert %}} 
### **添加了IFilePathProvider接口和HtmlSaveOptions.FilePathProvider属性**
Aspose.Cells for .NET 8.9.1允许获取/设置IFilePathProvider以将工作表导出为单独的HTML文件。这些新API对于一个工作表中的超链接指向另一个工作表的情况以及应用程序要求为每个工作表呈现为单独的HTML文件很有帮助。实现IFilePathProvider可以保持上述超链接完整，无论它们指向分离结果的HTML文件的位置。

以下是HtmlSaveOptions.FilePathProvider属性的简单使用场景。

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save each Worksheet to separate HTML file

for (int i = 0; i < book.Worksheets.Count; i++)

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



这里是如何实现IFilePathProvider接口。

**C#**

{{< highlight csharp >}}

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

有关此改进的更多详细信息，请查看[实现IFilePathProvider接口](/cells/zh/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)上的文章。

{{% /alert %}} 
### **添加了CopyOptions.ReferToDestinationSheet属性和Cells.CopyRows方法的重载**
Aspose.Cells for .NET API公开了布尔类型CopyOptions.ReferToDestinationSheet属性以及Cells.CopyRows方法的一种重载，以便在复制行时便于处理包含图表及其数据源的行。开发人员可以利用这些新API，将图表的数据源指向源或目标工作表。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

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

有关此功能的更多详细信息，请查看[复制行时控制图表的数据源](/cells/zh/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)上的文章。

{{% /alert %}} 
### **添加了CalculationOptions.Recursive属性**
Aspose.Cells for .NET 8.9.1公开了布尔类型CalculationOptions.Recursive属性。将CalculationOptions.Recursive属性设置为true并将对象传递给Workbook.CalculateFormula方法，Aspose.Cells API将在计算依赖于其他单元格的单元格时递归计算依赖单元格。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Initialize CalculationOptions & set Recursive property to true

var options = new CalculationOptions();

options.Recursive = true;

// Recalculate formulas

book.CalculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[优化计算时间](/cells/zh/net/decrease-the-calculation-time-of-cell-calculate-method/)上的文章。

{{% /alert %}}
## **已废弃的API**
### **已弃用CellsHelper.FontDir属性**
建议使用FontConfigs.SetFontFolder(string, bool)方法，其中文件夹递归设为false。
### **已弃用CellsHelper.FontDirs属性**
请使用FontConfigs.SetFontFolders(string[], bool)方法，将递归参数设置为false。
### **已废弃CellsHelper.FontFiles属性**
请使用FontConfigs.SetFontSources(FontSourceBase[])方法。
