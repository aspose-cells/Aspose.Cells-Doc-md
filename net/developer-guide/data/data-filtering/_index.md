---
title: Data Filtering
type: docs
weight: 85
url: /net/data-filtering/
---

{{% alert color="primary" %}}

Microsoft Excel provides some good features to autofilter worksheet data. Aspose.Cells fully supports Microsoft Excel's autofilter features. This article explains how to use the features in Microsoft Excel, and how to code them using Aspose.Cells.

{{% /alert %}}

## **Autofilter Data**

Autofiltering is the quickest way to select only those items from the worksheet that you want to display in a list. The autofilter feature allows users to filter items in a list according to a set criteria. Filter based on text, numbers or dates.

### **Autofilter in Microsoft Excel**

To activate the autofilter feature in Microsoft Excel:

1. Click the heading row in a worksheet.
1. From the **Data** menu, select **Filter** and then **AutoFilter**.

When you apply an autofilter to a worksheet, filter switches (black arrows) appear to the right of the column headings.

1. Click a filter arrow to see a list of filter options.

Some of the autofilter options are:

|**Options**|**Description**|
| :- | :- |
|All|Show all items in the list once.|
|Custom|Customize filter criteria like contains/not contains|
|Filter by Color|Filters based on filled color|
|Date Filters|Filters rows based on different criteria on date|
|Number Filters|Different types of filter on numbers like comparison, averages and Top 10 etc.|
|Text Filters|Different filters like begins with, ends with, contains etc,|
|Blanks/Non Blanks|These filters can be implemented through Text Filter Blank|

Users manually filter their worksheet data in Microsoft Excel using these options.

### **Autofilter with Aspose.Cells**

Aspose.Cells provides a class, Workbook that represents an Excel file. The Workbook class contains a Worksheets collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the Worksheet class. The Worksheet class provides a wide range of properties and methods to manage worksheets. To create an autofilter, use the AutoFilter property of the Worksheet class. The AutoFilter property is an object of the AutoFilter class, which provides the Range property for specifying the range of cells that make up a heading row. An autofilter is applied to the range of cells that is the heading row.

In each worksheet, you can only specify one filter range. This is limited by Microsoft Excel. For custom data filtering, use the AutoFilter.Custom method.

In the example given below, we have created the same AutoFilter using Aspose.Cells as we created using Microsoft Excel in the above section.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterData-1.cs" >}}

#### **Different types of Filter**

Aspose.Cells provides multiple options to apply different type of filters like Color Filter, Date Filter, Number Filter, Text Filter, Blank Filters and None Blank Filters.

##### **Fill Color**

Aspose.Cells provides a function AddFillColorFilter to filter data based upon the fill color property of the cells. In the example given below, a template file having different fill colors in the first column of the sheet is used to test the color filtering function. Sample files can be downloaded from the following links.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterColor-1.cs" >}}

##### **Date**

Different type of date filters can be implemented like filtering all the rows having dates in January 2018. Following sample code demonstrates this filter using AddDateFilter function. Sample files are given below.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDate-1.cs" >}}

##### **Dynamic Date**

Sometimes dynamic filters are required based on date like all the cells having dates in January irrespective of the year. In this case DynamicFilter function is used as given in the following sample code. Sample files are given below.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDynamicFilter-1.cs" >}}

##### **Number**

Custom filters can be applied using Aspose.Cells like selecting cells having number between a given range. Following example demonstrates the usage of Custom() function to filter numbers. Sample files are given below.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNumber-1.cs" >}}

##### **Text**

If a column contains text and cells are to be selected containing particular text, Filter() function can be used. In the following example, template file contains list of countries and row is to be selected containing particular country name. Following code demonstrates filtering text. Sample files are given below.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterText-1.cs" >}}

##### **Blanks**

If a column contains text such that few cells are blank, and filter is required to select those rows only where blank cells are present, MatchBlanks() function can be used as demonstrated below. Sample files are given below.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterBlank-1.cs" >}}

##### **Non Blanks**

When cells having any text are to be filtered, use MatchNonBlanks filter function as demonstrated below. Sample files are given below.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNonBlank-1.cs" >}}

##### **Custom filter with Contains**

Excel provides custom filters like filter rows which contain some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file. Sample files are given below.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-Contains-1.cs" >}}

##### **Custom filter with NotContains**

Excel provides custom filters like filter rows which does not contain some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file given below.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-NotContains-1.cs" >}}

##### **Custom filter with BeginsWith**

Excel provides custom filters like filter rows which begins with some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file given below.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterBeginsWith-1.cs" >}}

##### **Custom filter with EndsWith**

Excel provides custom filters like filter rows which ends with some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file given below.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterEndsWith-1.cs" >}}
