---
title: Inställning av ScaleCrop och LinksUpToDate egenskaper för inbyggda dokumentegenskaper
type: docs
weight: 1050
url: /sv/java/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Möjliga användningsscenario**
[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) och [LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) är två utökade inbyggda dokumentegenskaper som är definierade inom OpenXml-formatet. Syftet med dessa egenskaper är följande
## **1) ScaleCrop**
Denna komponent indikerar visningsläget för dokumentets miniatyrbild. Ställ in denna komponent till **true** för att aktivera skalning av dokumentets miniatyrbild för visningen. Ställ in denna komponent till **false** för att aktivera beskärning av dokumentets miniatyrbild för att visa endast avsnitt som passar i visningen.

De möjliga värdena för denna komponent definieras av W3C XML Schema boolean-datatypen.
## **2) LinksUpToDate**
Denna komponent indikerar om hyperlänkar i ett dokument är aktuella. Ställ in denna komponent till **true** för att indikera att hyperlänkar är uppdaterade. Ställ in denna komponent till **false** för att indikera att hyperlänkar är föråldrade.

De möjliga värdena för denna komponent definieras av W3C XML Schema boolean-datatypen.
## **Skärmbild som visar dessa egenskaper i app.xml-filen**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Inställning av ScaleCrop och LinksUpToDate egenskaper för inbyggda dokumentegenskaper**
Följande exempelkod ställer in [ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) och [LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) utökade inbyggda dokumentegenskaper för arbetsboken. Vänligen kontrollera den [utdata Excel-filen](5472494.xlsx) som genereras med denna kod, ändra dess förlängning till .zip och extrahera dess innehåll och visa aap.xml enligt skärmdumpen ovan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingScaleCropLinksUpToDate-SettingScaleCropLinksUpToDate.java" >}}
