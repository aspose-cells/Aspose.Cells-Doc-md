---  
title: Node.js kullanarak C++ ile Aralık Sınırını Belirleme  
linktitle: Aralık Sınırı Ayarlama  
type: docs  
weight: 600  
url: /tr/nodejs-cpp/set-range-border/  
---  

## **Olası Kullanım Senaryoları**  
Bir aralığın kenarlığını ayarlamak istediğinizde, her hücreyi tek tek ayarlamanıza gerek yoktur. Kenarlığı aralık üzerinde ayarlayabilirsiniz. Aspose.Cells for Node.js via C++ bu özelliği sunar.  
Bu makale, Aspose.Cells for Node.js via C++ kullanarak aralık sınırlarını ayarlayan örnek kod sağlar.  

## **Excel'de Aralık Sınırı Ayarlama**  
Excel'de bir aralığın sınırını ayarlamak için şu adımları takip edebilirsiniz:  
1. Sınırlıyı uygulamak istediğiniz hücre aralığını seçin.  
2. Kurdele'nin "Ana Sayfa" sekmesinde, "Yazı Tipi" grubunu bulun.  
3. "Yazı Tipi" grubu içinde, "Kenarlıklar" açılır düğmesine tıklayın.  
<br>  
<img src="border.png" />  
4. Açılır menüde istenilen kenar tipini seçin. Ön ayarlı kenar stilleri arasından seçim yapabilir veya kendi kenarınızı özelleştirebilirsiniz.  
5. İstenilen kenar stili seçildikten sonra, kenar seçilen hücre aralığına uygulanır.  

## **Aspose.Cells for Node.js via C++ kullanarak Aralık Kenarlığı Ayarla**  
Bu örnek aşağıdakileri göstermektedir:  

1. Bir çalışma kitabı oluşturma.  
2. İlk çalışma sayfasındaki hücrelere veri ekleyin.  
3. Bir [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) oluşturun.  
4. Aralığın iç kenarını ayarlayın.  
5. Aralığın dış kenarını ayarlayın.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Obtaining the reference of the newly added worksheet
const ws = workbook.getWorksheets().get(0);
const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

// Create a range (A1:C5).
const range = cells.createRange("A1", "C5");

// set inner border of range
const innerColor = workbook.createCellsColor();
innerColor.setColor(AsposeCells.Color.Red);
range.setInsideBorders(AsposeCells.BorderType.Vertical, AsposeCells.CellBorderType.Thin, innerColor);
innerColor.setColor(AsposeCells.Color.Green);
range.setInsideBorders(AsposeCells.BorderType.Horizontal, AsposeCells.CellBorderType.Thin, innerColor);

// set outer border of range
const outerColor = workbook.createCellsColor();
outerColor.setColor(AsposeCells.Color.Blue);
range.setOutlineBorders(AsposeCells.CellBorderType.Thin, outerColor);

workbook.save("out.xlsx");
```  
