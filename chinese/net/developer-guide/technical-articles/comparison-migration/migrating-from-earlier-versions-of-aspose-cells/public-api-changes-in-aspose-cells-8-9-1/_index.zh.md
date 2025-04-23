---
title: Aspose.Cells 8.9.1 的 public API 更改
type: docs
weight: 310
url: /zh/net/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

本文档描述了从版本 8.9.0 到 8.9.1 的 Aspose.Cells API 更改，可能对模块/应用程序开发者感兴趣。它不仅包括新的和更新的公共方法、已添加和已删除的类等，还描述了 Aspose.Cells 内部行为变化的说明。

{{% /alert %}} 
## **添加的 API**
### **可配置的字体源**
Aspose.Cells for .NET已经公开了许多类，以提供对呈现电子表格的可配置字体源的支持。下面是添加到Aspose.Cells for .NET 8.9.1中的类列表。

1. FontConfigs 类指定了字体设置。
1. FontSourceBase 类是各种允许用户指定不同字体源的类的抽象基类。
1. FileFontSource 类表示存储在文件系统中的单个 TrueType 字体文件。
1. FolderFontSource 类表示包含 TrueType 字体文件的文件夹。
1. MemoryFontSource 类表示存储在内存中的单个 TrueType 字体文件。
1. FontSourceType 枚举指定字体源的类型。

在上述变更位置，Aspose.Cells for .NET允许如下详细设置字体。

1. 使用 FontConfigs.SetFontFolder 方法设置一个自定义字体文件夹。
1. 使用 FontConfigs.SetFontFolders 方法设置多个自定义字体文件夹。
1. 使用 FontConfigs.SetFontSources 方法从自定义字体文件夹、单个字体文件或字体数据的字节数组设置字体源。

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

FontConfigs.SetFontFolder 和 FontConfigs.SetFontFolders 方法都接受一个布尔类型的第二个参数。将 true 作为第二个参数传递将指导 Aspose.Cells API 在字体文件中搜索子文件夹。

{{% /alert %}} 

Aspose.Cells for .NET还允许配置字体替换。当需要的字体在进行转换的计算机上不可用时，这种机制是有帮助的。用户可以提供作为原始所需字体的替代字体名称列表。为实现这一点，Aspose.Cells APIs已经公开了FontConfigs.SetFontSubstitutes方法，它接受2个参数。第一个参数是string类型的，应为需要替换的字体的名称。第二个参数是string类型的数组。用户可以提供作为原始字体名称的替代字体名单（在第一个参数中指定）。

以下是FontConfigs.SetFontSubstitutes方法的简单使用场景。

**C#**

{{< highlight csharp >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[] { "Times New Roman", "Calibri" });

{{< /highlight >}}



Aspose.Cells for .NET还提供了一种方式来收集关于已设置的字体源和替换的信息。

1. FontConfigs.GetFontSources 方法返回一个 FontSourceBase 类型的数组，其中包含指定字体源的列表。如果没有设置任何源，FontConfigs.GetFontSources 方法将返回一个空数组。
1. FontConfigs.GetFontSubstitutes 方法接受一个字符串类型的参数，用于指定已设置替换的字体名称。如果没有为指定的字体名称设置任何替换，则 FontConfigs.GetFontSubstitutes 方法将返回 null。

{{% alert color="primary" %}} 

有关 FontConfigs 的更多详细信息，请参阅[配置电子表格渲染字体](/cells/zh/net/configuring-fonts-for-rendering-spreadsheets/)文章。

{{% /alert %}} 
### **添加了IFilePathProvider接口和HtmlSaveOptions.FilePathProvider属性**
Aspose.Cells for .NET 8.9.1允许获取/设置IFilePathProvider，以便将工作表导出为单独的HTML文件。在工作表中的超链接指向另一个工作表的位置的情况下，这些新的API对于渲染每个工作表到单独的HTML文件的应用程序要求是十分有帮助的。实现IFilePathProvider允许保持上述超链接不受影响，无论它们是指向单独的结果HTML文件中的位置。

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



以下是如何实现 IFilePathProvider 接口。

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

有关此增强功能的更多详细信息，请参阅[实现 IFilePathProvider 接口](/cells/zh/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)文章。

{{% /alert %}} 
### **添加了 CopyOptions.ReferToDestinationSheet 属性和 Cells.CopyRows 方法的重载**
Aspose.Cells for .NET API已经公开了Boolean类型的CopyOptions.ReferToDestinationSheet属性以及Cells.CopyRows方法的重载，以便在复制包含图表及其数据源的行时便利地指向图表的数据源到源或目标工作表。开发人员可以利用这些新的API来完成这一操作。

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

有关此功能的更多详细信息，请参阅[在复制行时控制图表的数据源](/cells/zh/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)文章。

{{% /alert %}} 
### **添加了CalculationOptions.Recursive属性**
Aspose.Cells for .NET 8.9.1已经公开了Boolean类型的CalculationOptions.Recursive属性。将CalculationOptions.Recursive属性设置为true，并将该对象传递给Workbook.CalculateFormula方法，指导Aspose.Cells APIs在计算依赖其他单元格的单元格时递归计算。

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

有关此功能的更多详细信息，请参阅[优化计算时间](/cells/zh/net/decrease-the-calculation-time-of-cell-calculate-method/)文章。

{{% /alert %}}
## **已弃用的API**
### **已弃用CellsHelper.FontDir属性**
建议使用 FontConfigs.SetFontFolder(string, bool) 方法，将 folder recursive 设置为 false。
### **已废弃 CellsHelper.FontDirs 属性**
改用 FontConfigs.SetFontFolders(string[], bool) 方法，将 folder recursive 参数设为 false。
### **已废弃 CellsHelper.FontFiles 属性**
改用 FontConfigs.SetFontSources(FontSourceBase[]) 方法。
{{< app/cells/assistant language="csharp" >}}
