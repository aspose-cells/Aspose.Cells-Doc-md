---
title: Node.js kullanarak C++ üzerinden Sertifika ile Dijital Olarak Bir VBA Kod Projesini İmzala
linktitle: Sertifika ile bir VBA Kod Projesini Dijital Olarak İmzalama
type: docs
weight: 110
url: /tr/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Aspose.Cells for Node.js via C++ kullanarak bir VBA Kod Projesini dijital olarak sertifika ile imzalamayı öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells kullanarak ve [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-) yöntemi ile VBA kod projenizi dijital olarak imzalayabilirsiniz. Excel dosyanızın dijital olarak sertifika ile imzalanıp imzalanmadığını kontrol etmek için lütfen bu adımları izleyin.

- **Geliştirici** sekmesinden **Görsel Temel**'e tıklayarak **Görsel Temel Uygulamaları (IDE)**'ni açın.
- **Görsel Temel Uygulamaları IDE**'nin **Araçlar** > **Dijital İmzalar...**'ına tıklayın

ve **Dijital İmza Formu**'nu göstererek belgenin sertifika ile dijital olarak imzalanıp imzalanmadığını gösterecektir.

{{% /alert %}} 

## **Node.js ile Sertifika kullanarak VBA Kod Projesini Dijital Olarak İmzala**

Aşağıdaki örnek kod, [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-) yönteminin nasıl kullanılacağını gösterir. İşte örnek kodun giriş ve çıkış dosyaları. Bu kodu test etmek için herhangi bir Excel dosyası ve herhangi bir sertifika kullanabilirsiniz.

- Örnek Excel dosyası](5115028.xlsm) örnek kodda kullanılan.
- [Örnek pfx dosyası](5115039.pfx) Dijital İmza oluşturmak için. Bu kodu çalıştırmak için lütfen bilgisayarınıza kurun. Şifresi 1234'tür.
- [Çıktı Excel dosyası](5115029.xlsm) örnek kod tarafından oluşturulan.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Set up paths
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
const pfxPath = path.join(sourceDir, "sampleDigitallySignVbaProjectWithCertificate.pfx");
const workbookPath = path.join(sourceDir, "sampleDigitallySignVbaProjectWithCertificate.xlsm");

// Set Digital Signature
const password = "1234";
const comment = "Signing Digital Signature using Aspose.Cells";
const digitalSignature = new AsposeCells.DigitalSignature(fs.readFileSync(pfxPath), password, comment, new Date());

// Create workbook object from excel file
const workbook = new AsposeCells.Workbook(workbookPath);

// Sign VBA Code Project with Digital Signature
workbook.getVbaProject().sign(digitalSignature);

// Save the workbook
workbook.save(path.join(outputDir, "outputDigitallySignVbaProjectWithCertificate.xlsm"));
```
