---
title: Disable Downlevel Revealed Comments while saving to HTML
type: docs
weight: 20
url: /python-java/disable-downlevel-revealed-comments-while-saving-to/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Disable Downlevel Revealed Comments while saving to HTML**
When an Excel file is converted to HTML, Aspose.Cells adds Downlevel-revealed conditional comments to the output HTML file. These conditional comments are mostly relevant to old versions of Internet Explorer and are irrelevant in modern browsers. For additional information on Downlevel-revealed conditional comments, please visit the following link:

[Conditional comment - Downlevel-revealed conditional comment](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

To remove Downlevel-revealed conditional comments, Aspose.Cells provides the [HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) property. Setting the [HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) property to **True** will remove the Downlevel-revealed conditional comments from the output HTML file.

The following image shows the Downlevel-revealed conditional comments that will be removed from the output HTML file:

![todo:image_alt_text](Disable-Downlevel-Revealed-Comments.png)

## **Sample Code**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
