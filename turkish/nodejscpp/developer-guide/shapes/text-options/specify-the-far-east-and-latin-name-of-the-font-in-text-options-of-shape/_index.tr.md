---  
title: Node.js kullanarak C++ ile Şekil veya Metin Kutusunda Yazı Seçeneklerinin Far Doğu ve Latin İsimlerini Belirtin  
linktitle: Şekil Metin Seçenekleri nde Uzak Doğu ve Latin Yazı Tipi Adını Belirtin  
type: docs  
weight: 1600  
url: /tr/nodejs-cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/  
description: Aspose.Cells for Node.js via C++ kullanarak şekillerin yazı seçeneklerinde Far Doğu ve Latin font isimlerini nasıl belirteceğinizi öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Bazen Far Doğu dili fontlarında metin göstermek istersiniz; örneğin Japonca, Çince, Tayca vb. Aspose.Cells for Node.js via C++, Far Doğu dilinin font adını belirtmek için [**TextOptions.getFarEastName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getFarEastName--) özelliğini sağlar. Ayrıca, Latin font adını [**TextOptions.getLatinName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getLatinName--) özelliği kullanarak belirtebilirsiniz.  

## **Şekil Metin Seçenekleri'nde Uzak Doğu ve Latin Yazı Tipi Adını Belirtin**  

Aşağıdaki örnek kod, bir metin kutusu oluşturur ve içine bazı Japonca metinler ekler. Daha sonra, metnin Latin ve Doğu (Far East) yazı tipi adlarını belirler ve çalışma kitabını [çıktı Excel dosyası](67338274.xlsx) olarak kaydeder. Aşağıdaki ekran görüntüsü, Microsoft Excel'de çıktı metin kutusunun Latin ve Doğu yazı tipi adlarını gösterir.  

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add textbox inside the worksheet.
const idx = ws.getTextBoxes().add(5, 5, 50, 200);
const tb = ws.getTextBoxes().get(idx);

// Set the text of the textbox.
tb.setText("こんにちは世界");

// Specify the Far East and Latin name of the font.
tb.getTextOptions().setLatinName("Comic Sans MS");
tb.getTextOptions().setFarEastName("KaiTi");

// Save the output Excel file.
wb.save("outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

