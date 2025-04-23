---
title: Inaktivera kommentarer med låg nivå som upptäcks medan du sparar till HTML
type: docs
weight: 20
url: /sv/java/disable-downlevel-revealed-comments-while-saving-to-html/
---

## **Möjliga användningsscenario**

När du sparar din excelfil till HTML, avslöjar Aspose.Cells kommentarer med låg nivå. Dessa villkorliga kommentarer är mest relevanta för äldre versioner av Internet Explorer och är irrelevanta för moderna webbläsare. Du kan läsa mer om dem detalj på den följande länken.

- [Villkorlig kommentar - Låg nivå - avslöjad villkorlig kommentar](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells tillåter dig att eliminera dessa avslöjade kommentarer med låg nivå genom att ställa in egenskapen [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments) till **true**.

## **Inaktivera nivånedstiällda avslöjade kommentarer vid sparning till HTML**

Följande exempelkod visar användningen av egenskapen [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments). Skärmbilden visar effekten av denna egenskap när den inte är inställd på **true**. Vänligen ladda ner den [provexfilen Excel](50528267.xlsx) som används i denna kod samt [utdata-HTML](50528266.zip) som genereras av den för referens.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.java" >}}
{{< app/cells/assistant language="java" >}}
