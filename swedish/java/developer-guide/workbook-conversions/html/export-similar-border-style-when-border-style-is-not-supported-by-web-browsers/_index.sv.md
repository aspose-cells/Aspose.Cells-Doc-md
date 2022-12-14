---
title: Exportera liknande kantstil när kantstil inte stöds av webbläsare
type: docs
weight: 70
url: /sv/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---
## **Möjliga användningsscenarier**

Microsoft Excel stöder vissa typer av streckade gränser som inte stöds av webbläsare. När du konverterar en sådan Excel-fil till HTML med Aspose.Cells tas sådana gränser bort. Aspose.Cells kan dock också stödja att visa liknande ramar med[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle)fast egendom. Vänligen ställ in dess värde som**Sann**och gränserna som inte stöds kommer också att exporteras till HTML-fil.

## **Exportera liknande kantstil när kantstil inte stöds av webbläsare**

Följande exempelkod laddar[exempel på Excel-fil](64716832.xlsx)som innehåller några gränser som inte stöds som visas i följande skärmdump. Skärmdumpen illustrerar ytterligare effekten av[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle)egendom inuti[mata ut HTML](64716831.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportSimilarBorderStyle.java" >}}
