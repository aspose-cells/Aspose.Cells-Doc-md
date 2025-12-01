---
title: Public API Changes in Aspose.Cells 8.9.1
type: docs
weight: 320
url: /java/public-api-changes-in-aspose-cells-8-9-1/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.9.0 to 8.9.1 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Configurable Font Sources**
Aspose.Cells for Java has exposed a number of classes to provide the support for configurable font sources for rendering spreadsheets. Here is the list of classes which have been added with Aspose.Cells for Java 8.9.1.

1. FontConfigs class specifies the font settings.
1. FontSourceBase class is an abstract base class for the classes that allow the user to specify various font sources.
1. FileFontSource class represents the single TrueType font file stored in the file system.
1. FolderFontSource class represents the folder that contains TrueType font files.
1. MemoryFontSource class represents the single TrueType font file stored in memory.
1. FontSourceType enumeration specifies the type of a font source.

With above mentioned changes in place, the Aspose.Cells for Java allows to set the fonts as detailed below.

1. Set one custom font folder while using FontConfigs.setFontFolder method.
1. Set multiple custom font folder while using FontConfigs.setFontFolders method.
1. Set font sources from a custom font folder, a single font file or font data from an array of bytes while using FontConfigs.setFontSources method.

Here is simple usage scenario of aforementioned methods.

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

Both FontConfigs.setFontFolder & FontConfigs.setFontFolders methods accept a Boolean type second parameter. Passing true as second parameter will direct the Aspose.Cells APIs to search the sub folders for the fonts files. 

{{% /alert %}} 

Aspose.Cells for Java also allows to configure the font substitution. This mechanism is helpful when a required font is not available on the machine where conversion has to take place. Users can provide a list of font names as alternative to the originally required font. In order to achieve this, the Aspose.Cells APIs have exposed the FontConfigs.setFontSubstitutes method which accepts 2 parameters. The first parameter is of type string, which should be the name of the font that needs to be substituted. The second parameter is an array of type string. Users can provide a list of font names as substitution to the original font name (specified in the first parameter).

Here is simple usage scenario of FontConfigs.SetFontSubstitutes method.

**Java**

{{< highlight csharp >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

The Aspose.Cells for Java has also provided means to gather information on what sources and substitutions have been set.

1. FontConfigs.getFontSources method returns an array of type FontSourceBase containing the list of specified font sources. In case, no sources have been set, the FontConfigs.getFontSources method will return an empty array.
1. FontConfigs.getFontSubstitutes method accepts a parameter of type string allowing to specify the font name for which a substitution has been set. In case, no substitution has been set for the specified font name then the FontConfigs.getFontSubstitutes method will return null.

{{% alert color="primary" %}} 

For more details on FontConfigs, please review the article on [Configuring Fonts for Rendering Spreadsheets](/cells/java/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Added IFilePathProvider Interface & HtmlSaveOptions.FilePathProvider property**
Aspose.Cells for Java 8.9.1 allows to get/set the IFilePathProvider for exporting worksheets to separate HTML files. These new APIs are helpful in scenarios where hyperlinks in one worksheet points to a location in another worksheet, where application requirement is to render each worksheet to separate HTML file. Implementing the IFilePathProvider allows to keep the aforementioned hyperlinks intact regardless of the fact that they are pointing to a location in a separate resultant HTML file.

Following is the simple usage scenario of HtmlSaveOptions.FilePathProvider property.

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

For more details on this enhancement, please review the article on [Implementing IFilePathProvider Interface](/cells/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Added CopyOptions.ReferToDestinationSheet Property & Overload for Cells.copyRows Method**
Aspose.Cells for Java API has exposed the Boolean type CopyOptions.ReferToDestinationSheet property along with the an overload of Cells.copyRows method in order to facilitate the copy rows operation when rows to be copied also contains a chart and its data source. Developers can make use of these new APIs to point the chart's data source to the source or destination worksheets.

Following is the simple usage scenario.

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

For more details on this feature, please review the article on [Control the Data Source of Chart while Copying Rows](/cells/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Added CalculationOptions.Recursive Property**
Aspose.Cells for Java 8.9.1 has exposed the Boolean type CalculationOptions.Recursive property. Setting the CalculationOptions.Recursive property to true and passing the object to Workbook.calculateFormula method directs the Aspose.Cells APIs to calculate the dependent cells recursively when calculating cells which depends on other cells.

Following is the simple usage scenario.

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

For more details on this feature, please review the article on [Optimize Calculation Time](/cells/java/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **Obsoleted APIs**
### **Obsoleted CellsHelper.FontDir Property**
It is advised to use the FontConfigs.setFontFolder(String, boolean) method with folder recursive to false instead.
### **Obsoleted CellsHelper.FontDirs Property**
Use FontConfigs.setFontFolders(String[], boolean) method with folder recursive to false instead.
### **Obsoleted CellsHelper.FontFiles Property**
Use FontConfigs.setFontSources(FontSourceBase[]) method instead.
{{< app/cells/assistant language="java" >}}
