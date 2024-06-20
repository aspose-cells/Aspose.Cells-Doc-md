---
title: Inaktivera kommentarer med låg nivå som upptäcks medan du sparar till HTML
type: docs
weight: 20
url: /sv/net/disable-downlevel-revealed-comments-while-saving-to/
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML avslöjar Aspose.Cells Downlevel Conditional Comments. Dessa villkorliga kommentarer är mest relevanta för äldre versioner av Internet Explorer och är irrelevanta för moderna webbläsare. Du kan läsa om dem i detalj på följande länk.

- [Villkorlig kommentar - Låg nivå - avslöjad villkorlig kommentar](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells låter dig eliminera dessa Downlevel Revealed Comments genom att ställa in [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) egenskapen till **true**.

## **Inaktivera nivånedstiällda avslöjade kommentarer vid sparning till HTML**

Följande kodexempel visar användningen av [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) egenskapen. Skärmbilden visar effekten av denna egenskap när den inte är inställd på true. Vänligen ladda ner [provexelfilen](50528257.xlsx) som används i denna kod och den [utdata-HTML](50528258.zip) som genererats av den som referens.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.cs" >}}
