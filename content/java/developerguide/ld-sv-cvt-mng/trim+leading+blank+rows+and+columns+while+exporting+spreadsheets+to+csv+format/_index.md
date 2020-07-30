---
title : "Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format" 
description : "" 
weight : 12053 
toc : false
type: docs
url: /java/developerguide/ld-sv-cvt-mng/trim+leading+blank+rows+and+columns+while+exporting+spreadsheets+to+csv+format/
---

# Aspose.Cells for Java : Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format](#trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
## Possible Usage Scenarios

Sometimes, your Excel or CSV file has leading blank columns or rows. For example, consider this line

{{< code lang="cs" >}}
,,,data1,data2 
{{< /code >}}

Here the first three cells or columns are blank. When you open such a CSV file in Microsoft Excel, then Microsoft Excel discards these leading blank rows and columns.

By default, Aspose.Cells does not discard leading blank columns and rows on saving but if you want to remove them just like Microsoft Excel does, then Aspose.Cells provides [TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://apireference.aspose.com/java/cells/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) property. Please set it to **true** and then all the leading blank rows and columns will be discarded on saving.

Prior to the release of Aspose.Cells for .NET 20.4, the default value of [TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://apireference.aspose.com/java/cells/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) was **false**. Since the 20.4 release, the default value of [TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://apireference.aspose.com/java/cells/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) is **true.**

## Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format

The following sample code loads the source excel file which has two leading blank columns. It first saves the excel file in CSV format without any changes and then it sets [TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://apireference.aspose.com/java/cells/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) property to **true** and saves it again. The screenshot shows the [source excel file](https://docs.aspose.com/download/attachments/25002392/sampleTrimBlankColumns.xlsx?version=1&modificationDate=1487598739655&api=v2), [output CSV file without trimming](https://docs.aspose.com/download/attachments/25002392/outputWithoutTrimBlankColumns.csv?version=1&modificationDate=1487598617807&api=v2), and the [output CSV file with trimming](https://docs.aspose.com/download/attachments/25002392/outputTrimBlankColumns.csv?version=1&modificationDate=1487598755921&api=v2).

![](https://docs2.aspose.com/cells/java/attachments/25002392/25395206.png)

## Sample Code

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [effect-of-TxtSaveOptions.TrimLeadingBlankRowAndColumn-property.png.png](https://docs2.aspose.com/cells/java/attachments/25002806/25395222.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [outputTrimBlankColumns.csv](https://docs2.aspose.com/cells/java/attachments/25002806/25395223.csv) (text/csv)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [outputWithoutTrimBlankColumns.csv](https://docs2.aspose.com/cells/java/attachments/25002806/25395224.csv) (text/csv)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [sampleTrimBlankColumns.xlsx](https://docs2.aspose.com/cells/java/attachments/25002806/25395225.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

