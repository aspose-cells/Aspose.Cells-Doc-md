---  
title: Unterstützung für XAdES Signatur mit Node.js über C++  
linktitle: Unterstützung für XAdES Signatur  
type: docs  
weight: 110  
url: /de/nodejs-cpp/support-for-xades-signature/  
description: Dieser Artikel beschreibt die Unterstützung für XAdES Signaturen mit Node.js über C++ mit Aspose.Cells.  
keywords: Unterstützung für XAdES Signatur Node.js über C++, Wie man Excel mit XAdES Signatur Node.js über C++ signiert, Wie man XAdES Signatur Node.js über C++ hinzufügt.  
---  

## **Einführung**  

Aspose.Cells unterstützt das Signieren von Arbeitsmappen mit XAdES Signatur. Für diese API steht die [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature)-Klasse und das [**XAdESType**](https://reference.aspose.com/cells/nodejs-cpp/xadestype)-Aufzählung.  

## **Wie man eine XAdES-Signatur für Excel hinzufügt**  

Das folgende Codebeispiel zeigt die Verwendung der [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature)-Klasse zum Signieren der [Quelle](101089323.xlsx)-Arbeitsmappe.  

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

