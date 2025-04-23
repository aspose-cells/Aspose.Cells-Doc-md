---
title: Node.js ve C++ kullanarak Tick Label Yönünü Değiştir
linktitle: Tick Etiketi Yönünü Değiştirme
description: Node.js için Aspose.Cells te tick label yönünü nasıl değiştireceğinizi öğrenin. Kılavuzumuz, yatay, dik ve açıyla yönlendirilmiş eksenlerde tick label yönlerini nasıl ayarlayacağınızı anlamanıza yardımcı olacaktır.
keywords: Aspose.Cells for Node.js, tick labels, yön, yönlendirme, eksenler, yatay, dikey, açıyla.
type: docs
weight: 170
url: /tr/nodejs-cpp/change-tick-label-direction/
---

## **Tick Etiketi Yönünü Değiştirme**

Aspose.Cells, diyagram tik etiketi yönünü [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--) özelliği kullanarak değiştirme imkanı sağlar. [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--) özelliği, [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype) enumeration değerini kabul eder. [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype) enumeration aşağıdaki üyeleri sağlar:

- Yatay
- Dikey
- 90 Derece Döndür
- 270 Derece Döndür
- Yığınlanmış

Aşağıdaki görüntü kaynak ve çıktı dosyalarını karşılaştırır

### **Kaynak dosya görüntüsü**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Çıktı dosyası görüntüsü**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Aşağıdaki kod parçacığı, işaret etiket yönünü Rotate90'dan Yatay'a değiştirir.

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
const filePath = path.join(sourceDir, "SampleChangeTickLabelDirection.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Load the chart from source worksheet
const chart = worksheet.getCharts().get(0);

chart.getCategoryAxis().getTickLabels().setDirectionType(AsposeCells.ChartTextDirectionType.Horizontal);

// Output the file
workbook.save(path.join(outputDir, "outputChangeChartDataLableDirection.xlsx"));
```

Kaynak ve çıktı dosyaları aşağıdaki linklerden indirilebilir.

[Kaynak Dosya](105480221.xlsx)

[Çıktı Dosyası](105480223.xlsx)
