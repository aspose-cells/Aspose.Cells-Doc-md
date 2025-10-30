---
title: Exportera arbetsbladets CSS separat i utdata HTML filen
type: docs
weight: 80
url: /sv/python-net/export-worksheet-css-separately-in-output/
---

## **Möjliga användningsscenario**

Aspose.Cells för Python via .NET erbjuder funktionen att separat exportera kalkylblads-CSS när du konverterar din Excel-fil till HTML. Använd då [**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately)-egenskapen för detta ändamål och ställ in den till **true** när du sparar Excel-filen till HTML-format.

## **Exportera arbetsbladets CSS separat i utdata-HTML-filen**

Följande exempelkod skapar en Excel-fil, lägger till lite text i cellan **B5** i **röd** färg och sparar sedan den i HTML-format med [**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately)-egenskapen. Se [utdata-HTML-filen](60489766.zip) genererad av koden för referens. Du hittar **stylesheet.css** i utdata som ett resultat av exempelkoden.

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.py" >}}

## **Exportera arbetsbok med enkelt blad till HTML**

När en arbetsbok med flera blad konverteras till HTML med Aspose.Cells för Python via .NET, skapas en HTML-fil tillsammans med en mapp som innehåller CSS och flera HTML-filer. När den HTML-filen öppnas i webbläsaren syns flikarna. Samma beteende krävs för en arbetsbok med ett enda kalkylblad när den konverteras till HTML. Tidigare skapades inget separat mapp för arbetsböcker med ett enda blad, och endast HTML-filen skapades. Denna HTML-fil visar inte flikar när den öppnas i webbläsare. MS Excel skapar en ordentlig mapp och HTML även för ett enda blad och samma beteende har implementerats med Aspose.Cells för Python via .NET API. Denna exempelmall kan laddas ner från följande länk för användning i koden nedan:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetSingleSheetTabNameInHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
