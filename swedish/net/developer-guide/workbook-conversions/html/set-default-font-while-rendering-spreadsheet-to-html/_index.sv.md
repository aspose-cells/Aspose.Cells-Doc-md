---
title: Ställ in standardteckensnitt när du renderar kalkylark till HTML
type: docs
weight: 370
url: /sv/net/set-default-font-while-rendering-spreadsheet-to/
---
{{% alert color="primary" %}}

 Aspose.Cells låter dig ställa in standardteckensnitt medan du renderar kalkylblad till HTML. Vänligen använd[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) för det här syftet. Den här egenskapen är användbar när det finns celler i ett kalkylblad som har ogiltiga eller icke-existerande teckensnitt. Då kommer dessa celler att renderas i ett teckensnitt som anges med[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) fast egendom.

{{% /alert %}}

## Ställ in standardteckensnitt när du renderar kalkylark till HTML

Följande exempelkod skapar en arbetsbok och lägger till lite text i cell B4 i det första kalkylbladet och ställer in dess teckensnitt till något okänt/icke-existerande teckensnitt. Sedan sparar den arbetsboken i HTML genom att ställa in olika standardtypsnittsnamn som Courier New, Arial, Times New Roman, etc.

 Skärmdumpen visar effekten av att ställa in olika standardtypsnittsnamn via[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)fast egendom.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

 Koden genererar[mata ut HTML-fil med Courier New](5115516) , den[mata ut HTML med Arial](5115518) , och den[ut HTML-fil med Times New Roman](5115517).

## Exempelkod

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
