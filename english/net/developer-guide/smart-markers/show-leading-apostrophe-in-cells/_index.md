---  
title: Show leading apostrophe in cells  
type: docs  
weight: 70  
url: /net/show-leading-apostrophe-in-cells/  
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

In Microsoft Excel, the leading apostrophe in a cell's value is hidden. Aspose.Cells provides the feature to display the apostrophe by default. For this, the API provides the **Workbook.Settings.QuotePrefixToStyle** property. This property indicates whether to set the **QuotePrefix** property when entering a string value that starts with a single quote into the cell. Setting the **Workbook.Settings.QuotePrefixToStyle** property to **false** will display the leading apostrophe in the output **Excel** file.

The following screenshot shows the output **Excel** file with the visible apostrophe.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

The following code snippet demonstrates this by adding data with Smart Markers in the source **Excel** file. The source and output **Excel** files are attached for reference.

[Source File](98107425.xlsx)

[Output File](98107426.xlsx)

## **Sample Code**  
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-1.cs" >}}

The implementation of *DataObject* class is given below

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-2.cs" >}}  
{{< app/cells/assistant language="csharp" >}}
