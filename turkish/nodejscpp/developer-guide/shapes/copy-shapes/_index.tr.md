---
title: Node.js ve C++ kullanarak Sayfa İçinde Şekil Kopyalama
linktitle: Şekilleri Kopyalama
type: docs
weight: 200
url: /tr/nodejs-cpp/copy-shapes-between-worksheets/
description: Aspose.Cells for Node.js via C++ kullanarak sayfalar arasında resimler ve grafikler gibi şekillerin nasıl kopyalanacağını öğrenin.
---

{{% alert color="primary" %}}

Bazen, çalışma sayfasındaki öğeleri, örneğin resimler, grafikler ve diğer çizim nesnelerini, sayfalar arasında kopyalamanız gerekebilir. Aspose.Cells for Node.js via C++ bu özelliği destekler. Grafikler, görüntüler ve diğer nesneler en yüksek kesinlik derecesiyle kopyalanabilir.

Bu makale, çalışsayfalar arasında şekillerin nasıl kopyalanacağı konusunda size detaylı bir anlayış sağlar.

{{% /alert %}}

## **Bir Resmi Bir Çalışsayfasından Başka Birine Kopyalama**

Bir resmi bir çalışsayfasından diğerine kopyalamak için aşağıdaki örnek kodda gösterildiği gibi [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-) yöntemini kullanın.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_picture.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get the Picture from the "Picture" worksheet.
const picturesource = workbook.getWorksheets().get("Picture").getPictures().get(0);

// Save Picture to Memory Stream
const ms = picturesource.getData();

// Copy the picture to the Result Worksheet
workbook.getWorksheets().get("Result").getPictures().add(picturesource.getUpperLeftRow(), picturesource.getUpperLeftColumn(), ms, picturesource.getWidthScale(), picturesource.getHeightScale());

// Save the Worksheet
workbook.save(path.join(dataDir, "PictureCopied_out.xlsx"));
```

## **Bir Grafik Bir Çalışsayfasından Diğerine Kopyalama**

Aşağıdaki kod, bir çalışsayfasından diğerine bir grafik kopyalamak için [**ShapeCollection.addCopy(Shape, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addCopy-shape-number-number-number-number-) yönteminin kullanımını göstermektedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_chart.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get the Chart from the "Chart" worksheet.
const chartsource = workbook.getWorksheets().get("Chart").getCharts().get(0);
const cshape = chartsource.getChartObject();

// Copy the Chart to the Result Worksheet
workbook.getWorksheets().get("Result").getShapes().addCopy(cshape, 20, 0, 2, 0);

// Save the Worksheet
workbook.save(path.join(dataDir, "ChartCopied_out.xlsx"));
```

## **Denetimleri ve Diğer Çizim Nesnelerini Bir Çalışsayfasından Diğerine Kopyalama**

Kontroller ve diğer çizim nesnelerini kopyalamak için, aşağıdaki örnekte gösterildiği gibi [**ShapeCollection.addCopy(Shape, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addCopy-shape-number-number-number-number-) yöntemini kullanın.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_control.xlsx");
// Open the template file
const workbook = new AsposeCells.Workbook(filePath);

// Get the Shapes from the "Control" worksheet.
const shape = workbook.getWorksheets().get("Control").getShapes();

// Copy the Textbox to the Result Worksheet
workbook.getWorksheets().get("Result").getShapes().addCopy(shape.get(0), 5, 0, 2, 0);

// Copy the Oval Shape to the Result Worksheet
workbook.getWorksheets().get("Result").getShapes().addCopy(shape.get(1), 10, 0, 2, 0);

// Save the Worksheet
workbook.save(path.join(dataDir, "ControlsCopied_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
