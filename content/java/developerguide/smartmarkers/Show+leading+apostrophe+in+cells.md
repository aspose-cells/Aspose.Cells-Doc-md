+++
title = "Show leading apostrophe in cells" 
description = "" 
weight = 12264 
+++

Aspose.Cells for Java : Show leading apostrophe in cells  

# Aspose.Cells for Java : Show leading apostrophe in cells


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Show leading apostrophe in cells](#Showleadingapostropheincells-Showleadingapostropheincells)
    *   1.1 [Sample Code](#Showleadingapostropheincells-SampleCode)
{{< /panel >}}
 

# Show leading apostrophe in cells

In Microsoft Excel, the leading apostrophe in the cell's value is hidden. Aspose.Cells provides the feature to display the apostrophe by default. For this, the API provides [Workbook.Settings.QuotePrefixToStyle](https://apireference.aspose.com/java/cells/com.aspose.cells/workbooksettings#QuotePrefixToStyle) property. This property indicates whether to set the [QuotePrefix](https://apireference.aspose.com/java/cells/com.aspose.cells/Style#QuotePrefix) property when entering string value starting with a single quote to the cell. Setting the [Workbook.Settings.QuotePrefixToStyle](https://apireference.aspose.com/java/cells/com.aspose.cells/workbooksettings#QuotePrefixToStyle) property to **false **will display the leading apostrophe in the output excel file.

The following screenshot shows the output excel file with the visible apostrophe.

![](https://docs2.aspose.com/cells/java/attachments/97878713/98107424.jpg)

The following code snippet demonstrates this by adding data with Smart Markers in the source excel file. The source and output excel files are attached for reference.

[Source File](https://docs.aspose.com/download/attachments/97878713/AllowLeadingApostropheSample.xlsx?version=1&modificationDate=1577762799073&api=v2)

[Output File](https://docs.aspose.com/download/attachments/97878713/AllowLeadingApostropheSample_out.xlsx?version=1&modificationDate=1577762799076&api=v2)

### Sample Code

The implementation of *DataObject *class is given below

