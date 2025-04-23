---
title: Node.js ve C++ kullanarak Grafikler Olmadan Kaynak Excel Dosyasını Yükleyin
linktitle: Grafikleri Olmadan Kaynak Excel Dosyasını Yükle
type: docs
weight: 420
url: /tr/nodejs-cpp/load-source-excel-file-without-charts/
description: Aspose.Cells for Node.js via C++ kullanarak grafikler olmadan Excel dosyasını nasıl yükleyeceğinizi öğrenin. 
---

{{% alert color="primary" %}}

Aspose.Cells, Excel dosyanızı grafikler olmadan yüklemenize olanak tanır. Bu amaçla [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) özelliğini kullanabilirsiniz.

{{% /alert %}}

## **Grafikleri Olmadan Yayınları Yükle**

Aşağıdaki örnek kod, grafikler olmadan örnek Excel dosyasını yükler ve çıktı PDF formatında kaydeder.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the load options and filter the data
const options = new AsposeCells.LoadOptions();

// Include everything except charts
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Load the workbook with specified load options
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xlsx"), options);

// Save the workbook in PDF format
workbook.save(path.join(dataDir, "ResultWithoutChart.pdf"), AsposeCells.SaveFormat.Pdf);
```
