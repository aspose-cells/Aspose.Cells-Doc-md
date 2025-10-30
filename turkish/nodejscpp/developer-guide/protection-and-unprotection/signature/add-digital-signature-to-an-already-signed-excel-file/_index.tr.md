---
title: Node.js ve C++ kullanarak var olan bir Excel dosyasına Dijital İmza Ekleme
linktitle: Zaten İmzalanmış Bir Excel Dosyasına Dijital İmza Eklemek
type: docs
weight: 20
url: /tr/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Bu makale, Aspose.Cells for Node.js via C++ kullanarak Node.js ile zaten imzalanmış bir Excel dosyasına dijital imza eklemeyi anlatır.
keywords: Zaten imzalanmış bir Excel dosyasına dijital imza ekleyin, Node.js ve C++ kullanarak dijital imza nasıl eklenir?
---

## **Olası Kullanım Senaryoları**

Aspose.Cells for Node.js via C++, zaten imzalanmış bir Excel dosyasına dijital imza eklemek için [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) metodunu sağlar.

{{% alert color="primary" %}}

Lütfen, zaten imzalanmış bir Excel belgesine dijital imza eklerken, orijinal belge Aspose.Cells tarafından oluşturulmuşsa, düzgün çalışır. Ancak belgenin diğer motorlar (ör. Microsoft Excel vb.) tarafından oluşturulmuş olması durumunda, Aspose.Cells dosyayı yükledikten ve kaydettikten sonra aynı şekilde tutamayabilir, bu da orijinal imzayı geçersiz kılacaktır.

{{% /alert %}}

## **Zaten İmzalanmış Bir Excel Dosyasına Dijital İmza Eklemek**

Aşağıdaki örnek kod, [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) metodunu kullanarak zaten imzalanmış bir Excel dosyasına dijital imza eklemeyi gösterir. Lütfen bu kodda kullanılan [örnek Excel dosyasını](50528280.xlsx) kontrol edin. Bu dosya zaten dijital olarak imzalanmıştır. Lütfen kod tarafından oluşturulan [çıktı Excel dosyasını](50528281.xlsx) inceleyin. Bu kodda, şifre koruması için [AsposeDemo.pfx](50528279.pfx) adlı demo sertifikasını kullandık, şifresi **aspose**. Ekran görüntüsü, kodun çalışan sonrası örnek Excel dosyasındaki etkisini gösterir.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Örnek Kod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

const dataDir = path.join(__dirname, "data");
// Certificate file path and password
const certFileName = path.join(dataDir, "AsposeDemo.pfx");
const password = "aspose";

// Load the workbook which is already digitally signed to add new digital signature
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleDigitallySignedByCells.xlsx"));

// Create the digital signature collection
const dsCollection = new AsposeCells.DigitalSignatureCollection();


// Create new digital signature and add it in digital signature collection
const signature = new AsposeCells.DigitalSignature(certFileName, password, "Aspose.Cells added new digital signature in existing digitally signed workbook.", new Date());
dsCollection.add(signature);

// Add digital signature collection inside the workbook
workbook.addDigitalSignature(dsCollection);

// Save the workbook and dispose of it.
workbook.save(path.join(__dirname, "outputDigitallySignedByCells.xlsx"));
workbook.dispose();
```
{{< app/cells/assistant language="nodejs-cpp" >}}
