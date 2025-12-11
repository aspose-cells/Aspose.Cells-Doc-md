---  
title: Copy Ranges of Excel  
linktitle: Copy Ranges  
type: docs  
weight: 105  
url: /python-net/copy-ranges-of-excel/  
description: This article describes how to copy ranges of Excel with Aspose.Cells for Python via .NET library.  
keywords: Python Excel Library, Python How to Copy Ranges of Excel, Python How to Copy Range Data Only with python excel library, Python how to Paste Range With Options, Python how to Only Copy Data Of The Range.  
ai_search_scope: cells_pythonnet  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask" 
---  

## **Introduction**  

In Excel, you can select a range, copy the range, then paste it with specific options to the same worksheet, other worksheets, or other files.  

## **Copy Ranges Using Aspose.Cells for Python Excel Library**  

Aspose.Cells for Python via .NET provides several overloads of the **Range.copy** method to copy a range. The **Range.copy_style** method copies only the style of the range, and the **Range.copy_data** method copies only the values of the range.  

## **Copy Range**  

Create two ranges: the source range and the target range, then copy the source range to the target range using the **Range.copy** method.  

See the following code:  

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Copy-Range.py" >}}  

## **Paste Range With Options**  

Aspose.Cells for Python via .NET supports pasting the range with specific types.  

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Paste-Range.py" >}}  

## **Only Copy Data Of The Range**  

You can also copy the data using the **Range.copy_data** method, as shown in the following code:  

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Copy-Range-Data.py" >}}  

## **Advanced Topics**  

- [Copy Row Heights of Source Range to Destination Range](/cells/python-net/copy-row-heights-of-source-range-to-destination-range/)  

{{< app/cells/assistant language="python-net" >}}
