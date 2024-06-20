---
title: Ta bort överflödiga mellanslag efter radbrytning vid import av HTML
type: docs
weight: 620
url: /sv/java/delete-redundant-spaces-after-line-break-while-importing/
---

{{% alert color="primary" %}} 

Använd [HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces)-egenskapen och ställ in den som **true** för att ta bort alla överflödiga mellanslag som kommer efter radbrytningstaggen. Som standard är denna egenskap **false** och överflödiga mellanslag bevaras i utdataexcelfilerna.

{{% /alert %}} 
## **Effekten av att ställa in HtmlLoadOptions.DeleteRedundantSpaces-egenskapen till false och true**
Följande skärmbild visar effekten av att ställa denna egenskap till **false** och **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)
## **Ta bort överflödiga mellanslag efter radbrytning vid import av HTML**
Följande kodexempel visar användningen av [HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces)-egenskapen. Vänligen ställ in den som **true** eller **false** för att få utdatan som visas i den ovanstående skärmbilden.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-DeleteRedundantSpacesFromHtml-1.java" >}}
