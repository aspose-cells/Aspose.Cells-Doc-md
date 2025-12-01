---
title: Disable CSS while saving to HTML
type: docs
weight: 320
url: /net/disable-css-while-saving-to-html/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When you save your Excel file to a single page HTML, usually the CSS elements will be embedded within the HTML file and will be located in the HEAD section.If you attach this file as an content/body of an email,the CSS elements will be stripped out by most email clients, resulting in improper rendering. The 24.12 version of Aspose.Cells introduces an option which allows you optionally disable CSS, allowing styles to be directly applied within the HTML elements themselves. If you want set the html as the content/body of the email please use the [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disablecss) property and set it to **true**.

 

## **Disable CSS while saving to HTML**

The following sample code shows the usage of [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disablecss) property. 



## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-DisableCss-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
