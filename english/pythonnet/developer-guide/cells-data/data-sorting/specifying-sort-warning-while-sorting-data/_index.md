---  
title: Specifying Sort Warning While Sorting Data  
type: docs  
weight: 140  
url: /python-net/specifying-sort-warning-while-sorting-data/  
description: Learn how to specify sort warning while sorting data by using the Aspose.Cells for Python via .NET API.  
keywords: Python Excel Library, Python add sort warning when sorting data, Python set sort warning while sorting data, Python select sort warning when sorting data.  
ai_search_scope: cells_pythonnet  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask" 
---  

## **Possible Usage Scenarios**

Please consider this textual data, e.g., {11, 111, 22}. This textual data is sorted because, in terms of text, 111 comes before 22. However, if you want to sort this data not as text but as numbers, it will become {11, 22, 111} because numerically 111 comes after 22. Aspose.Cells for Python via .NET provides the [**DataSorter.sort_as_number**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_as_number/) property to deal with this issue. Please set this property to **true**, and your textual data will be sorted as numerical data. The following screenshot shows the sort warning displayed by Microsoft Excel when textual data that looks like numerical data is sorted.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Sample Code**

The following sample code illustrates the usage of the [**DataSorter.sort_as_number**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_as_number/) property as explained earlier. Please check its [sample Excel file](43352075.xlsx) and [output Excel file](43352076.xlsx) for more help.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SpecifyingSortWarningWhileSortingData.py" >}}  
{{< app/cells/assistant language="python-net" >}}
