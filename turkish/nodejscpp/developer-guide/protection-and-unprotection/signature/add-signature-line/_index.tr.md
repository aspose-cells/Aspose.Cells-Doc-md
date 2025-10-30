---
title: Node.js ve C++ kullanarak çalışma sayfasına İmza Çizgisi Ekleme
linktitle: Çalışma Sayfasına İmza Satırı Eklemek
type: docs
weight: 200
url: /tr/nodejs-cpp/add-signature-line/
description: Bu makale, Aspose.Cells for Node.js via C++ kullanarak Node.js kodu ile çalışma sayfasına imza çizgisi eklemeyi açıklar.
keywords: Node.js ve C++ kullanarak çalışma sayfasına İmza Çizgisi ekleme, Node.js ve C++ kullanarak çalışma sayfasına İmza Çizgisi Nasıl Eklenir?, Çalışma sayfasına imza çizgisi ekleme yöntemleri.
---

## **Giriş**

Aspose.Cells, çalışma sayfasına imza satırı eklemek için [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) özelliğini sağlar.

## **Çalışma Sayfasına İmza Çizgisi Eklemek**

Aşağıdaki örnek kod, [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) özelliğini kullanarak çalışma sayfasının imza çizgisini eklemeyi gösterir. Çalışma sonrası ekran görüntüsü, örnek kodun etkisini gösterir.

![todo:image_alt_text](add-signature-line.png)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiating a Workbook object
const wb = new AsposeCells.Workbook();

const signatureLine = new AsposeCells.SignatureLine();
signatureLine.setSigner("Aspose.Cells");
signatureLine.setTitle("signed by Aspose.Cells");
wb.getWorksheets().get(0).getShapes().addSignatureLine(1, 1, signatureLine);

const certificatePath = path.join(dataDir, "AsposeDemo.pfx");
const signature = new AsposeCells.DigitalSignature(certificatePath, "aspose", "test Microsoft Office signature line", new Date());


const dsCollection = new AsposeCells.DigitalSignatureCollection();
dsCollection.add(signature);
wb.setDigitalSignature(dsCollection);
wb.save(path.join(dataDir, "signatureLine.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
