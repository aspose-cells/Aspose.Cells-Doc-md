---
title: Show leading apostrophe in cells
type: docs
weight: 70
url: /net/show-leading-apostrophe-in-cells/
---

In Microsoft Excel, the leading apostrophe in the cell's value is hidden. Aspose.Cells provides the feature to display the apostrophe by default. For this, the API provides [Workbook.Settings.QuotePrefixToStyle](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/quoteprefixtostyle) property. This property indicates whether to set the [QuotePrefix](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/quoteprefix) property when entering string value starting with a single quote to the cell. Setting the [Workbook.Settings.QuotePrefixToStyle](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/quoteprefixtostyle) property to **false** will display the leading apostrophe in the output excel file.

The following screenshot shows the output excel file with the visible apostrophe.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

The following code snippet demonstrates this by adding data with Smart Markers in the source excel file. The source and output excel files are attached for reference.

[Source File](98107425.xlsx)

[Output File](98107426.xlsx)
## **Sample Code**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-1.cs" >}}

The implementation of *DataObject* class is given below

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-2.cs" >}}
