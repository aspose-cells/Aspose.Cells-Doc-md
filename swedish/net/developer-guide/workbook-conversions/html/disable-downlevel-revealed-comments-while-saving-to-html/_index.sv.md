---
title: Inaktivera Downlevel Revealed Comments medan du sparar till HTML
type: docs
weight: 20
url: /sv/net/disable-downlevel-revealed-comments-while-saving-to/
---
## **Möjliga användningsscenarier**

När du sparar din Excel-fil till HTML avslöjar Aspose.Cells Downlevel Conditional Comments. Dessa villkorliga kommentarer är mestadels relevanta för äldre versioner av Internet Explorer och är irrelevanta för moderna webbläsare. Du kan läsa om dem i detalj på följande länk.

- [Villkorlig kommentar - Nedåtnivå-avslöjad villkorlig kommentar](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells låter dig eliminera dessa avslöjade kommentarer på nednivå genom att ställa in[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) egendom till**Sann**.

## **Inaktivera Downlevel Revealed Comments medan du sparar till HTML**

Följande exempelkod visar användningen av[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) fast egendom. Skärmdumpen visar effekten av den här egenskapen när den inte är inställd på sant. Vänligen ladda ner[exempel på Excel-fil](50528257.xlsx) används i den här koden och[utgång HTML](50528258.zip) genereras av den för en referens.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.cs" >}}
