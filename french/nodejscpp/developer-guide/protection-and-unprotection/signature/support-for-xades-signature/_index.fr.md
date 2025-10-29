---  
title: Support du Signature XAdES avec Node.js via C++  
linktitle: Prise en charge des signatures XAdES  
type: docs  
weight: 110  
url: /fr/nodejs-cpp/support-for-xades-signature/  
description: Cet article décrit le support de la signature XAdES en utilisant Node.js via C++ avec Aspose.Cells.  
keywords: Support pour XAdES Signature Node.js via C++, Comment signer Excel avec XAdES Signature Node.js via C++, Comment ajouter une signature XAdES Node.js via C++.  
---  

## **Introduction**  

Aspose.Cells prend en charge la signature des classeurs avec XAdES Signature. Pour cela, l'API fournit la classe [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature) et l'énumération [**XAdESType**](https://reference.aspose.com/cells/nodejs-cpp/xadestype).  

## **Comment ajouter une signature XAdES pour Excel**  

Le fragment de code suivant illustre l'utilisation de la classe [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature) pour signer le classeur [source](101089323.xlsx).  

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
