---  
title: Prevent Exporting Hidden Worksheet Contents on Saving to HTML  
type: docs  
weight: 210  
url: /python-net/prevent-exporting-hidden-worksheet-contents-on-saving-to/  
ai_search_scope: cells_pythonnet  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask" 
---  

{{% alert color="primary" %}}  

You can save Excel workbooks to HTML. However, if the workbook contains hidden worksheets, Aspose.Cells by default exports the hidden worksheet contents to the HTML output (_files) directory, which contains files such as worksheets, images, tabstrip.htm, stylesheet.css, etc. Sometimes, exporting the content of the hidden worksheets this way isn’t appropriate. For example, if the hidden worksheet contains images that should not be exported to the _files directory.  

{{% /alert %}}  

Aspose.Cells provides the [**HtmlSaveOptions.export_hidden_worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_hidden_worksheet) property. By default, it is set to **true**, and hidden worksheets are exported to HTML. If you set it **to false**, Aspose.Cells will not export hidden worksheet contents.  

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-PreventExportingHiddenContentWhileSavingAsHTML.py" >}}  

{{< app/cells/assistant language="python-net" >}}
