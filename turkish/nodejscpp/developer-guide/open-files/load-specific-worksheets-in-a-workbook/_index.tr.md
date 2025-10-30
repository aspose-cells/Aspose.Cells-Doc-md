---
title: Çalışma Kitabında Belirli Çalışma Sayfalarını Yükleyin ve Node.js ile C++ kullanın
linktitle: Aşağıdaki örnek kod, örnek excel dosyasını grafikleri olmadan yükler ve çıktı PDF formatında kaydeder.
type: docs
weight: 100
url: /tr/nodejs-cpp/load-specific-worksheets-in-a-workbook/
description: Aspose.Cells for Node.js via C++ kullanarak çalışma kitabında belirli çalışma sayfalarını nasıl yükleyeceğinizi öğrenin. Performansı artırın ve bellek kullanımını azaltın.
---

{{% alert color="primary" %}}

Çalışma Kitabında Belirli Çalışma Sayfalarını Yükle

{{% /alert %}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Define a new Workbook.
let workbook;

// Load the workbook with the specified worksheet only.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
loadOptions.setLoadFilter(new CustomLoad());

// Create the workbook.
workbook = new AsposeCells.Workbook(path.join(dataDir, "TestData.xlsx"), loadOptions);

// Perform your desired task.

// Save the workbook.
workbook.save(path.join(dataDir, "outputFile.out.xlsx"));
```

İşte CustomLoad sınıfının uygulaması.

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomLoad extends AsposeCells.LoadFilter {
startSheet(sheet) {
if (sheet.getName() === "Sheet2") {
// Load everything from worksheet "Sheet2"
this.setLoadDataFilterOptions(AsposeCells.LoadDataFilterOptions.All);
} else {
// Load nothing
this.setLoadDataFilterOptions(AsposeCells.LoadDataFilterOptions.Structure);
}
}
}
```


{{< app/cells/assistant language="nodejs-cpp" >}}
