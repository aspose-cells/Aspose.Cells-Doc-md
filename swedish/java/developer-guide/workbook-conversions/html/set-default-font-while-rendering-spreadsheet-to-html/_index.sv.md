---
title: Ställ in standardteckensnitt när du renderar kalkylark till HTML
type: docs
weight: 830
url: /sv/java/set-default-font-while-rendering-spreadsheet-to/
---
{{% alert color="primary" %}} 

 Aspose.Cells låter dig ställa in standardteckensnitt medan du renderar kalkylblad till HTML. Vänligen använd[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)för det här syftet. Den här egenskapen är användbar när det finns celler i ett kalkylblad som har ogiltiga eller icke-existerande teckensnitt. Då kommer dessa celler att renderas i ett teckensnitt som anges med[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) fast egendom.

{{% /alert %}} 
## **Ställ in standardteckensnitt när du renderar kalkylark till HTML**
Följande exempelkod skapar en arbetsbok och lägger till lite text i cell B4 i det första kalkylbladet och ställer in dess teckensnitt till något okänt/icke-existerande teckensnitt. Sedan sparar den arbetsboken i HTML genom att ställa in olika standardtypsnittsnamn som Courier New, Arial, Times New Roman, etc.

 Skärmdumpen visar effekten av att ställa in olika standardtypsnittsnamn via[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)fast egendom.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

 Koden genererar[mata ut HTML-fil med Courier New](5472568) , den[mata ut HTML med Arial](5472567) och den[ut HTML-fil med Times New Roman](5472565).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
