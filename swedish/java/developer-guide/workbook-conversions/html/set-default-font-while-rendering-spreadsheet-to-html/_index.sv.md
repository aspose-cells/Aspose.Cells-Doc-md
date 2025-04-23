---
title: Ange standardfonten vid rendering av kalkylblad till HTML
type: docs
weight: 830
url: /sv/java/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}} 

Aspose.Cells tillåter dig att ange standardfonten vid rendering av kalkylblad till HTML. Använd [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) för detta ändamål. Den här egenskapen är användbar när det finns celler i ett kalkylblad som har ogiltiga eller icke-existerande fonter. Då kommer dessa celler att renderas i en font som anges med [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)-egenskapen.

{{% /alert %}} 
## **Ange standardfonten vid rendering av kalkylblad till HTML**
Den följande exempelkoden skapar en arbetsbok och lägger till lite text i cellen B4 på den första arbetsbladet och anger dess font till någon okänd/icke-existerande font. Sedan sparar den arbetsboken i HTML genom att ange olika standardfontnamn som Courier New, Arial, Times New Roman, osv.

Skärmbilden visar effekten av att ange olika standardfontnamn via [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)-egenskapen.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Koden genererar [utdata HTML-fil med Courier New](5472568), [utdata HTML med Arial](5472567) och [utdata HTML-fil med Times New Roman](5472565).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
{{< app/cells/assistant language="java" >}}
