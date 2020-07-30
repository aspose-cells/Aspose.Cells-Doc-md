---
title : "Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria" 
description : "" 
weight : 12178 
toc : false
type: docs
url: /java/developerguide/data/apply+advanced+filter+of+microsoft+excel+to+display+records+meeting+complex+criteria/
---

# Aspose.Cells for Java : Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria](#apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

Microsoft Excel allows you to apply *Advanced Filter* on worksheet data to display records that meet complex criteria. You can apply Advanced Filter with Microsoft Excel via its *Data > Advanced* command as shown in this screenshot.

![](https://docs2.aspose.com/cells/java/attachments/48136911/48496704.png)

Aspose.Cells also allows you to apply the Advanced Filter using the [Worksheet.advancedFilter()](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#advancedFilter(boolean,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20boolean)) method. Just like Microsoft Excel, it accepts the following parameters.

**isFilter**

Indicates whether filtering the list in place.

**listRange**

The list range.

**criteriaRange**

The criteria range.

**copyTo**

The range where copying data to.

**uniqueRecordOnly**

Only displaying or copying unique rows.

## Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria

The following sample code applies the advanced filter on the [Sample Excel File](https://docs2.aspose.com/cells/java/attachments/48136911/48496702.xlsx) and generates the [Output Excel File](https://docs2.aspose.com/cells/java/attachments/48136911/48496705.xlsx). The screenshot shows both files for comparison. As you can see inside the screenshot, data has been filtered inside the output Excel file according to complex criteria.

![](https://docs2.aspose.com/cells/java/attachments/48136911/48496703.png)

## Sample Code

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [sampleAdvancedFilter.xlsx](https://docs2.aspose.com/cells/java/attachments/48136911/48496702.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Before-and-After-Advanced-Filtering.png](https://docs2.aspose.com/cells/java/attachments/48136911/48496703.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [outputAdvancedFilter.xlsx](https://docs2.aspose.com/cells/java/attachments/48136911/48496705.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Microsoft-Excel-Advanced-Filtering-Interface.png](https://docs2.aspose.com/cells/java/attachments/48136911/48496704.png) (image/png)  

