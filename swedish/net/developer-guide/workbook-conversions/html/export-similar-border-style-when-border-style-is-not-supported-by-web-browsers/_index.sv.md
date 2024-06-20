---
title: Exportera liknande kantsytel när kantsytele inte stöds av webbläsare
type: docs
weight: 70
url: /sv/net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Möjliga användningsscenario**

Microsoft Excel stödjer vissa typer av stiplede ramar som inte stöds av webbläsare. När du konverterar en sådan Excel-fil till HTML med Aspose.Cells, tas sådana ramar bort. Aspose.Cells kan emellertid också stödja att visa sådana ramar med [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) egenskapen. Ange dess värde som **true** och de icke-stödda ramarna kommer också att exporteras till HTML-filen.

## **Exportera liknande kantstilmall när kantstil inte stöds av webbläsare**

Följande exempelkod laddar [exempel Excel-filen](64716806.xlsx) som innehåller några icke-stödda ramar enligt följande skärmbild. Skärmbilden illustrerar hur [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) egenskapen påverkar den [utdata-HTML-filen](64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
