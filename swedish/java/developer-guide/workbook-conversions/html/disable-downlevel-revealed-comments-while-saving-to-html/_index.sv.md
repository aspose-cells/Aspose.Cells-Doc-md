---
title: Inaktivera Downlevel Revealed Comments medan du sparar till HTML
type: docs
weight: 20
url: /sv/java/disable-downlevel-revealed-comments-while-saving-to-html/
---
## **Möjliga användningsscenarier**

När du sparar din Excel-fil till HTML avslöjar Aspose.Cells Downlevel Conditional Comments. Dessa villkorliga kommentarer är mestadels relevanta för gamla versioner av Internet Explorer och är irrelevanta för moderna webbläsare. Du kan läsa om dem i detalj på följande länk.

- [Villkorlig kommentar - Nedåtnivå-avslöjad villkorlig kommentar](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells låter dig eliminera dessa avslöjade kommentarer på nednivå genom att ställa in[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments)egendom till**Sann**.

## **Inaktivera Downlevel Revealed Comments medan du sparar till HTML**

Följande exempelkod visar användningen av[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments) fast egendom. Skärmdumpen visar effekten av den här egenskapen när den inte är inställd på**Sann**Vänligen ladda ner[exempel på Excel-fil](50528267.xlsx)används i den här koden och[mata ut HTML](50528266.zip)fil som genereras av den för en referens.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.java" >}}
