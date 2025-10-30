---  
title: Supporto per la firma XAdES con Node.js tramite C++  
linktitle: Supporto per la firma XAdES  
type: docs  
weight: 110  
url: /it/nodejs-cpp/support-for-xades-signature/  
description: Questo articolo descrive il supporto per la firma XAdES usando Node.js tramite C++ con Aspose.Cells.  
keywords: Supporto per Node.js XAdES Signature tramite C++, Come firmare Excel con XAdES Signature Node.js tramite C++, Come aggiungere firma XAdES Node.js tramite C++.  
---  

## **Introduzione**  

Aspose.Cells offre supporto per la firma dei fogli di lavoro con XAdES Signature. Per questo, l'API fornisce la classe [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature) e l'enumerazione [**XAdESType**](https://reference.aspose.com/cells/nodejs-cpp/xadestype).  

## **Come Aggiungere la Firma XAdES per Excel**  

Il seguente esempio di codice dimostra l'uso della classe [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature) per firmare il foglio di lavoro [source](101089323.xlsx).  

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
