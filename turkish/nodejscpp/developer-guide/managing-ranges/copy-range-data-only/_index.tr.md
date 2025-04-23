---  
title: Node.js ile Çekirdek C++ ile Sadece Aralık Verisini Kopyala  
linktitle: Yalnızca Aralık Verilerini Kopyala  
type: docs  
weight: 600  
url: /tr/nodejs-cpp/copy-range-data-only/  
description: Aspose.Cells for Node.js via C++ kullanarak bir hücre aralığından diğerine veri kopyalamayı öğrenin.  
---  

{{% alert color="primary" %}}  
Bazen, verileri bir hücre aralığından başka bir hücre aralığına kopyalamak isteyebilirsiniz, sadece verileri ve biçimlendirmeyi kopyalayarak. Aspose.Cells bu özelliği sunar.  

Bu makale, Aspose.Cells'i veri aralığını kopyalamak için kullanan bir örnek kod sunmaktadır.  
{{% /alert %}}  

Bu örnek aşağıdakileri göstermektedir:  

1. Bir çalışma kitabı oluşturma.  
1. İlk çalışma sayfasındaki hücrelere veri ekleme.  
1. Bir [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) oluşturma.  
1. Belirtilen biçimlendirme özniteliklerine sahip bir [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesi oluşturur.  
1. Stil biçimlendirmesini aralığa uygular.  
1. Başka bir hücre aralığı oluşturun.  
1. İlk aralığın verilerini bu ikinci aralığa kopyalayın.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first Worksheet Cells.
const cells = workbook.getWorksheets().get(0).getCells();

// Fill some sample data into the cells.
for (let i = 0; i < 50; i++) {
for (let j = 0; j < 10; j++) {
cells.get(i, j).putValue(`${i},${j}`);
}
}

// Create a range (A1:D3).
const range = cells.createRange("A1", "D3");

// Create a style object.
const style = workbook.createStyle();
// Specify the font attribute.
style.getFont().setName("Calibri");
// Specify the shading color.
style.setForegroundColor(AsposeCells.Color.Yellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
// Specify the border attributes.
style.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Blue);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Blue);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Blue);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Blue);

// Create the style flag object.
const flag1 = new AsposeCells.StyleFlag();
// Implement font attribute
flag1.setFontName(true);
// Implement the shading / fill color.
flag1.setCellShading(true);
// Implement border attributes.
flag1.setBorders(true);
// Set the Range style.
range.applyStyle(style, flag1);

// Create a second range (C10:F12).
const range2 = cells.createRange("C10", "F12");

// Copy the range data only.
range2.copyData(range);

const outputFilePath = path.join(dataDir, "CopyRangeData.out.xlsx");
// Save the excel file.
workbook.save(outputFilePath);
```  

