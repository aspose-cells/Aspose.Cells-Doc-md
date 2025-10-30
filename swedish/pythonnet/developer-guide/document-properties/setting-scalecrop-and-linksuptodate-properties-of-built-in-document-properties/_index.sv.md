---
title: Inställning av ScaleCrop och LinksUpToDate egenskaper för inbyggda dokumentegenskaper
type: docs
weight: 320
url: /sv/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Möjliga användningsscenario**
[scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) och [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) är två utökade inbyggda dokumentegenskaper definierade inom OpenXml-formatet. Syftet med dessa egenskaper är följande
## **1) ScaleCrop**
Detta element indikerar visningsläget för miniatyrbilden av dokumentet. Ange detta element till **TRUE** för att aktivera skalning av miniatyrbilden av dokumentet. Ange detta element till **FALSE** för att aktivera urskärning av miniatyrbilden för att visa endast sektioner som passar i displayen.

De möjliga värdena för denna komponent definieras av W3C XML Schema boolean-datatypen.
## **2) LinksUpToDate**
Detta element indikerar om hyperlänkar i ett dokument är uppdaterade. Ange detta element till **TRUE** för att ange att hyperlänkar är uppdaterade. Ange detta element till **FALSE** för att ange att hyperlänkar är föråldrade.

De möjliga värdena för denna komponent definieras av W3C XML Schema boolean-datatypen.
## **Skärmbild som visar dessa egenskaper i app.xml-filen**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Inställning av ScaleCrop och LinksUpToDate egenskaper för inbyggda dokumentegenskaper**
Följande exempel gör det möjligt att ställa in de utökade inbyggda dokumentegenskaperna [scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) och [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) för arbetsboken. Kontrollera den [genererade excel-filen](5115500.xlsx) med denna kod, byt ut dess extension till .zip och extrahera dess innehåll och visa app.xml som visas i skärmkoppsbilden ovan.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-SettingScaleCropAndLinksUpToDateProperties.py" >}}
{{< app/cells/assistant language="python-net" >}}
