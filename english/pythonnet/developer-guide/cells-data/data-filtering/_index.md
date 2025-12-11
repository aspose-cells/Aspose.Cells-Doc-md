---
title: Data Filtering
type: docs
weight: 85
url: /python-net/data-filtering/
description: Learn how to add data filters using the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Add Filter by Color, Python Add Date Filters, Python Add Number Filters, Python Add Dynamic Filter, Python Add Text Filters, Python Add custom filter with Contains, Python Add custom filter with NotContains, Python Add custom filter with BeginsWith, Python Add custom filter with EndsWith
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Microsoft Excel provides some good features to autofilter worksheet data. Aspose.Cells for Python via .NET fully supports Microsoft Excel's autofilter features. This article explains how to use the features in Microsoft Excel, and how to code them using Aspose.Cells for Python via .NET.

{{% /alert %}}

## **Autofilter Data**

Autofiltering is the quickest way to select only those items from the worksheet that you want to display in a list. The autofilter feature allows users to filter items in a list according to a set of criteria. Filter based on text, numbers, or dates.

### **Autofilter in Microsoft Excel**

To activate the autofilter feature in Microsoft Excel:

1. Click the heading row in a worksheet.  
2. From the **Data** menu, select **Filter** and then **AutoFilter**.

When you apply an autofilter to a worksheet, filter switches (black arrows) appear to the right of the column headings.

1. Click a filter arrow to see a list of filter options.

Some of the autofilter options are:

| **Options**            | **Description**                                                                      |
|------------------------|--------------------------------------------------------------------------------------|
| All                    | Show all items in the list once.                                                     |
| Custom                 | Customize filter criteria like contains/not contains                               |
| Filter by Color        | Filters based on filled color                                                        |
| Date Filters           | Filters rows based on different date criteria                                        |
| Number Filters         | Different types of filters on numbers, such as comparisons, averages, and Top 10 etc. |
| Text Filters           | Different filters like begins with, ends with, contains etc                        |
| Blanks/Non Blanks      | These filters can be implemented through the Text Filter “Blank”                   |

Users manually filter their worksheet data in Microsoft Excel using these options.

### **Autofilter with Aspose.Cells for Python Excel Library**

Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), that represents an Excel file. The Workbook class contains a **Worksheets** collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The Worksheet class provides a wide range of properties and methods to manage worksheets. To create an autofilter, use the **AutoFilter** property of the Worksheet class. The AutoFilter property is an object of the **AutoFilter** class, which provides the **Range** property for specifying the range of cells that make up a heading row. An autofilter is applied to the range of cells that is the heading row.

In each worksheet, you can only specify one filter range. This is limited by Microsoft Excel. For custom data filtering, use the **AutoFilter.Custom** method.

In the example given below, we have created the same AutoFilter using Aspose.Cells for Python via .NET as we created using Microsoft Excel in the above section.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterData-1.py" >}}

#### **Different types of Filter**

Aspose.Cells for Python via .NET provides multiple options to apply different types of filters such as Color Filter, Date Filter, Number Filter, Text Filter, Blank Filters, and Non‑Blank Filters.

##### **Fill Color**

Aspose.Cells for Python via .NET provides a function **AddFillColorFilter** to filter data based upon the fill‑color property of the cells. In the example given below, a template file having different fill colors in the first column of the sheet is used to test the color‑filtering function. Sample files can be downloaded from the following links.

1. [ColouredCells.xlsx](72417315.xlsx)  
2. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterColor-1.py" >}}

##### **Date**

Different types of date filters can be implemented, such as filtering all the rows having dates in January 2018. The following sample code demonstrates this filter using the **AddDateFilter** function. Sample files are given below.

1. [Date.xlsx](72417317.xlsx)  
2. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDate-1.py" >}}

##### **Dynamic Date**

Sometimes dynamic filters are required based on date, such as all the cells having dates in January irrespective of the year. In this case the **DynamicFilter** function is used, as shown in the following sample code. Sample files are given below.

1. [Date.xlsx](72417317.xlsx)  
2. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDynamicFilter-1.py" >}}

##### **Number**

Custom filters can be applied using Aspose.Cells for Python via .NET, such as selecting cells having numbers between a given range. The following example demonstrates the usage of the **Custom()** function to filter numbers. Sample files are given below.

1. [Number.xlsx](72417320.xlsx)  
2. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNumber-1.py" >}}

##### **Text**

If a column contains text and cells are to be selected containing particular text, the **Filter()** function can be used. In the following example, the template file contains a list of countries, and rows are selected that contain a particular country name. The code demonstrates filtering text. Sample files are given below.

1. [Text.xlsx](72417322.xlsx)  
2. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterText-1.py" >}}

##### **Blanks**

If a column contains text such that a few cells are blank, and a filter is required to select only those rows where blank cells are present, the **MatchBlanks()** function can be used as demonstrated below. Sample files are given below.

1. [Blank.xlsx](72417324.xlsx)  
2. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterBlank-1.py" >}}

##### **Non Blanks**

When cells having any text are to be filtered, use the **MatchNonBlanks** filter function as demonstrated below. Sample files are given below.

1. [Blank.xlsx](72417324.xlsx)  
2. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNonBlank-1.py" >}}

##### **Custom filter with Contains**

Excel provides custom filters such as filtering rows that contain a specific string. This feature is available in Aspose.Cells for Python via .NET and is demonstrated below by filtering the names in the sample file. Sample files are given below.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)  
2. [outSourceSampleCountryNames.xlsx](outSourceSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-Contains-1.py" >}}

##### **Custom filter with NotContains**

Excel provides custom filters such as filtering rows that do **not** contain a specific string. This feature is available in Aspose.Cells for Python via .NET and is demonstrated below by filtering the names in the sample file.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-NotContains-1.py" >}}

##### **Custom filter with BeginsWith**

Excel provides custom filters such as filtering rows that begin with a specific string. This feature is available in Aspose.Cells for Python via .NET and is demonstrated below by filtering the names in the sample file.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterBeginsWith-1.py" >}}

##### **Custom filter with EndsWith**

Excel provides custom filters such as filtering rows that end with a specific string. This feature is available in Aspose.Cells for Python via .NET and is demonstrated below by filtering the names in the sample file.

1. [sourceSampleCountryNames.xlsx](sourceSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterEndsWith-1.py" >}}

## **Advanced topics**
- [Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria](/cells/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Get All Hidden Rows Indices after Refreshing AutoFilter](/cells/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
{{< app/cells/assistant language="python-net" >}}
