---
title : "Data Filtering" 
description : "" 
weight : 12223 
toc : false
type: docs
url: /net/developerguide/data/data+filtering/
---

# Aspose.Cells for .NET : Data Filtering


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
2.  From the **Data** menu, select **Filter** and then **AutoFilter**.

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

Aspose.Cells provides a class, `Workbook` that represents an Excel file. The `Workbook` class contains a `Worksheets` collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the `Worksheet` class. The `Worksheet` class provides a wide range of properties and methods to manage worksheets. To create an autofilter, use the `AutoFilter` property of the `Worksheet` class. The `AutoFilter` property is an object of the `AutoFilter` class, which provides the `Range` property for specifying the range of cells that make up a heading row. An autofilter is applied to the range of cells that is the heading row.

In each worksheet, you can only specify one filter range. This is limited by Microsoft Excel. For custom data filtering, use the `AutoFilter.Custom` method.

In the example given below, we have created the same AutoFilter using Aspose.Cells as we created using Microsoft Excel in the above section.

#### Different types of Filter

Aspose.Cells provides multiple options to apply different type of filters like Color Filter, Date Filter, Number Filter, Text Filter, Blank Filters and None Blank Filters.

##### Fill Color

Aspose.Cells provides a function `AddFillColorFilter` to filter data based upon the fill color property of the cells. In the example given below, a template file having different fill colors in the first column of the sheet is used to test the color filtering function. Sample files can be downloaded from the following links.

1.  [ColouredCells.xlsx](https://docs.dynabic.com/download/attachments/72188214/ColouredCells.xlsx?version=1&modificationDate=1537799182094&api=v2)
2.  [FilteredColouredCells.xlsx](https://docs.dynabic.com/download/attachments/72188214/FilteredColouredCells.xlsx?version=1&modificationDate=1537799189763&api=v2)

##### Date

Different type of date filters can be implemented like filtering all the rows having dates in January 2018. Following sample code demonstrates this filter using `AddDateFilter` function. Sample files are given below.

1.  [Date.xlsx](https://docs.dynabic.com/download/attachments/72188214/Date.xlsx?version=1&modificationDate=1537801347425&api=v2)
2.  [FilteredDate.xlsx](https://docs.dynabic.com/download/attachments/72188214/FilteredDate.xlsx?version=1&modificationDate=1537801351866&api=v2)

##### Dynamic Date

Sometimes dynamic filters are required based on date like all the cells having dates in January irrespective of the year. In this case `DynamicFilter` function is used as given in the following sample code. Sample files are given below.

1.  [Date.xlsx](https://docs.dynabic.com/download/attachments/72188214/Date.xlsx?version=1&modificationDate=1537801347425&api=v2)
2.  [FilteredDynamicDate.xlsx](https://docs.dynabic.com/download/attachments/72188214/FilteredDynamicDate.xlsx?version=1&modificationDate=1537802485867&api=v2)

##### Number

Custom filters can be applied using Aspose.Cells like selecting cells having number between a given range. Following example demonstrates the usage of `Custom`() function to filter numbers. Sample files are given below.

1.  [Number.xlsx](https://docs.dynabic.com/download/attachments/72188214/Number.xlsx?version=1&modificationDate=1537803180915&api=v2)
2.  [FilteredNumber.xlsx](https://docs.dynabic.com/download/attachments/72188214/FilteredNumber.xlsx?version=1&modificationDate=1537803185489&api=v2)

##### Text

If a column contains text and cells are to be selected containing particular text, `Filter()` function can be used. In the following example, template file contains list of countries and row is to be selected containing particular country name. Following code demonstrates filtering text. Sample files are given below.

1.  [Text.xlsx](https://docs.dynabic.com/download/attachments/72188214/Text.xlsx?version=1&modificationDate=1537804327872&api=v2)
2.  [FilteredText.xlsx](https://docs.dynabic.com/download/attachments/72188214/FilteredText.xlsx?version=1&modificationDate=1537804332987&api=v2)

##### Blanks

If a column contains text such that few cells are blank, and filter is required to select those rows only where blank cells are present, `MatchBlanks`() function can be used as demonstrated below. Sample files are given below.

1.  [Blank.xlsx](https://docs.dynabic.com/download/attachments/72188214/Blank.xlsx?version=1&modificationDate=1537806074220&api=v2)
2.  [FilteredBlank.xlsx](https://docs.dynabic.com/download/attachments/72188214/FilteredBlank.xlsx?version=1&modificationDate=1537806078903&api=v2)

##### Non Blanks

When cells having any text are to be filtered, use `MatchNonBlanks` filter function as demonstrated below. Sample files are given below.

1.  [Blank.xlsx](https://docs.dynabic.com/download/attachments/72188214/Blank.xlsx?version=1&modificationDate=1537806074220&api=v2)
2.  [FilteredNonBlank.xlsx](https://docs.dynabic.com/download/attachments/72188214/FilteredNonBlank.xlsx?version=1&modificationDate=1537806668615&api=v2)

##### Custom filter with Contains

Excel provides custom filters like filter rows which contain some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file. Sample files are given below.

1.   [sourseSampleCountryNames.xlsx](https://docs2.aspose.com/cells/net/attachments/68944719/72417288.xlsx)
2.  [outSourseSampleCountryNames.xlsx](https://docs2.aspose.com/cells/net/attachments/68944719/72417289.xlsx).

##### Custom filter with NotContains

Excel provides custom filters like filter rows which does not contain some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file given below.

1.  [sourseSampleCountryNames.xlsx](https://docs2.aspose.com/cells/net/attachments/68944719/72417288.xlsx).

##### Custom filter with BeginsWith

Excel provides custom filters like filter rows which begins with some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file given below.

1.  [sourseSampleCountryNames.xlsx](https://docs2.aspose.com/cells/net/attachments/68944719/72417288.xlsx).

##### Custom filter with EndsWith

Excel provides custom filters like filter rows which ends with some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file given below.

1.  [sourseSampleCountryNames.xlsx](https://docs2.aspose.com/cells/net/attachments/68944719/72417288.xlsx).

