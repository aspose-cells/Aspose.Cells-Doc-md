---
title: Exportera kalkylblads CSS separat i utdata HTML med Golang via C++
linktitle: Exportera arbetsbladets CSS separat i utdata HTML filen
type: docs
weight: 80
url: /sv/go-cpp/export-worksheet-css-separately-in-output/
description: Lär dig hur du exporterar kalkylblads CSS separat när du konverterar Excel filer till HTML med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Aspose.Cells ger funktionen att exportera worksheet CSS separat när du konverterar din Excel-fil till HTML. Använd [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportworksheetcssseparately/)-egenskapen för detta ändamål och ställ in den på **true** vid sparning av Excel-filen i HTML-format.

## **Exportera arbetsbladets CSS separat i utdata-HTML-filen**

Följande exempelkod skapar en Excel-fil, lägger till lite text i cellan **B5** i **röd** färg och sparar sedan den i HTML-format med [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportworksheetcssseparately/)-egenskapen. Se [utdata-HTML-filen](60489766.zip) genererad av koden för referens. Du hittar **stylesheet.css** i utdata som ett resultat av exempelkoden.

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportWorksheetCssSeparatelyInOutputHtml.go" >}}
## **Exportera enkelbladig arbetsbok till HTML**

När en arbetsbok med flera blad konverteras till HTML med Aspose.Cells skapas en HTML-fil tillsammans med en mapp som innehåller CSS och flera HTML-filer. När denna HTML-fil öppnas i webbläsaren är flikarna synliga. Samma beteende krävs för en arbetsbok med ett enda arbetsblad när den konverteras till HTML. Tidigare skapades ingen separat mapp för enbladiga arbetsböcker, och endast en HTML-fil skapades. En sådan HTML-fil visar inte någon flik när den öppnas i webbläsaren. MS Excel skapar också en riktig mapp och HTML för ett enblad, och därför implementeras samma beteende med Aspose.Cells API:er. Mallen kan laddas ner från länken nedan för användning i exempel-koden nedan:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportWorksheetCssSeparatelyInOutputHtml-1.go" >}}
