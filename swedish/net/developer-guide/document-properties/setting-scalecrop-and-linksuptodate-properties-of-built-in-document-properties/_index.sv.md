---
title: Inställning av ScaleCrop och LinksUpToDate egenskaper för inbyggda dokumentegenskaper
type: docs
weight: 320
url: /sv/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Möjliga användningsscenario**
[ScaleCrop](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) och [LinksUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) är två utökade inbyggda dokumentegenskaper definierade inom OpenXml-formatet. Syftet med dessa egenskaper är följande
## **1) ScaleCrop**
Detta element indikerar visningsläget för miniatyrbilden av dokumentet. Ange detta element till **TRUE** för att aktivera skalning av miniatyrbilden av dokumentet. Ange detta element till **FALSE** för att aktivera urskärning av miniatyrbilden för att visa endast sektioner som passar i displayen.

De möjliga värdena för denna komponent definieras av W3C XML Schema boolean-datatypen.
## **2) LinksUpToDate**
Detta element indikerar om hyperlänkar i ett dokument är uppdaterade. Ange detta element till **TRUE** för att ange att hyperlänkar är uppdaterade. Ange detta element till **FALSE** för att ange att hyperlänkar är föråldrade.

De möjliga värdena för denna komponent definieras av W3C XML Schema boolean-datatypen.
## **Skärmbild som visar dessa egenskaper i app.xml-filen**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Inställning av ScaleCrop och LinksUpToDate egenskaper för inbyggda dokumentegenskaper**
Följande exempelkod ställer in [ScaleCrop](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) och [LinksUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) utökade inbyggda dokumentegenskaperna för arbetsboken. Vänligen kontrollera den [utdataexcel-fil](5115500.xlsx) som genererats med denna kod, ändra dess förlängning till .zip och extrahera dess innehåll och visa app.xml som visas i skärmdumpen ovan.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingScaleCropAndLinksUpToDateProperties.cs" >}}
