---
title: Data Filtering with Golang via C++
linktitle: Data Filtering
type: docs
weight: 85
url: /go-cpp/data-filtering/
description: Learn how to add a data filter by using the Aspose.Cells for Go via Go API.
keywords: Add Filter by Color, Add Date Filters, Add Number Filters, Add Dynamic Filter, Add Text Filters, Add custom filter with Contains, Add custom filter with NotContains, Add custom filter with BeginsWith, Add custom filter with EndsWith
---

{{% alert color="primary" %}}

Microsoft Excel provides several useful features to autofilter worksheet data. Aspose.Cells fully supports Microsoft Excel's autofilter features. This article explains how to use the features in Microsoft Excel, and how to code them using Aspose.Cells.

{{% /alert %}}

## **AutoFilter Data**

AutoFiltering is the quickest way to select only those items from the worksheet that you want to display in a list. The AutoFilter feature allows users to filter items in a list according to a set of criteria. Filters can be based on text, numbers, or dates.

### **AutoFilter in Microsoft Excel**

To activate the AutoFilter feature in Microsoft Excel:

1. Click a heading row in a worksheet.  
2. From the **Data** menu, select **Filter** and then **AutoFilter**.

When you apply an AutoFilter to a worksheet, filter switches (black arrows) appear to the right of the column headings.

1. Click a filter arrow to see a list of filter options.

Some of the AutoFilter options are:

|**Options**|**Description**|
| :- | :- |
|All|Show all items in the list once.|
|Custom|Customize filter criteria like contains/not contains|
|Filter by Color|Filters based on filled color|
|Date Filters|Filters rows based on different date criteria|
|Number Filters|Different types of filters on numbers, such as comparisons, averages, and Top 10, etc.|
|Text Filters|Different filters like begins with, ends with, contains, etc.|
|Blanks/Non Blanks|These filters can be implemented through the Text Filter Blank option|

Users manually filter their worksheet data in Microsoft Excel using these options.

### **AutoFilter with Aspose.Cells**

Aspose.Cells provides a class `Workbook` that represents an Excel file. The `Workbook` class contains a `Worksheets` collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the `Worksheet` class. The `Worksheet` class provides a wide range of properties and methods to manage worksheets. To create an AutoFilter, use the `AutoFilter` property of the `Worksheet` class. The `AutoFilter` property is an object of the `AutoFilter` class, which provides the `Range` property for specifying the range of cells that make up a heading row. An AutoFilter is applied to the range of cells that is the heading row.

In each worksheet, you can specify only one filter range. This limitation is imposed by Microsoft Excel. For custom data filtering, use the `AutoFilter.Custom` method.

In the example given below, we have created the same AutoFilter using Aspose.Cells as we created using Microsoft Excel in the above section.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataFiltering.go" >}}

#### **Different Types of Filters**

Aspose.Cells provides multiple options to apply different types of filters, such as Color Filter, Date Filter, Number Filter, Text Filter, Blank Filters, and Non‑Blank Filters.

##### **Fill Color**

Aspose.Cells provides a function `AddFillColorFilter` to filter data based upon the fill‑color property of the cells. In the example given below, a template file having different fill colors in the first column of the sheet is used to test the color‑filtering function. Sample files can be downloaded from the following links.

1. [ColouredCells.xlsx](72417315.xlsx)  
2. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataFiltering-1.go" >}}

##### **Date**

Different types of date filters can be implemented, such as filtering all rows that have dates in January 2018. The following sample code demonstrates this filter using the `AddDateFilter` function. Sample files are given below.

1. [Date.xlsx](72417317.xlsx)  
2. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataFiltering-2.go" >}}

##### **Dynamic Date**

Sometimes dynamic filters are required based on date, such as all cells having dates in January irrespective of the year. In this case the `DynamicFilter` function is used, as shown in the following sample code. Sample files are given below.

1. [Date.xlsx](72417317.xlsx)  
2. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataFiltering-3.go" >}}

##### **Number**

Custom filters can be applied using Aspose.Cells, such as selecting cells that have numbers between a given range. The following example demonstrates the usage of the `Custom()` function to filter numbers. Sample files are given below.

1. [Number.xlsx](72417320.xlsx)  
2. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataFiltering-4.go" >}}

##### **Text**

If a column contains text and you want to select cells containing particular text, the `Filter()` function can be used. In the following example, the template file contains a list of countries, and rows are selected that contain a particular country name. Sample files are given below.

1. [Text.xlsx](72417322.xlsx)  
2. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataFiltering-5.go" >}}

##### **Blanks**

If a column contains text but some cells are blank, and you need to filter to select only rows where the cells are blank, the `MatchBlanks()` function can be used as demonstrated below. Sample files are given below.

1. [Blank.xlsx](72417324.xlsx)  
2. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataFiltering-6.go" >}}

##### **Non‑Blank**

When cells containing any text are to be filtered, use the `MatchNonBlanks()` filter function as demonstrated below. Sample files are given below.

1. [Blank.xlsx](72417324.xlsx)  
2. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataFiltering-7.go" >}}

##### **Custom filter with Contains**

Excel provides custom filters, such as filtering rows that contain a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file. Sample files are given below.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)  
2. [outSourceSampleCountryNames.xlsx](outSourceSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataFiltering-8.go" >}}

##### **Custom filter with NotContains**

Excel provides custom filters, such as filtering rows that do **not** contain a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file. Sample file is given below.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataFiltering-9.go" >}}

##### **Custom filter with BeginsWith**

Excel provides custom filters, such as filtering rows that begin with a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file. Sample file is given below.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataFiltering-10.go" >}}

##### **Custom filter with EndsWith**

Excel provides custom filters, such as filtering rows that end with a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file. Sample file is given below.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataFiltering-11.go" >}}

## **Advanced Topics**
- [Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria](/cells/go-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Get All Hidden Rows Indices after Refreshing AutoFilter](/cells/go-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
{{< app/cells/assistant language="go" >}}
