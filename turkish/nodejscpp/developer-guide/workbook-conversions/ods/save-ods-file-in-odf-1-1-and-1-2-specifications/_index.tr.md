---
title: ODF 1.1, 1.2 ve 1.3 olarak kaydetmek Node.js kullanarak C++ ile
linktitle: ODS Dosyasını ODF 1.1, 1.2 ve 1.3 sürümlerinde Kaydet
description: Excel i Aspose.Cells for Node.js via C++ ile ODF 1.1, 1.2 ve 1.3 özelliklerine dönüştürün.
type: docs
weight: 230
url: /tr/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells, ODS dosyasını (**OpenDocument Elektronik Tablo**) ODF (**OpenDocument Format**) 1.1, 1.2 ve 1.3 spesifikasyonlara kaydetmeyi destekler. Aspose.Cells'in [**OdsSaveOptions.getOdfStrictVersion()**](https://reference.aspose.com/cells/nodejs-cpp/odssaveoptions/#getOdfStrictVersion--) özelliği, ODS dosyalarını kaydetmek için ODF sürümünü belirler. Bu özellik varsayılan olarak [**OpenDocumentFormatVersionType.odf12**](https://reference.aspose.com/cells/nodejs-cpp/opendocumentformatversiontype/)'dir, bu yüzden bu ayar olmadan kaydedilen ODS dosyası 1.2 spesifikasyonunu kullanır.

{{% /alert %}}

Aşağıdaki örnek kod, bir çalışma kitabı nesnesi oluşturur, ilk sayfadaki A1 hücresine bazı değerler ekler ve ardından ODS dosyasını ODF 1.1, 1.2 ve 1.3 spesifikasyonlarıyla kaydeder. Varsayılan olarak, ODS dosyası ODF 1.2 spesifikasyonu ile kaydedilir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some value in cell A1
const cell = worksheet.getCells().get("A1");
cell.putValue("Welcome to Aspose!");

// Save ODS in ODF 1.2 version which is default
let options = new AsposeCells.OdsSaveOptions();
workbook.save(path.join(dataDir, "ODF1.2_out.ods"), options);

// Save ODS in ODF 1.1 version
options.setOdfStrictVersion(AsposeCells.OpenDocumentFormatVersionType.Odf11);
workbook.save(path.join(dataDir, "ODF1.1_out.ods"), options);

// Save ODS in ODF 1.3 version
options.setOdfStrictVersion(AsposeCells.OpenDocumentFormatVersionType.Odf13);
workbook.save(path.join(dataDir, "ODF1.3_out.ods"), options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
