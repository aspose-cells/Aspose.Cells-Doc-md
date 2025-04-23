---
title: Apple Inc. tarafından geliştirilen Numbers elektronik tablosunu Aspose.Cells for Node.js via C++ kullanarak okuma
linktitle: Aspose.Cells tarafından geliştirilen Numbers Elektronik Tablo Uygulamasını Oku ve Apple Inc. tarafından geliştirildi.
type: docs
weight: 140
url: /tr/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: Apple Inc. tarafından geliştirilen Numbers elektronik tablolarını Aspose.Cells for Node.js via C++ kullanarak nasıl okunacağını öğrenin. 
---

## **Olası Kullanım Senaryoları**

Numbers, Apple Inc. tarafından geliştirilen bir elektronik tablo uygulamasıdır. Aspose.Cells, Numbers tablolarını okuyabilir, fakat yazma desteği yoktur. Numbers tablolarının Veri, Stil ve Formüllerini okuyabilir.

## **Apple Inc. tarafından geliştirilen Numbers elektronik tablolarını Aspose.Cells for Node.js via C++ kullanarak okuma**

Aşağıdaki örnek kod, [Sample Numbers Spreadsheet](sampleNumbersByAppleInc.numbers) dosyasını yükler ve onu [Output PDF Format](outputNumbersByAppleInc.pdf) biçimine dönüştürür. Başarılı yükleme için [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) sınıfını kullanmalı ve yapıcısında [**LoadFormat.Numbers**](https://reference.aspose.com/cells/nodejs-cpp/loadformat) parametresini belirtmelisiniz. İki dosyayı da verilen bağlantılardan indirmeniz gerekir. Kodu herhangi bir Numbers elektronik tablosu ile deneyebilirsiniz. Daha fazla yardım için kodun yorumlarını okuyun.

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleNumbersByAppleInc.numbers");
const outputFilePath = path.join(dataDir, "outputNumbersByAppleInc.pdf");

// Specify load options, we want to load Numbers spreadsheet
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Numbers);

// Load the Numbers spreadsheet in workbook with above load options
const wb = new AsposeCells.Workbook(sourceFilePath, opts);

// Save the workbook to pdf format
wb.save(outputFilePath, AsposeCells.SaveFormat.Pdf);
```

