---
title : "Show leading apostrophe in cells" 
description : "" 
weight : 12311 
toc : false
type: docs
url: /net/developerguide/smartmarkers/show+leading+apostrophe+in+cells/
---

# Aspose.Cells for .NET : Show leading apostrophe in cells


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Show leading apostrophe in cells](#show-leading-apostrophe-in-cells)
    *   1.1 [Sample Code](#sample-code)
{{< /panel >}}
 

# Show leading apostrophe in cells

In Microsoft Excel, the leading apostrophe in the cell's value is hidden. Aspose.Cells provides the feature to display the apostrophe by default. For this, the API provides [Workbook.Settings.QuotePrefixToStyle](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/quoteprefixtostyle) property. This property indicates whether to set the [QuotePrefix](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/quoteprefix) property when entering string value starting with a single quote to the cell. Setting the [Workbook.Settings.QuotePrefixToStyle](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/quoteprefixtostyle) property to **false **will display the leading apostrophe in the output excel file.

The following screenshot shows the output excel file with the visible apostrophe.

![](https://docs2.aspose.com/cells/net/attachments/97878713/98107424.jpg)

The following code snippet demonstrates this by adding data with Smart Markers in the source excel file. The source and output excel files are attached for reference.

[Source File](https://docs2.aspose.com/cells/net/attachments/97878713/98107425.xlsx)

[Output File](https://docs2.aspose.com/cells/net/attachments/97878713/98107426.xlsx)

### Sample Code

The implementation of *DataObject *class is given below

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [dest.xlsx](https://docs2.aspose.com/cells/net/attachments/97878713/98107419.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [SmartMarker1.xlsx](https://docs2.aspose.com/cells/net/attachments/97878713/98107420.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Book1.xlsx](https://docs2.aspose.com/cells/net/attachments/97878713/98107421.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [WorkingWithContentTypeProperties\_out.xlsx](https://docs2.aspose.com/cells/net/attachments/97878713/98107422.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [WorkingWithContentTypeProperties.jpg](https://docs2.aspose.com/cells/net/attachments/97878713/98107423.jpg) (image/jpeg)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [AllowLeadingApostrophe.jpg](https://docs2.aspose.com/cells/net/attachments/97878713/98107424.jpg) (image/jpeg)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [AllowLeadingApostropheSample.xlsx](https://docs2.aspose.com/cells/net/attachments/97878713/98107425.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [AllowLeadingApostropheSample\_out.xlsx](https://docs2.aspose.com/cells/net/attachments/97878713/98107426.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

