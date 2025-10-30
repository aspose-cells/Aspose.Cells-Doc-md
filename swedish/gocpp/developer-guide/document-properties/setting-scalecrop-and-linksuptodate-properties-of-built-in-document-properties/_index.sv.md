---
title: Ställa in ScaleCrop och LinksUpToDate egenskaper för inbyggda dokumentegenskaper med Golang via C++
linktitle: Ställa in ScaleCrop och LinksUpToDate egenskaper
type: docs
weight: 320
url: /sv/go-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Lär dig att ställa in ScaleCrop och LinksUpToDate egenskaper för inbyggda dokumentegenskaper med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**
[GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/) och [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) är två utökade inbyggda dokumentegenskaper definierade inom OpenXml-formatet. Syftet med dessa egenskaper är följande:

## **1) ScaleCrop**
Detta element indikerar visningsläget för miniatyrbilden av dokumentet. Ange detta element till **TRUE** för att aktivera skalning av miniatyrbilden av dokumentet. Ange detta element till **FALSE** för att aktivera urskärning av miniatyrbilden för att visa endast sektioner som passar i displayen.

De möjliga värdena för denna komponent definieras av W3C XML Schema boolean-datatypen.

## **2) LinksUpToDate**
Detta element indikerar om hyperlänkar i ett dokument är uppdaterade. Ange detta element till **TRUE** för att ange att hyperlänkar är uppdaterade. Ange detta element till **FALSE** för att ange att hyperlänkar är föråldrade.

De möjliga värdena för denna komponent definieras av W3C XML Schema boolean-datatypen.

## **Skärmbild som visar dessa egenskaper i app.xml-filen**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Ställ in ScaleCrop- och LinksUpToDate-egenskaper för inbyggda dokumentegenskaper**
 Följande exempel kod sätter de utökade inbyggda dokumentegenskaperna [GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/) och [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) för arbetsbokens dokument. Kontrollera den [genererade excel-filen](5115500.xlsx) med denna kod, byta ut dess filändelse till .zip och extrahera innehållet för att visa app.xml som i skärmdumpen ovan.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingScalecropAndLinksuptodatePropertiesOfBuiltInDocumentProperties.go" >}}
