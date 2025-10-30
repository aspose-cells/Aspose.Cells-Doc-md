---
title: Inaktivera Downlevel Revealed Comments medan du sparar till HTML med Golang via C++
linktitle: Inaktivera Downlevel Revealed Comments
type: docs
weight: 20
url: /sv/go-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Eliminera Downlevel Revealed Comments medan du sparar Excel filer till HTML med Aspose.Cells med Golang via C++.
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML, visar Aspose.Cells Downlevel Conditional Comments. Dessa villkorskommentarer är mest relevanta för äldre versioner av Internet Explorer och är OKÄNDA för moderna webbläsare. Läs mer i detalj på följande länk.

- [Villkorlig kommentar - Låg nivå - avslöjad villkorlig kommentar](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells tillåter dig att eliminera dessa Downlevel Revealed Comments genom att ställa in [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisabledownlevelrevealedcomments/)-egenskapen till **true**.

## **Inaktivera nivånedstiällda avslöjade kommentarer vid sparning till HTML**

Följande exempel visar användningen av [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisabledownlevelrevealedcomments/)-egenskapen. Skärmbilden visar effekten av denna egenskap när den inte är inställd på true. Ladda ner [dokumentnamnet Excel-fil](50528257.xlsx) som används i detta exempel och den [genererade HTML-filen](50528258.zip) för referens.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableDownlevelRevealedCommentsWhileSavingToHtml.go" >}}
