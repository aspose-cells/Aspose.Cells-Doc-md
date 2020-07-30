---
title : "Data Filtering" 
description : "" 
weight : 12165 
toc : false
type: docs
url: /java/developerguide/data/data+filtering/
---

# Aspose.Cells for Java : Data Filtering


Microsoft Excel provides some good features to autofilter worksheet data. Aspose.Cells fully supports Microsoft Excel's autofilter features. This article explains how to use the features in Microsoft Excel, and how to code them using Aspose.Cells.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Autofilter Data](#autofilter-data)
    *   1.1 [Autofilter in Microsoft Excel](#autofilter-in-microsoft-excel)
    *   1.2 [Autofilter with Aspose.Cells](#autofilter-with-aspose.cells)
        *   1.2.1 [Different types of Filter](#different-types-of-filter)
            *   1.2.1.1 [Fill Color](#fill-color)
            *   1.2.1.2 [Date](#date)
            *   1.2.1.3 [Dynamic Date](#dynamic-date)
            *   1.2.1.4 [Number](#number)
            *   1.2.1.5 [Text](#text)
            *   1.2.1.6 [Blanks](#blanks)
            *   1.2.1.7 [Non Blanks](#non-blanks)
            *   1.2.1.8 [Custom filter with Contains](#custom-filter-with-contains)
            *   1.2.1.9 [Custom filter with NotContains](#custom-filter-with-notcontains)
            *   1.2.1.10 [Custom filter with BeginsWith](#custom-filter-with-beginswith)
            *   1.2.1.11 [Custom filter with EndsWith](#custom-filter-with-endswith)
{{< /panel >}}
 

## Autofilter Data

Autofiltering is the quickest way to select only those items from the worksheet that you want to display in a list. The autofilter feature allows users to filter items in a list according to a set criteria. Filter based on text, numbers or dates.

### Autofilter in Microsoft Excel

To activate the autofilter feature in Microsoft Excel:

1.  Click the heading row in a worksheet.
2.  From the **Data** menu, select **Filter** and then **AutoFilter**.

When you apply an autofilter to a worksheet, filter switches (black arrows) appear to the right of the column headings.

1.  Click a filter arrow to see a list of filter options.

Some of the autofilter options are:

{{< table style="table-striped" >}}
|Options|Description|
|:----|:----|
|All|Show all items in the list once.|
|Custom|Customize filter criteria like contains/not contains|
|Filter by Color|Filters based on filled color|
|Date Filters|Filters rows based on different criteria on date|
|Number Filters|Different type of filter on numbers like comparison, averages and Top 10 etc.|
|Text Filters|Different filters like begins with, ends with, contains etc,|
|Blanks/Non Blanks|These filters can be implemented through Text Filter Blank|
{{< /table >}}

Users manually filter their worksheet data in Microsoft Excel using these options.

### Autofilter with Aspose.Cells

Aspose.Cells provides a class, [Workbook](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Workbook) that represents an Excel file. The [Workbook](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Workbook) class contains a [WorksheetCollection](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/WorksheetCollection) that allows access to each worksheet in the Excel file.

A worksheet is represented by the [Worksheet](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Worksheet) class. The [Worksheet](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Worksheet) class provides a wide range of properties and methods to manage worksheets. To create an autofilter, use the [AutoFilter](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#AutoFilter) property of the [Worksheet](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Worksheet) class. The [AutoFilter](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#AutoFilter) property is an object of the [AutoFilter](https://apireference.aspose.com/java/cells/com.aspose.cells/AutoFilter) class, which provides the [Range](https://apireference.aspose.com/java/cells/com.aspose.cells/autofilter#Range) property for specifying the range of cells that make up a heading row. An autofilter is applied to the range of cells that is the heading row.

In each worksheet, you can only specify one filter range. This is limited by Microsoft Excel. For custom data filtering, use the [AutoFilter.Custom](https://apireference.aspose.com/java/cells/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) method.

In the example given below, we have created the same AutoFilter using Aspose.Cells as we created using Microsoft Excel in the above section.

#### Different types of Filter

Aspose.Cells provides multiple options to apply different type of filters like Color Filter, Date Filter, Number Filter, Text Filter, Blank Filters and None Blank Filters.

##### Fill Color

Aspose.Cells provides a function [addFillColorFilter](https://apireference.aspose.com/java/cells/com.aspose.cells/autofilter#addFillColorFilter(int,%20int,%20com.aspose.cells.CellsColor,%20com.aspose.cells.CellsColor)) to filter data based upon the fill color property of the cells. In the example given below, a template file having different fill colors in the first column of the sheet is used to test the color filtering function. Following files can be downloaded to check the functionality.

1.  [ColouredCells.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417315.xlsx)
2.  [FilteredColouredCells.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417316.xlsx)

##### Date

Different types of date filters can be implemented like filtering all the rows having dates in January 2018. Following sample code demonstrates this filter using [addDateFilter](https://apireference.aspose.com/java/cells/com.aspose.cells/autofilter#addDateFilter(int,%20int,%20int,%20int,%20int,%20int,%20int,%20int)) function. Following files can be used for testing this functionality.

1.  [Date.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417317.xlsx)
2.  [FilteredDate.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417318.xlsx)

##### Dynamic Date

Sometimes dynamic filters are required based on a date like all the cells having dates in January irrespective of the year. In this case, [DynamicFilter](https://apireference.aspose.com/java/cells/com.aspose.cells/autofilter#dynamicFilter(int,%20int)) function is used as given in the following sample code. Following files can be used for testing.

1.  [Date.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417317.xlsx)
2.  [FilteredDynamicDate.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417319.xlsx)

##### Number

Custom filters can be applied using Aspose.Cells like selecting cells having number between a given range. Following example demonstrates the usage of [custom()](https://apireference.aspose.com/java/cells/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) function to filter numbers. Sample files can be downloaded from the following links.

1.  [Number.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417320.xlsx)
2.  [FilteredNumber.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417321.xlsx)

##### Text

If a column contains text and cells are to be selected containing particular text, [filter()](https://apireference.aspose.com/java/cells/com.aspose.cells/autofilter#filter(int,%20java.lang.String)) function can be used. In the following example, the template file contains a list of countries and row is to be selected containing particular country name. Following code demonstrates filtering text using the below sample files.

1.  [Text.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417322.xlsx)
2.  [FilteredText.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417323.xlsx)

##### Blanks

If a column contains text such that few cells are blank, and filter is required to select those rows only where blank cells are present, [matchBlanks()](https://apireference.aspose.com/java/cells/com.aspose.cells/autofilter#matchBlanks(int)) function can be used as demonstrated below. Sample files can be downloaded from the following links.

1.  [Blank.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417324.xlsx)
2.  [FilteredBlank.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417325.xlsx)

##### Non Blanks

When cells having any text are to be filtered, use [MatchNonBlanks](https://apireference.aspose.com/java/cells/com.aspose.cells/autofilter#matchNonBlanks(int)) filter function as demonstrated below. Sample files can be downloaded from the following links.

1.  [Blank.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417324.xlsx)
2.  [FilteredNonBlank.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417326.xlsx)

##### Custom filter with Contains

Excel provides custom filters like filter rows which contain some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file. Sample files can be downloaded from the following links. 

1.  [sourseSampleCountryNames.xlsx](https://docs.aspose.com/download/attachments/68944719/sourseSampleCountryNames.xlsx?version=1&modificationDate=1537209516129&api=v2)
2.  [outSourseSampleCountryNames.xlsx](https://docs.aspose.com/download/attachments/68944719/outSourseSampleCountryNames.xlsx?version=1&modificationDate=1537209549009&api=v2)

##### Custom filter with NotContains

Excel provides custom filters like filter rows which does not contain some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file given below.

1.   [sourseSampleCountryNames.xlsx](https://docs.aspose.com/download/attachments/68944719/sourseSampleCountryNames.xlsx?version=1&modificationDate=1537209516129&api=v2).

##### Custom filter with BeginsWith

Excel provides custom filters like filter rows which begins with some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file given below.

1.   [sourseSampleCountryNames.xlsx](https://docs.aspose.com/download/attachments/68944719/sourseSampleCountryNames.xlsx?version=1&modificationDate=1537209516129&api=v2).

##### Custom filter with EndsWith

Excel provides custom filters like filter rows which end with some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file given below.

1.   [sourseSampleCountryNames.xlsx](https://docs.aspose.com/download/attachments/68944719/sourseSampleCountryNames.xlsx?version=1&modificationDate=1537209516129&api=v2).

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Data Filtering and Validation-002.png](https://docs2.aspose.com/cells/java/attachments/72188214/72417298.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Data Filtering and Validation-003.png](https://docs2.aspose.com/cells/java/attachments/72188214/72417297.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Data Filtering and Validation-001.png](https://docs2.aspose.com/cells/java/attachments/72188214/72417299.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [AFData.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417300.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [AFData\_out.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417301.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [ColouredCells.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417315.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [FilteredColouredCells.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417316.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Date.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417317.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [FilteredDate.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417318.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [FilteredDynamicDate.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417319.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Number.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417320.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [FilteredNumber.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417321.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Text.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417322.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [FilteredText.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417323.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Blank.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417324.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [FilteredBlank.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417325.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [FilteredNonBlank.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/72417326.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [sourseSampleCountryNames.xlsx](https://docs2.aspose.com/cells/java/attachments/72188214/74776605.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

