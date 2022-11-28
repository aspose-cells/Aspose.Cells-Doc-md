---
title: Data Filtering
type: docs
weight: 60
url: /java/data-filtering/
---

{{% alert color="primary" %}}

Microsoft Excel provides some good features to autofilter worksheet data. Aspose.Cells fully supports Microsoft Excel's autofilter features. This article explains how to use the features in Microsoft Excel, and how to code them using Aspose.Cells.

{{% /alert %}}

## **Autofilter Data**

Autofiltering is the quickest way to select only those items from the worksheet that you want to display in a list. The autofilter feature allows users to filter items in a list according to a set criteria. Filter based on text, numbers or dates.

### **Autofilter in Microsoft Excel**

To activate the autofilter feature in Microsoft Excel:

1. Click the heading row in a worksheet.
1. From the **Data** menu, select **Filter** and then **AutoFilter**.

When you apply an autofilter to a worksheet, filter switches (black arrows) appear to the right of the column headings.

1. Click a filter arrow to see a list of filter options.

Some of the autofilter options are:

|**Options**|**Description**|
| :- | :- |
|All|Show all items in the list once.|
|Custom|Customize filter criteria like contains/not contains|
|Filter by Color|Filters based on filled color|
|Date Filters|Filters rows based on different criteria on date|
|Number Filters|Different type of filter on numbers like comparison, averages and Top 10 etc.|
|Text Filters|Different filters like begins with, ends with, contains etc,|
|Blanks/Non Blanks|These filters can be implemented through Text Filter Blank|
Users manually filter their worksheet data in Microsoft Excel using these options.

### **Autofilter with Aspose.Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class contains a [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) that allows access to each worksheet in the Excel file.

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class provides a wide range of properties and methods to manage worksheets. To create an autofilter, use the [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) property of the [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class. The [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) property is an object of the [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) class, which provides the [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range) property for specifying the range of cells that make up a heading row. An autofilter is applied to the range of cells that is the heading row.

In each worksheet, you can only specify one filter range. This is limited by Microsoft Excel. For custom data filtering, use the [**AutoFilter.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) method.

In the example given below, we have created the same AutoFilter using Aspose.Cells as we created using Microsoft Excel in the above section.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **Different types of Filter**

Aspose.Cells provides multiple options to apply different type of filters like Color Filter, Date Filter, Number Filter, Text Filter, Blank Filters and None Blank Filters.

##### **Fill Color**

Aspose.Cells provides a function [**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter(int,%20int,%20com.aspose.cells.CellsColor,%20com.aspose.cells.CellsColor)) to filter data based upon the fill color property of the cells. In the example given below, a template file having different fill colors in the first column of the sheet is used to test the color filtering function. Following files can be downloaded to check the functionality.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **Date**

Different types of date filters can be implemented like filtering all the rows having dates in January 2018. Following sample code demonstrates this filter using [**addDateFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter(int,%20int,%20int,%20int,%20int,%20int,%20int,%20int)) function. Following files can be used for testing this functionality.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **Dynamic Date**

Sometimes dynamic filters are required based on a date like all the cells having dates in January irrespective of the year. In this case, [**DynamicFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter(int,%20int)) function is used as given in the following sample code. Following files can be used for testing.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **Number**

Custom filters can be applied using Aspose.Cells like selecting cells having number between a given range. Following example demonstrates the usage of [**custom()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) function to filter numbers. Sample files can be downloaded from the following links.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **Text**

If a column contains text and cells are to be selected containing particular text, [**filter()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter(int,%20java.lang.String)) function can be used. In the following example, the template file contains a list of countries and row is to be selected containing particular country name. Following code demonstrates filtering text using the below sample files.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **Blanks**

If a column contains text such that few cells are blank, and filter is required to select those rows only where blank cells are present, [**matchBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks(int)) function can be used as demonstrated below. Sample files can be downloaded from the following links.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **Non Blanks**

When cells having any text are to be filtered, use [**MatchNonBlanks**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks(int)) filter function as demonstrated below. Sample files can be downloaded from the following links.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **Custom filter with Contains**

Excel provides custom filters like filter rows which contain some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file. Sample files can be downloaded from the following links.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **Custom filter with NotContains**

Excel provides custom filters like filter rows which does not contain some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file given below.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **Custom filter with BeginsWith**

Excel provides custom filters like filter rows which begins with some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file given below.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **Custom filter with EndsWith**

Excel provides custom filters like filter rows which end with some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file given below.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **Advance topics**
- [Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria](/cells/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Get All Hidden Rows Indices after Refreshing AutoFilter](/cells/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

