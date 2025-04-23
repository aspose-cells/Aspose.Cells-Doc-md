---  
title: XAdES İmza Desteği Node.js ve C++ ile  
linktitle: XAdES İmza Desteği  
type: docs  
weight: 110  
url: /tr/nodejs-cpp/support-for-xades-signature/  
description: Bu makale, Aspose.Cells kullanarak Node.js ve C++ ile XAdES İmza desteğini açıklar.  
keywords: C++ aracılığıyla Node.js için XAdES İmza Desteği, Excel i Node.js kullanarak C++ aracılığıyla XAdES İmzası ile nasıl imzalanır, Node.js ile C++ kullanarak XAdES imzası ekleme.  
---  

## **Giriş**  

Aspose.Cells, çalışma kitaplarını XAdES İmzası ile imzalamayı destekler. Bunun için API, [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature) sınıfı ve [**XAdESType**](https://reference.aspose.com/cells/nodejs-cpp/xadestype) enum'larını sağlar.  

## **Excel için XAdES İmza Ekleme**  

Aşağıdaki kod örneği, [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature) sınıfını kullanarak [kaynak](101089323.xlsx) çalışma kitabını nasıl imzalayacağınızı gösterir.  

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

