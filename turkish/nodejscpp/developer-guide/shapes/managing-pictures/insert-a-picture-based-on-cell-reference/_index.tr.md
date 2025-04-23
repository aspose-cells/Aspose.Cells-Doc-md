---
title: Node.js ve C++ kullanarak Hücre Referansı Bazlı Resim Ekleme
linktitle: Hücre Referansına Dayalı Bir Resim Eklemek
type: docs
weight: 150
url: /tr/nodejs-cpp/insert-a-picture-based-on-cell-reference/
description: Aspose.Cells for Node.js via C++ kullanarak, hücre referansına göre çalışma sayfasına resim eklemeyi öğrenin. Hücre verilerini bir resimde gösterin.
---

{{% alert color="primary" %}}
Bazen boş bir resminiz vardır ve resimde verileri veya içeriği bir hücre referansı belirleyerek göstermek istersiniz. Aspose.Cells bu özelliği destekler (Microsoft Excel 2010).
{{% /alert %}}

## Hücre Referansına Dayalı Bir Resim Eklemek

Aspose.Cells for Node.js via C++, hücre veya hücre aralığının grafik nesnesine bağlanmasını destekler. Bu şekilde, o hücre veya hücre aralığında yapılan değişiklikler otomatik olarak grafik nesnesinde görünür. Bir resmi, [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) metodunu çağırarak, kollekciyonun [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection) parçası olarak ekleyin (bu nesne ile kapsüllenmiştir). Hücre aralığını, [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture) nesnesinin [**Picture.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--) özelliğiyle belirtin.

### Kod Örneği

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet's cells collection
const cells = workbook.getWorksheets().get(0).getCells();

// Add string values to the cells
cells.get("A1").putValue("A1");
cells.get("C10").putValue("C10");

// Get the conditional icon's image data
const imagedata = AsposeCells.ConditionalFormattingIcon.getIconImageData(AsposeCells.IconSetType.TrafficLights31, 0);
// Create a stream based on the image data
const stream = Uint8Array.from(imagedata);

// Add a blank picture to the D1 cell
const pic = workbook.getWorksheets().get(0).getShapes().addPicture(0, 3, stream, 10, 10);
// Specify the formula that refers to the source range of cells
pic.setFormula("A1:C10");
// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "referencedpicture.out.xlsx"));
```
