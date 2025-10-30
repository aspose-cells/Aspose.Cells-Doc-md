---  
title: Soporte para firma XAdES con Node.js a través de C++  
linktitle: Soporte para Firma XAdES  
type: docs  
weight: 110  
url: /es/nodejs-cpp/support-for-xades-signature/  
description: Este artículo describe el soporte para la firma XAdES usando Node.js a través de C++ con Aspose.Cells.  
keywords: Soporte para firma XAdES en Node.js vía C++, Cómo firmar Excel con firma XAdES en Node.js vía C++, Cómo agregar firma XAdES en Node.js vía C++.  
---  

## **Introducción**  

Aspose.Cells ofrece soporte para firmar libros de trabajo con firma XAdES. Para esto, la API proporciona la clase [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature) y la enumeración [**XAdESType**](https://reference.aspose.com/cells/nodejs-cpp/xadestype).  

## **Cómo agregar firma XAdES a Excel**  

El siguiente fragmento de código demuestra el uso de la clase [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature) para firmar el libro de trabajo [origen](101089323.xlsx).  

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
