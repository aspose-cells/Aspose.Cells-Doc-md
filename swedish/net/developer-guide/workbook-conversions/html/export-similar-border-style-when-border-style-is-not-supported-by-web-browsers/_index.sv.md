---
title: Exportera liknande kantstil när kantstil inte stöds av webbläsare
type: docs
weight: 70
url: /sv/net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---
## **Möjliga användningsscenarier**

Microsoft Excel stöder någon typ av streckade kanter som inte stöds av webbläsare. När du konverterar en sådan Excel-fil till HTML med Aspose.Cells tas sådana gränser bort. Aspose.Cells kan dock också stödja att visa sådana gränser med[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) fast egendom. Vänligen ställ in dess värde som**Sann**och gränserna som inte stöds kommer också att exporteras till HTML-fil.

## **Exportera liknande kantstil när kantstil inte stöds av webbläsare**

Följande exempelkod laddar[exempel på Excel-fil](64716806.xlsx) som innehåller några gränser som inte stöds som visas i följande skärmdump. Skärmdumpen illustrerar ytterligare effekten av[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle)egendom inuti[mata ut HTML](64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
