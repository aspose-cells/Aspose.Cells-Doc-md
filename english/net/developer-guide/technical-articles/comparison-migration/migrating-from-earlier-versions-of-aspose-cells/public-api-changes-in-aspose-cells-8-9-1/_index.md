---
title: Public API Changes in Aspose.Cells 8.9.1
type: docs
weight: 310
url: /net/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.9.0 to 8.9.1 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Configurable Font Sources**
Aspose.Cells for .NET has exposed a number of classes to provide the support for configurable font sources for rendering spreadsheets. Here is the list of classes which have been added with Aspose.Cells for .NET 8.9.1.

1. FontConfigs class specifies the font settings.
1. FontSourceBase class is an abstract base class for the classes that allow the user to specify various font sources.
1. FileFontSource class represents the single TrueType font file stored in the file system.
1. FolderFontSource class represents the folder that contains TrueType font files.
1. MemoryFontSource class represents the single TrueType font file stored in memory.
1. FontSourceType enumeration specifies the type of a font source.

With above mentioned changes in place, the Aspose.Cells for .NET allows to set the fonts as detailed below.

1. Set one custom font folder while using FontConfigs.SetFontFolder method.
1. Set multiple custom font folder while using FontConfigs.SetFontFolders method.
1. Set font sources from a custom font folder, a single font file or font data from an array of bytes while using FontConfigs.SetFontSources method.

Here is simple usage scenario of aforementioned methods.

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

Both FontConfigs.SetFontFolder & FontConfigs.SetFontFolders methods accept a Boolean type second parameter. Passing true as second parameter will direct the Aspose.Cells APIs to search the sub folders for the fonts files.

{{% /alert %}} 

Aspose.Cells for .NET also allows to configure the font substitution. This mechanism is helpful when a required font is not available on the machine where conversion has to take place. Users can provide a list of font names as alternative to the originally required font. In order to achieve this, the Aspose.Cells APIs have exposed the FontConfigs.SetFontSubstitutes method which accepts 2 parameters. The first parameter is of type string, which should be the name of the font that needs to be substituted. The second parameter is an array of type string. Users can provide a list of font names as substitution to the original font name (specified in the first parameter).

Here is simple usage scenario of FontConfigs.SetFontSubstitutes method.

**C#**

{{< highlight csharp >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[] { "Times New Roman", "Calibri" });

{{< /highlight >}}



The Aspose.Cells for .NET has also provided means to gather information on what sources and substitutions have been set.

1. FontConfigs.GetFontSources method returns an array of type FontSourceBase containing the list of specified font sources. In case, no sources have been set, the FontConfigs.GetFontSources method will return an empty array.
1. FontConfigs.GetFontSubstitutes method accepts a parameter of type string allowing to specify the font name for which a substitution has been set. In case, no substitution has been set for the specified font name then the FontConfigs.GetFontSubstitutes method will return null.

{{% alert color="primary" %}} 

For more details on FontConfigs, please review the article on [Configuring Fonts for Rendering Spreadsheets](/cells/net/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Added IFilePathProvider Interface & HtmlSaveOptions.FilePathProvider property**
Aspose.Cells for .NET 8.9.1 allows to get/set the IFilePathProvider for exporting worksheets to separate HTML files. These new APIs are helpful in scenarios where hyperlinks in one worksheet points to a location in another worksheet, where application requirement is to render each worksheet to separate HTML file. Implementing the IFilePathProvider allows to keep the aforementioned hyperlinks intact regardless of the fact that they are pointing to a location in a separate resultant HTML file.

Following is the simple usage scenario of HtmlSaveOptions.FilePathProvider property.

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



Here is how to implement the IFilePathProvider interface.

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

For more details on this enhancement, please review the article on [Implementing IFilePathProvider Interface](/cells/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Added CopyOptions.ReferToDestinationSheet Property & Overload for Cells.CopyRows Method**
Aspose.Cells for .NET API has exposed the Boolean type CopyOptions.ReferToDestinationSheet property along with the an overload of Cells.CopyRows method in order to facilitate the copy rows operation when rows to be copied also contains a chart and its data source. Developers can make use of these new APIs to point the chart's data source to the source or destination worksheets.

Following is the simple usage scenario.

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

For more details on this feature, please review the article on [Control the Data Source of Chart while Copying Rows](/cells/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Added CalculationOptions.Recursive Property**
Aspose.Cells for .NET 8.9.1 has exposed the Boolean type CalculationOptions.Recursive property. Setting the CalculationOptions.Recursive property to true and passing the object to Workbook.CalculateFormula method directs the Aspose.Cells APIs to calculate the dependent cells recursively when calculating cells which depends on other cells.

Following is the simple usage scenario.

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

For more details on this feature, please review the article on [Optimize Calculation Time](/cells/net/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **Obsoleted APIs**
### **Obsoleted CellsHelper.FontDir Property**
It is advised to use the FontConfigs.SetFontFolder(string, bool) method with folder recursive to false instead.
### **Obsoleted CellsHelper.FontDirs Property**
Use FontConfigs.SetFontFolders(string[], bool) method with folder recursive to false instead.
### **Obsoleted CellsHelper.FontFiles Property**
Use FontConfigs.SetFontSources(FontSourceBase[]) method instead.
