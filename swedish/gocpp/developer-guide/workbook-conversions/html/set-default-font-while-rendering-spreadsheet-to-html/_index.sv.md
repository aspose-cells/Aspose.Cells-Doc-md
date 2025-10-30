---
title: Set Default Font while rendering spreadsheet to HTML with Golang via C++
linktitle: Ange standardfonten vid rendering av kalkylblad till HTML
type: docs
weight: 370
url: /sv/go-cpp/set-default-font-while-rendering-spreadsheet-to/
description: Lär dig hur du ställer in standardteckensnitt vid rendering av kalkylblad till HTML med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells tillåter dig att ställa in standardteckensnitt vid rendering av kalkylblad till HTML. Använd [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/) för detta ändamål. Denna egenskap är användbar om vissa celler i kalkylbladet har ogiltiga eller icke-existerande teckensnitt. Då kommer dessa celler att renderas med det teckensnitt som anges med [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/) egenskapen.

{{% /alert %}}

## Ställ in standardtypsnittet vid rendering av kalkylblad till HTML

Den följande exempelkoden skapar en arbetsbok och lägger till lite text i cellen B4 på den första arbetsbladet och anger dess font till någon okänd/icke-existerande font. Sedan sparar den arbetsboken i HTML genom att ange olika standardfontnamn som Courier New, Arial, Times New Roman, osv.

Skärmbilden visar effekten av att ställa in olika standardteckensnittsnamn via [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/) egenskap.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Koden genererar [utmatnings-HTML-fil med Courier New](5115516), [utmatnings-HTML med Arial](5115518) och [utmatnings-HTML-fil med Times New Roman](5115517).

## Exempelkod

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetDefaultFontWhileRenderingSpreadsheetToHtml.go" >}}
