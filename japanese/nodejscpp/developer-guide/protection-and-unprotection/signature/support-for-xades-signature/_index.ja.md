---  
title: Node.jsをC++経由で使用したXAdES署名のサポート  
linktitle: XAdES署名のサポート  
type: docs  
weight: 110  
url: /ja/nodejs-cpp/support-for-xades-signature/  
description: この記事は、Aspose.Cellsを用いたNode.js経由のC++でのXAdES署名サポートについて説明します。  
keywords: Node.jsをC++経由で使用したXAdES署名サポート、Node.js経由でExcelにXAdES署名を追加する方法、Node.jsをC++で使用してXAdES署名を追加する方法。  
---  

## **紹介**  

Aspose.CellsはXAdES署名を用いたワークブックの署名サポートを提供します。これには[**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature)クラスと[**XAdESType**](https://reference.aspose.com/cells/nodejs-cpp/xadestype)列挙型が含まれています。  

## **ExcelにXAdES Signatureを追加する方法**  

次のコードスニペットは、[**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature)クラスを使用して[source](101089323.xlsx)ワークブックに署名する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sourceFile.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const password = "pfxPassword";

const pfx = path.join(sourceDir, "AsposeDemo.pfx");


const signature = new AsposeCells.DigitalSignature(pfx, "aspose", "testXAdES", new Date());
signature.setXAdESType(AsposeCells.XAdESType.XAdES);
const dsCollection = new AsposeCells.DigitalSignatureCollection();
dsCollection.add(signature);

workbook.setDigitalSignature(dsCollection);

workbook.save(outputDir + "XAdESSignatureSupport_out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
