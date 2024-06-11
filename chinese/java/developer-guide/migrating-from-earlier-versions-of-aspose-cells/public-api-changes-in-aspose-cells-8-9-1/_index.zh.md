---
title: Aspose.Cells 8.9.1 的 public API 更改
type: docs
weight: 320
url: /zh/java/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

本文档描述了从版本 8.9.0 到 8.9.1 的 Aspose.Cells API 更改，可能对模块/应用程序开发者感兴趣。它不仅包括新的和更新的公共方法、已添加和已删除的类等，还描述了 Aspose.Cells 内部行为变化的说明。

{{% /alert %}} 
## **添加的 API**
### **可配置的字体源**
Aspose.Cells for Java已暴露了许多类以提供对可配置字体源的支持，用于渲染电子表格。以下是已添加到Aspose.Cells for Java 8.9.1中的类列表。

1. FontConfigs 类指定了字体设置。
1. FontSourceBase 类是各种允许用户指定不同字体源的类的抽象基类。
1. FileFontSource 类表示存储在文件系统中的单个 TrueType 字体文件。
1. FolderFontSource 类表示包含 TrueType 字体文件的文件夹。
1. MemoryFontSource 类表示存储在内存中的单个 TrueType 字体文件。
1. FontSourceType 枚举指定字体源的类型。

在上述变更生效的情况下，Aspose.Cells for Java允许按以下详细信息设置字体。

1. 使用 FontConfigs.setFontFolder 方法设置单个自定义字体文件夹。
1. 使用 FontConfigs.setFontFolders 方法设置多个自定义字体文件夹。
1. 使用 FontConfigs.setFontSources 方法从自定义字体文件夹、单个字体文件或字体数据字节数组中设置字体源。

以下是上述方法的简单使用场景。

Java

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

FontConfigs.setFontFolder和FontConfigs.setFontFolders方法接受Boolean类型的第二个参数。将true作为第二个参数传递将指导Aspose.Cells API搜索字体文件的子文件夹。 

{{% /alert %}} 

Aspose.Cells for Java还允许配置字体替换。当所需的字体在执行转换的计算机上不可用时，此机制很有帮助。用户可以提供替代原始所需字体的字体名称列表。为实现此目的，Aspose.Cells API已经暴露了FontConfigs.setFontSubstitutes方法，该方法接受2个参数。第一个参数是字符串类型，应为需要替换的字体名称。第二个参数是字符串数组类型。用户可以提供作为原始字体名称替代的字体名称列表（指定在第一个参数中的字体名称）。

以下是FontConfigs.SetFontSubstitutes方法的简单使用场景。

Java

{{< highlight csharp >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

Aspose.Cells for Java还提供了收集设置的来源和替换信息的手段。

1. FontConfigs.getFontSources方法返回一个FontSourceBase类型的数组，其中包含指定字体源的列表。如果未设置任何源，则FontConfigs.getFontSources方法将返回一个空数组。
1. FontConfigs.getFontSubstitutes方法接受一个字符串类型的参数，允许指定为其设置替换的字体名称。如果未为指定的字体名称设置替代，则FontConfigs.getFontSubstitutes方法将返回null。

{{% alert color="primary" %}} 

有关FontConfigs的更多详细信息，请查看[为电子表格渲染配置字体](/cells/zh/java/configuring-fonts-for-rendering-spreadsheets/)的文章。

{{% /alert %}} 
### **添加了IFilePathProvider接口和HtmlSaveOptions.FilePathProvider属性**
Aspose.Cells for Java 8.9.1版本允许获取/设置用于将工作表导出为独立HTML文件的IFilePathProvider。这些新API在一张工作表中的超链接指向其他工作表的场景中很有用，其中应用程序要求将每个工作表渲染为独立的HTML文件。实现IFilePathProvider允许保持上述超链接不受影响，无论它们指向单独的生成的HTML文件中的位置。

以下是HtmlSaveOptions.FilePathProvider属性的简单使用场景。

Java

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

有关此增强功能的更多详细信息，请查看[实现IFilePathProvider接口](/cells/zh/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)的文章。

{{% /alert %}} 
### **添加了CopyOptions.ReferToDestinationSheet属性和Cells.copyRows方法的重载**
Aspose.Cells for Java API已暴露了布尔类型的CopyOptions.ReferToDestinationSheet属性以及Cells.copyRows方法的重载，以便在要复制的行中还包含图表及其数据源的情况下进行复制行操作。开发人员可以利用这些新API来将图表的数据源指向源或目标工作表。

以下是简单的使用场景。

Java

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

有关此功能的更多详细信息，请查看[在复制行时控制图表的数据源](/cells/zh/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)的文章。

{{% /alert %}} 
### **添加了CalculationOptions.Recursive属性**
Aspose.Cells for Java 8.9.1版本已暴露了布尔类型的CalculationOptions.Recursive属性。将CalculationOptions.Recursive属性设置为true，并将对象传递给Workbook.calculateFormula方法时，指示Aspose.Cells API在计算依赖其他单元格的单元格时递归计算这些单元格。

以下是简单的使用场景。

Java

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

有关此功能的更多详细信息，请查看[优化计算时间](/cells/zh/java/decrease-the-calculation-time-of-cell-calculate-method/)的文章。

{{% /alert %}}
## **已弃用的API**
### **已弃用CellsHelper.FontDir属性**
建议使用 FontConfigs.setFontFolder(String, boolean) 方法，将递归设置为 false。
### **已废弃 CellsHelper.FontDirs 属性**
建议使用 FontConfigs.setFontFolders(String[], boolean) 方法，将递归设置为 false。
### **已废弃 CellsHelper.FontFiles 属性**
建议使用 FontConfigs.setFontSources(FontSourceBase[]) 方法。
