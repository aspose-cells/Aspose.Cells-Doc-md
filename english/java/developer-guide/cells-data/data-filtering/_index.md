---
title: Data Filtering
type: docs
weight: 60
url: /java/data-filtering/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Microsoft Excel provides some good features to autofilter worksheet data. Aspose.Cells fully supports Microsoft Excel's autofilter features. This article explains how to use the features in Microsoft Excel, and how to code them using Aspose.Cells.

{{% /alert %}}

## **Autofilter Data**

Autofiltering is the quickest way to select only those items from the worksheet that you want to display in a list. The autofilter feature allows users to filter items in a list according to a set **of** criteria. Filters based on text, numbers or dates.

### **Autofilter in Microsoft Excel**

To activate the autofilter feature in Microsoft Excel:

1. Click the heading row in a worksheet.  
1. From the **Data** menu, select **Filter** and then **AutoFilter**.

When you apply an autofilter to a worksheet, filter switches (black arrows) appear to the right of the column headings.

1. Click a filter arrow to see a list of filter options.

Some of the autofilter options are:

|**Options**|**Description**|
| :- | :- |
|All|Show all items in the list.|
|Custom|Customize filter criteria like contains / not contains|
|Filter by Color|Filters based on filled color|
|Date Filters|Filters rows based on different date criteria|
|Number Filters|Different types of filters on numbers, such as comparisons, averages, and Top 10, etc.|
|Text Filters|Different filters like begins with, ends with, contains, etc.|
|Blanks/Non‑Blanks|These filters can be implemented through the Text Filter Blank option.|

Users manually filter their worksheet data in Microsoft Excel using these options.

### **Autofilter with Aspose.Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class contains a [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) that allows access to each worksheet in the Excel file.

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class provides a wide range of properties and methods to manage worksheets. To create an autofilter, use the [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#getAutoFilter--) property of the [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class. The [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#getAutoFilter--) property is an object of the [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter) class, which provides the [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#getRange--) property for specifying the range of cells that make up a heading row. An autofilter is applied to the range of cells that is the heading row.

In each worksheet, you can only specify one filter range. This is limited by Microsoft Excel. For custom data filtering, use the [**AutoFilter.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom-int-int-java.lang.Object-) method.

In the example given below, we have created the same AutoFilter using Aspose.Cells as we created using Microsoft Excel in the above section.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **Different Types of Filter**

Aspose.Cells provides multiple options to apply different types of filters like Color Filter, Date Filter, Number Filter, Text Filter, Blank Filters and Non‑Blank Filters.

##### **Fill Color**

Aspose.Cells provides a function [**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter-int-int-com.aspose.cells.CellsColor-com.aspose.cells.CellsColor-) to filter data based upon the fill‑color property of the cells. In the example given below, a template file having different fill colors in the first column of the sheet is used to test the color‑filtering function. The following files can be downloaded to check the functionality.

1. [ColouredCells.xlsx](72417315.xlsx)  
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **Date**

Different types of date filters can be implemented, such as filtering all rows that have dates in January 2018. The following sample code demonstrates this filter using the [**addDateFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter-int-int-int-int-int-int-int-int-) function. The following files can be used for testing this functionality.

1. [Date.xlsx](72417317.xlsx)  
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **Dynamic Date**

Sometimes dynamic filters are required based on a date, such as all cells having dates in January irrespective of the year. In this case, the [**DynamicFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter-int-int-) function is used, as shown in the following sample code. The following files can be used for testing.

1. [Date.xlsx](72417317.xlsx)  
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **Number**

Custom filters can be applied using Aspose.Cells, such as selecting cells that contain numbers between a given range. The following example demonstrates the usage of the [**custom()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom-int-int-java.lang.Object-) function to filter numbers. Sample files can be downloaded from the following links.

1. [Number.xlsx](72417320.xlsx)  
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **Text**

If a column contains text and you need to select cells that contain particular text, the [**filter()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter-int-java.lang.String-) function can be used. In the following example, the template file contains a list of countries and rows are selected that contain a particular country name. The code demonstrates filtering text using the sample files below.

1. [Text.xlsx](72417322.xlsx)  
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **Blanks**

If a column contains text such that a few cells are blank, and you need to filter only those rows where blank cells are present, the [**matchBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks-int-) function can be used as demonstrated below. Sample files can be downloaded from the following links.

1. [Blank.xlsx](72417324.xlsx)  
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **Non‑Blanks**

When cells containing any text are to be filtered, use the [**matchNonBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks-int-) function as demonstrated below. Sample files can be downloaded from the following links.

1. [Blank.xlsx](72417324.xlsx)  
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **Custom Filter with Contains**

Excel provides custom filters that filter rows which contain a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file. Sample files can be downloaded from the following links.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)  
1. [outSourceSampleCountryNames.xlsx](outSourceSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **Custom Filter with NotContains**

Excel provides custom filters that filter rows which do **not** contain a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **Custom Filter with BeginsWith**

Excel provides custom filters that filter rows which begin with a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **Custom Filter with EndsWith**

Excel provides custom filters that filter rows which end with a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **Advanced Topics**
- [Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria](/cells/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Get All Hidden Rows Indices after Refreshing AutoFilter](/cells/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

{{< app/cells/assistant language="java" >}}
