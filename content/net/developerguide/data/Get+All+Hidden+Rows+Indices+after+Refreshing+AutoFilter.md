+++
title = "Get All Hidden Rows Indices after Refreshing AutoFilter" 
description = "" 
weight = 12220 
+++

Aspose.Cells for .NET : Get All Hidden Rows Indices after Refreshing AutoFilter  

# Aspose.Cells for .NET : Get All Hidden Rows Indices after Refreshing AutoFilter


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#GetAllHiddenRowsIndicesafterRefreshingAutoFilter-PossibleUsageScenarios)
*   2 [Get All Hidden Rows Indices after Refreshing AutoFilter](#GetAllHiddenRowsIndicesafterRefreshingAutoFilter-GetAllHiddenRowsIndicesafterRefreshingAutoFilter)
*   3 [Sample Code](#GetAllHiddenRowsIndicesafterRefreshingAutoFilter-SampleCode)
*   4 [Console Output](#GetAllHiddenRowsIndicesafterRefreshingAutoFilter-ConsoleOutput)
{{< /panel >}}
 

## Possible Usage Scenarios

When you apply the auto filter on worksheet cells, then some of the rows get hidden automatically. But it might be the case that some of the rows are already hidden manually by Excel end user and they are not hidden by an auto filter. It therefore makes difficult to know which of the rows are hidden by the auto filter and which of them are hidden manually by Excel end user. Aspose.Cells deals with this problem using the int\[\] [AutoFilter.Refresh(bool hideRows)](https://apireference.aspose.com/net/cells/aspose.cells.autofilter/refresh/methods/1) method. This method returns the row indices of all the rows that are hidden by the auto filter and not manually by the Excel end user.

## Get All Hidden Rows Indices after Refreshing AutoFilter

Please see the following sample code that loads the [sample Excel file](https://docs2.aspose.com/cells/net/attachments/64456077/64716909.xlsx) which contains some of the rows hidden manually by Excel end user. The code applies the auto filter and refreshes it using the int\[\] [AutoFilter.Refresh(bool hideRows)](https://apireference.aspose.com/net/cells/aspose.cells.autofilter/refresh/methods/1) method that returns the row indices of all the hidden rows by the auto filter. It then prints the indices of the hidden rows on the console along with cells names and values.

## Sample Code

## Console Output

{{< code lang="cs" >}}
Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.
--------------------------
1       A2      Apple
2       A3      Apple
3       A4      Apple
6       A7      Apple
7       A8      Apple
11      A12     Pear
12      A13     Pear
{{< /code >}}

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sampleGetAllHiddenRowsIndicesAfterRefreshingAutoFilter.xlsx](https://docs2.aspose.com/cells/net/attachments/64456077/64716909.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

