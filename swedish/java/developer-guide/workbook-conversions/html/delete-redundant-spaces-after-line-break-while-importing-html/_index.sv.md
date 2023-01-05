---
title: Ta bort redundanta blanksteg efter radbrytning vid import av HTML
type: docs
weight: 620
url: /sv/java/delete-redundant-spaces-after-line-break-while-importing/
---
{{% alert color="primary" %}} 

 Snälla använd[HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces) egendom och ställ in den**Sann** för att ta bort alla redundanta mellanslag som kommer efter radbrytningstaggen. Som standard är den här egenskapen**falsk**och redundanta utrymmen bevaras i utdata Excel-filer.

{{% /alert %}} 
## **Effekten av att ställa in egenskapen HtmlLoadOptions.DeleteRedundantSpaces till false och true**
 Följande skärmdump visar effekten av att ställa in den här egenskapen till**falsk** och**Sann**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)
## **Ta bort redundanta blanksteg efter radbrytning vid import av HTML**
 Följande exempelkod visar användningen av[HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces) fast egendom. Vänligen ställ in det**Sann** eller**falsk** för att få utdata som visas i skärmdumpen ovan.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-DeleteRedundantSpacesFromHtml-1.java" >}}
