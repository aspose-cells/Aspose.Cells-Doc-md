---
title: Node.js ile Style ile birlikte Aralık Stili Kopyala (C++ ile)
linktitle: Sadece Aralık Stilini Kopyala
type: docs
weight: 620
url: /tr/nodejs-cpp/copy-range-style-only/
description: Aspose.Cells for Node.js via C++ kullanarak yalnızca bir aralık stilini kopyalamayı, veriyle birlikte işlerken nasıl yapacağınızı öğrenin. 
---

{{% alert color="primary" %}}

[Sadece Aralık Verisini Kopyala](/cells/tr/nodejs-cpp/copy-range-data-only/) ve [Stil ile birlikte Aralık Verisini Kopyala](/cells/tr/nodejs-cpp/copy-range-data-with-style/) aralık verisini başka bir aralığa bağımsız olarak veya tamamen biçimlendirmeyle kopyalama konusunda nasıl yapıldığını açıkladı. Aynı zamanda yalnızca biçimlendirmeyi de kopyalayabilirsiniz. Bu makale nasıl yapıldığını gösteriyor.

{{% /alert %}} 

Bu örnek bir çalışma kitabı oluşturur, veri ile doldurur ve yalnızca bir aralığın stilini kopyalar.

1. Bir aralık oluştur.
1. Belirtilen biçimlendirme özellikleriyle bir `Stil` nesnesi oluşturun.
1. Stil biçimlendirmesini aralığa uygular.
1. Hücrelerin ikinci bir aralığını oluşturur.
1. İlk aralığın biçimlendirmesini ikinci aralığa kopyalar.

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
for (let i = 0; i < 50; i++)
{
for (let j = 0; j < 10; j++) 
{
cells.get(i, j).putValue(i.toString() + "," + j.toString());
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
const top = style.getBorders().get(AsposeCells.BorderType.TopBorder);
top.setLineStyle(AsposeCells.CellBorderType.Thin);
top.setColor(AsposeCells.Color.Blue);

const bottom = style.getBorders().get(AsposeCells.BorderType.BottomBorder);
bottom.setLineStyle(AsposeCells.CellBorderType.Thin);
bottom.setColor(AsposeCells.Color.Blue);

const left = style.getBorders().get(AsposeCells.BorderType.LeftBorder);
left.setLineStyle(AsposeCells.CellBorderType.Thin);
left.setColor(AsposeCells.Color.Blue);

const right = style.getBorders().get(AsposeCells.BorderType.RightBorder);
right.setLineStyle(AsposeCells.CellBorderType.Thin);
right.setColor(AsposeCells.Color.Blue);


// Create the styleflag object.
const flag1 = new AsposeCells.StyleFlag();
// Implement font attribute
flag1.setFontName(true);
// Implement the shading / fill color.
flag1.setCellShading(true);
// Implement border attributes.
flag1.setBorders(true);
// Set the Range style.
range.applyStyle(style, flag1);

// Create a second range (C10:E13).
const range2 = cells.createRange("C10", "E13");

// Copy the range style only.
range2.copyStyle(range);

const outputFilePath = path.join(dataDir, "copyrangestyle.out.xls");
// Save the excel file.
workbook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
