---  
title: Node.js ile Style ile birlikte Çekirdek C++ kullanarak Aralık Verisi Kopyala  
linktitle: Stil ile Aralık Verileri Kopyalama  
type: docs  
weight: 610  
url: /tr/nodejs-cpp/copy-range-data-with-style/  
description: Aspose.Cells for Node.js via C++ kullanarak biçimlendirmeyle birlikte hücre aralığını nasıl kopyalayacağınızı öğrenin.  
---  

{{% alert color="primary" %}}  

[Sadece Aralık Verisini Kopyala](/cells/tr/nodejs-cpp/copy-range-data-only/) aralık verisini başka bir aralığa kopyalama konusunda nasıl yapılacağını açıkladı. Özellikle, kopyalanan hücrelere yeni bir stil seti uygulanır. Aspose.Cells ayrıca, biçimlendirmeyle birlikte tam bir aralık kopyalayabilir. Bu makale nasıl yapıldığını anlatıyor.  

{{% /alert %}}  

Aspose.Cells, örneğin [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-), [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/) ve [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#applyStyle-style-styleflag-) gibi aralıklarla çalışmak için bir dizi sınıf ve yöntem sağlar.  

Bu örnek:  

1. Bir çalışma kitabı oluşturur.  
2. Birinci sayfadaki bir dizi hücreyi veriyle doldurur.  
3. Bir [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/) oluşturur.  
4. Belirtilen biçimlendirme özellikleriyle bir [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style/) nesnesi oluşturur.  
5. Bu stili veri aralığına uygular.  
6. İkinci bir hücre aralığı oluşturur.  
7. Birinci aralıktaki veriyi ve biçimlendirmeyi ikinci aralığa kopyalar.  

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
cells.get(i, j).putValue(`${i},${j}`);
}
}

// Create a range (A1:D3).
const range = cells.createRange("A1", "D3");

// Create a style object.
let style = workbook.createStyle();
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

// Create a second range (C10:F12).
const range2 = cells.createRange("C10", "F12");

// Copy the range data with formatting.
range2.copy(range);

const outputFilePath = path.join(dataDir, "CopyRange.out.xlsx");
// Save the excel file.
workbook.save(outputFilePath);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
