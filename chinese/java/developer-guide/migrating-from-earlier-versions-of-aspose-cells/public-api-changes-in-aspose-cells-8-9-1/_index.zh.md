---
title: Aspose.Cells 8.9.1 中的公共 API 更改
type: docs
weight: 320
url: /zh/java/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

此文档描述了从版本 8.9.0 到 8.9.1 的 Aspose.Cells API 中的更改，可能对模块/应用程序开发人员感兴趣。除了新的和更新的公共方法，添加和删除的类等，还包括任何在 Aspose.Cells 底层行为中的更改的描述。

{{% /alert %}} 
## **已添加API**
### **可配置的字体源**
Aspose.Cells for Java 已公开了一些类，为呈现电子表格提供了可配置字体源的支持。以下是使用 Aspose.Cells for Java 8.9.1 新增的类列表。

1. FontConfigs 类指定字体设置。
1. FontSourceBase 类是用于允许用户指定各种字体源的类的抽象基类。
1. FileFontSource 类表示存储在文件系统中的单个 TrueType 字体文件。
1. FolderFontSource 类表示包含 TrueType 字体文件的文件夹。
1. MemoryFontSource 类表示存储在内存中的单个 TrueType 字体文件。
1. FontSourceType枚举指定字体源的类型。

有了上述更改，Aspose.Cells for Java 允许按下面详细说明的方式设置字体。

1. 使用 FontConfigs.setFontFolder 方法设置一个自定义字体文件夹。
1. 使用 FontConfigs.setFontFolders 方法设置多个自定义字体文件夹。
1. 使用 FontConfigs.setFontSources 方法从自定义字体文件夹、单个字体文件或字体数据数组中设置字体源。

以下是上述方法的简单使用场景。

**Java**

{{< highlight csharp >}}

 //Defining string variables to store paths to font folders & font file

String fontFolder1 = "D:/Arial";

String fontFolder2 = "D:/Calibri";

String fontFile = "D:/Arial/arial.ttf";

//Setting first font folder with setFontFolder method

//Second parameter directs the API to search the sub folders for font files

FontConfigs.setFontFolder(fontFolder1, true);

//Setting both font folders with setFontFolders method

//Second parameter prohibits the API to search the sub folders for font files

FontConfigs.setFontFolders(new String[] { fontFolder1, fontFolder2 }, false);

//Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

//Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

//Defining MemoryFontSource

byte[] bytes = Files.readAllBytes(new File(fontFile).toPath());

MemoryFontSource sourceMemory = new MemoryFontSource(bytes);

//Setting font sources

FontConfigs.setFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

FontConfigs.setFontFolder 和 FontConfigs.setFontFolders 方法都接受一个布尔类型的第二个参数。将 true 作为第二个参数传递将指导 Aspose.Cells APIs 在字体文件中搜索子文件夹。 

{{% /alert %}} 

Aspose.Cells for Java 还允许配置字体替换。当在必须进行转换的机器上找不到所需的字体时，这种机制是有帮助的。用户可以提供替代原始所需字体的字体名称列表。为了实现这一点，Aspose.Cells APIs 公开了 FontConfigs.setFontSubstitutes 方法，它接受 2 个参数。第一个参数是字符串类型，应该是需要替换的字体的名称。第二个参数是一个字符串类型的数组。用户可以提供字体名称列表作为原始字体名称（在第一个参数中指定）的替代。

以下是FontConfigs.SetFontSubstitutes方法的简单使用场景。

**Java**

