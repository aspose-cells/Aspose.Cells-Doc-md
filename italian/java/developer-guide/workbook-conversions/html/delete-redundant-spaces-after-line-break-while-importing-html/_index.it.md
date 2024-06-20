---
title: Eliminare gli spazi ridondanti dopo un interruzione di riga durante l importazione di HTML
type: docs
weight: 620
url: /it/java/delete-redundant-spaces-after-line-break-while-importing/
---

{{% alert color="primary" %}} 

Si prega di utilizzare la proprietà [HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces) e impostarla su **true** per eliminare tutti gli spazi ridondanti che seguono il tag di interruzione di riga. Per impostazione predefinita, questa proprietà è **false** e gli spazi ridondanti vengono conservati nei file Excel di output.

{{% /alert %}} 
## **Effetto dell'impostazione della proprietà HtmlLoadOptions.DeleteRedundantSpaces su false e true**
Nella seguente schermata è mostrato l'effetto dell'impostazione di questa proprietà su **false** e **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)
## **Eliminare gli spazi ridondanti dopo un'interruzione di riga durante l'importazione di HTML**
Il seguente esempio di codice mostra l'uso della proprietà [HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces). Si prega di impostarla su **true** o **false** per ottenere l'output come mostrato nella schermata precedente.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-DeleteRedundantSpacesFromHtml-1.java" >}}
