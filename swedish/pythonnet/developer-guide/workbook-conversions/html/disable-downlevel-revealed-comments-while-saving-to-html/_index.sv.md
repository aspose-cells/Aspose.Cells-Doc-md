---
title: Inaktivera kommentarer med låg nivå som upptäcks medan du sparar till HTML
type: docs
weight: 20
url: /sv/python-net/disable-downlevel-revealed-comments-while-saving-to/
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML, visar Aspose.Cells för Python via .NET nedgradering av villkorade kommentarer. Dessa villkorade kommentarer är mest relevanta för äldre versioner av Internet Explorer och är irrelevant för moderna webbläsare. Du kan läsa mer om dem på följande länk.

- [Villkorlig kommentar - Låg nivå - avslöjad villkorlig kommentar](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells för Python via .NET låter dig eliminera dessa nedgraderade komentarsvisningar genom att ställa in [**HtmlSaveOptions.disable_downlevel_revealed_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_downlevel_revealed_comments)-egenskapen till **true**.

## **Inaktivera nivånedstiällda avslöjade kommentarer vid sparning till HTML**

Följande kodexempel visar användningen av [**HtmlSaveOptions.disable_downlevel_revealed_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_downlevel_revealed_comments) egenskapen. Skärmbilden visar effekten av denna egenskap när den inte är inställd på true. Vänligen ladda ner [provexelfilen](50528257.xlsx) som används i denna kod och den [utdata-HTML](50528258.zip) som genererats av den som referens.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
{{< app/cells/assistant language="python-net" >}}
