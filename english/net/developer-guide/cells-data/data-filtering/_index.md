---
title: Data Filtering
type: docs
weight: 85
url: /net/data-filtering/
description: Learn how to add data filters using the Aspose.Cells for .NET API.
keywords: Add Filter by Color, Add Date Filters, Add Number Filters, Add Dynamic Filter, Add Text Filters, Add custom filter with Contains, Add custom filter with NotContains, Add custom filter with BeginsWith, Add custom filter with EndsWith
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Microsoft Excel provides some good features to autofilter worksheet data. Aspose.Cells fully supports Microsoft Excel's autofilter features. This article explains how to use the features in Microsoft Excel, and how to code them using Aspose.Cells.

{{% /alert %}}

## **Autofilter Data**

Autofiltering is the quickest way to select only those items from the worksheet that you want to display in a list. The autofilter feature allows users to filter items in a list according to a set of criteria. Filters are based on text, numbers, or dates.

### **Autofilter in Microsoft Excel**

To activate the autofilter feature in Microsoft Excel:

1. Click the heading row in a worksheet.  
2. From the **Data** menu, select **Filter** and then **AutoFilter**.

When you apply an autofilter to a worksheet, filter switches (black arrows) appear to the right of the column headings.

1. Click a filter arrow to see a list of filter options.

Some of the autofilter options are:

| **Options** | **Description** |
| :- | :- |
| All | Show all items in the list once. |
| Custom | Customize filter criteria such as contains/not contains |
| Filter by Color | Filters based on filled color |
| Date Filters | Filters rows based on different date criteria |
| Number Filters | Different types of filters on numbers such as comparison, averages, and Top 10, etc. |
| Text Filters | Different filters like begins with, ends with, contains, etc. |
| Blanks/Non Blanks | These filters can be implemented through the Text Filter Blank option |

Users manually filter their worksheet data in Microsoft Excel using these options.

### **Autofilter with Aspose.Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), that represents an Excel file. The Workbook class contains a Worksheets collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The Worksheet class provides a wide range of properties and methods to manage worksheets. To create an autofilter, use the **AutoFilter** property of the Worksheet class. The AutoFilter property is an object of the **AutoFilter** class, which provides the **Range** property for specifying the range of cells that make up a heading row. An autofilter is applied to the range of cells that is the heading row.

In each worksheet, you can only specify one filter range. This is limited by Microsoft Excel. For custom data filtering, use the **AutoFilter.Custom** method.

In the example given below, we have created the same AutoFilter using Aspose.Cells as we created using Microsoft Excel in the above section.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterData-1.cs" >}}

#### **Different Types of Filter**

Aspose.Cells provides multiple options to apply different types of filters such as Color Filter, Date Filter, Number Filter, Text Filter, Blank Filters, and Non‑Blank Filters.

##### **Fill Color**

Aspose.Cells provides a function **AddFillColorFilter** to filter data based upon the fill‑color property of the cells. In the example given below, a template file having different fill colors in the first column of the sheet is used to test the color‑filtering function. Sample files can be downloaded from the following links.

1. [ColouredCells.xlsx](72417315.xlsx)  
2. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterColor-1.cs" >}}

##### **Date**

Different types of date filters can be implemented, such as filtering all rows that have dates in January 2018. The following sample code demonstrates this filter using the **AddDateFilter** function. Sample files are given below.

1. [Date.xlsx](72417317.xlsx)  
2. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDate-1.cs" >}}

##### **Dynamic Date**

Sometimes dynamic filters are required based on dates, such as all cells having dates in January regardless of the year. In this case the **DynamicFilter** function is used, as shown in the following sample code. Sample files are given below.

1. [Date.xlsx](72417317.xlsx)  
2. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDynamicFilter-1.cs" >}}

##### **Number**

Custom filters can be applied using Aspose.Cells, such as selecting cells that have numbers between a given range. The following example demonstrates the usage of the **Custom()** function to filter numbers. Sample files are given below.

1. [Number.xlsx](72417320.xlsx)  
2. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNumber-1.cs" >}}

##### **Text**

If a column contains text and you want to select cells containing particular text, the **Filter()** function can be used. In the following example, the template file contains a list of countries and the row to be selected contains a particular country name. The following code demonstrates text filtering. Sample files are given below.

1. [Text.xlsx](72417322.xlsx)  
2. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterText-1.cs" >}}

##### **Blanks**

If a column contains text such that a few cells are blank, and you need to filter rows where the cells are blank, the **MatchBlanks()** function can be used as demonstrated below. Sample files are given below.

1. [Blank.xlsx](72417324.xlsx)  
2. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterBlank-1.cs" >}}

##### **Non Blanks**

When cells containing any text are to be filtered, use the **MatchNonBlanks** filter function as demonstrated below. Sample files are given below.

1. [Blank.xlsx](72417324.xlsx)  
2. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNonBlank-1.cs" >}}

##### **Custom Filter with Contains**

Excel provides custom filters such as filtering rows that contain a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file. Sample files are given below.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)  
2. [outSourceSampleCountryNames.xlsx](outSourceSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-Contains-1.cs" >}}

##### **Custom Filter with NotContains**

Excel provides custom filters such as filtering rows that do not contain a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-NotContains-1.cs" >}}

##### **Custom Filter with BeginsWith**

Excel provides custom filters such as filtering rows that begin with a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterBeginsWith-1.cs" >}}

##### **Custom Filter with EndsWith**

Excel provides custom filters such as filtering rows that end with a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterEndsWith-1.cs" >}}

## **Advanced Topics**
- [Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria](/cells/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Get All Hidden Rows Indices after Refreshing AutoFilter](/cells/net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
{{< app/cells/assistant language="csharp" >}}
