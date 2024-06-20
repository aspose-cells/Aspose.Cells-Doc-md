---
title: Überflüssige Leerzeichen nach Zeilenumbruch beim Importieren von HTML löschen
type: docs
weight: 620
url: /de/java/delete-redundant-spaces-after-line-break-while-importing/
---

{{% alert color="primary" %}} 

Bitte verwenden Sie die [HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces)-Eigenschaft und setzen Sie sie auf **true**, um alle überflüssigen Leerzeichen nach dem Zeilenumbruch-Tag zu löschen. Standardmäßig ist diese Eigenschaft **false** und überflüssige Leerzeichen werden in den Ausgabedateien beibehalten.

{{% /alert %}} 
## **Effekt der Einstellung der Eigenschaft HtmlLoadOptions.DeleteRedundantSpaces auf false und true**
Der folgende Screenshot zeigt den Effekt der Einstellung dieser Eigenschaft auf false und true.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)
## **Löschen überflüssiger Leerzeichen nach einem Zeilenumbruch beim Importieren von HTML**
Der folgende Beispielcode zeigt die Verwendung der [HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces) Eigenschaft. Bitte setzen Sie sie auf true oder false, um die Ausgabe wie im obigen Screenshot gezeigt zu erhalten.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-DeleteRedundantSpacesFromHtml-1.java" >}}
