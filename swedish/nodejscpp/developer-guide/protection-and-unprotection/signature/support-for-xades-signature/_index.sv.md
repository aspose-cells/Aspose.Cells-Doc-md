---  
title: Stöd för XAdES signatur med Node.js via C++  
linktitle: Stöd för XAdES signatur  
type: docs  
weight: 110  
url: /sv/nodejs-cpp/support-for-xades-signature/  
description: Denna artikel beskriver stöd för XAdES signatur med Node.js via C++ med Aspose.Cells.  
keywords: Stöd för XAdES signatur Node.js via C++, Hur man signerar Excel med XAdES signatur Node.js via C++, Hur man lägger till XAdES signatur Node.js via C++.  
---  

## **Introduktion**  

Aspose.Cells ger stöd för att signera arbetsböcker med XAdES-signatur. För detta tillhandahåller API:n klassen [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature) och enumeneringen [**XAdESType**](https://reference.aspose.com/cells/nodejs-cpp/xadestype).  

## **Hur man lägger till XAdES-signatur för Excel**  

Följande kodstycke visar användningen av klassen [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature) för att signera [källfilen](101089323.xlsx).  

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
