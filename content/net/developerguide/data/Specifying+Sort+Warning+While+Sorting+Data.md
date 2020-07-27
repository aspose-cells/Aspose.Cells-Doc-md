+++
title = "Specifying Sort Warning While Sorting Data" 
description = "" 
weight = 12202 
+++

Aspose.Cells for .NET : Specifying Sort Warning While Sorting Data  

# Aspose.Cells for .NET : Specifying Sort Warning While Sorting Data


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#SpecifyingSortWarningWhileSortingData-PossibleUsageScenarios)
*   2 [Sample Code](#SpecifyingSortWarningWhileSortingData-SampleCode)
{{< /panel >}}
 

 

## Possible Usage Scenarios

Please consider this textual data i.e. {11, 111, 22}. This textual data is sorted because, in terms of text, 111 comes before 22. But, if you want to sort this data not as text but as numbers, then it will become {11, 22, 111} because numerically 111 comes after 22. Aspose.Cells provides [DataSorter.SortAsNumber](https://apireference.aspose.com/net/cells/aspose.cells/datasorter/properties/sortasnumber) property to deal with this issue. Please set this property **true** and your textual data will be sorted as numerical data. The following screenshot shows the sort warning shown by Microsoft Excel when textual data which looks like numerical data is sorted.

![](https://docs2.aspose.com/cells/net/attachments/42729848/43352084.png)

## Sample Code

The following sample code illustrates the usage of [DataSorter.SortAsNumber](https://apireference.aspose.com/net/cells/aspose.cells/datasorter/properties/sortasnumber) property as explained earlier. Please check its [sample Excel file](https://docs2.aspose.com/cells/net/attachments/42729848/43352075.xlsx) and [output Excel file](https://docs2.aspose.com/cells/net/attachments/42729848/43352076.xlsx) for more help.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sampleSortAsNumber.xlsx](https://docs2.aspose.com/cells/net/attachments/42729848/43352075.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [outputSortAsNumber.xlsx](https://docs2.aspose.com/cells/net/attachments/42729848/43352076.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sort-textual-data-as-numbers.png](https://docs2.aspose.com/cells/net/attachments/42729848/43352084.png) (image/png)  

