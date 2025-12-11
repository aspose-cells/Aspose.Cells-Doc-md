---  
title: Get Max Range In A Worksheet  
type: docs  
weight: 360  
url: /python-net/get-max-range-in-a-worksheet/  
description: This article describes how to get the max range, max data range, and max display range of Excel files with Aspose.Cells for Python via .NET library.  
keywords: Python Excel Library, Python get the max range, Python get max data range, Python get max display range.  
ai_search_scope: cells_pythonnet  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask" 
---  

{{% alert color="primary" %}}  

When reading data from the worksheet, we need to know the maximum area.  

When copying all data from a worksheet, we need to know the maximum area.  

When exporting the specified area to HTML and PDF, we need to know the maximum area.  

Aspose.Cells for Python via .NET contains different ways to find the max range in a worksheet.  

{{% /alert %}}  



## **How to Get Max Range**  
In Aspose.Cells for Python via .NET, if the [**row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) and [**column**](https://reference.aspose.com/cells/python-net/aspose.cells/column) objects are initialized, these rows and columns will be counted toward the maximum area, even if there is no data in empty rows or columns.  

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Range.py" >}}  



## **How to Get Max Data Range**  
In most cases, we only need to obtain the range containing all the data, even if the empty cells outside the range are formatted, and settings for shapes, tables, and pivot tables are ignored.  

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Data-Range.py" >}}  



## **How to Get Max Display Range**  
When we export all data from the worksheet to HTML, PDF, or images, we need to obtain an area containing all visible objects, including data, styles, graphics, tables, and pivot tables.  
The following code shows how to render the max display range to HTML:  

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Display-Range.py" >}}  

Here is the source Excel file: [Book1.xlsx](Book1.xlsx).  
{{< app/cells/assistant language="python-net" >}}