{{< highlight csharp >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

Aspose.Cells for Java 还提供了一种方法，以获取已设置的字体源和替换的信息。

1. FontConfigs.getFontSources 方法返回一个 FontSourceBase 类型的数组，其中包含指定字体源的列表。如果没有设置源，则 FontConfigs.getFontSources 方法将返回一个空数组。
1. FontConfigs.getFontSubstitutes 方法接受一个字符串类型的参数，允许指定已设置替换的字体名称。如果没有为指定的字体名称设置替代，则 FontConfigs.getFontSubstitutes 方法将返回 null。

{{% alert color="primary" %}} 

有关 FontConfigs 的更多细节，请查看[配置呈现电子表格的字体](/cells/zh/java/configuring-fonts-for-rendering-spreadsheets/)文章。

{{% /alert %}} 
### **添加了IFilePathProvider接口和HtmlSaveOptions.FilePathProvider属性**
Aspose.Cells for Java 8.9.1 允许获取/设置 IFilePathProvider 以将工作表导出为单独的 HTML 文件。这些新的 API 对于工作表中的超链接指向另一个工作表的情况很有帮助，其中应用程序要求将每个工作表呈现为单独的 HTML 文件。实现 IFilePathProvider 允许保持上述超链接不受影响，而不管它们指向单独的结果 HTML 文件还是源 HTML 文件。

以下是HtmlSaveOptions.FilePathProvider属性的简单使用场景。

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save each Worksheet to separate  HTML file

for (int i = 0; i < book.getWorksheets().getCount(); i++)

{

	book.getWorksheets().setActiveSheetIndex(i);

	//Create an instance of HtmlSaveOptions & set FilePathProvider property

	HtmlSaveOptions options = new HtmlSaveOptions();

	options.setExportActiveWorksheetOnly(true);

	options.setFilePathProvider(new IFilePathProvider() 

	{ 

		public String getFullName(String sheetName)

		{

		    if ("Sheet2".equals(sheetName))

		    {

		        return "sheet1.html";

		    }

		    else if ("Sheet3".equals(sheetName))

		    {

		        return "sheet2.html";

		    }



		    return "";

		}

	});



	 //Write HTML file to disc

	 book.save(dir + "sheet"+ i +".html", options);

}

{{< /highlight >}}

{{% alert color="primary" %}} 

有关这一增强功能的更多细节，请查看[实现 IFilePathProvider 接口](/cells/zh/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)文章。

{{% /alert %}} 
### **添加了CopyOptions.ReferToDestinationSheet 属性和 Cells.copyRows 方法的重载**
Aspose.Cells for Java API 公开了布尔类型的 CopyOptions.ReferToDestinationSheet 属性，以及 Cells.copyRows 方法的重载，以便在要复制的行中包含图表及其数据源时便利地进行复制行操作。开发人员可以使用这些新的 API 将图表的数据源指向源工作表或目标工作表。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet containing the chart & its data source

Worksheet source = book.getWorksheets().get(0);

//Add a new worksheet to the collection

Worksheet destination = book.getWorksheets().get(book.getWorksheets().add());

//Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.setReferToDestinationSheet(true);

//Copy the rows

destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

//Save the result on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

有关这一功能的更多细节，请查看[复制行时控制图表的数据源](/cells/zh/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)文章。

{{% /alert %}} 
### **添加了CalculationOptions.Recursive属性**
Aspose.Cells for Java 8.9.1 公开了布尔类型的 CalculationOptions.Recursive 属性。将 CalculationOptions.Recursive 属性设置为 true，并将对象传递给 Workbook.calculateFormula 方法，将指导 Aspose.Cells APIs 在计算依赖其他单元格的单元格时递归计算。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Initialize CalculationOptions & set Recursive property to true

CalculationOptions options = new CalculationOptions();

options.setRecursive(true);

//Recalculate formulas

book.calculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

有关这一功能的更多细节，请查看[优化计算时间](/cells/zh/java/decrease-the-calculation-time-of-cell-calculate-method/)文章。

{{% /alert %}}
## **已废弃的API**
### **已弃用CellsHelper.FontDir属性**
建议使用 FontConfigs.setFontFolder(String, boolean) 方法，其中文件夹递归设置为 false。
### **已弃用CellsHelper.FontDirs属性**
建议使用 FontConfigs.setFontFolders(String[], boolean) 方法，其中文件夹递归设置为 false。
### **已废弃CellsHelper.FontFiles属性**
建议使用 FontConfigs.setFontSources(FontSourceBase[]) 方法。
