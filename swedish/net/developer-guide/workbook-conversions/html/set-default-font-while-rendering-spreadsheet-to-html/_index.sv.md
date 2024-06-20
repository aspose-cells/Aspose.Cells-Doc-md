---
title: Ange standardfonten vid rendering av kalkylblad till HTML
type: docs
weight: 370
url: /sv/net/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}}

Aspose.Cells tillåter dig att ställa in standardtypsnittet vid rendering av kalkylblad till HTML. Använd [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) för detta ändamål. Denna egenskap är användbar när det finns några celler i ett kalkylblad som har ogiltiga eller icke-existerande typsnitt. Då kommer dessa celler att renderas i ett typsnitt som anges med egenskapen [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname).

{{% /alert %}}

## Ställ in standardtypsnittet vid rendering av kalkylblad till HTML

Den följande exempelkoden skapar en arbetsbok och lägger till lite text i cellen B4 på den första arbetsbladet och anger dess font till någon okänd/icke-existerande font. Sedan sparar den arbetsboken i HTML genom att ange olika standardfontnamn som Courier New, Arial, Times New Roman, osv.

Skärmbilden visar effekten av att ställa in olika standardtypsnamn via [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) egenskapen.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Koden genererar [utmatnings-HTML-fil med Courier New](5115516), [utmatnings-HTML med Arial](5115518) och [utmatnings-HTML-fil med Times New Roman](5115517).

## Exempelkod

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
