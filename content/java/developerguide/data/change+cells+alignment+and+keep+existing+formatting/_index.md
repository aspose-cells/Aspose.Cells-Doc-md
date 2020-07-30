---
title : "Change Cells Alignment and Keep Existing Formatting" 
description : "" 
weight : 12185 
toc : false
type: docs
url: /java/developerguide/data/change+cells+alignment+and+keep+existing+formatting/
---

# Aspose.Cells for Java : Change Cells Alignment and Keep Existing Formatting


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Change Cells Alignment and Keep Existing Formatting](#change-cells-alignment-and-keep-existing-formatting)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

Sometimes, you want to change the alignment of multiple cells but also want to keep existing formatting. Aspose.Cells allows you to do it using the [StyleFlag.Alignments](https://apireference.aspose.com/java/cells/com.aspose.cells/styleflag#Alignments) property. If you will set it **true**, changes in alignment will take place otherwise not. Please note, [StyleFlag](https://apireference.aspose.com/java/cells/com.aspose.cells/StyleFlag) object is passed as a parameter to [Range.applyStyle()](https://apireference.aspose.com/java/cells/com.aspose.cells/range#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) method which actually applies the formatting to the range of cells.

## Change Cells Alignment and Keep Existing Formatting

The following sample code loads the [sample Excel file](https://docs2.aspose.com/cells/java/attachments/66950282/67338592.xlsx), creates the range and center aligns it horizontally and vertically and keeps the existing formatting intact. The following screenshot compares the sample Excel file and [output Excel file](https://docs2.aspose.com/cells/java/attachments/66950282/67338591.xlsx) and shows that all existing formatting of the cells is the same except that cells are now center aligned horizontally and vertically.

![](https://docs2.aspose.com/cells/java/attachments/66950282/67338590.png)

## Sample Code

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Change-Cells-Alignment-and-Keep-Existing-Formatting.png](https://docs2.aspose.com/cells/java/attachments/66950282/67338590.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [sampleChangeCellsAlignmentAndKeepExistingFormatting.xlsx](https://docs2.aspose.com/cells/java/attachments/66950282/67338592.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [outputChangeCellsAlignmentAndKeepExistingFormatting.xlsx](https://docs2.aspose.com/cells/java/attachments/66950282/67338591.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

