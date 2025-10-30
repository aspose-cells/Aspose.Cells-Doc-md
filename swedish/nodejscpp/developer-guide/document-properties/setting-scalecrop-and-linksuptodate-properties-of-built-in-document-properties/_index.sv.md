---
title: Ställa in egenskaperna ScaleCrop och LinksUpToDate för inbyggda dokumentegenskaper med Node.js via C++
linktitle: Inställning av ScaleCrop och LinksUpToDate egenskaper för inbyggda dokumentegenskaper
type: docs
weight: 320
url: /sv/nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Lär dig hur man ställer in egenskaperna ScaleCrop och LinksUpToDate för inbyggda dokumentegenskaper med Aspose.Cells for Node.js via C++.
---

## **Möjliga användningsscenario**
[BuiltInDocumentPropertyCollection.getScaleCrop()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getScaleCrop--) och [BuiltInDocumentPropertyCollection.getLinksUpToDate()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLinksUpToDate--) är två utökade inbyggda dokumentegenskaper definierade inom OpenXml-formatet. Syftet med dessa egenskaper är följande.

## **1) ScaleCrop**
Detta element indikerar visningsläget för miniatyrbilden av dokumentet. Ange detta element till **TRUE** för att aktivera skalning av miniatyrbilden av dokumentet. Ange detta element till **FALSE** för att aktivera urskärning av miniatyrbilden för att visa endast sektioner som passar i displayen.

De möjliga värdena för denna komponent definieras av W3C XML Schema boolean-datatypen.

## **2) LinksUpToDate**
Detta element indikerar om hyperlänkar i ett dokument är uppdaterade. Ange detta element till **TRUE** för att ange att hyperlänkar är uppdaterade. Ange detta element till **FALSE** för att ange att hyperlänkar är föråldrade.

De möjliga värdena för denna komponent definieras av W3C XML Schema boolean-datatypen.

## **Skärmbild som visar dessa egenskaper i app.xml-filen**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Inställning av ScaleCrop och LinksUpToDate egenskaper för inbyggda dokumentegenskaper**
Följande exempelkod sätter [BuiltInDocumentPropertyCollection.getScaleCrop()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getScaleCrop--) och [BuiltInDocumentPropertyCollection.getLinksUpToDate()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLinksUpToDate--) utökade inbyggda dokumentegenskaper för arbetsboken. Kontrollera den genererade [utdataexcel-filen](5115500.xlsx), ändra dess extension till .zip och extrahera dess innehåll samt visa app.xml som i skärmbilden ovan.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object.
const workbook = new AsposeCells.Workbook();

// Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
workbook.getBuiltInDocumentProperties().getScaleCrop(true);
workbook.getBuiltInDocumentProperties().setLinksUpToDate(true);

// Saving the Excel file.
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Auto);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
